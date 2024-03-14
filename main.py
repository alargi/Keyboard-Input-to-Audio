import os
import string
from random import shuffle
from pynput import keyboard
from playsound import playsound

# 预设音频文件夹地址 （文件夹内音频要求为 wav 或 mp3 格式）
MUSIC_FOLDER = r"B:\code\键盘转音频\music"

# 预处理
key_list = list(string.ascii_lowercase + string.digits)
shuffle(key_list)

# 读取音频文件
match_list = {}
n = 0
for filename in os.listdir(MUSIC_FOLDER):
    # 检查文件是否是音频文件
    if filename.endswith(".wav") or filename.endswith(".mp3"):
        # 获取文件的完整路径
        file_path = os.path.join(MUSIC_FOLDER, filename)
        match_list[key_list[n]] = file_pa
        n += 1
        if n >= 36:
            break


# 定义按键按下事件处理函数
def on_press(key):
    try:
        file_path = match_list.get(key.char)
        if file_path:
            print(key.char, file_path)
            playsound(file_path)
            # 暂停键盘监听器
            listener.stop()
        else:
            print("No audio file found for key:", key.char)
    except AttributeError:
        print("Special key pressed:", key)


# 循环创建和启动键盘监听器
while True:
    # 创建键盘监听器
    listener = keyboard.Listener(on_press=on_press)
    # 启动键盘监听器
    listener.start()
    # 阻塞主线程，等待键盘监听器结束
    listener.join()
