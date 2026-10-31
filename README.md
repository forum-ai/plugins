# FORUM-AI plugins

Plugins from the FORUM-AI team for AI apps. Add this list to your app once, then install the plugins you want from it.

## Plugins

<!-- plugins:start -->
| Plugin | What it does | Version | Install name |
|---|---|---|---|
| [Materials Project](https://github.com/forum-ai/mp-mcp) | Live Materials Project data in Claude Code: every MP API endpoint, band structures, DOS, phonons, phase diagrams and MP's documentation, with a skill that knows which call answers which materials question | 0.4.0 (unreleased) | `mp-mcp@forum-ai` |
<!-- plugins:end -->

Each plugin's own page, linked in the table, says what you need before you start, such as an API key.

## Claude Code

**Add the list and install a plugin**

1. **In a terminal**, start Claude Code:

   ```bash
   claude
   ```

2. **In Claude Code**, add the FORUM-AI list:

   ```
   /plugin marketplace add forum-ai/plugins
   ```

3. **In Claude Code**, install a plugin by its install name from the table, for example:

   ```
   /plugin install mp-mcp@forum-ai
   ```

   If the plugin needs a key, a box asks for it; paste it and press Enter.

**Remove a plugin, or the whole list**

1. **In a terminal**, remove one plugin:

   ```bash
   claude plugin uninstall mp-mcp@forum-ai
   ```

2. Optional, **in a terminal**: remove the FORUM-AI list and every plugin installed from it:

   ```bash
   claude plugin marketplace remove forum-ai
   ```

## Codex (not yet tried)

**Add the list and install a plugin**

1. **In a terminal**, add the FORUM-AI list:

   ```bash
   codex plugin marketplace add forum-ai/plugins
   ```

2. **In Codex**, type `/plugins`, choose a plugin from the list, and install it.

**Remove a plugin, or the whole list**

1. **In Codex**, type `/plugins`, choose the plugin, and uninstall it.
2. Optional, **in a terminal**: remove the FORUM-AI list:

   ```bash
   codex plugin marketplace remove forum-ai
   ```

## Other apps

Antigravity, Gemini CLI, VS Code and Cursor install each plugin from its own page instead of from this list. Follow the link in the table.

## For FORUM-AI developers: adding a plugin

The catalog files in this repository are generated; don't edit them by hand. `members.json` is the only file you change.

1. **In the plugin's repository**, ship a `.claude-plugin/plugin.json` (and a root `plugin.json` if it supports Codex), and publish each release as a GitHub release with a tag such as `v1.2.0`.
2. **In this repository**, open a pull request that adds one line to `members.json`: `{ "repo": "forum-ai/your-repo", "category": "Productivity" }`.
3. **On GitHub**, after it merges, run Actions → Sync → Run workflow, or wait for the daily run.

The sync job points every entry at the plugin's latest release, by tag and commit, so this repository never holds a copy of a plugin. A new release reaches the catalog within a day, or at once when someone runs the Sync workflow.
