import tkinter as tk
import subprocess
import shutil
import os
import sys


class BookInfo:
    def __init__(self,source,book_ID,book_format,keyword):   
                        #书源，ID，格式(下载)，关键字（构建）
        self.source = source
        self.book_ID = book_ID
        self.book_format = book_format
        self.keyword = keyword
class Command:
    def __init__(self,type_command):
        self.type_command = type_command
    def run(self):
        if self.type_command == "download":
            print("下载ing")
            subprocess.run("novel-cli.exe download "+MainBook.book_ID.get()+" --source "+MainBook.source.get()+" --format "+MainBook.book_format.get())
        elif self.type_command == "build":
            print("构建ing")
            book_folder_tuple = eval(dropdown_book_folder.get())
            book_folder = book_folder_tuple[0] if book_folder_tuple else None

            subprocess.run("novel-cli.exe build "+book_folder)
            shutil.rmtree(book_folder)
        elif self.type_command == "search":
            print("搜索ing")
            subprocess.run("novel-cli.exe search "+MainBook.keyword.get()+" --source "+MainBook.source.get())


def run_cli(type_command):
    global MainBook,MainCommand
    MainBook=BookInfo(dropdown_book_source,entry_book_id,dropdown_book_format,entry_keyword)
    MainCommand=Command(type_command)
    MainCommand.run()


def start_check():
    print("检察环境ing")
    if os.path.exists("novel-cli.exe"):
        print("环境正常")
    else:
        print("环境异常，请下载novel-cli.exe")

def gui_search():
    global  entry_keyword, dropdown_book_source
    type_command="search"
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
    
    button_run = tk.Button(search_window, text="搜索", font=("微软雅黑", 18), command=lambda: run_cli(type_command))
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
    global  entry_book_id, dropdown_book_format, dropdown_book_source
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

    button_run = tk.Button(download_window, text="下载", font=("微软雅黑", 18), command=lambda:run_cli("download"))
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
    option_menu_book_folder = tk.OptionMenu(build_window, dropdown_book_folder, folder_name)
    option_menu_book_folder.config(font=("微软雅黑", 18))  # 设置字体
    
    button_run = tk.Button(build_window, text="构建", font=("微软雅黑", 18), command=lambda:run_cli("build"))
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









#主程序
start_check()
#初始化数据
dropdown_book_source=None
entry_book_id=None
dropdown_book_format=None
entry_keyword=None
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
