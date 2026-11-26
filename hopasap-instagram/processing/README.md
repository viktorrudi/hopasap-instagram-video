# Processing (how the clips in `assets/clips/processed/` were made)

These scripts need the original iPhone MOVs, which are intentionally not in this repo. They are kept to document the process and to allow re-runs.

1. **Tone-map to SDR, 1080 × 1920, 60 fps** with ffmpeg built with libzimg (zscale), using HyperFrames' curve:
   `zscale=w=1080:h=1920:t=linear:npl=203,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,fps=60,format=yuv420p`
2. **Clean the audio**: `clean_audio.sh <in.MOV> <out.wav> <rnnoise model> <mix> <target LUFS>`. The model is `std.rnnn` from [richardpl/arnndn-models](https://github.com/richardpl/arnndn-models). Speech clips used mix 0.9 and −17 (mono, which is about −14 stereo); the tunnel clip used 0.6 and −24.
3. **Detect plates**: `detect.py <model.pt> <sdr.mp4> <out.json>` with `morsetechlab/yolov11-license-plate-detection` (`license-plate-finetune-v1m.pt`). Needs `pip install ultralytics opencv-python-headless`.
4. **Build smooth tracks**: `track.py <det.json> <tracks.json>`. The `*.tracks.json` files here are the tracks that were used.
5. **Blur and mux**: `blur.py render <sdr.mp4> <tracks.json|-> <clean.wav> <out.mp4>`. `blur.py sheet|crops …` writes review images.

`cabin-light-4757.json` is the per-frame brightness of the (now cut) taxi clip that was used to sync an earlier logo version.

Set `FFMPEG=/path/to/ffmpeg` if the default `ffmpeg` on PATH lacks zscale.
