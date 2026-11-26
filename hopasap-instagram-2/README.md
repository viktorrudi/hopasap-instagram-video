# hopasap — Instagram Reel 2: the van (HyperFrames project)

An 18.5 s vertical (1080 × 1920) Czech-language Instagram Reel for **hopasap**, built with [HyperFrames](https://hyperframes.heygen.com). Reel 1 is next door in [`../hopasap-instagram/`](../hopasap-instagram/).

▶ **Final video:** run `npm run render` in this folder; it writes `renders/hopasap-instagram-2-final.mp4` (renders are not stored in the repo).

## Open it and keep editing

Requirements: Node.js 22+, `ffmpeg`/`ffprobe` on PATH, and Chrome or another Chromium browser. Run these **inside this folder** (`hopasap-instagram-2/`):

```bash
npx --yes hyperframes@0.9.96 preview --background   # starts Studio in the background
npx --yes hyperframes@0.9.96 preview --status       # prints the Studio URL to open
```

Open the printed Studio URL, e.g. `http://localhost:3003/#project/hopasap-instagram-2`, in your browser.

| Command | What it does |
| --- | --- |
| `npm run check` | Lint plus runtime, layout and contrast checks. Run after every edit. |
| `npm run render` | Renders `renders/hopasap-instagram-2-final.mp4` at delivery quality. |
| `npx --yes hyperframes@0.9.96 preview --stop` | Stops the background preview. |

`BRIEF.md` has the timeline, the van-reveal effects and how to make the smaller (< 25 MB) upload copy.

## What's inside

```text
index.html                  root composition: footage, speed ramp, camera wrapper, sparkles, audio, scene hosts
compositions/captions.html  Czech subtitles (one captions track, word-by-word highlight)
compositions/car-hype.html  van-reveal light effects (flash, streak, bloom, vignette, leak, sheen)
compositions/logo-end.html  logo end card
assets/clips/processed/     plate-blurred, voice-cleaned, SDR clips (full length)
assets/audio/               continuous clean voice for clip 3, end-card voiceover
assets/sfx/, assets/music/  ElevenLabs sound effects and the hip-hop beat
processing/                 scripts and data used to make the processed clips
BRIEF.md                    timeline, decisions and editing conventions
```

The original iPhone footage is intentionally **not** included: it has unblurred number plates and GPS metadata.
