import tkinter as tk
import subprocess
import shutil
import os
import requests
import zipfile
import sys

def run_cli():
    if type_command == "search":
        keyword = entry_keyword.get()
        book_source = dropdown_book_source.get()
        command = ['./novel-cli', 'search', keyword, '--source', book_source]
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError:
            pass
    elif type_command == "download":
        book_id = entry_book_id.get()
        book_source = dropdown_book_source.get()
        book_format = dropdown_book_format.get()
        command = ['./novel-cli', 'download', book_id, '--source', book_source, '--format', book_format]
        try:
            subprocess.run(command, check=True)
            pass
        except subprocess.CalledProcessError:
            pass
    elif type_command == "build":
        book_folder = dropdown_book_folder.get()
        
        characters_to_remove = ["(", ")", "'", ","]

        for character in characters_to_remove:
            book_folder = book_folder.replace(character, "")
        
        command = ['./novel-cli', 'build', book_folder]
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError:
            pass
        shutil.rmtree(book_folder)
    else:
        print("未知操作类型")


            
            

def start_check():
    print("初始化中")
    if os.path.exists("novel-cli.exe"):
        print("初始化完成")
    else:
        url = "https://github.com/novel-rs/cli/releases/download/0.5.0/novel-cli-x86_64-pc-windows-msvc.zip"
        response = requests.get(url)

        if response.status_code == 200:
            file_name = url.split("/")[-1]
            with open(file_name, "wb") as file:
                file.write(response.content)
            print("文件下载成功！")
        else:
            print("文件下载失败。")

        zip_file = 'novel-cli-x86_64-pc-windows-msvc.zip'
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall()
        os.remove(zip_file)
        print("初始化完成")

def gui_search():
    global type_command, entry_keyword, dropdown_book_source
    type_command = "search"
    main.withdraw()  # 隐藏主窗口
    search_window = tk.Toplevel()  # 创建新的搜索窗口
    search_window.title("Novel-RS-GUI")

    
    # 创建控件
    title_id = tk.Label(search_window, text="Novel-RS-GUI", font=("微软雅黑", 35))
    command_type = tk.Label(search_window, text="搜索", font=("微软雅黑", 24))
    
    label_book_source = tk.Label(search_window, text="小说网站:", font=("微软雅黑", 18))
    dropdown_book_source = tk.StringVar()
    option_menu_book_source = tk.OptionMenu(search_window, dropdown_book_source, "sfacg", "ciweimao")
    dropdown_book_source.set("sfacg")
    option_menu_book_source.config(font=("微软雅黑", 18))  # 设置字体
    
    label_keyword = tk.Label(search_window, text="关键词:", font=("微软雅黑", 18))
    entry_keyword = tk.Entry(search_window, width=10, font=("微软雅黑", 18))
    
    button_run = tk.Button(search_window, text="搜索", font=("微软雅黑", 18), command=run_cli)
    button_back = tk.Button(search_window, text="返回", font=("微软雅黑", 18), command=lambda: close_window(search_window))
    
    # 设置控件布局
    title_id.grid(row=0, pady=10, column=0, columnspan=2)
    command_type.grid(row=1, pady=10, column=0, columnspan=2)
    label_book_source.grid(row=2, pady=10, column=0)
    option_menu_book_source.grid(row=2, pady=10, column=1)
    label_keyword.grid(row=3, pady=10, column=0)
    entry_keyword.grid(row=3, pady=10, column=1)
    button_run.grid(row=4, pady=10, column=0)
    button_back.grid(row=4, pady=10, column=1)

