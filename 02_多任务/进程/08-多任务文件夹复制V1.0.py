import os
import multiprocessing


def copy_file(file_name, old_folder_name, new_folder_name):
    """完成文件物质"""
    print("模拟复制文件:从 %s ---> 到 %s, 文件名：%s" % (old_folder_name, new_folder_name, file_name))
    old_f = open(old_folder_name + "/" + file_name, "rb")
    content = old_f.read()
    old_f.close()

    new_f = open(new_folder_name + "/" + file_name, "wb")
    new_f.write(content)
    new_f.close()


def main():
    # 1. 获取用户要复制的文件夹的名字
    old_folder_name = input("请输入要复制的文件夹名字")
    # 2. 创建一个新的文件夹
    try:
        new_folder_name = old_folder_name + "[复件]"
        os.mkdir(new_folder_name)
    except:
        pass
    
    # 3. 获取文件夹中所有的待复制的文件名字 os.listdir()
    file_names = os.listdir(old_folder_name)

    # 4. 创建进程池
    po = multiprocessing.Pool(5)

    # 5. 向进程池中添加拷贝文件的任务
    for file_name in file_names:
        po.apply_async(copy_file, args=(file_name, old_folder_name, new_folder_name))
    po.close()
    po.join()
    

if __name__ == "__main__":
    main()
