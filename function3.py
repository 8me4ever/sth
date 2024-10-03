# function3.py

import pandas as pd
import matplotlib.pyplot as plt
from tkinter import messagebox
from file_operations import get_dataframe

def visualize_data(column_name, chart_type="柱状图", xlabel=None, ylabel=None):
    """
    根据用户选择的特征名称、图表类型和自定义坐标名称对数据进行可视化展示。
    :param column_name: 特征名称（列名）
    :param chart_type: 图表类型（柱状图、折线图、饼图）
    :param xlabel: 自定义横轴名称（可选）
    :param ylabel: 自定义纵轴名称（可选）
    """
    df = get_dataframe()  # 获取主界面加载的Excel数据
    if df is None:
        return

    try:
        # 检查特征列是否存在
        if column_name not in df.columns:
            messagebox.showerror("错误", f"特征名称 '{column_name}' 不存在于Excel文件中！")
            return

        # 获取指定列的数据
        data = df[column_name].dropna()  # 去除空值
        if data.empty:
            messagebox.showinfo("提示", f"特征列 '{column_name}' 中没有有效数据！")
            return

        # 根据图表类型选择进行可视化
        plt.figure(figsize=(10, 6))  # 设置图表大小
        if chart_type == "柱状图":
            data.value_counts().plot(kind='bar', color='skyblue')
            plt.title(f"{column_name} - 柱状图")

        elif chart_type == "折线图":
            data.plot(kind='line', marker='o', linestyle='-', color='skyblue')
            plt.title(f"{column_name} - 折线图")

        elif chart_type == "饼图":
            data.value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'lightgreen', 'coral', 'orange'])
            plt.title(f"{column_name} - 饼图")
            plt.ylabel('')  # 隐藏饼图默认的y轴标签

        else:
            messagebox.showerror("错误", "无效的图表类型选择！")
            return

        # 设置自定义的横纵坐标名称
        plt.xlabel(xlabel if xlabel else column_name)  # 如果未输入横轴名称，则使用特征名称作为横轴标签
        plt.ylabel(ylabel if ylabel else "频率")  # 如果未输入纵轴名称，则默认显示“频率”

        # 显示图表
        plt.tight_layout()
        plt.show()

    except Exception as e:
        messagebox.showerror("错误", f"数据可视化失败: {e}")
