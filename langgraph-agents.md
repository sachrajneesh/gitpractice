# Course-in-a-box: LangGraph Agents (coding-first)

Give this file to **Claude Code** (claude.ai/code) in an empty directory. Claude will scaffold a 12-module, hands-on course for building AI agents with LangChain and LangGraph — per-module READMEs, runnable examples, and TODO-style exercises paired with solutions.

The "mcp-by-sdk" name is historical: this recipe is a sibling of an earlier MCP (Model Context Protocol) course built the same way. The style generalizes — you can adapt the curriculum section to any SDK.

---

## Quick start for your friend

1. **Install Claude Code** if you haven't: https://claude.com/claude-code
2. Open a terminal in the parent directory where you want the course to live:
   ```bash
   cd ~/workspace/learning     # or wherever you keep projects
   ```
3. Start Claude Code and paste the prompt below (everything between the `>>>` markers).
4. Answer Claude's two clarifying questions (LLM provider, directory name).
5. Let Claude scaffold — it creates ~70 files.
6. Install deps, fill in `.env`, run `main.py`, then open module 1.

---

## Prompt to paste into Claude Code

>>> START OF PROMPT >>>

I want you to scaffold a coding-first course on my machine for building AI agents with **LangChain and LangGraph**. The style is "hands-on exercises with TODO markers, paired with solutions, so I can code step by step."

Please follow the spec in the rest of this message exactly.

### Course goals
- LangGraph-heavy (agent focus): ~12 modules. LangChain covered only enough to get to graphs.
- Every module has runnable examples *and* fill-in-the-blank exercises with solutions.
- No hand-holding prose — short READMEs, code does the teaching.

### Before you scaffold, ask me
1. **LLM provider** — pick one: Anthropic direct, OpenAI, Ollama (local), or OpenAI-compatible proxy (LiteLLM / custom `base_url`).
2. **Directory name** — default to `langgraph-agents` in the current working directory.

Then create the layout below.

### Directory layout

```
<course-dir>/
├── README.md               # install, .env, smoke test
├── COURSE_CATALOG.md       # 12-module outline with status markers
├── LEARNING_APPROACH.md    # coding-first teaching style
├── QUICK_START.md          # resume guide
├── PROJECT_STRUCTURE.md    # file layout reference
├── pyproject.toml          # langchain, langgraph, langchain-<provider>, python-dotenv, pydantic
├── .python-version         # 3.12
├── .gitignore              # .env, .venv, __pycache__, *.sqlite
├── .env.example            # placeholder env vars for the chosen provider
├── main.py                 # one-line smoke test that prints an LLM response
├── _shared/
│   ├── __init__.py
│   └── llm.py              # get_llm() helper reading .env
└── modules/
    ├── README.md           # index table of all 12 modules
    ├── module01_agent_fundamentals/
    ├── module02_environment_setup/
    ├── module03_first_chain/
    ├── module04_tools_and_tool_calling/
    ├── module05_langgraph_basics/
    ├── module06_react_agent/
    ├── module07_memory_and_persistence/
    ├── module08_human_in_the_loop/
    ├── module09_multi_agent_systems/
    ├── module10_streaming_and_observability/
    ├── module11_project_research_agent/
    └── module12_testing_and_deployment/
```

Each module directory contains:
- `README.md` — objectives, topics, exercise list, completion checkboxes
- `notes.md` — cheat sheet / API reference
- `examples/` — numbered runnable files (`01_*.py`, `02_*.py`, …)
- `exercises/` — `exerciseNN_<topic>.py` (starter with `# TODO:` markers) + `exerciseNN_solution.py`

### 12-module curriculum

| # | Module | Focus | Deliverable exercise |
|---|--------|-------|----------------------|
| 01 | Agent Fundamentals | What an agent is: LLM + tools + loop. LangChain vs LangGraph. Why graphs. | Concept quiz in `notes.md` (no code) |
| 02 | Environment Setup | Install packages, configure provider via `.env`, first chat call. | `exercise01_first_call.py` — one LLM call, print response + usage |
| 03 | First Chain (LangChain primer) | `ChatPromptTemplate`, LCEL `prompt \| llm \| parser`, `with_structured_output`. | Text-to-bullets summarizer + Pydantic product-review extractor |
| 04 | Tools & Tool Calling | `@tool`, `bind_tools`, parse `AIMessage.tool_calls`, hand-rolled ReAct loop (no LangGraph). | Calculator agent with add/sub/mul/div, `while`-loop driver |
| 05 | LangGraph Basics | `StateGraph`, `TypedDict` state, reducers, `add_conditional_edges`, `.compile()`. | 2-node graph: classify user intent → respond in matching tone |
| 06 | ReAct Agent in LangGraph | `MessagesState`, agent node + `ToolNode`, conditional edge, then prebuilt `create_react_agent`. | Multi-tool agent (calculator, fake web search, current time) built from scratch |
| 07 | Memory & Persistence | `MemorySaver`, `SqliteSaver`, `thread_id`. | Chatbot that remembers across process restarts |
| 08 | Human-in-the-loop | `interrupt_before`, `get_state`, `update_state`. | Email-sender agent that pauses for approval before the send tool |
| 09 | Multi-Agent Systems | Supervisor pattern, `Command`, subgraphs. | Researcher + writer team that produces a short report |
| 10 | Streaming & Observability | `.stream(stream_mode=…)`, LangSmith (optional). | Stream tokens + per-node updates for a ReAct agent |
| 11 | Project — Research Agent 🏆 | Capstone combining tools + memory + HITL + streaming. | REPL research agent with persisted notes |
| 12 | Testing & Deployment | Fake LLMs for unit tests, pytest, FastAPI `/chat` + SSE. | Pytest suite + FastAPI endpoint wrapping the Module 6 agent |

