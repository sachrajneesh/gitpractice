# Course-in-a-box: MCP by SDK (coding-first)

Give this file to **Claude Code** (claude.ai/code) in an empty directory. Claude will scaffold a 15-module, hands-on course for the **Model Context Protocol (MCP)** using the official Python SDK — per-module READMEs, runnable examples, and TODO-style exercises paired with solutions.

The style matches the LangGraph "agents" recipe (`langgraph-agents.md`) — same coding-first philosophy, different subject.

---

## Quick start for your friend

1. **Install Claude Code** if you haven't: https://claude.com/claude-code
2. Open a terminal in the parent directory where you want the course to live:
   ```bash
   cd ~/workspace/learning
   ```
3. Start Claude Code and paste the prompt below (everything between the `>>>` markers).
4. Answer Claude's one clarifying question (directory name).
5. Let Claude scaffold — it creates ~80 files.
6. Install deps, run the smoke test, then open module 1.

> **Why MCP first?** If she'll eventually build AI agents, understanding MCP lets her expose any tool, data source, or API to Claude Desktop / Cursor / any MCP client in a standard way. It's the "USB-C for AI tools."

---

## Prompt to paste into Claude Code

>>> START OF PROMPT >>>

I want you to scaffold a coding-first course on my machine for learning the **Model Context Protocol (MCP)** with the official **Python SDK** (package: `mcp`). The style is "hands-on exercises with TODO markers, paired with solutions, so I can code step by step."

Please follow the spec in the rest of this message exactly.

### Course goals
- 15 modules covering MCP from first principles through deployment
- Every module has runnable examples *and* fill-in-the-blank exercises with solutions
- No hand-holding prose — short READMEs, code does the teaching
- SDK reference: https://github.com/modelcontextprotocol/python-sdk

### Before you scaffold, ask me
- **Directory name** — default to `mcp-by-sdk` in the current working directory.

Then create the layout below.

### Directory layout

```
<course-dir>/
├── README.md                # install, corporate-proxy notes, smoke test
├── COURSE_CATALOG.md        # 15-module outline with status markers
├── LEARNING_APPROACH.md     # coding-first teaching style
├── QUICK_START.md           # resume guide
├── PROJECT_STRUCTURE.md     # file layout reference
├── pyproject.toml           # mcp>=1.22, pytest (optional)
├── .python-version          # 3.12
├── .gitignore               # .venv, __pycache__
├── main.py                  # trivial entrypoint / version print
└── modules/
    ├── README.md            # index table
    ├── module01_fundamentals/
    ├── module02_environment_setup/
    ├── module03_first_server/
    ├── module04_resources/
    ├── module05_tools/
    ├── module06_prompts/
    ├── module07_transports/
    ├── module08_error_handling/
    ├── module09_advanced_features/
    ├── module10_client_development/
    ├── module11_database_integration/
    ├── module12_filesystem_operations/
    ├── module13_api_integration/
    ├── module14_testing_debugging/
    └── module15_deployment/
```

Each module directory contains:
- `README.md` — objectives, topics, exercise list, completion checkboxes
- `API_REFERENCE.md` — cheat sheet for the SDK surface used in that module
- `examples/` — numbered runnable files (`01_*.py`, `02_*.py`, …)
- `exercises/` — `exerciseNN_<topic>.py` (starter with `# TODO:` markers) + `exerciseNN_solution.py`

### 15-module curriculum

| # | Module | Focus | Deliverable exercise |
|---|--------|-------|----------------------|
| 01 | Fundamentals | What MCP is; clients, servers, transports; resources vs tools vs prompts; JSON-RPC 2.0; lifecycle. | Concept quiz in `notes.md` (no code) |
| 02 | Environment Setup | `uv venv`, install `mcp`, verify import. Corporate-proxy cert notes. | `verify_setup.py` — imports and prints SDK version |
| 03 | Your First MCP Server | `Server(name)`, `stdio_server()`, async/await, stdout vs stderr, FastMCP preview. | Build "my-first-server" with logging to stderr; integrated test that launches it as a subprocess |
| 04 | Resources | Static vs dynamic resources, URIs, templates, `list_resources`, `read_resource`. | Server exposing 3 resources (static greeting, dynamic timestamp, templated file-by-name) |
| 05 | Tools | `@server.call_tool()`, input schemas via JSON Schema, result formatting, `list_tools`. | Server with 3 tools: echo, add, fetch_joke (validated inputs) |
| 06 | Prompts | Prompt templates with arguments, `list_prompts`, `get_prompt`. | Server exposing a "code-review" prompt parameterized by language + snippet |
| 07 | Server Transports | stdio, SSE, WebSocket; when to pick which. | Same server wired up three ways (stdio, SSE, WS), with a README comparing them |
| 08 | Error Handling & Validation | MCP error codes, JSON-RPC error shape, input validation, logging. | Harden the Module 5 tools server: validate inputs, return structured errors, log to stderr |
| 09 | Advanced Features | Progress notifications, cancellation, pagination, streaming. | Long-running tool that reports progress and honors cancellation |
| 10 | Client Development | `ClientSession`, connecting over stdio, calling tools, reading resources, getting prompts. | Standalone Python client that connects to the Module 8 server and exercises every capability |
| 11 | Project — Database Integration | SQLite-backed server: schema as resources, CRUD as tools, transactions. | Complete DB server with safe queries (parameterized), schema introspection resource, and integration tests |
| 12 | Project — Filesystem Operations | File/dir resources, read/write/delete tools, path-traversal defense, search. | Sandboxed filesystem server that refuses paths outside a root |
| 13 | Project — API Integration | HTTP client, auth (API key or OAuth), caching, rate limiting, retries. | Server wrapping a public API (e.g. GitHub public endpoints) with caching + retry |
| 14 | Testing & Debugging | pytest for MCP servers, mocking sessions, integration tests, profiling. | Test suite for the Module 11 DB server covering success and error paths |
| 15 | Deployment & Best Practices | Packaging, env config, security posture, logging, docs, maintenance. | Package one server as installable (`pip install .`); production checklist |

