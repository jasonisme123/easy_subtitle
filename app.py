import Bilingual
import json
import subprocess
from pydub import AudioSegment
from moviepy.editor import *
import handle_audio
import pysubs2


def video2audio(video_name):
    my_audio_clip = AudioFileClip(video_name)
    my_audio_clip.write_audiofile('overview.mp3')


def audio2srt():
    handle_audio.main()


def video_merge_srt(input_mp4):
    output_mp4 = "output.mp4"
    subtitles_srt = 'subtitle.srt'
    command = [
        "ffmpeg",
        "-i",
        input_mp4,
        "-vf",
        f"subtitles={subtitles_srt}",
        output_mp4,
    ]

    subprocess.run(command, check=True)


def main():
    video_name = 'overview.mp4'
    video2audio(video_name)
    audio2srt()
    Bilingual.split_srt()
    video_merge_srt(video_name)


if __name__ == '__main__':
    main()
