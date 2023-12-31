import sys
import os
from PyInstaller.__main__ import run
from src.constants.constants import ROOT_PATH

from src.util.file_tools import FileTools


CUR_PATH = os.path.dirname(os.path.abspath(__file__))
VERSION = "debug"

if __name__ == "__main__":
    program_path = ROOT_PATH + r"\src\E5KeepActive.py"
    performable_path = ROOT_PATH + r"\bin"
    icon_file_path = ROOT_PATH + r"\resources\ico\E5KeepActive.ico"
    work_path = CUR_PATH + r"\E5KeepActive_build"
    # 创建运行时需要的文件夹
    new_folder = [ROOT_PATH + r"\tmp", ROOT_PATH + r"\logs"]

    for folder in new_folder:
        FileTools.delete_file_or_folder(folder)
        os.mkdir(folder)

    # 设置编译参数和选项
    options = [
        "--onefile",  # 打包成单个可执行文件
        # "--onedir",  # 生成一个包含可执行文件的目录
        # '--noconsole',  # 不显示控制台窗口
        "--clean",  # 清理临时文件
        "--name={}".format("E5KeepActive"),  # 指定生成的可执行文件名称
        "--distpath={}".format(performable_path),  # 指定生成的可执行文件路径
        "--icon={}".format(icon_file_path),  # 指定生成的可执行文件图标
        "--specpath={}".format(CUR_PATH),  # 指定 .spec 文件的输出路径
        "--workpath={}".format(work_path),  # 指定build 文件夹路径
        "--hidden-import={}".format("msgraph"),  # 强制将模块包含在可执行文件中
        "--hidden-import={}".format("azure.identity"),
        "--paths={}".format(
            "D:\\Programs\\Python\\Python310\\Lib\\site-packages"
        ),  # 用于搜索导入的路径
    ]

    if "release" == VERSION:
        options.append("--noconsole")  # 不显示控制台窗口

    print(options)
    # 运行 PyInstaller
    try:
        run(
            [
                str(program_path),
                *options,
            ]
        )
    except Exception as e:
        print(e)
        sys.exit(1)
