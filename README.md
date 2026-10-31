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

## For FORUM-AI developers

To add a plugin to this list, see [Adding a plugin](ADDING_A_PLUGIN.md).
