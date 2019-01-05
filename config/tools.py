import os

seperate_label = [
    '。',
]


def get_contents_by_dir(path):
    files = os.listdir(path=path)  # 得到文件夹下的所有文件名称
    article_list = []

    for file in files:  # 遍历文件夹
        if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
            f = open(path + "/" + file)  # 打开文件
            iter_f = iter(f)  # 创建迭代器
            str = ""
            for line in iter_f:  # 遍历文件，一行行遍历，读取文本
                if not line.strip() == '':
                    str = str + line
            article_list.append(str)
    return article_list
