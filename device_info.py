import tkinter as tk
import platform
import socket
import psutil

def get_device_info():
    # 获取设备信息
    device_name = platform.node()
    system = platform.system()
    processor = platform.processor()
    memory = psutil.virtual_memory().total / (1024 ** 3)  # 转换为GB
    ip_address = socket.gethostbyname(socket.gethostname())

    # 在结果文本框中显示设备信息
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"设备名称: {device_name}\n")
    result_text.insert(tk.END, f"操作系统: {system}\n")
    result_text.insert(tk.END, f"处理器: {processor}\n")
    result_text.insert(tk.END, f"内存: {memory:.2f} GB\n")
    result_text.insert(tk.END, f"IP地址: {ip_address}\n")

# 创建窗口
window = tk.Tk()
window.title("设备信息获取软件")
window.geometry("1024x700")  # 设置窗口尺寸为 1024x700

# 添加获取按钮
get_info_button = tk.Button(window, text="获取设备信息", command=get_device_info)
get_info_button.pack(pady=10)

# 添加结果文本框
result_text = tk.Text(window, height=20, width=80)
result_text.pack()

# 运行窗口主循环
window.mainloop()
