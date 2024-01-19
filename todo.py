import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("待办事项")
        
        # 待办事项列表
        self.todo_list = []

        # 创建布局
        self.create_layout()

    def create_layout(self):
        # 标签
        label = tk.Label(self.root, text="添加待办事项:")
        label.grid(row=0, column=0, padx=10, pady=10)

        # 输入框
        self.todo_entry = tk.Entry(self.root, width=30)
        self.todo_entry.grid(row=0, column=1, padx=10, pady=10)

        # 添加按钮
        add_button = tk.Button(self.root, text="添加", command=self.add_todo)
        add_button.grid(row=0, column=2, padx=10, pady=10)

        # 待办事项列表框
        self.listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, width=40, height=10)
        self.listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # 删除按钮
        delete_button = tk.Button(self.root, text="删除", command=self.delete_todo)
        delete_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    def add_todo(self):
        # 获取输入的待办事项
        todo_text = self.todo_entry.get().strip()

        if todo_text:
            # 获取当前时间
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # 添加到待办事项列表
            todo_item = f"{current_time}: {todo_text}"
            self.todo_list.append(todo_item)
            
            # 更新列表框
            self.update_listbox()

            # 清空输入框
            self.todo_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("警告", "请输入待办事项内容！")

    def delete_todo(self):
        # 获取选中的待办事项索引
        selected_index = self.listbox.curselection()

        if selected_index:
            # 删除选中的待办事项
            del self.todo_list[selected_index[0]]

            # 更新列表框
            self.update_listbox()
        else:
            messagebox.showwarning("警告", "请选择要删除的待办事项！")

    def update_listbox(self):
        # 清空列表框
        self.listbox.delete(0, tk.END)

        # 更新列表框内容
        for todo_item in self.todo_list:
            self.listbox.insert(tk.END, todo_item)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
