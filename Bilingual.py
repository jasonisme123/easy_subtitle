import pysrt
import json
import re
import time
import g4f
import random
from googletranslatepy import Translator
translator = Translator(proxies='http://127.0.0.1:7890')
def translate(sentence):
    while True:
        try:
            text = translator.translate(sentence)
            break
        except Exception as e:
            print(e)
            time.sleep(2)  # 等待 2 秒后重试
    return text



def split_srt():
    # 打开SRT文件
    subs = pysrt.open('subtitle.srt')
    # 遍历所有字幕并将它们添加到数组中
    for i, sub in enumerate(subs):
        subtitle_line = sub.text.strip()
        try:
            text = translate(subtitle_line)
            modify_srt(text,i)      
        except Exception as e:
            print("translate google Disconnected")
           

# def split_srt():
#     # 打开SRT文件
#     subs = pysrt.open('subtitle.srt')
    
#     # 遍历所有字幕并将它们添加到数组中
#     pre = 0
#     subtitle_all = ''
#     for i, sub in enumerate(subs):
#         subtitle_line = sub.text.strip()
#         subtitle_all = subtitle_all + ' ' + subtitle_line
#         if subtitle_line.endswith('.') or subtitle_line.endswith('?') or subtitle_line.endswith('!'):
#             while True:
#                 try:
#                     text = translate(subtitle_all)
#                     modify_srt(text, pre, i+1-pre)
#                     pre = i + 1
#                     subtitle_all = ''
#                     break
#                 except Exception as e:
#                     print("translate google Disconnected")
#                     time.sleep(5)
#             time.sleep(2)


def modify_srt(subtitle,index):
    subs = pysrt.open('subtitle.srt')
    subs[index].text = subs[index].text.strip()+'\n'+subtitle
    subs.save('subtitle.srt')


# def modify_srt(subtitle, start_index, distanct):
#     subs = pysrt.open('subtitle.srt')
#     length = distanct+start_index
#     try:
#         text_length = len(subtitle)//distanct
#     except Exception as e:
#         raise e

#     segments = []
#     for i in range(0, len(subtitle), text_length):
#         segments.append(subtitle[i:i+text_length])

#     j = 0
#     for i in range(start_index, length):
#         subs[i].text = subs[i].text.strip()+'\n'+segments[j]
#         j = j+1

#     subs.save('subtitle.srt')


# split_srt()
