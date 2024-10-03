# function2.py

import pandas as pd
from tkinter import messagebox
from file_operations import get_dataframe, save_file

def sort_data(column_name, ascending=True):
    df = get_dataframe()  # 获取主界面加载的Excel数据
    if df is None:
        return

    try:
        # 检查特征列是否存在
        if column_name not in df.columns:
            messagebox.showerror("错误", f"特征名称 '{column_name}' 不存在于Excel文件中！")
            return

        # 将特征列的数据类型转换为字符串，然后去除百分号并转换为浮点数
        def convert_to_float(value):
            if isinstance(value, str):
                # 如果是字符串形式的百分比，去除百分号并转换为浮点数
                if "%" in value:
                    try:
                        return float(value.replace("%", "")) / 100
                    except ValueError:
                        return None
                else:
                    try:
                        return float(value)
                    except ValueError:
                        return None
            else:
                return value

        # 应用数据转换到指定列
        df[column_name] = df[column_name].apply(convert_to_float)

        # 检查是否转换失败（即列中存在无法转换的非数值数据）
        if df[column_name].isnull().all():
            messagebox.showerror("错误", f"列 '{column_name}' 中的数据无法转换为数值格式，请检查数据类型！")
            return

        # 根据用户选择进行排序
        sorted_df = df.sort_values(by=column_name, ascending=ascending)

        # 保存排序结果
        save_file(sorted_df, title="保存排序结果为")

    except Exception as e:
        messagebox.showerror("错误", f"文件处理失败: {e}")
