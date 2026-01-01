# Software Engineering in 2026

Are you already behind? Probably! Let's fix that.

## TLDR Workflow

```
1. PROMPT   → One focused task at a time
2. REVIEW   → Use a diff viewer
3. SECURE   → Check for injection, secrets, OWASP top 10
4. REDUCE   → Refactor and minimize complexity
5. TEST     → Run tests, smoke test
6. REPEAT   → Iterate until production-ready
```

**Golden Rules:**
- Never ship unreviewed code
- Smaller prompts = better results
- AI writes it, you own it

## The AI Reality Check

**For non-engineers:** AI seems magical. It's a senior developer who never sleeps.

**For daily engineers:** You'll see the limits:
- Produces plausible code that needs review
- Doesn't understand your architecture without guidance
- Optimizes for wrong things without constraints
- Requires discipline for production-quality results

The gap between "runs" and "ships to production" is where expertise matters.

**Productivity Paradox:**
- Non-engineers see 10,000% improvement (can't build → prototype).
- Engineers see ~20% boost.

Headlines are calibrated for non-engineers. AI amplifies engineers, doesn't replace them.

## Core Philosophy

**"Can the AI do the work for me? Yes!"**

- AI writes the code
- AI validates the code
- AI handles docs, specs, presentations too

## AI Caution

- AI hallucinates and makes mistakes
- Verify critical code and security decisions
- Don't vibe-code sensitive apps (fintech, healthcare) without expertise
- Human oversight remains essential

## Your Role: Director of Agents

The typing is solved. Now you need deeper engineering skills to guide AI effectively.

**Your new responsibilities:**
- Architecture, planning, testing, verification
- Review code with a proper diff viewer
- Provide approvals as Director of Agents

**Observability is critical.** AI code may work but fail silently. Use:
- OpenTelemetry (instrumentation)
- Grafana (visualization)
- Splunk (log aggregation)

## CLAUDE.md Configuration

Create separate CLAUDE.md files using ALWAYS/NEVER format:
- Root: general rules
- Frontend: UI patterns
- Backend: server conventions
- Python/Data: data science workflows

Reference: https://www.anthropic.com/engineering/claude-code-best-practices

## Breaks Are Easy Now

- Submit prompt, take a break
- Background agents process while you're away
- Parallel subagents: 2-day tasks → 4 hours

## Generative Coding Workflow

**Brainstorm → Plan → Implement** (separate prompts):

1. **Brainstorm**: Discuss approach with AI
2. **Plan**: Create implementation plan before coding
3. **Implement**: Execute in focused chunks
4. **Review**: Verify requirements met
5. **Test**: RED/GREEN TDD
6. **Code Review**: Subagent or second session
7. **Merge/PR**: Create PR, merge

**Git Worktrees:** Create per task to avoid conflicts, keep main clean.

**Let AI Write Prompts:** Point Claude at a planning doc, ask it to write prompts for execution.

## Prompting Guidelines

- **Intent**: Be clear about what you want
- **Goal**: State expected outcome
- **Simple**: Break complex tasks into smaller ones
- **Context**: Provide background
- **Best Practices**: Say it explicitly, tell AI to have strong opinions

## Project Planning

### Documents to Create
| Document | Content |
|----------|---------|
| USER_STORIES.md | "As a [ROLE], I should be able to [feature]" |
| DATA_MODELS.md | Database architecture, endpoint schemas |
| TECH_STACK.md | Technology choices and rationale |
| DEVELOPMENT_PLAN.md | Phased implementation |
| SECURITY_PLAN.md | Security considerations |

### Planning Steps
1. Describe app and features to AI
2. Generate user stories for ALL roles
3. Create database schema from stories
4. Plan security early, implement later
5. Bootstrap with framework scaffolding
6. Create README.md
7. Set up git repo

### Avoid Premature Optimization
AI optimizes too early. Watch for rate limiting, retry logic, caching before basics work. Ask: "Is this necessary for launch?" If not, add to "FUTURE IMPROVEMENTS".

## Code Quality Tools

| Category | Tools |
|----------|-------|
| **Linters** | Biome.js (JS), StyleLint (CSS), Ruff (Python), Rubocop (Ruby), golangci-lint (Go), clippy (Rust) |
| **Type Systems** | TypeScript (JS), BasedPydantic/mypy (Python), Sorbet (Ruby) |

Ask AI to use linters, type checkers, test runners, and profilers.

## AI Validation Checklist

Security review, smoke testing, stress testing, code reduction, test coverage, documentation, dead code removal, 12 Factor coverage, observability coverage

## TDD with AI

**RED/GREEN Workflow:**
1. Write failing test (RED)
2. Implement to pass (GREEN)
3. Refactor if needed
4. Next test

AI writes tests from user stories. Use eval frameworks (LangFuse, LangSmith) for AI-powered features.

## Debugging with AI

**Create these scripts:**
- `trace.sh`: Capture distributed traces
- `profile.sh`: Run CPU/memory profilers
- `debug.sh`: Attach debugger
- `logs.sh`: Aggregate and filter logs

Scripts give AI standardized diagnostic info and reduce back-and-forth.

**Provide debug info from:** Server logs, browser console, network dev tools

## Vibe Coding vs SE-Focused Generative Coding

| Vibe Coding | SE-Focused |
|-------------|------------|
| "Build feature XYZ" | Small, focused tasks |
| Paste error stack | Structured approach |
| Large brush strokes | "Create function with these inputs/outputs" |

## AI Agents and Skills

You can write agents that write agents. Claude Code is built this way.

### Skills (Superpowers)
Markdown files teaching agents specific tasks:
- Agents learn by reading SKILL.md files
- Self-improving agents write their own skills
- Test skills on subagents for reliability

### Skill Workflow
1. Describe the workflow
2. Claude creates SKILL.md files
3. Test with pressure scenarios
4. Iterate until reliable

### Agent Memory
- Store transcripts outside .claude (prevents auto-deletion)
- Vector index in SQLite for semantic search
- Summarize with fast models (Haiku)
- Search via subagents to keep main context clean

### Available Skills

| Skill | When to Use |
|-------|-------------|
| `superpowers:using-superpowers` | Starting conversations |
| `superpowers:brainstorming` | Before creative work |
| `superpowers:writing-plans` | Multi-step task specs |
| `superpowers:test-driven-development` | Before implementation |
| `superpowers:using-git-worktrees` | Feature isolation |
| `superpowers:subagent-driven-development` | Independent tasks in plans |
| `superpowers:systematic-debugging` | Bugs or test failures |
| `superpowers:executing-plans` | Plan execution |
| `superpowers:verification-before-completion` | Before claiming done |
| `superpowers:finishing-a-development-branch` | Implementation complete |
| `superpowers:requesting-code-review` | Before merging |
| `superpowers:receiving-code-review` | Receiving feedback |
| `superpowers:dispatching-parallel-agents` | 2+ independent tasks |
| `superpowers:writing-skills` | Creating/editing skills |

**The 1% Rule**: If even 1% chance a skill applies, invoke it.

## AI Models and Tools

Models change frequently. Stay current.

| Category | Options |
|----------|---------|
| **Primary** | Claude Code (superior quality, excellent tooling) |
| **Research** | OpenAI Codex/GPT 5.2 (aggressive web search) |
| **Alternatives** | Cursor, Brokk, Gemini (mixed results) |
| **Fast tasks** | Haiku (memory, quick tasks) |
| **Images** | GPT-4o (multimodal for RAG) |

Same model in different tools produces different quality (system prompts matter). Use multiple agents to cross-check.

## Key Concepts

### RAG (Retrieval Augmented Generation)
AI enhanced by retrieving context from external sources before generating.

**Implementation:**
1. Vector DB: PGVector or Pinecone
2. Ingestion: Docling for chunking with LLM summaries
3. Images: S3/R2 + multimodal models
4. Embeddings: OpenAI, Google, or Voyage

### Embeddings
Semantic retrieval vs keyword matching. Maps user terms to expected terminology. Reduces tokens by retrieving less, more relevant text.

## New Skills for 2026

Agents/subagents, prompting, context management, RAG/embeddings, CLI modes, tools/plugins, skills/hooks, MCP, LSP, slash commands, workflows, IDE integrations

## MCP (Model Context Protocol)

Universal adapter letting LLMs access external systems (databases, APIs, files, tools).

### Why Needed
LLMs only know training data + context window:
- **Stale knowledge**: Training cutoff date
- **No private data**: Can't see your codebase
- **Read-only**: Can't create files, run commands
- **Context limits**: Can't fit entire codebase

### MCP Solves This
- **Read** from files, databases, APIs, docs
- **Write** to external systems
- **Execute** tests, deployments
- **Search** large datasets without loading all

### Architecture
```
LLM ←→ MCP Client ←→ MCP Server ←→ External System
```

### Installation
```bash
# Global
claude mcp add --global <name> <command>

# Per-project (recommended)
claude mcp add <name> <command>
```

### Essential MCPs
- **GitHub**: PRs, issues, actions
- **Jira**: Project management
- **Confluence**: Documentation

### Recommended MCPs
```bash
# Context7 - Up-to-date docs
claude mcp add --transport http context7 https://mcp.context7.com/mcp --header "CONTEXT7_API_KEY: YOUR_KEY"

# Figma Dev Mode
claude mcp add --transport http figma-desktop http://127.0.0.1:3845/mcp

# Shopify Dev
claude mcp add shopify-dev-mcp npx @shopify/dev-mcp@latest
```

Also: Sosumi (Apple/iOS docs) - https://sosumi.ai/

## LSP (Language Server Protocol)

Standardized protocol for code intelligence (autocomplete, go-to-definition, diagnostics, refactoring). Created by Microsoft, now industry standard.

### Why LSP Matters for AI
| Capability | Benefit |
|------------|---------|
| Precise navigation | Knows where `foo` is defined across files |
| Type information | Knows `user.name` is a string |
| Semantic understanding | Distinguishes call vs declaration vs string |
| Real-time diagnostics | Errors without running code |
| Refactoring | Knows all places to change |

### LSP vs Text Search
| Operation | grep | LSP |
|-----------|------|-----|
| Find definition | Searches text | Jumps to actual definition |
| Find references | Matches everywhere | Only actual usages |
| Rename | Breaks strings/comments | Only the symbol |
| Type info | None | Full signatures |
| Dead code | Can't detect | Highlights it |

### LSP Features in Claude Code
Go to Definition, Find References, Hover Info, Document Symbols, Workspace Symbols, Call Hierarchy

### Common Language Servers
| Language | Server | Install |
|----------|--------|---------|
| TS/JS | tsserver | Bundled with `typescript` |
| Python | Pylsp, Pyright | `pip install python-lsp-server` |
| Go | gopls | `go install golang.org/x/tools/gopls@latest` |
| Rust | rust-analyzer | `rustup component add rust-analyzer` |
| Ruby | Solargraph | `gem install solargraph` |
| Java | Eclipse JDT | Via IDE |
| C/C++ | clangd | `brew install llvm` |

**MCP + LSP + LLM = production-ready AI coding**

## Local LLMs

Privacy, cost savings, offline. Trade-off: lower quality than cloud.

### Popular Models (2026)
DeepSeek R1/V3, Kimi K2 (1M+ tokens), MiniMax, Llama 4, Qwen 3, Mistral Large

### Inference Tools
- **Ollama**: Simple CLI (`brew install ollama`)
- **LM Studio**: GUI
- **vLLM**: Production server
- **llama.cpp**: CPU, Apple Silicon optimized

### Local vs Cloud
| Local | Cloud |
|-------|-------|
| Sensitive data | Max quality needed |
| High volume | Sporadic usage |
| Offline | Frontier capabilities |
| Cost optimization | Complex reasoning |

### Hardware
- **Minimum**: M1/M2 16GB RAM or GPU 8GB VRAM
- **Recommended**: M3 Pro/Max 32GB+ or RTX 4090 24GB
- Use Q4/Q5 quantized models to reduce memory

## Context Management

### Avoid Compaction
Quality drops after compaction. Keep sessions clean and focused.
- Separate sessions for research vs implementation
- Use subagents to search without polluting main context

### Best Practices
- Different agents cross-check plans
- Research in one session, execute in fresh session
- Markdown > plain text for LLMs
- Consider TOON format: https://github.com/toon-format/toon

## Building AI Apps

### Chat UI
Vercel AI SDK UI, Assistant UI. Look for: streaming (SSE), auto-resize textarea, image upload, thinking UI

### Token Optimization
- **Prompt Caching**: Lower cost for repeated tokens
- **Model Routing**: Switch models by complexity (LangGraph, OpenRouter)

### Agent Frameworks
- **Simple**: Vercel AI SDK, Inngest AgentKit
- **Advanced**: LangGraph

### Tools for AI
Plan thoroughly. Follow OpenAI/Anthropic specs or use LangChain/Vercel SDK tools.

### Prompt Management
Don't hardcode. Use dependency injection or hosted tools (Vellum, Langsmith). Iterate constantly.

### Observability
Posthog LLM Tracing (simple) or LangSmith (advanced). Collect thumbs up/down feedback.

### Eval (Testing AI)
Test for: PII exposure, hallucinations, wrong info, toxicity. Tools: LangFuse, LangSmith.

### Fine Tuning
Avoid unless: massive budget, exhausted other methods. Can't migrate to newer models.

## AI-Powered DevOps

Pod restart remediation, scaling, log triage, rollback

## Security

### Code
- Run `/security-review` in Claude Code
- SEMGREP in GitHub Actions: https://semgrep.dev/docs/getting-started/quickstart-managed-scans
- Never commit secrets; use `.env` + `.gitignore`

### User Data
- Lock down S3 buckets
- Strip EXIF from uploaded images
- Vault/encrypt sensitive data

### AI Security
- PromptFoo for security testing
- Guardrails against prompt injection
- Multiple layers, test regularly

## Recommended Tech Stack (2026)

### Web
| Type | Options |
|------|---------|
| Frontend | React (TypeScript) |
| Full-stack | Next.js, Remix (Shopify) |
| Backend | Bun/Express/Fastify, Python, Go, Rails, Rust |

### Mobile
React Native + Expo (cross-platform). Native Swift/Kotlin has limited AI tooling.

### Database
PostgreSQL (default), Supabase, PGVector, Pinecone

### Hosting
Render.com, Fly.io, Vercel. Avoid Heroku.

### Tools
| Category | Tool |
|----------|------|
| JS packages | Bun |
| Python packages | uv |
| Ruby packages | Bundler |
| Frontend builds | Vite |

## GitHub CLI

`brew install gh` - Automates GitHub work. Claude Code integrates for PRs, reviews.

Run `/install-github-app` for Claude GitHub action (auto-review PRs).

## Development Principles

- **DRY**: Code appears 3+ times → extract to utility
- **SRP**: Each module does one thing. No God Classes.
- AI doesn't always check existing patterns. Prompt: "Look at workflow code for DRY/SRP violations"

## AI Visualizations

- Architecture diagrams
- Workflow diagrams
- Gemini Flash 3 draws full pictures

## Beyond Code

Docs, specs, presentations. Keep prompting to improve.

## The Future is Now

Claude Code is 100% written by Claude Code. Anthropic achieves 4 releases per engineer per day.

AI isn't replacing engineers—it's accelerating what each can ship.

## Resources

- [Spec Driven Development - GitHub Spec Kit](https://github.com/github/spec-kit)
