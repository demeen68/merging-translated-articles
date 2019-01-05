import Levenshtein
import os
from config.tools import seperate_label, get_contents_by_dir

path = "/home/demeen/Desktop/data/check_fanyi/data"  # 文件夹目录
article_list = get_contents_by_dir(path=path)
distance_list = []
for index in range(len(article_list) - 1):
    # todo at first think about the whole sentence

    pass

    # distance = Levenshtein.distance(article_list[index], article_list[index + 1])
    # print(distance)
    # print(len(article_list[index]))
# dis = Levenshtein.distance('abc', 'acb')
# print(dis)
