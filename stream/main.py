import os

from keep_alive import keep_alive

keep_alive()

os.system(
    'ffmpeg -ignore_loop 0 -i bg2.gif -stream_loop -1 -re -i https://stream-152.zeno.fm/ez4m4918n98uv?zs=T1OHrzJoRjqCVpZTWFy7Jw -vcodec libx264 -pix_fmt rgb24 -maxrate 2048k -preset ultrafast -r 12 -framerate 30 -g 50 -crf 51 -c:a aac -b:a 128k -ar 44100 -strict experimental -video_track_timescale 100 -b:v 500k -s 1920x1080 -f flv  rtmp://a.rtmp.youtube.com/live2/streamkey')
