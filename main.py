import zipfile
import os
from notion2md import *
from sys import argv


# run
def run(token, _url):
    # 导出
    print("start export notion file")
    try:
        export_cli(token, _url, 1)
    except:
        print("export notion file fail checkout your token or url")
    else:
        print("finish export notion file")
        # 压缩
        print("start compress output dir ")
        target = './notion2md_output'
        compress(target, "notionExport.zip")
        print("finish compress output dir to notionExport.zip")
        # 清理操作
        print("clean output dir")
        os.system(" rm -rf ./notion2md_output")
        print(" everything is done ")


# compress to zip
def compress(dir, file_name):
    z = zipfile.ZipFile(file_name, 'w', zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(dir):
        fpath = dirpath.replace(dir, '')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dirpath, filename), fpath + filename)
    z.close()


# check args
if len(argv) != 3:
    print("miss args,you can run this script like 'python3 main.py token_v2 url' ")
else:
    token_v2 = argv[1]
    url = argv[2]
    run(token_v2, url)
