# file_operations.py

import pandas as pd
from tkinter import filedialog, messagebox

# 定义全局变量来存储文件路径和数据框
file_path = ""
dataframe = None

# 选择Excel文件函数
def load_excel_file():
    global file_path, dataframe
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    if file_path:
        try:
            # 读取Excel文件并存入全局数据框
            dataframe = pd.read_excel(file_path)
            return file_path, dataframe
        except Exception as e:
            messagebox.showerror("错误", f"文件读取失败: {e}")
            file_path = ""
            dataframe = None
            return None, None
    else:
        messagebox.showerror("错误", "未选择文件！")
        return None, None

# 获取加载的Excel数据框
def get_dataframe():
    global dataframe
    if dataframe is not None:
        return dataframe
    else:
        messagebox.showerror("错误", "未加载数据！")
        return None

# 保存Excel文件函数
def save_file(dataframe, title="保存文件为"):
    output_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")], title=title)
    if output_path:
        try:
            dataframe.to_excel(output_path, index=False)
            messagebox.showinfo("成功", f"数据已成功保存至：\n{output_path}")
        except Exception as e:
            messagebox.showerror("错误", f"文件保存失败: {e}")
    else:
        messagebox.showwarning("提示", "未选择保存路径！")
