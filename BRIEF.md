---
workflow: hyperframes
flow: companion
storyboard: no
destination: instagram
aspect: "9:16"
status: delivered
---
# hopasap — Instagram Reel

A 20 s vertical (1080 × 1920, 30 fps) Czech-language Instagram reel for the brand **hopasap**. The story: a woman looks for hopasap and heads for a yellow Lamborghini. A guy stops her ("Ne, ne, ne! Tohle není hopasap. Pojď sem!"), shows her an old silver Daihatsu ("Tohle je hopasap."), and the car is revealed with over-the-top hype effects. It ends on a black pause and the hopasap logo, with the voiceover "Již brzy v Brně a okolí."

Final render: `renders/hopasap-instagram-final.mp4` (-15 LUFS, peak -1.8 dBFS).

## Timeline (root `index.html`)

| Time (s) | What |
| --- | --- |
| 0 – 5.832 | Clip 1 (IMG_4752): "Ah, hopasap! Skvělý, jdu na to." She walks to the Lamborghini. |
| 5.84 – 9.44 | Clip 2 (IMG_4754): "Ne, ne, ne! Tohle není hopasap. Pojď sem!" |
| 9.44 – 10.474 | Clip 3a (IMG_4755): "Tohle…" while he points at the car. |
| 10.47 – 12.467 | Clip 3b: speed ramp (2.65× → 0.42× slow motion → 1× at the cut), "…je hopasap." |
| 12.47 – 16.096 | Clip 3c: pan across the car front, then the pull-back. |
| 16.096 – 16.62 | Intentional black pause (the editor's choice). |
| 16.62 – 20 | Logo end card on black. Voiceover at 17.0 s: "Již brzy v Brně a okolí." (subtitled under the logo). |

Clips 4 and 5 (tunnel and taxi) were cut. Their processed files remain in `assets/clips/processed/` in case they are wanted back.

## Building blocks

- **Footage.** `assets/clips/processed/IMG_*.mp4`: full-length, 1080 × 1920, 60 fps H.264. iPhone HLG was tone-mapped to SDR with HyperFrames' hable curve. Number plates are blurred (YOLOv11 plate detector, smoothed tracks, feathered blur), and the audio is voice-cleaned. Timing matches the iPhone originals, so `data-media-start` values are original-file seconds. The originals are not in the repo: they contain unblurred plates and GPS metadata.
- **Audio.** Each clip's audio chain: mono, 85 Hz high-pass, RNNoise (`arnndn`), FFT denoise, EQ (−2.5 dB at 230 Hz, +3 dB at 3.2 kHz), de-esser, compressor, gain to about −14 LUFS and a limiter (`processing/clean_audio.sh`). Clip 3's three video pieces are muted. Their voice plays from one continuous track, `#clip-03-voice` (`assets/audio/IMG_4755-clean.wav`), so speech is natural through the slow motion.
- **Voiceover.** `assets/audio/vo-jiz-brzy-v-brne.mp3` (ElevenLabs voice, supplied by the client), played at 17.0 s as `#vo-jiz-brzy`.
- **Sound effects.** `assets/sfx/el-*.mp3` were generated with ElevenLabs: ramp whoosh, slow-mo bass drop, two chrome glints, the cut swoosh and the logo "neon switch-on".
- **Car reveal, visuals.**
  - `#hype-cam` is an untimed wrapper around clips 3b and 3c. The main timeline in `index.html` keyframes on it: a punch-in to 1.14 with an impact shake at 11.19 s, a slow push, a pull-out from 1.22 at the 12.47 s cut, a push during the pan and a settle.
  - Four `.sparkle` stars ride inside the wrapper, on positions measured from the footage (headlight at 11.4 s, badge at 12.88 s).
  - `compositions/car-hype.html` holds the screen-space light: impact flash, anamorphic streak and bloom on the headlight, vignette, brand-orange light leak, cut flash, a sheen sweep masked to the car body, and a badge streak.
- **Captions.** `compositions/captions.html` is one captions track with 8 static, editable groups. Each spoken word lights up on an orange pill. "hopasap" is always brand orange on a near-black pill. Word times come from spectrograms plus Whisper large-v3 / Parakeet, corrected by the editor.
- **End card.** `compositions/logo-end.html`: the logo flickers on like a neon sign, then gets a brand-orange glow, a shine sweep and a sparkle, and holds until the end.

## Brand

- Logo: `assets/hopasap-logo-reversed.svg`, the reversed version for dark backgrounds.
- Colours: orange `#FF5A36` and white.
- The brand name is always written lowercase: "hopasap".

## Conventions for edits

- Run `npm run check` after every edit (0 errors, 0 warnings at delivery). Snapshot the changed moments before rendering.
- Moving or trimming any clip-3 piece requires moving `#clip-03-voice`, the SFX, the `#hype-cam` keyframes, the sparkle positions and the `car-hype` host to match.
- `processing/` holds the scripts and data that produced the processed clips (plate tracks, audio chain). Re-running them needs the original MOVs, which are not in this repo.
