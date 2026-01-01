# Software Engineering in 2026

Are you already behind? Probably! Let's fix that.


## 
TODO
AI Over-hype story
if you are not a daily software engineer, then using ai will seem magical 
if you are a daily software engineer, you will see the limitations and the need for discipline and structure to get the best results



## Core Principles

 - AI should be writing the code
 - AI should be reading the code to validate work
 - AI should be more than just code, your docs, specs, presentations

## AI Religion - Don't oversubscribe to AI

Don't use AI to DDoS social reality.
We have to be diligent and careful when using AI.
Always retain your judgement and critical thinking skills.

- AI can hallucinate and make mistakes
- Always verify critical code and security decisions
- Don't vibe code sensitive apps (fintech, healthcare) without proper expertise
- Human oversight remains essential

## Your Engineering Expertise is Needed More Than Ever

Now that the typing and manual clicking on your computer is mostly solved by AI, your role as an engineer is shifting.

### Director of Agents
Our work as engineers and architects now is much harder - we need to pay extra care for architecture, planning, testing, verifying, making sure we stand to KPIs and then provide approvals as a Director of Agents.

Use a proper GUI diff viewer to review code changes and approve edits.

## CLAUDE.md Configuration

Claude uses CLAUDE.md files to receive persistent instructions. Best practices:
- Use ALWAYS/NEVER format for clarity
- Create separate CLAUDE.md files for different parts of your codebase:
  - Root CLAUDE.md for general rules
  - Frontend CLAUDE.md for UI-specific patterns
  - Backend CLAUDE.md for server-side conventions
  - Python/Data CLAUDE.md for data science workflows
- Ask Claude to create and maintain these files based on your tech stack
- Reference: https://www.anthropic.com/engineering/claude-code-best-practices

## Taking a break is way easier now

 - Submit prompt, take a break!
 - Allows you to remain productive even when tired
 - Use background agents to process while you're away
 - Parallel subagents can reduce 2-day tasks to 4-hour tasks

## Workflow using Generative Coding

### Brainstorm -> Plan -> Implement Workflow
Each of the following are separate prompts in a workflow:

1. **Brainstorm**: Describe your goal, discuss approach with AI
2. **Plan**: Create detailed implementation plan before coding
3. **Implement**: Execute the plan in focused chunks
4. **Review**: Verify code actually implements the requirements
5. **Test**: Use RED/GREEN TDD - write failing test, implement, pass
6. **Code Review**: Dispatch to subagent or second session for review
7. **Merge/PR**: Create PR, merge to main branch

### Git Worktrees for Parallel Work
- Create worktrees for each task so parallel work doesn't clobber each other
- Keeps main branch clean while experimenting

### Let AI Write Your Prompts
- Point Claude at a planning document
- Ask it to write a prompt to execute a specific phase in a new session
- Unbias original agent by asking "Do you agree with this feedback?"

## Prompting Guidelines

- Intent: Be clear about what you want
- Goal: State the expected outcome
- Simple: Break complex tasks into smaller ones
- Context: Provide relevant background information
- Best Practices: Say "best practices" explicitly, tell AI to have strong opinions

## Project Planning Methodology

Before coding, plan extensively with AI:

### Planning Documents to Create
- **USER_STORIES.md**: "As a [ROLE], I should be able to [feature]" format
- **DATA_MODELS.md**: Database architecture and endpoint schemas
- **TECH_STACK.md**: Technology choices and rationale
- **DEVELOPMENT_PLAN.md**: Phased implementation approach
- **SECURITY_PLAN.md**: Security considerations and mitigations

### Planning Steps
1. Describe the app and features to AI
2. Generate user stories for ALL roles (user, admin, owner, etc.)
3. Create database schema from user stories
4. Plan security early but implement later
5. Bootstrap project using framework's scaffolding tools
6. Create README.md documenting the project
7. Set up git repo and remote

### Pitfall: Premature Optimization
AI likes to optimize too early. Watch for:
- Rate limiting before basic functionality works
- Retry logic and caching before launch
- Advanced security features you don't need yet

Ask: "Is this necessary for launch?" If not, add to README's "FUTURE IMPROVEMENTS" section.

## Code Quality Tools

### Static Analysis & Linters
- **Biome.js**: JavaScript
- **StyleLint**: CSS
- **Ruff**: Python
- **Rubocop**: Ruby
- **golangci-lint**: Go
- **clippy**: Rust

