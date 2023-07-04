import tkinter as tk
import subprocess
import shutil
import os

def download_novel():
    book_id = entry_book_id.get()
    book_source = dropdown_book_source.get()
    book_format = dropdown_book_format.get()
    if book_format == "epub":
        book_format = "pandoc"
        command = ['./novel-cli', 'download', book_id, '--source', book_source, '--format', book_format]
        try:
            subprocess.run(command, check=True)
            label_status.config(text="下载完成")   
        except subprocess.CalledProcessError:
            label_status.config(text="下载出错")   
        # 获取当前程序所在的文件夹路径
        current_folder = os.path.dirname(os.path.abspath(__file__))
        # 获取当前文件夹内的所有文件夹名称列表类型
        folder_name = [folder for folder in os.listdir(current_folder) if os.path.isdir(os.path.join(current_folder, folder))]
        for folder_name_str in folder_name:
            build_command = ['./novel-cli', 'build', folder_name_str]
            try:
                subprocess.run(build_command, check=True)
                label_status.config(text="转换完成")
            except subprocess.CalledProcessError:
                label_status.config(text="转换出错")
                continue
        # 删除临时文件夹
            shutil.rmtree(folder_name_str)
        label_status.config(text="流程结束")   
    else:    
        command = ['./novel-cli', 'download', book_id, '--source', book_source, '--format', book_format]
        try:
            subprocess.run(command, check=True)
            label_status.config(text="下载完成")
        except subprocess.CalledProcessError:
            label_status.config(text="下载出错")


def build_novel():
    # 获取当前程序所在的文件夹路径
    current_folder = os.path.dirname(os.path.abspath(__file__))
    # 获取当前文件夹内的所有文件夹名称列表类型
    folder_name = [folder for folder in os.listdir(current_folder) if
                   os.path.isdir(os.path.join(current_folder, folder))]
    for folder_name_str in folder_name:
        build_command = ['./novel-cli', 'build', folder_name_str]
        try:
            subprocess.run(build_command, check=True)
            label_status.config(text="转换完成")
        except subprocess.CalledProcessError:
            label_status.config(text="转换出错")
            continue
        # 删除临时文件夹
        shutil.rmtree(folder_name_str)




# 创建窗口
window = tk.Tk()
window.title("小说下载GUI")
window.geometry('235x310')
window.resizable(False, False)
# 创建控件
title_id = tk.Label(window, text="novel-cli-gui", font=("微软雅黑", 25))
author_id = tk.Label(window, text="GUI作者：TenSin", font=("微软雅黑", 12))
label_book_id = tk.Label(window, text="小说ID:", font=("微软雅黑", 15))
entry_book_id = tk.Entry(window, width=10, font=("微软雅黑", 15))

label_book_source = tk.Label(window, text="小说网站:", font=("微软雅黑", 15))
dropdown_book_source = tk.StringVar()
option_menu_book_source = tk.OptionMenu(window, dropdown_book_source, "sfacg", "ciweimao")
dropdown_book_source.set("sfacg")
label_book_format = tk.Label(window, text="下载格式:", font=("微软雅黑", 15))
dropdown_book_format = tk.StringVar()
option_menu_book_format = tk.OptionMenu(window, dropdown_book_format, "mdbook", "pandoc", "epub")
dropdown_book_format.set("epub")
button_bulid = tk.Button(window, text="构建", font=("微软雅黑", 15), command=build_novel)
button_download = tk.Button(window, text="下载", font=("微软雅黑", 20), command=download_novel)


label_status = tk.Label(window, text="",font=("微软雅黑", 15))

# 设置控件布局
title_id.grid(row=0, column=0,columnspan=2)
author_id.grid(row=1, column=1)

label_book_id.grid(row=2, column=0)
entry_book_id.grid(row=2, column=1)

label_book_source.grid(row=3, column=0)
option_menu_book_source.grid(row=3, column=1)

label_book_format.grid(row=4, column=0)
option_menu_book_format.grid(row=4, column=1)

button_bulid.grid(row=5, column=0)
button_download.grid(row=5, column=1)

label_status.grid(row=6, column=0,columnspan=2)


option_menu_book_source.config(font=("微软雅黑", 15))
option_menu_book_format.config(font=("微软雅黑", 15))
# 运行窗口
window.mainloop()
