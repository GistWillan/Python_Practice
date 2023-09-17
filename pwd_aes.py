import tkinter as tk
from tkinter import messagebox
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

def generate_password():
    # 获取用户输入的密码
    password = password_entry.get()

    # 生成随机的 256 位密钥
    key = get_random_bytes(32)

    # 使用 AES256 加密密码
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(password.encode())

    # 将密钥和加密后的密码转换为 Base64 编码字符串
    key_string = b64encode(key).decode()
    ciphertext_string = b64encode(ciphertext).decode()

    # 在结果文本框中显示生成的密码和密钥
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"生成的密码: {ciphertext_string}\n")
    result_text.insert(tk.END, f"密钥: {key_string}\n")

    # 弹出对话框显示成功生成密码
    messagebox.showinfo("密码生成器", "密码已成功生成！")

# 创建窗口
window = tk.Tk()
window.title("密码生成器")
window.geometry("1024x700")  # 设置窗口尺寸为 1024x700

# 添加密码输入框和生成按钮
password_label = tk.Label(window, text="输入密码:")
password_label.pack(pady=10)

password_entry = tk.Entry(window, show="*")
password_entry.pack()

generate_button = tk.Button(window, text="生成密码", command=generate_password)
generate_button.pack(pady=10)

# 添加结果文本框
result_text = tk.Text(window, height=20, width=80)
result_text.pack()

# 运行窗口主循环
window.mainloop()
