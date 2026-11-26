---
workflow: hyperframes
flow: companion
storyboard: no
destination: instagram
aspect: "9:16"
status: delivered
---
# hopasap — Instagram Reel 2 (the van)

The second 18.5 s vertical (1080 × 1920, 30 fps) Czech-language Instagram reel for **hopasap**, made in the same style as reel 1 (`../hopasap-instagram/`). The story: in a go-kart hall she heads for a kart, and he stops her ("Ne, ne. Tohle není hopasap. Pojď."). Outside he shows her an old red Opel van ("Tohle je hopasap!"), which gets the over-the-top reveal treatment. She pulls off her balaclava ("Ah, hopasap! Tak já jdu na to."), he says "Na shledanou." and walks off. It ends on the hopasap logo with the voiceover "Již brzy v Brně a okolí."

Final render: `npm run render` writes `renders/hopasap-instagram-2-final.mp4` (about −15.5 LUFS, peak −1.0 dBFS). Renders are not committed.

## Timeline (root `index.html`)

| Time (s) | What |
| --- | --- |
| 0 – 3.41 | Clip 1 (IMG_4760, source 1.41 s on): go-kart hall, no dialogue. |
| 3.41 – 6.81 | Clip 2 (IMG_4768, source 5.6 s on): "Ne, ne. Tohle není hopasap. Pojď." The first, unscripted run of the line (source 1.4–4.7 s) is not used. |
| 6.81 – 14.51 | Clip 3 (IMG_4772, source 1.3 s on): the van. "Tohle je hopasap!" → speed ramp and reveal (8.43–9.82) → "Ah, hopasap! Tak já jdu na to." → "Na shledanou." and the walk-off. |
| 14.51 – 18.51 | Logo end card. Logo "neon switch-on" sound at 14.51, voiceover "Již brzy v Brně a okolí." at 15.15 (subtitled under the logo). |

"Na shledanou" was said twice in IMG_4772 (two takes). `#clip-03-voice` stops after the first one, so the repeat is not heard while the picture runs through the walk-off.

## Building blocks

- **Footage.** `assets/clips/processed/IMG_*.mp4`: full-length, 1080 × 1920, 60 fps H.264, tone-mapped from iPhone HLG to SDR, plates blurred (IMG_4772 only), audio voice-cleaned. Timing matches the iPhone originals, so `data-media-start` values are original-file seconds. See `processing/README.md`.
- **Clip 3 voice.** The clip-3 video is muted. Its voice plays from one continuous track, `#clip-03-voice` (`assets/audio/IMG_4772-clean.wav`), so speech stays natural through the speed ramp.
- **Van reveal, picture.**
  - Speed ramp on `#clip-03-img-4772` (`data-automation`, `rate` lane, clip-local seconds): 1x → 3x whip onto the van at 8.43 s, 0.4x slow motion on the headlight 8.88–9.67 s, back to 1x at 9.82 s. The ramp uses exactly as much source as it lasts, so the picture is back in sync with the voice from 9.82 s. If you change the ramp, keep that balance or lip sync drifts.
  - `#hype-cam` is an untimed wrapper around clip 3. The main timeline keyframes it: a small push during the whip, a punch-in to 1.16 with an impact shake at 8.84 s, a slow push to 1.22, a pull-out at 9.81 s, a push across the van front and a settle at 11.46 s.
  - Four `.sparkle` stars ride inside the wrapper on positions measured from the footage: the headlight at 8.99 / 9.15 s and the Opel badge and grille chrome at 11.31 / 11.45 s.
  - `compositions/car-hype.html` (host 8.43–12.03 s) holds the screen-space light: impact flash, anamorphic streak and bloom on the headlight, vignette, brand-orange light leak, a soft flash at the return to 1x, a sheen sweep masked to the van front, and a badge streak.
- **Van reveal, sound.** ElevenLabs SFX (`assets/sfx/el-*.mp3`, shared with reel 1): ramp whoosh 8.43, slow-mo bass drop 8.84, glint 8.99 (headlight) and 11.31 (badge), swoosh 9.78 with the sheen. The hip-hop beat `#music-beat` (`assets/music/beat-hiphop-90bpm.mp3`) starts on the 8.84 s impact, ducks under "Ah, hopasap!" and "Tak já jdu na to", and fades out at 11.69 s.
- **Captions.** `compositions/captions.html`, one captions track, same style as reel 1: each spoken word lights up on an orange pill, "hopasap" is always brand orange on a near-black pill. The host starts at 3.41 s with `data-playback-start="7.887"`, so times inside `captions.html` are 4.477 s later than the main timeline (they come from an earlier, longer cut).
- **End card.** `compositions/logo-end.html` (same as reel 1): the logo flickers on like a neon sign, then glows and holds. Voiceover `assets/audio/vo-jiz-brzy-v-brne.mp3` (ElevenLabs voice, supplied by the client).

## Brand

- Logo: `assets/hopasap-logo-reversed.svg`, the reversed version for dark backgrounds.
- Colours: orange `#FF5A36` and white.
- The brand name is always written lowercase: "hopasap".

## Conventions for edits

- Run `npm run check` after every edit and fix all errors. Snapshot the changed moments before rendering.
- Moving or trimming clip 3 means moving `#clip-03-voice`, the reveal SFX, `#music-beat`, the `#hype-cam` keyframes, the sparkle times and the `car-hype` host together (all keyed to the 8.43 s ramp start and the 8.84 s impact).
- A smaller copy for upload (under 25 MB): two-pass H.264 at 7.6 Mb/s, AAC 160k, for example
  `ffmpeg -y -i renders/hopasap-instagram-2-final.mp4 -c:v libx264 -preset slow -b:v 7600k -maxrate 11000k -bufsize 15000k -pass 1 -an -f mp4 /dev/null && ffmpeg -y -i renders/hopasap-instagram-2-final.mp4 -c:v libx264 -preset slow -b:v 7600k -maxrate 11000k -bufsize 15000k -pass 2 -c:a aac -b:a 160k -movflags +faststart renders/hopasap-instagram-2-final-small.mp4` (on Windows use `NUL` instead of `/dev/null`).
- The original iPhone MOVs are not in the repo: they contain unblurred plates and GPS metadata. Never add them.
