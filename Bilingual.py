import pysrt
import json
import re
import time
import g4f
import random
from googletranslatepy import Translator
import baidu_translate_spider_api as baidu_translator
translator = Translator(proxies='http://127.0.0.1:7890')
def translate(sentence):
    while True:
        try:
            text = translator.translate(sentence)
            # text = baidu_translator.baidutrans(sentence)
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
           


def modify_srt(subtitle,index):
    subs = pysrt.open('subtitle.srt')
    subs[index].text = subs[index].text.strip()+'\n'+subtitle
    # subs[index].text = subtitle
    subs.save('subtitle.srt')



# split_srt()
