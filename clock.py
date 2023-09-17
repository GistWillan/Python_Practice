import tkinter as tk
import time

def start_timer():
    duration = int(entry.get()) * 60  # 获取输入的分钟数并转换为秒
    countdown(duration)

def countdown(seconds):
    if seconds > 0:
        label['text'] = f"倒计时：{seconds // 60:02d}:{seconds % 60:02d}"
        label.after(1000, countdown, seconds - 1)
    else:
        label['text'] = "时间到！"

# 创建窗口
window = tk.Tk()
window.title("专注时钟")

# 添加标签和输入框
label = tk.Label(window, text="输入专注时间（分钟）：")
label.pack()
entry = tk.Entry(window)
entry.pack()

# 添加开始按钮
start_button = tk.Button(window, text="开始", command=start_timer)
start_button.pack()

# 运行窗口主循环
window.mainloop()
