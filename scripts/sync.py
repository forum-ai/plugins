"""Rebuild the catalog files from members.json and each member's latest release.

    python scripts/sync.py

For every repository in members.json this reads its latest GitHub release (or its default
branch when it has none yet), takes the plugin's name, description and version from the
repository's own .claude-plugin/plugin.json at that commit, and writes:

- .claude-plugin/marketplace.json   the catalog Claude Code reads
- .agents/plugins/marketplace.json  the catalog Codex reads (members that ship a root plugin.json)
- the plugin table in README.md, between the plugins:start and plugins:end markers

Each entry points at the member repository by tag and commit, so this repository holds no
copy of any plugin. Set GITHUB_TOKEN to raise the GitHub API rate limit. Standard library only.
"""
from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OWNER = {"name": "FORUM-AI development team", "email": "FORUM-AI@lbl.gov"}
CATALOG = "forum-ai"
DESCRIPTION = "Plugins from the FORUM-AI team: AI-app access to scientific data and tools"


def get(url: str) -> bytes | None:
    headers = {"User-Agent": "forum-ai-plugins-sync", "Accept": "application/vnd.github+json"}
    if (token := os.environ.get("GITHUB_TOKEN")) and url.startswith("https://api.github.com/"):
        headers["Authorization"] = f"Bearer {token}"
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def api(path: str):
    body = get(f"https://api.github.com/{path}")
    return None if body is None else json.loads(body)


def file_at(repo: str, sha: str, path: str):
    body = get(f"https://raw.githubusercontent.com/{repo}/{sha}/{path}")
    return None if body is None else json.loads(body)


def member(repo: str, category: str) -> tuple[dict, dict | None, dict]:
    release = api(f"repos/{repo}/releases/latest")
    tag = release["tag_name"] if release else None
    ref = tag or api(f"repos/{repo}")["default_branch"]
    sha = api(f"repos/{repo}/commits/{ref}")["sha"]
    manifest = file_at(repo, sha, ".claude-plugin/plugin.json")
    if manifest is None:
        sys.exit(f"{repo} has no .claude-plugin/plugin.json at {ref}")
    name = manifest["name"]

    claude_source = {"source": "github", "repo": repo}
    if tag:
        claude_source |= {"ref": tag, "sha": sha}
    claude = {"name": name, "source": claude_source, "description": manifest.get("description", "")}

    codex = None
    if file_at(repo, sha, "plugin.json") is not None:
        codex_source = {"source": "url", "url": f"https://github.com/{repo}.git"}
        if tag:
            codex_source["ref"] = tag
        codex = {"name": name, "source": codex_source,
                 "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}, "category": category}

    row = {"name": manifest.get("displayName", name), "install": name, "repo": repo,
           "description": manifest.get("description", ""), "version": manifest.get("version", ""), "tag": tag}
    return claude, codex, row


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def table(rows: list[dict]) -> str:
    lines = ["| Plugin | What it does | Version | Install name |", "|---|---|---|---|"]
    for r in rows:
        version = r["tag"] or f"{r['version']} (unreleased)"
        lines.append(f"| [{r['name']}](https://github.com/{r['repo']}) | {r['description']} | {version} | `{r['install']}@{CATALOG}` |")
    return "\n".join(lines)


def main() -> None:
    members = json.loads((ROOT / "members.json").read_text())["plugins"]
    claude, codex, rows = [], [], []
    for m in members:
        c, x, r = member(m["repo"], m.get("category", "Productivity"))
        claude.append(c)
        rows.append(r)
        if x:
            codex.append(x)
    write_json(ROOT / ".claude-plugin/marketplace.json", {"name": CATALOG, "owner": OWNER, "description": DESCRIPTION, "plugins": claude})
    write_json(ROOT / ".agents/plugins/marketplace.json", {"name": CATALOG, "plugins": codex})
    readme = ROOT / "README.md"
    text, n = re.subn(r"(<!-- plugins:start -->).*?(<!-- plugins:end -->)",
                      lambda mt: mt.group(1) + "\n" + table(rows) + "\n" + mt.group(2), readme.read_text(), flags=re.S)
    if n != 1:
        sys.exit("README.md is missing the plugins:start / plugins:end markers")
    readme.write_text(text)
    for r in rows:
        print(f"{r['repo']}: {r['tag'] or 'default branch (no release yet)'}")


if __name__ == "__main__":
    main()
