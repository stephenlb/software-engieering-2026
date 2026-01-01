# Software Engineering in 2026

Are you already behind? Probably! Let's fix that.

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

## You Engineering Experties is needed more than ever
Now that the typing and manual clicking on your computer is mostly solved by AI, your role as an engineer is shifting.

### Director of Agents
Our work as engineers and architects now is much harder - we need to pay extra care for architecture, planning, testing, verifying, making sure we stand to KPIs
and then provide approvals as a Director of Agents.

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

## AI make Visualizations
 - ask AI to draw diagrams of architecture
 - Generative diagrams of workflows
 - Gemini flash 3 draw full pictures

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

## Beyond just AI

 - Using 🦀 Rust for all new code
     - clippy fmt audit
 - More Rustdoc tripple slashes
 - Strong type checking
 - With Python use type checkers like mypy

## Yes it's Already Starting

Claude Code is already 100% being written by Claude Code.
Anthropic has openly stated that they are using 100% of AI to write their codebase.
Yes it is scary.
Anthropic used Claude with a profiler to fix a memory leak in claude code
The skynet scenario is closer than you think.
Well maybe not the distopian skynet scenario, but definitely a world where AI is writing and validating code.
We are appriaching the 2028 Singularity faster than you think.

## Beyond COde Generation
 - Write docs and specs
 - Make your presentations for you

It won't get everying 100% correct on the first pass.
Keep prompting to improve to hit your target goal.

## 
like having scripts that you can run to get traces profilers debugers on the product is so useful

## Ask AI to Use Tools
 - Use linters
 - Use type checkers
 - Use test runners
 - Use Profilers

## AI Validation "reading"

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

AI needs specific information to debug effectively:

### Server Logs
- Copy terminal output from `rails server`, `npm run dev`, `bun run dev`
- Paste into Claude Code for troubleshooting

### Browser Console
- Right-click -> Inspect Element -> Console tab
- Copy JavaScript errors and logs for front-end debugging

### Network Dev Tools
- Use Network tab to troubleshoot API issues
- Search for specific requests to diagnose problems


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
- Test driven development with AI "common well defined processes that have been proven to work well"

## AI Agents written by AI Agents "Claude Code"

You can write an AI agent that writes other AI agents.
This is how Claude Code is built as mentioned above.

### Skills System (Superpowers)
- Skills are markdown files that teach agents how to do specific tasks
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


## Different AI Models and Tools

Keep on top of the best model of the day - it changes frequently.

### Coding Agents
- **Claude Code**: Superior output quality, excellent tooling
- **OpenAI Codex (GPT 5.2)**: Good for research, aggressive web searching
- **Cursor**: Inferior to Claude Code CLI/extension even with same models
- **Brokk**: Alternative option
- **Gemini**: Mixed results, banned on some projects

### Model Comparison Notes
- Same model in Cursor vs Claude Code produces different quality (system prompts matter)
- Use multiple agents to cross-check work
- Different agents trained on different technologies

### When to Use Each
- **Claude Code**: Primary coding agent
- **OpenAI Codex**: Double-check Claude's work, research with web search
- **Fast models (Haiku)**: Memory summarization, quick tasks
- **Multimodal models (GPT-4o)**: Image processing for RAG

## Github CLI
gh tool in Claude Code so it automates all my github work including setting up CI/CD and whatnot. `brew install gh`

## More Than Just Coding

- Tasklet
- AI writes tests
- Code review by human and AI
- You should still skim code changes
- Use AI to help you define specs

## Key Concepts

### RAG (Retrieval Augmented Generation)
AI models enhanced by retrieving relevant context from external sources (codebase, docs, databases) before generating responses. This allows AI to work with up-to-date, project-specific information rather than relying solely on training data.

## New Skills to Master

Skills in 2026 that go beyond traditional programming:

- Agents and subagents
  -  use a coding agents subagents feature - so for example, work that would take 2 days sequentially would take 4 hours with parallel subagents spawn by claude
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

## Resources

