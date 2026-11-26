# Handoff prompt

Paste everything below the line into your coding agent (Claude Code, Codex or similar) on your own machine.

---

You are taking over an Instagram Reel project built with **HyperFrames**, HeyGen's open-source HTML-to-video framework. The video is in Czech, for the brand **hopasap**. Get it running locally and open it in my main browser so I can keep editing.

**Repository:** https://github.com/viktorrudi/hopasap-instagram-video

## 1. Check the tools, and install anything missing (ask me before installing)

- `git`
- Node.js **22 or newer**, with `npm` and `npx` (`node --version`)
- `ffmpeg` and `ffprobe` on PATH (macOS: `brew install ffmpeg`; Ubuntu: `sudo apt install ffmpeg`; Windows: `winget install ffmpeg`)
- Google Chrome or another Chromium browser as my main browser. HyperFrames downloads its own headless Chrome for rendering on first use.
- Optional: Python 3.10+, only to re-run the scripts in `processing/` (they need the original footage, which is not in the repo).
- Optional: an ElevenLabs API key, only if new sound effects should be generated.

## 2. Clone the repo and load the skills

```bash
git clone https://github.com/viktorrudi/hopasap-instagram-video.git
cd hopasap-instagram-video
```

The repo vendors the HyperFrames agent skills (Apache-2.0) in `skills/`. Install them where you, the agent, load skills, scoped to this project:

- Claude Code: `mkdir -p .claude/skills && cp -R skills/* .claude/skills/`
- Codex and other agents that read `.agents/skills`: `mkdir -p .agents/skills && cp -R skills/* .agents/skills/`

Then reload or restart yourself so the skills are picked up. Read `skills/hyperframes/SKILL.md` first; it is the entry point and routes to the others. To refresh the skills to the latest release instead, run `npx hyperframes skills update`.

## 3. Read the project notes

Read `BRIEF.md` (timeline, building blocks, editing conventions) and `README.md`. `AGENTS.md` / `CLAUDE.md` are the HyperFrames project rules.

## 4. Start the editor and open it in my main browser

```bash
npx --yes hyperframes@0.9.96 preview --background
npx --yes hyperframes@0.9.96 preview --status
```

The status output prints a **Studio** URL, e.g. `http://localhost:3002/#project/hopasap-instagram`. The port can differ, so use the one printed. Open that exact URL in my default browser:

- macOS: `open "<Studio URL>"`
- Linux: `xdg-open "<Studio URL>"`
- Windows: `start "" "<Studio URL>"`

The first load may take a minute while HyperFrames builds preview caches. Changes to the HTML files reload in the browser automatically. Stop the preview later with `npx --yes hyperframes@0.9.96 preview --stop`.

## 5. Working rules

- The composition lives in `index.html`, with scenes in `compositions/` (`captions.html`, `car-hype.html`, `logo-end.html`).
- After every edit, run `npx --yes hyperframes@0.9.96 check` and fix all errors. Then look at the moments you changed with `npx --yes hyperframes@0.9.96 snapshot --at <seconds>`.
- Render the final with `npm run render`, which writes `renders/hopasap-instagram-final.mp4`: 1080 × 1920, 30 fps, about −15 LUFS.
- Subtitles are Czech. The brand name is always lowercase "hopasap". Brand colours are orange `#FF5A36` and white.
- Clip 3 (the car) is muted. Its voice comes from `#clip-03-voice`, and the reveal effects are timed to it. If you retime clip 3, move the voice, sound effects, `#hype-cam` keyframes, sparkles and the `car-hype` host together (see `BRIEF.md`).
- Never add or publish the original iPhone `.MOV` files. They contain unblurred number plates and GPS location.

Once Studio is open in my browser, tell me the URL. Then wait for my editing instructions.
