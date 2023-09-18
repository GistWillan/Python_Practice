import tkinter as tk
from tkinter import filedialog
from PIL import Image

class ImageCutterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("图片切割软件")
        
        self.image_path = ""
        self.crop_x = tk.StringVar()
        self.crop_y = tk.StringVar()
        self.crop_width = tk.StringVar()
        self.crop_height = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        # 选择图片按钮
        self.select_image_button = tk.Button(self.root, text="选择图片", command=self.select_image)
        self.select_image_button.pack(pady=10)
        
        # 裁切位置和大小输入框
        self.crop_frame = tk.Frame(self.root)
        self.crop_frame.pack(pady=10)
        
        tk.Label(self.crop_frame, text="裁切位置 (x, y):").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(self.crop_frame, textvariable=self.crop_x).grid(row=0, column=1, padx=5, pady=5)
        tk.Entry(self.crop_frame, textvariable=self.crop_y).grid(row=0, column=2, padx=5, pady=5)
        
        tk.Label(self.crop_frame, text="裁切大小 (宽度, 高度):").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(self.crop_frame, textvariable=self.crop_width).grid(row=1, column=1, padx=5, pady=5)
        tk.Entry(self.crop_frame, textvariable=self.crop_height).grid(row=1, column=2, padx=5, pady=5)
        
        # 切割按钮
        self.crop_button = tk.Button(self.root, text="切割图片", command=self.crop_image, state=tk.DISABLED)
        self.crop_button.pack(pady=10)
        
        # 显示切割结果的标签
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=10)
    
    def select_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if self.image_path:
            self.crop_button.config(state=tk.NORMAL)
            self.result_label.config(text="")
    
    def crop_image(self):
        try:
            image = Image.open(self.image_path)
            x = int(self.crop_x.get())
            y = int(self.crop_y.get())
            width = int(self.crop_width.get())
            height = int(self.crop_height.get())
            
            cropped_image = image.crop((x, y, x + width, y + height))
            cropped_image.show()
            self.result_label.config(text="图片切割成功！")
        except Exception as e:
            self.result_label.config(text="图片切割失败：" + str(e))
    
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageCutterApp(root)
    root.mainloop()