- [Spec Driven Development - GitHub Spec Kit](https://github.com/github/spec-kit)

## Local LLMS
TODO fill out
 - GPT OSS
 - Kimi K2
 - MiniMax
 - DeepSeek


## Agents and Size Matters
Smaller, faster agents are better for many tasks.
Tradeoff of speed vs accuracy.

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

### RAG (Retrieval Augmented Generation)
AI models enhanced by retrieving relevant context from external sources before generating responses.

Implementation:
1. **Vector Database**: PGVector (Postgres) or Pinecone
2. **Document Ingestion**: Docling for chunking with LLM summaries
3. **Image Processing**: Store on S3/R2, enrich with multimodal models (GPT-4o)
4. **Embeddings**: OpenAI or Google (Anthropic uses Voyage/MongoDB)

### Embeddings
- Improve RAG with semantic retrieval vs keyword matching
- Like a glossary mapping user terms to expected terminology
- Reduces input tokens by retrieving less, more relevant text

### Token Optimization
- **Prompt Caching**: All major providers charge less for repeated input tokens
- **Model Routing**: Switch between models based on task complexity
  - Use LangGraph or OpenRouter/Vercel AI Gateway

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


## Fringe AI with AI powered Operations
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
- Don't vibe code fintech or healthcare apps without expertise

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

### Static Analysis & Linters
- **Biome.js**: JavaScript
- **StyleLint**: CSS
- **Ruff**: Python
- **Rubocop**: Ruby
- **golangci-lint**: Go

### Type Systems
- **TypeScript**: JavaScript
- **BasedPydantic**: Python (watch for Astral's `ty`)
- **Sorbet**: Ruby

### Package Managers
- **Bun**: JavaScript (alternative to npm)
- **uv**: Python
- **Bundler**: Ruby

### Build Tools
- **Vite**: Front-end builds

## Useful CLI Tools

### GitHub CLI
`brew install gh` - Automates all GitHub work including CI/CD setup.
Claude Code integrates with gh for PR creation, reviews, etc.

### Code Review with GitHub Actions
Run `/install-github-app` in Claude Code to:
- Install Claude GitHub action
- Auto-review PRs for bugs and issues

### Development Principles

#### DRY (Don't Repeat Yourself)
If code appears 3+ times, extract to reusable utility.

#### SRP (Single Responsibility Principle)
Each module should do one thing well. Avoid "God Classes/Functions".

#### Check for Existing Conventions
AI doesn't always check existing patterns before coding:
```
Please look at the workflow code to identify violations of best practices like DRY and SRP
```
# Claude Code Superpowers Skills

A comprehensive guide to the superpowers skills available in Claude Code for AI-powered software development.

## What are Superpowers?

Superpowers are specialized workflows and best practices built into Claude Code that help structure complex development tasks. They provide rigorous, battle-tested approaches to common software engineering challenges.

## Available Skills

### Getting Started

#### `superpowers:using-superpowers`
**When to use:** Starting any conversation

Establishes how to find and use skills, requiring Skill tool invocation before ANY response including clarifying questions. This is the foundational skill that teaches Claude Code how to properly leverage all other skills.

---

### Planning & Design

#### `superpowers:brainstorming`
**When to use:** Before any creative work - creating features, building components, adding functionality, or modifying behavior

Explores user intent, requirements and design before implementation. **MUST use this before creative work.**

#### `superpowers:writing-plans`
**When to use:** When you have a spec or requirements for a multi-step task, before touching code

Creates detailed implementation plans that break down complex tasks into manageable steps with clear checkpoints.

---

### Development Workflows

#### `superpowers:test-driven-development`
**When to use:** When implementing any feature or bugfix, before writing implementation code

Ensures tests are written first, driving the design and implementation of reliable, well-tested code.

#### `superpowers:using-git-worktrees`
**When to use:** Starting feature work that needs isolation from current workspace or before executing implementation plans

Creates isolated git worktrees with smart directory selection and safety verification, allowing you to work on multiple features simultaneously without conflicts.

#### `superpowers:subagent-driven-development`
**When to use:** Executing implementation plans with independent tasks in the current session

Coordinates multiple parallel development streams for efficient task completion.

---

### Debugging & Problem Solving

#### `superpowers:systematic-debugging`
**When to use:** When encountering any bug, test failure, or unexpected behavior, before proposing fixes

Provides a structured approach to identifying root causes and implementing proper fixes rather than quick patches.

---

### Execution & Completion

#### `superpowers:executing-plans`
**When to use:** When you have a written implementation plan to execute in a separate session with review checkpoints

Guides the execution of implementation plans with structured review points to ensure quality.

#### `superpowers:verification-before-completion`
**When to use:** When about to claim work is complete, fixed, or passing, before committing or creating PRs

Requires running verification commands and confirming output before making any success claims - evidence before assertions always.

#### `superpowers:finishing-a-development-branch`
**When to use:** Implementation is complete, all tests pass, and you need to decide how to integrate the work

Guides completion of development work by presenting structured options for merge, PR, or cleanup.

---

### Collaboration & Review

#### `superpowers:requesting-code-review`
**When to use:** Completing tasks, implementing major features, or before merging to verify work meets requirements

Structures code review requests to ensure thorough evaluation of changes.

#### `superpowers:receiving-code-review`
**When to use:** Receiving code review feedback, before implementing suggestions

Requires technical rigor and verification, not performative agreement or blind implementation - especially if feedback seems unclear or technically questionable.

---

### Parallel Workflows

#### `superpowers:dispatching-parallel-agents`
**When to use:** Facing 2+ independent tasks that can be worked on without shared state or sequential dependencies

Maximizes efficiency by running independent tasks concurrently.

---

### Meta: Building Skills

#### `superpowers:writing-skills`
**When to use:** Creating new skills, editing existing skills, or verifying skills work before deployment

A meta-skill for extending the superpowers system itself with new workflows and best practices.

---

## Key Principles

### The 1% Rule
If you think there is even a 1% chance a skill might apply to what you are doing, you **MUST** invoke the skill. This is not negotiable.

### Skill Priority
When multiple skills could apply:
1. **Process skills first** (brainstorming, debugging) - these determine HOW to approach the task
2. **Implementation skills second** - these guide execution

### Skill Types
- **Rigid skills** (TDD, debugging): Follow exactly. Don't adapt away discipline.
- **Flexible skills** (patterns): Adapt principles to context.

---

## Common Anti-Patterns to Avoid

| ❌ Rationalization | ✅ Reality |
|-------------------|-----------|
| "This is just a simple question" | Questions are tasks. Check for skills. |
| "I need more context first" | Skill check comes BEFORE clarifying questions. |
| "Let me explore the codebase first" | Skills tell you HOW to explore. Check first. |
| "I can check git/files quickly" | Files lack conversation context. Check for skills. |
| "This doesn't need a formal skill" | If a skill exists, use it. |
| "The skill is overkill" | Simple things become complex. Use it. |
