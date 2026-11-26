# hopasap — Instagram Reels (HyperFrames projects)

Two vertical (1080 × 1920) Czech-language Instagram Reels for **hopasap**, built with [HyperFrames](https://hyperframes.heygen.com): HTML, CSS and GSAP rendered to video, and editable in the browser. Each reel is its own HyperFrames project in its own folder.

| Folder | Reel | Length | Story |
| --- | --- | --- | --- |
| [`hopasap-instagram/`](hopasap-instagram/) | Reel 1: the Daihatsu | 20 s | She heads for a yellow Lamborghini, he stops her and shows her an old silver Daihatsu. |
| [`hopasap-instagram-2/`](hopasap-instagram-2/) | Reel 2: the van | 18.5 s | Go-kart hall, then he shows her an old red Opel van. She pulls off her balaclava. |

Both end on the hopasap logo with the voiceover "Již brzy v Brně a okolí." They share the same caption style, end card, sound effects and reveal treatment (speed ramp, punch-in, sparkles, light effects).

## Open a reel and keep editing

Requirements: Node.js 22+, `ffmpeg`/`ffprobe` on PATH, and Chrome or another Chromium browser. Every command runs **inside the reel's folder**:

```bash
cd hopasap-instagram-2                               # or hopasap-instagram
npx --yes hyperframes@0.9.96 preview --background   # starts Studio in the background
npx --yes hyperframes@0.9.96 preview --status       # prints the Studio URL to open
npm run check                                       # after every edit
npm run render                                      # final MP4 in renders/ (not committed)
npx --yes hyperframes@0.9.96 preview --stop         # when done
```

Both previews can run at the same time; each gets its own port.

Handing this to someone with an AI coding agent? Give them [`HANDOFF.md`](HANDOFF.md).

## Layout

```text
hopasap-instagram/     reel 1 (README.md, BRIEF.md, index.html, compositions/, assets/, processing/)
hopasap-instagram-2/   reel 2 (same structure)
skills/                HyperFrames agent skills (Apache-2.0, vendored), shared by both reels
HANDOFF.md             setup prompt for the next person's coding agent
```

The original iPhone footage is intentionally **not** included: it has unblurred number plates and GPS metadata.

## Credits

- Built with HyperFrames by HeyGen (Apache-2.0). The skills in `skills/` are from [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes); see `skills/LICENSE-hyperframes`.
- Plate detection: YOLOv11 licence-plate model by morsetechlab (Hugging Face).
- Sound effects, beat and end-card voice: ElevenLabs.