### Depth of authoring

- **Fully flesh out Modules 01–03** (README + API_REFERENCE + examples + starter exercise + solution). These are the foundation — the user must be able to run a working MCP server by the end of module 3.
- **Scaffold Modules 04–15** with README + API_REFERENCE stub + a single placeholder exercise file. The user fleshes these out as they progress.

### Module 3 specifics (critical)

Module 3 must include these concepts visibly:

- **stdout is SACRED** — it carries JSON-RPC messages. Never `print()` to stdout. Use `sys.stderr` or `logging` to stderr.
- **async/await everywhere** — MCP is an async SDK.
- **Integrated test pattern** — an `examples/integrated_test.py` file that launches the server as a subprocess and connects to it with a `ClientSession`, so the user can verify end-to-end without Claude Desktop.
- **FastMCP mention** — note that `FastMCP` is a higher-level ergonomic wrapper; this course uses the lower-level `Server` API first so the user understands what FastMCP hides.

### Shared conventions

- All servers use `Server(name)` from `mcp.server` and `stdio_server()` from `mcp.server.stdio`
- All examples runnable standalone: `.venv/bin/python modules/<module>/examples/<file>.py`
- Logging goes to stderr; errors raise `McpError` with appropriate codes when applicable
- Every exercise has a matching `*_solution.py`

### Exercise file template

```python
"""
Exercise N 🟢|🟡|🔴: <title>

Task:
  <what to build, in plain English>

Requirements:
  - <bullet>
  - <bullet>

How to test:
  .venv/bin/python modules/<module>/exercises/<file>.py
  (or use the matching integrated test from examples/)

Hints:
  - <one helpful pointer per gotcha>
"""

import asyncio
import sys
from mcp.server import Server
from mcp.server.stdio import stdio_server
# other imports

async def main():
    # TODO: ...
    server = Server("<name>")
    # ...
    async with stdio_server() as (read, write):
        await server.run(read, write, server.create_initialization_options())

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("stopped", file=sys.stderr)
```

The matching `*_solution.py` has the same structure, fully implemented.

### Security & safety

- This course does **not** make outbound network calls until Module 13. Modules 1–12 are local-only.
- Module 12 (filesystem) must include explicit path-sandboxing — refuse `..`, refuse paths outside a declared root. Make this a graded requirement.
- Module 13 (API) must use env vars for keys — never hardcode. Include `.env.example`.
- Never install packages or run code as part of scaffolding — leave install and verification to the user.

### Verification (tell me these commands at the end)

```bash
cd <course-dir>
uv venv && source .venv/bin/activate
uv pip install --python .venv/bin/python -e .
.venv/bin/python -c "import mcp; print(mcp.__version__)"
.venv/bin/python modules/module03_first_server/examples/integrated_test.py
```

Now ask for the directory name, then scaffold the whole thing.

>>> END OF PROMPT >>>

---

## What your friend ends up with

- **~80 files**, one `uv pip install -e .` away from runnable
- A working MCP server and integrated test by end of module 3 — she can open Claude Desktop and wire it up
- **3 modules of real exercises** to start coding immediately
- **12 more scaffolded modules** with READMEs and API-reference stubs, ready to flesh out
- Every exercise has a `*_solution.py` next to it — code first, peek second

## Troubleshooting tips for your friend

- **`ModuleNotFoundError: mcp`** → `uv pip install -e .` from project root
- **Server hangs or client times out** → she probably `print()`ed to stdout. Search for bare `print(` in her server code; replace with `print(..., file=sys.stderr)`
- **Corporate proxy that intercepts TLS** → if `uv pip install` fails with SSL errors, point Python at your system cert bundle before installing:
  ```bash
  export PIP_CERT=<path-to-your-cert-bundle>
  export REQUESTS_CA_BUNDLE=<path-to-your-cert-bundle>
  export SSL_CERT_FILE=<path-to-your-cert-bundle>
  ```
  On macOS the bundle is typically `/private/etc/ssl/cert.pem`; on Linux it varies by distro.
- **Claude Desktop can't see the server** → check the `claude_desktop_config.json` path is absolute, and that the `command` points at the venv's Python, not system Python

## Customizing the recipe

- **TypeScript SDK instead of Python**: swap `pyproject.toml` for `package.json`, swap `mcp` for `@modelcontextprotocol/sdk`, rewrite examples as `.ts`. Curriculum maps 1:1.
- **Shorter course**: drop Modules 11–13 (the real-world projects) and merge 14–15 into a single deployment module.
- **Different teaching style**: edit `LEARNING_APPROACH.md` requirements in the prompt.

The prompt is the source of truth. Edit it, hand it to Claude Code, and you get a new course in ~15 minutes.

---

## Companion recipe

For building **AI agents** once she's comfortable with MCP, see `langgraph-agents.md` — same philosophy, 12 modules on LangChain + LangGraph.
