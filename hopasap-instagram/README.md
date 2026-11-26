# hopasap — Instagram Reel (HyperFrames project)

A 20 s vertical (1080 × 1920) Czech-language Instagram Reel for **hopasap**, built with [HyperFrames](https://hyperframes.heygen.com): HTML, CSS and GSAP rendered to video, and editable in the browser. Reel 2 is next door in [`../hopasap-instagram-2/`](../hopasap-instagram-2/).

▶ **Final video:** run `npm run render` in this folder; it writes `renders/hopasap-instagram-final.mp4` (renders are not stored in the repo).

## Open it and keep editing

Requirements: Node.js 22+, `ffmpeg`/`ffprobe` on PATH, and Chrome or another Chromium browser. Run these **inside this folder** (`hopasap-instagram/`):

```bash
npx --yes hyperframes@0.9.96 preview --background   # starts Studio in the background
npx --yes hyperframes@0.9.96 preview --status       # prints the Studio URL to open
```

Open the printed Studio URL, e.g. `http://localhost:3002/#project/hopasap-instagram`, in your browser.

| Command | What it does |
| --- | --- |
| `npm run check` | Lint plus runtime, layout and contrast checks. Run after every edit. |
| `npm run render` | Renders `renders/hopasap-instagram-final.mp4` at delivery quality. |
| `npx --yes hyperframes@0.9.96 preview --stop` | Stops the background preview. |

Handing this to someone with an AI coding agent? Give them [`../HANDOFF.md`](../HANDOFF.md).

## What's inside

```text
index.html                  root composition: footage, camera wrapper, audio, scene hosts
compositions/captions.html  Czech subtitles (one captions track, word-by-word highlight)
compositions/car-hype.html  car-reveal light effects (flash, streaks, vignette, leak, sheen)
compositions/logo-end.html  logo end card
assets/clips/processed/     plate-blurred, voice-cleaned, SDR clips (full length)
assets/audio/               continuous clean voice for clip 3
assets/sfx/                 custom sound effects (generated with ElevenLabs)
assets/music/               hip-hop beat under the car reveal (ElevenLabs)
assets/hopasap-logo-reversed.svg
processing/                 scripts and data used to make the processed clips
BRIEF.md                    timeline, decisions and editing conventions
```

The original iPhone footage is intentionally **not** included: it has unblurred number plates and GPS metadata.

## Credits

- Built with HyperFrames by HeyGen (Apache-2.0). The skills in the repo's `skills/` folder are from [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes); see `../skills/LICENSE-hyperframes`.
- Plate detection: YOLOv11 licence-plate model by morsetechlab (Hugging Face).
- Sound effects, beat and end-card voice: ElevenLabs.
