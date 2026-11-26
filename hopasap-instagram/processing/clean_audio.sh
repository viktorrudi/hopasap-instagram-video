#!/bin/zsh
# usage: clean_audio.sh <in.MOV> <out.wav> <rnn model> <rnn mix> <target LUFS>
set -e
FF=${FFMPEG:-ffmpeg}
in=$1; out=$2; model=$3; mix=$4; target=$5
pre="pan=mono|c0=0.5*c0+0.5*c1,highpass=f=85:p=2,arnndn=m='${model}':mix=${mix},afftdn=nr=6:nf=-50:tn=1,equalizer=f=230:t=q:w=1.0:g=-2.5,equalizer=f=3200:t=q:w=1.2:g=3,equalizer=f=9000:t=h:w=0.7:g=1.5,deesser=i=0.3,acompressor=threshold=-26dB:ratio=3:attack=6:release=150:knee=4:makeup=3"
mI=$($FF -hide_banner -nostats -i $in -map 0:a:0 -af "${pre},ebur128=framelog=quiet" -f null - 2>&1 | grep -E '^ +I:' | tail -1 | awk '{print $2}')
gain=$(python3 -c "print(round(${target}-(${mI}),2))")
$FF -v error -y -i $in -map 0:a:0 -af "${pre},volume=${gain}dB,alimiter=limit=0.75:attack=2:release=60:level=false:asc=1,pan=stereo|c0=c0|c1=c0,aresample=48000" -c:a pcm_s16le $out
echo "$(basename $out) pre_I=${mI} gain=${gain}dB"
