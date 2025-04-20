# MCP email tools

This is an example of an MCP server in Python with two email tools, which allow you to send emails using Proton Mail or Gmail.

It uses the [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) and a third-party [ProtonMail wrapper](https://github.com/opulentfox-29/protonmail-api-client).

## Using this server

To use this with the Claude desktop app:

Clone the repo, and then run `uv sync` or `pip install .` to install the requirements from the `pyproject.toml` file.

If you're using `uv` (and if you're not, you really should be), simply type `uv run mcp` and then `mcp install main.py` to add it to Claude.

Otherwise, create or edit the `claude_desktop_config.json` file at `~/Library/Application\ Support/Claude/claude_desktop_config.json` on Mac/Linux or `%APPDATA%\Claude\` on Windows. Add this content:

```json
{
    "mcpServers": {
      "proton_server": {
        "command": "python3",
        "args": [
          "PATH_TO/main.py"
        ]
      }
    }
}
```

You'll need environment variables - `p_username` and `p_password` for Proton or `g_username` and `g_password` for Gmail. The Gmail password needs to be an [app-specific password](https://myaccount.google.com/apppasswords), not your regular account password. You can put these in an `env.py` file if you want.

Restart Claude, and you should see the two tools under the hammer icon below the chat.

You can then use prompts like: "Write an email with a HTML body accepting the invitation to the Bloomsday lecture."

Use at your own risk. It's a proof-of-concept, not a finished product.

## Contributing

Feel free to fork the repo and make a PR if you'd like to suggest changes. Failing that, you could always...

<a href="https://www.buymeacoffee.com/mattrudge" target="_blank"><img src="https://mattrudge.net/images/bmac.png" alt="Buy Matt A Coffee"></a>

-----
Matt Rudge<br/>
April, 2025