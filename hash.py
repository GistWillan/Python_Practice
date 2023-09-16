import tkinter as tk
import hashlib
from tkinter import filedialog

def calculate_hash():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'rb') as file:
            content = file.read()
            hash_value = hashlib.sha256(content).hexdigest()
            hash_label.config(text=hash_value)

def compare_hash():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'rb') as file:
            content = file.read()
            hash_value = hashlib.sha256(content).hexdigest()
            if hash_value == hash_label.cget("text"):
                result_label.config(text="哈希值匹配！")
            else:
                result_label.config(text="哈希值不匹配！")

root = tk.Tk()
root.title("文件哈希值查看器")
root.geometry("1024x400")

hash_label = tk.Label(root, text="哈希值", font=("Helvetica", 16))
hash_label.pack(pady=10)

calculate_button = tk.Button(root, text="计算哈希值", command=calculate_hash)
calculate_button.pack(pady=5)

compare_button = tk.Button(root, text="比较哈希值", command=compare_hash)
compare_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

root.mainloop()
