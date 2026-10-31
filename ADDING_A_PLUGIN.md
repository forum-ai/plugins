# Adding a plugin to the FORUM-AI catalog

For FORUM-AI developers. Users install plugins as the [README](README.md) describes.

The catalog files in this repository are generated; don't edit them by hand. `members.json` is the only file you change.

1. **In the plugin's repository**, ship a `.claude-plugin/plugin.json` (and a root `plugin.json` if it supports Codex), and publish each release as a GitHub release with a tag such as `v1.2.0`.
2. **In this repository**, open a pull request that adds one line to `members.json`: `{ "repo": "forum-ai/your-repo", "category": "Productivity" }`.
3. **On GitHub**, after it merges, run Actions → Sync → Run workflow, or wait for the daily run.

The sync job points every entry at the plugin's latest release, by tag and commit, so this repository never holds a copy of a plugin. A new release reaches the catalog within a day, or at once when someone runs the Sync workflow.
