# function1.py

import pandas as pd
from tkinter import messagebox
from file_operations import get_dataframe, save_file

def extract_data(column_name, filter_value=None, min_value=None, max_value=None):
    """
    根据特征名称和筛选条件提取数据。
    :param column_name: 要筛选的特征列名称
    :param filter_value: 精确匹配筛选值（可选）
    :param min_value: 最小值，用于区间筛选（可选）
    :param max_value: 最大值，用于区间筛选（可选）
    """
    df = get_dataframe()  # 获取主界面加载的Excel数据
    if df is None:
        return

    try:
        if column_name not in df.columns:
            messagebox.showerror("错误", f"特征名称 '{column_name}' 不存在于Excel文件中！")
            return

        # 筛选数据
        if filter_value:
            # 精确匹配筛选
            filtered_df = df[df[column_name] == filter_value]
        else:
            # 区间筛选
            try:
                min_value = float(min_value) if min_value is not None else None
                max_value = float(max_value) if max_value is not None else None
            except ValueError:
                messagebox.showerror("错误", "请确保最小值和最大值为有效数值！")
                return

            if min_value is not None and max_value is not None:
                filtered_df = df[(df[column_name] >= min_value) & (df[column_name] <= max_value)]
            elif min_value is not None:
                filtered_df = df[df[column_name] >= min_value]
            elif max_value is not None:
                filtered_df = df[df[column_name] <= max_value]
            else:
                messagebox.showerror("错误", "请提供有效的最小值或最大值！")
                return

        if filtered_df.empty:
            messagebox.showinfo("提示", f"未找到符合条件的 '{column_name}' 数据行！")
            return

        # 添加统计行
        data_count = len(filtered_df)
        stats_row = {col: "" for col in filtered_df.columns}
        stats_row[column_name] = f"数据行数: {data_count}"
        stats_df = pd.DataFrame([stats_row])
        output_df = pd.concat([filtered_df, stats_df], ignore_index=True)

        # 保存筛选结果
        save_file(output_df, title="保存筛选结果为")

    except Exception as e:
        messagebox.showerror("错误", f"文件处理失败: {e}")