### Depth of authoring

- **Fully flesh out Modules 01–06** (README + notes + examples + starter exercise + solution)
- **Scaffold Modules 07–12** with README + notes stub + a single placeholder exercise file. The user fleshes these out as they reach them.

### LLM helper

`_shared/llm.py` must expose one function:

```python
def get_llm(model: str | None = None, temperature: float = 0.0, **kwargs): ...
```

It reads provider config from `.env` (via `python-dotenv`) and returns a LangChain chat model. Implementation depends on the provider picked at step 1:

- **Anthropic** → `ChatAnthropic(model=…, api_key=ANTHROPIC_API_KEY)`
- **OpenAI** → `ChatOpenAI(model=…, api_key=OPENAI_API_KEY)`
- **Ollama** → `ChatOllama(model=…, base_url=OLLAMA_BASE_URL)`
- **OpenAI-compatible proxy (LiteLLM, etc.)** → `ChatOpenAI(base_url=…, api_key=…, model=…)`

All examples and exercises must import via `from _shared.llm import get_llm` so the user can switch providers centrally.

### Exercise file template

```python
"""
Exercise N 🟢|🟡|🔴: <title>

Task:
  <what to build, in plain English>

Requirements:
  - <bullet>
  - <bullet>

Test:
  .venv/bin/python modules/<module>/exercises/<file>.py

Hints:
  - <one helpful pointer per gotcha>
"""

from _shared.llm import get_llm
# other imports

# TODO: <stub>
def foo():
    ...


def main() -> None:
    # visible assertions / prints that show the user their code works
    ...


if __name__ == "__main__":
    main()
```

The matching `*_solution.py` has the same structure, fully implemented, and lives next to the starter.

### Security and safety

- Never write real API keys or secrets into any file. `.env.example` uses `<placeholder>` values.
- `.env` is in `.gitignore`.
- `get_llm()` must raise a clear error if required env vars are missing.
- Don't install packages or run code as part of scaffolding — leave install and verification to the user.

### Verification (tell me these commands at the end)

```bash
cd <course-dir>
uv venv && source .venv/bin/activate
uv pip install --python .venv/bin/python -e .
cp .env.example .env     # then fill in real values
.venv/bin/python main.py
.venv/bin/python modules/module02_environment_setup/examples/01_verify_setup.py
.venv/bin/python modules/module06_react_agent/exercises/exercise01_solution.py
```

Now ask your two clarifying questions, then scaffold the whole thing.

>>> END OF PROMPT >>>

---

## What your friend ends up with

- **~70 files**, one `uv pip install -e .` away from runnable
- A working smoke test (`main.py`) after she fills in her `.env`
- **6 modules of real exercises** to start coding immediately
- **6 more scaffolded modules** with stubs and READMEs, ready to flesh out as she progresses
- Every exercise has a `*_solution.py` sitting next to it — she codes first, peeks second

## Troubleshooting tips for your friend

- **`Environment variable '…' is not set`** → `.env` isn't being loaded. Run scripts from the project root, or `cd` there first.
- **`ImportError: langchain_openai`** (or similar) → re-run `uv pip install -e .`
- **Behind a corporate proxy that intercepts TLS** → export `PIP_CERT`, `REQUESTS_CA_BUNDLE`, and `SSL_CERT_FILE` pointing at your system cert bundle before `uv pip install`.
- **Ollama picked but no models** → `ollama pull llama3.1` first.

## Customizing the recipe

- **Different SDK** (e.g., AutoGen, CrewAI, LlamaIndex workflows): replace the "12-module curriculum" table with your own and change package names in `pyproject.toml`.
- **Different depth**: change the "Depth of authoring" section — e.g., "flesh out all 12 modules" or "only scaffold, don't author any exercises."
- **Different teaching style**: edit `LEARNING_APPROACH.md` requirements in the prompt (e.g., "add a quiz at the end of each module").

The prompt is the source of truth. Edit it, hand it to Claude Code, and you get a new course in ~15 minutes.
