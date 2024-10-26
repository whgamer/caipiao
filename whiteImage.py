import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageEnhance, ImageFilter
import os

# 定义背景替换函数
def process_image(file_path, target_size_kb):
    try:
        img = Image.open(file_path)
        img = img.convert("RGB")

        # 增强对比度
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(2)

        # 增强边缘
        img = img.filter(ImageFilter.EDGE_ENHANCE)

        # 获取像素数据
        datas = img.getdata()

        # 扩大黑色范围
        black_range = [(0, 0, 0), (80, 80, 80)]

        new_data = []
        for item in datas:
            if black_range[0] <= item <= black_range[1]:
                new_data.append(item)  # 保留黑色文字
            else:
                new_data.append((255, 255, 255))  # 替换为纯白色

        img.putdata(new_data)

        # 重采样图像分辨率
        width, height = img.size
        output_file = os.path.splitext(file_path)[0] + "_output.jpg"
        quality = 85  # 初始质量

        # 递归压缩
        while True:
            img.save(output_file, "JPEG", quality=quality)
            file_size_kb = os.path.getsize(output_file) / 1024
            
            if file_size_kb <= target_size_kb:
                break

            # 如果文件大小仍然过大，降低质量，并逐渐缩小图像尺寸
            quality -= 5
            width = int(width * 0.9)  # 每次缩小10%的分辨率
            height = int(height * 0.9)
            img = img.resize((width, height), Image.ANTIALIAS)
            
            if quality < 10 or width < 50 or height < 50:
                break  # 避免过度压缩导致图像质量严重下降或尺寸过小

        messagebox.showinfo("成功", f"图像处理完成！文件已保存为 {output_file}，大小为 {file_size_kb:.2f} KB")

    except Exception as e:
        messagebox.showerror("错误", f"处理图像时出错：{e}")

# 定义选择文件的函数
def select_file():
    file_path = filedialog.askopenfilename(
        title="选择图片文件",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]
    )
    if file_path:
        try:
            # 获取用户输入的目标文件大小
            target_size_kb = float(size_entry.get())
            process_image(file_path, target_size_kb)
        except ValueError:
            messagebox.showerror("错误", "请输入有效的文件大小（KB）")

# 创建主窗口
root = tk.Tk()
root.title("图像背景处理工具")
root.geometry("300x200")

# 创建并放置文件大小标签
size_label = tk.Label(root, text="目标文件大小 (KB)：")
size_label.pack(pady=5)

# 创建并放置文件大小输入框，默认值为5
size_entry = tk.Entry(root)
size_entry.insert(0, "5")  # 默认值为 5KB
size_entry.pack(pady=5)

# 创建并放置选择文件按钮
select_button = tk.Button(root, text="选择图片文件", command=select_file, height=2, width=20)
select_button.pack(pady=20)

# 运行主循环
root.mainloop()
