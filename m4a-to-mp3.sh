#!/bin/bash

find . -type f -name "*.m4a" | while read f
do
	echo "$f"
	base=`basename "$f" .m4a`
	cvlc -v "$f" --sout "#transcode{vcodec=none,acodec=mp3,ab=128,channels=2,samplerate=44100}:std{access=file,mux=raw,dst=-}" vlc://quit > "$base".mp3
done