### Type Systems
- **TypeScript**: JavaScript
- **BasedPydantic**: Python (watch for Astral's `ty`)
- **mypy**: Python type checker
- **Sorbet**: Ruby

### Ask AI to Use Tools
- Use linters
- Use type checkers
- Use test runners
- Use profilers

## AI Validation

- Security review
- Smoke testing
- Stress testing
- Code reduction
- Test coverage
- Documentation
- Dead code removal (Housekeeping)
- 12 Factor coverage
- Observability coverage

## TDD and Unit Testing with AI

### RED/GREEN TDD Workflow
1. Write a failing test first (RED)
2. Implement only enough code to make the test pass (GREEN)
3. Refactor if needed
4. Move to next test

### AI-Assisted Testing
- AI writes tests based on user stories
- Code review by both human and AI
- Use eval frameworks for AI-powered features (LangFuse, LangSmith)
- Test skills on subagents to ensure they're comprehensible and complete

## Debugging with AI

AI needs specific information to debug effectively.

### Recommended Scripts to Create
- **trace.sh**: Capture distributed traces across services
- **profile.sh**: Run CPU/memory profilers on specific endpoints
- **debug.sh**: Attach debugger to running process with proper symbols
- **logs.sh**: Aggregate and filter logs from multiple services

Why Scripts Matter:
- AI can run these scripts to gather diagnostic information
- Standardized output formats make it easier for AI to parse
- Reduces back-and-forth when debugging issues
- Creates reproducible debugging workflows

### Providing Debug Information
- **Server Logs**: Copy terminal output from `rails server`, `npm run dev`, `bun run dev`
- **Browser Console**: Right-click -> Inspect Element -> Console tab
- **Network Dev Tools**: Use Network tab to troubleshoot API issues

## Vibe Coding vs Professional SE-Focused Generative Coding

### Vibe Coding
Submits prompts with large brush strokes:
- "Build this feature XYZ"
- "Fix this bug:" *pasted error stack trace*

### SE-Focused Generative Coding
- Minimize errors by focusing on small tasks
- Ask AI to refactor and reduce code
- More deliberate and structured approach
- Example: "Create a function that takes these inputs and produces this output"
- Example: "Refactor this function to improve readability and reduce complexity"
- Test driven development with AI

## AI Agents and Skills System

You can write an AI agent that writes other AI agents. This is how Claude Code is built.

### Skills (Superpowers)
Skills are markdown files that teach agents how to do specific tasks:
- Agents can learn new skills by reading SKILL.md files
- Self-improving agents write their own skills
- TDD for skills: test on subagents to ensure comprehensibility

### Skill Creation Workflow
1. Describe how you want a workflow to work
2. Claude creates or updates SKILL.md files
3. Test skills with pressure scenarios on subagents
4. Iterate until skills are reliable

### Memory Systems for Agents
- Store conversation transcripts outside .claude (prevents auto-deletion)
- Use vector index in SQLite for semantic search
- Generate summaries with fast models (Haiku)
- Search memories via subagents to keep main context clean

### Available Superpowers Skills

| Skill | When to Use |
|-------|-------------|
| `superpowers:using-superpowers` | Starting any conversation |
| `superpowers:brainstorming` | Before any creative work |
| `superpowers:writing-plans` | When you have specs for a multi-step task |
| `superpowers:test-driven-development` | Before writing implementation code |
| `superpowers:using-git-worktrees` | Starting feature work needing isolation |
| `superpowers:subagent-driven-development` | Executing plans with independent tasks |
| `superpowers:systematic-debugging` | When encountering bugs or test failures |
| `superpowers:executing-plans` | When you have a plan to execute |
| `superpowers:verification-before-completion` | Before claiming work is complete |
| `superpowers:finishing-a-development-branch` | When implementation is complete |
| `superpowers:requesting-code-review` | Before merging to verify work |
| `superpowers:receiving-code-review` | When receiving feedback |
| `superpowers:dispatching-parallel-agents` | Facing 2+ independent tasks |
| `superpowers:writing-skills` | Creating or editing skills |

**The 1% Rule**: If you think there is even a 1% chance a skill might apply, you **MUST** invoke it.

## Different AI Models and Tools

Keep on top of the best model of the day - it changes frequently.

### Coding Agents
- **Claude Code**: Superior output quality, excellent tooling (primary choice)
- **OpenAI Codex (GPT 5.2)**: Good for research, aggressive web searching
- **Cursor**: Inferior to Claude Code CLI/extension even with same models
- **Brokk**: Alternative option
- **Gemini**: Mixed results, banned on some projects

### Model Selection
- Same model in Cursor vs Claude Code produces different quality (system prompts matter)
- Use multiple agents to cross-check work
- **Fast models (Haiku)**: Memory summarization, quick tasks
- **Multimodal models (GPT-4o)**: Image processing for RAG

## Key Concepts

### RAG (Retrieval Augmented Generation)
AI models enhanced by retrieving relevant context from external sources (codebase, docs, databases) before generating responses. This allows AI to work with up-to-date, project-specific information.

**Implementation:**
1. **Vector Database**: PGVector (Postgres) or Pinecone
2. **Document Ingestion**: Docling for chunking with LLM summaries
3. **Image Processing**: Store on S3/R2, enrich with multimodal models (GPT-4o)
4. **Embeddings**: OpenAI or Google (Anthropic uses Voyage/MongoDB)

### Embeddings
- Improve RAG with semantic retrieval vs keyword matching
- Like a glossary mapping user terms to expected terminology
- Reduces input tokens by retrieving less, more relevant text

## New Skills to Master

Skills in 2026 that go beyond traditional programming:

- Agents and subagents
- Prompting
- Context management
- RAG patterns and embeddings
- CLI modes
- Tools and plugins
- Skills and hooks
- MCP (Model Context Protocol)
- LSP (Language Server Protocol)
- Slash commands
- Workflows
- IDE integrations

## Useful MCPs

MCPs (Model Context Protocol) provide important context to improve code quality:

### Essential MCPs
- **GitHub**: Full GitHub integration for PRs, issues, actions
- **Jira (Atlassian)**: Project management integration
- **Confluence (Atlassian)**: Documentation integration

### Recommended MCPs
- **Context7**: Up-to-date documentation for any technology
  ```
  claude mcp add --transport http context7 https://mcp.context7.com/mcp --header "CONTEXT7_API_KEY: YOUR_KEY"
  ```
  Add "Use Context7" to prompts for accuracy

- **Figma Dev Mode**: Code Figma designs directly
  ```
  claude mcp add --transport http figma-desktop http://127.0.0.1:3845/mcp
  ```
  Works best with components and autolayout

- **Shopify Dev**: Build Shopify apps and websites
  ```
  claude mcp add shopify-dev-mcp npx @shopify/dev-mcp@latest
  ```

- **Sosumi**: Apple/iOS documentation (https://sosumi.ai/)

Note: MCPs usually need to be installed per-project directory

## Local LLMs

Running models locally provides privacy, cost savings, and offline capability. Trade-off: generally lower quality than cloud APIs.

### Popular Local Models (2026)
- **DeepSeek R1/V3**: Strong reasoning, competitive with frontier models, open weights
- **Kimi K2**: Multi-modal, long context (1M+ tokens), good for document analysis
- **MiniMax**: Fast inference, good for real-time applications
- **Llama 4**: Meta's open model family, excellent fine-tuning ecosystem
- **Qwen 3**: Alibaba's model, strong multilingual and coding
- **Mistral Large**: European alternative, good balance of size/quality

### Local Inference Tools
- **Ollama**: Simple CLI for running models locally (`brew install ollama`)
- **LM Studio**: GUI for downloading and running models
- **vLLM**: High-throughput inference server for production
- **llama.cpp**: C++ inference, runs on CPU, optimized for Apple Silicon

### When to Use Local vs Cloud
| Use Local | Use Cloud |
|-----------|-----------|
| Sensitive/private data | Maximum quality needed |
| High volume, predictable load | Sporadic usage |
| Offline requirements | Latest frontier capabilities |
| Cost optimization | Complex reasoning tasks |

### Hardware Requirements
- **Minimum**: M1/M2 Mac with 16GB RAM, or NVIDIA GPU with 8GB VRAM
- **Recommended**: M3 Pro/Max with 32GB+ RAM, or RTX 4090 with 24GB VRAM
- **Quantization**: Use Q4/Q5 quantized models to reduce memory requirements

## Context Management

### Avoid Compaction
- Code quality drops dramatically after session compaction
- Keep sessions clean and focused
- Use separate sessions for research vs implementation
- Use subagents to search codebase without polluting main context

### Context Window Best Practices
- Let different agents check your plans (they have different training)
- Use research sessions to map codebase, then execute in fresh session
- Markdown is easier for LLMs to parse than plain text
- YAML may be better than JSON for structured data (debatable in 2026)
- Consider TOON format for token efficiency: https://github.com/toon-format/toon

## Building AI-Powered Applications

### Chat UI Frameworks
- **Vercel AI SDK UI**: Comprehensive, well-documented
- **Assistant UI**: Alternative option
- Features to look for: streaming (SSE), auto-resizing textarea, image upload, thinking UI

### Token Optimization
- **Prompt Caching**: All major providers charge less for repeated input tokens
- **Model Routing**: Switch between models based on task complexity (LangGraph or OpenRouter/Vercel AI Gateway)

### AI Agent Frameworks
- **Simple**: Vercel AI SDK, Inngest AgentKit
- **Advanced**: LangGraph (requires architecture knowledge)

### Tools for AI
Tools are code AI can execute to get information:
- Plan tools thoroughly before building
- Follow provider specs: OpenAI, Anthropic
- Or use model-agnostic: LangChain tools, Vercel SDK tools

### Prompt Management
System prompts are critical to success:
- Don't hardcode prompts in app
- Use dependency injection or hosted tools (Vellum, Langsmith)
- Constantly iterate and improve prompts

### Observability / LLM Tracing
- **Posthog LLM Tracing**: Simple, sufficient for most needs
- **LangSmith**: More advanced, higher cost
- Collect user feedback with thumbs up/down on responses

### Eval (Testing AI)
Critical for AI apps - like unit tests but for AI behavior:
- Test for: PII exposure, hallucinations, irrelevant replies, wrong info, toxicity
- Tools: LangFuse, LangSmith
- Use real or synthetic data

### Fine Tuning
Generally avoid unless:
- Massive budget
- Exhausted all other optimization methods
- Warning: Can't migrate to newer models, must retrain

## AI-Powered Operations

- Remediation like pod restart
- Scaling
- Log triage
- Rollback

## Security Best Practices

### Code Security
- Run `/security-review` in Claude Code
- Use SEMGREP in GitHub Actions: https://semgrep.dev/docs/getting-started/quickstart-managed-scans
- Never commit API keys or secrets to git
- Use `.env` files and add to `.gitignore`

### User Data Security
- Lock down S3 buckets for user uploads
- Strip EXIF data from uploaded images (location data)
- Use vaulting/encryption for sensitive data (bank accounts, health info)

### AI Security
- Use PromptFoo to test for common AI security flaws
- Implement guardrails against prompt injection and jailbreaking
- Multiple layers of protection
- Test regularly (uses many tokens, can be expensive)

## Recommended Tech Stack (2026)

### Web Frameworks
- **React**: Front-end, prefer TypeScript
- **Next.js**: Full-stack, front-end + backend
- **Remix**: SSR, preferred for Shopify apps
- **Bun/Express/Fastify**: Backend (Bun is faster Node replacement)
- **Python**: AI/ML tooling, slower but great ecosystem
- **Go**: Extremely fast, harder to debug
- **Ruby on Rails**: Ship CRUD apps fast, slower performance
- **Rust**: High performance, strong type safety

### Mobile
- **React Native + Expo**: Cross-platform
- Native Swift/Kotlin: Limited AI tooling support currently

### Database
- **PostgreSQL**: Default choice
- **Supabase**: Hosted Postgres with great AI tooling
- **PGVector**: Vector storage for AI apps
- **Pinecone**: Dedicated vector database

### Hosting
- **Render.com**: General purpose
- **Fly.io**: Edge computing
- **Vercel**: Great for Next.js/Remix
- Avoid Heroku (outdated)

### Package Managers
- **Bun**: JavaScript (alternative to npm)
- **uv**: Python
- **Bundler**: Ruby

### Build Tools
- **Vite**: Front-end builds

## Useful CLI Tools

### GitHub CLI
`brew install gh` - Automates all GitHub work including CI/CD setup. Claude Code integrates with gh for PR creation, reviews, etc.

Run `/install-github-app` in Claude Code to:
- Install Claude GitHub action
- Auto-review PRs for bugs and issues

## Development Principles

### DRY (Don't Repeat Yourself)
If code appears 3+ times, extract to reusable utility.

### SRP (Single Responsibility Principle)
Each module should do one thing well. Avoid "God Classes/Functions".

### Check for Existing Conventions
AI doesn't always check existing patterns before coding:
```
Please look at the workflow code to identify violations of best practices like DRY and SRP
```

## AI Visualizations

- Ask AI to draw diagrams of architecture
- Generative diagrams of workflows
- Gemini flash 3 can draw full pictures

## Beyond Code Generation

- Write docs and specs
- Make your presentations for you
- Use AI to help you define specs

It won't get everything 100% correct on the first pass. Keep prompting to improve to hit your target goal.

## The Future is Now

Claude Code is already 100% being written by Claude Code. Anthropic has openly stated that they are using AI to write their codebase. Anthropic used Claude with a profiler to fix a memory leak in Claude Code.
TODO:
Anthropic has 4 relases per engineer per day

We are approaching a world where AI is writing and validating code at scale.

## Resources

- [Spec Driven Development - GitHub Spec Kit](https://github.com/github/spec-kit)