def gui_download():
    global type_command, entry_book_id, dropdown_book_format, dropdown_book_source
    type_command = "download"
    main.withdraw()  # 隐藏主窗口
    download_window = tk.Toplevel()  # 创建一个新的下载窗口
    download_window.title("Novel-RS-GUI")


    # 创建小部件（控件）
    title_id = tk.Label(download_window, text="Novel-RS-GUI", font=("微软雅黑", 35))
    command_type = tk.Label(download_window, text="下载", font=("微软雅黑", 24))

    label_book_source = tk.Label(download_window, text="小说网站:", font=("微软雅黑", 18))
    dropdown_book_source = tk.StringVar()
    option_menu_book_source = tk.OptionMenu(download_window, dropdown_book_source, "sfacg", "ciweimao")
    dropdown_book_source.set("sfacg")
    option_menu_book_source.config(font=("微软雅黑", 18))  # 设置字体

    label_book_format = tk.Label(download_window, text="下载格式:", font=("微软雅黑", 15))
    dropdown_book_format = tk.StringVar()
    option_menu_book_format = tk.OptionMenu(download_window, dropdown_book_format, "mdbook", "pandoc")
    dropdown_book_format.set("pandoc")
    option_menu_book_format.config(font=("微软雅黑", 18))  # 设置字体

    label_book_id = tk.Label(download_window, text="ID:", font=("微软雅黑", 18))
    entry_book_id = tk.Entry(download_window, width=10, font=("微软雅黑", 18))

    button_run = tk.Button(download_window, text="下载", font=("微软雅黑", 18), command=run_cli)
    button_back = tk.Button(download_window, text="返回", font=("微软雅黑", 18), command=lambda: close_window(download_window))

    # 设置小部件布局
    title_id.grid(row=0, pady=10, column=0, columnspan=2)
    command_type.grid(row=1, pady=10, column=0, columnspan=2)

    label_book_source.grid(row=2, pady=10, column=0)
    option_menu_book_source.grid(row=2, pady=10, column=1)

    label_book_format.grid(row=3, pady=10, column=0)
    option_menu_book_format.grid(row=3, pady=10, column=1)

    label_book_id.grid(row=4, pady=10, column=0)
    entry_book_id.grid(row=4, pady=10, column=1)

    button_run.grid(row=5, pady=10, column=0)
    button_back.grid(row=5, pady=10, column=1)


def gui_build():
    global type_command, dropdown_book_folder
    type_command = "build"
# 获取可执行文件的路径
    executable_path = os.path.abspath(sys.argv[0])

# 获取可执行文件所在文件夹的路径
    folder_path = os.path.dirname(executable_path)

# 获取可执行文件所在文件夹中的所有文件夹名称，并存储为列表
    folder_name = [name for name in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, name))]

                   
    main.withdraw()  # 隐藏主窗口
    build_window = tk.Toplevel()  # 创建一个新的下载窗口
    build_window.title("Novel-RS-GUI")

    
    # 创建小部件（控件）
    title_id = tk.Label(build_window, text="Novel-RS-GUI", font=("微软雅黑", 35))
    command_type = tk.Label(build_window, text="构建", font=("微软雅黑", 24))
    
    label_book_folder = tk.Label(build_window, text="选择文件夹:", font=("微软雅黑", 18))
    dropdown_book_folder = tk.StringVar()
    option_menu_book_folder = tk.OptionMenu(build_window, dropdown_book_folder, *folder_name)
    option_menu_book_folder.config(font=("微软雅黑", 18))  # 设置字体
    
    button_run = tk.Button(build_window, text="构建", font=("微软雅黑", 18), command=run_cli)
    button_back = tk.Button(build_window, text="返回", font=("微软雅黑", 18), command=lambda: close_window(build_window))
    
    # 设置小部件布局
    title_id.grid(row=0, pady=10, column=0, columnspan=2)
    command_type.grid(row=1, pady=10, column=0, columnspan=2)

    label_book_folder.grid(row=2, pady=10, column=0)
    option_menu_book_folder.grid(row=2, pady=10, column=1)
    
    button_run.grid(row=3, pady=10, column=0)
    button_back.grid(row=3, pady=10, column=1)

    


def close_window(window):
    window.destroy()
    main.deiconify()

start_check()

# 初始化
type_command = ""  # 0.搜索 1.下载 2.构建

# 创建窗口
main = tk.Tk()
main.title("Novel-RS-GUI")


# 创建控件
label_title = tk.Label(main, text="Novel-RS-GUI", font=("微软雅黑", 35))
label_author = tk.Label(main, text="GUI作者：TenSin", font=("微软雅黑", 18))

button_search = tk.Button(main, text="搜索", font=("微软雅黑", 20), command=gui_search)
button_download = tk.Button(main, text="下载", font=("微软雅黑", 20), command=gui_download)
button_build = tk.Button(main, text="构建", font=("微软雅黑", 20), command=gui_build)

# 设置控件布局
label_title.grid(row=0, pady=10, column=0, columnspan=3)
label_author.grid(row=1, pady=10, column=1, columnspan=2)

button_search.grid(row=2, pady=10, column=0)
button_download.grid(row=2, pady=10, column=1)
button_build.grid(row=2, pady=10, column=2)

# 运行窗口
main.mainloop()
