import json
from pydub import AudioSegment
from moviepy.editor import *
from datetime import timedelta
from faster_whisper import WhisperModel


def text_insert_srt(text, start_time, end_time, index):
    output_file = 'subtitle.srt'
    with open(output_file, 'a', encoding='utf-8') as output:
        output.write(str(index) + '\n')
        start = adjust_time(start_time)
        end = adjust_time(end_time)
        output.write(f"{start} --> {end}\n")
        output.write(text)
        output.write('\n\n')


def adjust_time(time_str):
    # 将字符串转换为浮点数
    time_in_seconds = float(time_str)

    # 将浮点数转换为时间差对象
    delta = timedelta(seconds=time_in_seconds)

    # 计算出小时、分钟、秒和毫秒
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = delta.microseconds // 1000

    # 将时间格式化为"00:02:12,560"的格式
    result = f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

    return result


def transcribe(audio_name):
    model_size = "small"
    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    segments, info = model.transcribe(audio_name, beam_size=5)

    for i, segment in enumerate(segments):
        segment_start = "{:.3f}".format(segment.start)
        segment_end = "{:.3f}".format(segment.end)
        segment_text = segment.text.strip()
        text_insert_srt(segment_text, segment_start, segment_end, i+1)


def main():
    transcribe('overview.mp3')


# main()
