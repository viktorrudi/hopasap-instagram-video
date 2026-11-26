# Handoff prompt

Paste everything below the line into your coding agent (Claude Code, Codex or similar) on your own machine.

---

You are taking over two Instagram Reel projects built with **HyperFrames**, HeyGen's open-source HTML-to-video framework. Both videos are in Czech, for the brand **hopasap**. Get them running locally and open both in my main browser so I can keep editing.

**Repository:** https://github.com/viktorrudi/hopasap-instagram-video

The repo holds **two separate recordings**. Each one is its own, independent HyperFrames project in its own folder:

| Folder | Video | Final render |
| --- | --- | --- |
| `hopasap-instagram/` | Reel 1, "the Daihatsu" (20 s): the yellow Lamborghini, then the old silver Daihatsu reveal | `hopasap-instagram/renders/hopasap-instagram-final.mp4` |
| `hopasap-instagram-2/` | Reel 2, "the van" (18.5 s): the go-kart hall, then the old red Opel van reveal | `hopasap-instagram-2/renders/hopasap-instagram-2-final.mp4` |

The repo root only holds `README.md`, this `HANDOFF.md` and the shared `skills/` folder. **Every HyperFrames and npm command runs inside a reel's folder, never in the repo root.**

## 1. Check the tools, and install anything missing (ask me before installing)

- `git`
- Node.js **22 or newer**, with `npm` and `npx` (`node --version`)
- `ffmpeg` and `ffprobe` on PATH (macOS: `brew install ffmpeg`; Ubuntu: `sudo apt install ffmpeg`; Windows: `winget install ffmpeg`)
- Google Chrome or another Chromium browser as my main browser. HyperFrames downloads its own headless Chrome for rendering on first use.
- Optional: Python 3.10+, only to re-run the scripts in each `processing/` folder (they need the original footage, which is not in the repo).
- Optional: an ElevenLabs API key, only if new sound effects should be generated.

## 2. Get the repo

**If I already set up this repo from the earlier prompt** (it used to contain only reel 1, at the repo root), update the existing clone instead of cloning again. Reel 1 has moved into `hopasap-instagram/`.

1. Go to the existing clone and stop the old preview **before** pulling, while the root is still a project: `npx --yes hyperframes@0.9.96 preview --stop`
2. Run `git status`. If there are local changes to tracked files, show me what they are and ask whether to commit or stash them. Don't discard anything.
3. `git pull`. Git moves the reel 1 files into `hopasap-instagram/` and adds `hopasap-instagram-2/`. If you previously copied the skills into `.claude/skills` or `.agents/skills` at the repo root, they still work there.

**Otherwise, clone fresh:**

```bash
git clone https://github.com/viktorrudi/hopasap-instagram-video.git
cd hopasap-instagram-video
```

## 3. Load the skills

The repo vendors the HyperFrames agent skills (Apache-2.0) in `skills/` at the repo root, shared by both reels. Install them where you, the agent, load skills, scoped to this repo (run these in the repo root):

- Claude Code: `mkdir -p .claude/skills && cp -R skills/* .claude/skills/`
- Codex and other agents that read `.agents/skills`: `mkdir -p .agents/skills && cp -R skills/* .agents/skills/`

Skip this if they are already installed from the earlier setup. Then reload or restart yourself so the skills are picked up. Read `skills/hyperframes/SKILL.md` first; it is the entry point and routes to the others. To refresh the skills to the latest release instead, run `npx hyperframes skills update`.

## 4. Read the project notes

Read the root `README.md`, then each reel's `README.md` and `BRIEF.md` (timeline, building blocks, editing conventions). Each reel's `AGENTS.md` / `CLAUDE.md` are the HyperFrames project rules.

## 5. Start both editors and open them in my main browser

Start a background Studio preview in **each** reel folder. They run at the same time on different ports:

```bash
cd hopasap-instagram
npx --yes hyperframes@0.9.96 preview --background
npx --yes hyperframes@0.9.96 preview --status
cd ../hopasap-instagram-2
npx --yes hyperframes@0.9.96 preview --background
npx --yes hyperframes@0.9.96 preview --status
```

Each status output prints a **Studio** URL, e.g. `http://localhost:3002/#project/hopasap-instagram` and `http://localhost:3003/#project/hopasap-instagram-2`. The ports can differ, so use the ones printed. Open both exact URLs in my default browser, one tab each:

- macOS: `open "<Studio URL>"`
- Linux: `xdg-open "<Studio URL>"`
- Windows: `start "" "<Studio URL>"`

The first load may take a minute while HyperFrames builds preview caches. Changes to the HTML files reload in the browser automatically. Stop a preview later by running `npx --yes hyperframes@0.9.96 preview --stop` inside that reel's folder.

## 6. Working rules

- Always know which reel I'm talking about. "The van", "the Opel", "the go-kart" or "video 2" means `hopasap-instagram-2/`. "The Daihatsu", "the Lamborghini" or "video 1" means `hopasap-instagram/`. If it's unclear, ask me.
- In each reel, the composition lives in `index.html`, with scenes in `compositions/` (`captions.html`, `car-hype.html`, `logo-end.html`).
- After every edit, run `npm run check` in that reel's folder and fix all errors. Then look at the moments you changed with `npx --yes hyperframes@0.9.96 snapshot --at <seconds>`.
- Render with `npm run render` in the reel's folder: 1080 × 1920, 30 fps, about −15 LUFS. For a smaller upload copy (under 25 MB), use the two-pass ffmpeg command in `hopasap-instagram-2/BRIEF.md` (it works for either reel; change the file names).
- Subtitles are Czech. The brand name is always lowercase "hopasap". Brand colours are orange `#FF5A36` and white.
- In both reels, clip 3 (the car reveal) is muted. Its voice comes from `#clip-03-voice`, and the reveal effects (speed ramp, `#hype-cam` keyframes, sparkles, sound effects, beat and the `car-hype` host) are timed to it. If you retime clip 3, move them together; each `BRIEF.md` lists the times.
- Reel 2's clip 3 has a speed ramp that uses exactly as much source as it lasts, so the picture stays in sync with the voice. Keep that balance if you change it (see `hopasap-instagram-2/BRIEF.md`).
- Never add or publish the original iPhone `.MOV` files. They contain unblurred number plates and GPS location.

Once both Studios are open in my browser, tell me both URLs and which reel each one is. Then wait for my editing instructions.
