# gui.py

import tkinter as tk
from file_operations import load_excel_file, file_path
from function1 import extract_data
from function2 import sort_data
from function3 import visualize_data  # 新增：导入 function3 模块
from tkinter import ttk

# 定义 Function1 界面
def show_function1():
    function1_window = tk.Toplevel(root)
    function1_window.title("Function1: 提取数据文件")
    function1_window.geometry("600x500")

    # 当前文件路径标签
    file_label = tk.Label(function1_window, text=f"当前操作的文件路径：{file_path}", font=("Arial", 12))
    file_label.pack(pady=5)

    # 特征名称输入框
    column_label = tk.Label(function1_window, text="输入特征名称（如：学费金额）", font=("Arial", 12))
    column_label.pack(pady=10)

    column_entry = tk.Entry(function1_window, font=("Arial", 12), width=30)
    column_entry.pack(pady=5)

    # 精确筛选值输入框
    value_label = tk.Label(function1_window, text="输入筛选值（精确匹配，可选）", font=("Arial", 12))
    value_label.pack(pady=10)

    value_entry = tk.Entry(function1_window, font=("Arial", 12), width=30)
    value_entry.pack(pady=5)

    # 区间筛选最小值输入框
    min_label = tk.Label(function1_window, text="输入筛选最小值（区间筛选，可选）", font=("Arial", 12))
    min_label.pack(pady=10)

    min_entry = tk.Entry(function1_window, font=("Arial", 12), width=30)
    min_entry.pack(pady=5)

    # 区间筛选最大值输入框
    max_label = tk.Label(function1_window, text="输入筛选最大值（区间筛选，可选）", font=("Arial", 12))
    max_label.pack(pady=10)

    max_entry = tk.Entry(function1_window, font=("Arial", 12), width=30)
    max_entry.pack(pady=5)

    # 提取数据并保存按钮
    extract_button = tk.Button(function1_window, text="开始提取并保存", font=("Arial", 12),
                               command=lambda: extract_data(column_entry.get(),
                                                            filter_value=value_entry.get(),
                                                            min_value=min_entry.get(),
                                                            max_value=max_entry.get()))
    extract_button.pack(pady=20)

# 定义 Function2 界面
def show_function2():
    function2_window = tk.Toplevel(root)
    function2_window.title("Function2: 特征值排序")
    function2_window.geometry("600x400")

    # 当前文件路径标签
    file_label = tk.Label(function2_window, text=f"当前操作的文件路径：{file_path}", font=("Arial", 12))
    file_label.pack(pady=5)

    # 特征名称输入框
    sort_column_label = tk.Label(function2_window, text="输入特征名称（如：复购率）", font=("Arial", 12))
    sort_column_label.pack(pady=10)

    sort_column_entry = tk.Entry(function2_window, font=("Arial", 12), width=30)
    sort_column_entry.pack(pady=5)

    # 排序顺序选择
    order_label = tk.Label(function2_window, text="选择排序顺序", font=("Arial", 12))
    order_label.pack(pady=10)

    order_var = tk.StringVar(value="升序")  # 默认选择升序
    ascending_radio = tk.Radiobutton(function2_window, text="升序", variable=order_var, value="升序", font=("Arial", 12))
    ascending_radio.pack(pady=5)

    descending_radio = tk.Radiobutton(function2_window, text="降序", variable=order_var, value="降序", font=("Arial", 12))
    descending_radio.pack(pady=5)

    # 排序并保存按钮
    sort_button = tk.Button(function2_window, text="开始排序并保存", font=("Arial", 12),
                            command=lambda: sort_data(sort_column_entry.get(), order_var.get() == "升序"))
    sort_button.pack(pady=20)

# gui.py

# 定义 Function3 界面
def show_function3():
    function3_window = tk.Toplevel(root)
    function3_window.title("Function3: 数据可视化")
    function3_window.geometry("600x600")  # 增大窗口以容纳更多输入框

    # 当前文件路径标签
    file_label = tk.Label(function3_window, text=f"当前操作的文件路径：{file_path}", font=("Arial", 12))
    file_label.pack(pady=5)

    # 特征名称输入框
    column_label = tk.Label(function3_window, text="输入特征名称（如：学费金额）", font=("Arial", 12))
    column_label.pack(pady=10)

    column_entry = tk.Entry(function3_window, font=("Arial", 12), width=30)
    column_entry.pack(pady=5)

    # 图表类型选择下拉菜单
    chart_type_label = tk.Label(function3_window, text="选择图表类型", font=("Arial", 12))
    chart_type_label.pack(pady=10)

    chart_type_var = tk.StringVar()
    chart_type_menu = ttk.Combobox(function3_window, textvariable=chart_type_var, font=("Arial", 12), width=27)
    chart_type_menu['values'] = ("柱状图", "折线图", "饼图")  # 可视化图表类型选项
    chart_type_menu.current(0)  # 设置默认值为"柱状图"
    chart_type_menu.pack(pady=5)

    # 横轴名称输入框
    xlabel_label = tk.Label(function3_window, text="输入横轴名称（可选）", font=("Arial", 12))
    xlabel_label.pack(pady=10)

    xlabel_entry = tk.Entry(function3_window, font=("Arial", 12), width=30)
    xlabel_entry.pack(pady=5)

    # 纵轴名称输入框
    ylabel_label = tk.Label(function3_window, text="输入纵轴名称（可选）", font=("Arial", 12))
    ylabel_label.pack(pady=10)

    ylabel_entry = tk.Entry(function3_window, font=("Arial", 12), width=30)
    ylabel_entry.pack(pady=5)

    # 可视化按钮
    visualize_button = tk.Button(function3_window, text="开始可视化", font=("Arial", 12),
                                 command=lambda: visualize_data(
                                     column_name=column_entry.get(),
                                     chart_type=chart_type_var.get(),
                                     xlabel=xlabel_entry.get(),
                                     ylabel=ylabel_entry.get()
                                 ))
    visualize_button.pack(pady=20)




# 主界面
root = tk.Tk()
root.title("Excel 数据处理工具")
root.geometry("500x400")

# 加载Excel文件按钮
load_button = tk.Button(root, text="加载Excel文件", command=load_excel_file, font=("Arial", 14))
load_button.pack(pady=20)

# 显示当前选择的文件路径
file_path_label = tk.Label(root, text=f"当前文件路径：{file_path}", font=("Arial", 12))
file_path_label.pack(pady=10)

# 功能选择按钮
function1_button = tk.Button(root, text="Function1: 提取数据文件", command=show_function1, font=("Arial", 14), width=30)
function1_button.pack(pady=20)

function2_button = tk.Button(root, text="Function2: 特征值排序", command=show_function2, font=("Arial", 14), width=30)
function2_button.pack(pady=20)

function3_button = tk.Button(root, text="Function3: 数据可视化", command=show_function3, font=("Arial", 14), width=30)
function3_button.pack(pady=20)

root.mainloop()
