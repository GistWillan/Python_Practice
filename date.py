import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

def calculate_date():
    try:
        # 获取用户输入的日期和天数
        date_str = date_entry.get()
        days = int(days_entry.get())

        # 将用户输入的日期字符串转换为日期对象
        date = datetime.strptime(date_str, "%Y-%m-%d")

        # 计算新日期
        new_date = date + timedelta(days=days)

        # 显示计算结果
        result_label['text'] = f"计算结果：{new_date.strftime('%Y-%m-%d')}"
    except ValueError:
        messagebox.showerror("错误", "请输入有效的日期和天数！")

# 创建窗口
window = tk.Tk()
window.title("日期计算器")

# 添加日期标签和输入框
date_label = tk.Label(window, text="请输入日期（YYYY-MM-DD）：")
date_label.pack()
date_entry = tk.Entry(window)
date_entry.pack()

# 添加天数标签和输入框
days_label = tk.Label(window, text="请输入天数：")
days_label.pack()
days_entry = tk.Entry(window)
days_entry.pack()

# 添加计算按钮
calculate_button = tk.Button(window, text="计算", command=calculate_date)
calculate_button.pack()

# 添加结果标签
result_label = tk.Label(window, text="计算结果：")
result_label.pack()

# 运行窗口主循环
window.mainloop()
