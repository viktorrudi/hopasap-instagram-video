# HyperFrames agent skills (vendored)

These are the [HyperFrames](https://github.com/heygen-com/hyperframes) agent skills by HeyGen, licensed Apache-2.0 (see `LICENSE-hyperframes`). They are copied here unchanged so that a coding agent can work on this project with the same guidance it was built with.

Install them for your agent, scoped to this project:

- Claude Code: `mkdir -p .claude/skills && cp -R skills/* .claude/skills/`
- Codex and other agents that read `.agents/skills`: `mkdir -p .agents/skills && cp -R skills/* .agents/skills/`

Start with `hyperframes/SKILL.md`. To get the newest release instead, run `npx hyperframes skills update`.
