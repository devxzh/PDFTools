# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 12:43:01 2020

@author: cherish
"""

shorthelp = """\
输入参数及参数说明
——————————————————————————
1. pdf源文件  2. txt格式的目录文件  3. 设置页码补偿参数
——————————————————————————
1. 添加目录后的 pdf文件与源文件同目录(文件名后添加'-new')
2. txt 文件详见此程序同目录下的 'demo.txt'
3. 页码补偿为 目录页码 与实际 pdf页码的偏差，
    如txt目录中页码为12 对应实际pdf的18页
    则页码补偿应为 6，此值默认设置为 0
——————————————————————————\
"""

demostr = """
# =========================================================================
# 本应用主要针对无目录pdf文件(扫描或文字版)
# 目录可在各大图书网站(如豆瓣，京东，当当)查找，然后复制目录到 .txt 文件
# 根据需要适当调整 ，txt文件中可添加注释，以 '#' 开头，单独占一行
# =========================================================================
# 
# 建议在如下网站搜集目录：
#           1.京东图书 https://book.jd.com/
#           2.豆瓣读书 https://book.douban.com/
#           3.当当图书 http://book.dangdang.com/
#           4.文泉书局 https://wqbook.wqxuetang.com/
# 
# =========================================================================
# 标准格式1 如下:(空行不影响)
# 特征 ：两部分构成： 标题 + 空格 + 页码
# 标题中含 '第' 和 '章' 的会识别为一级标题，其他为二级标题
# =========================================================================

第1章概述     1
什么是OpenCV        1
OpenCV怎么用        2
什么是计算机视觉     3
OpenCV的起源        6
OpenCV的结构    7
使用IPP来加速OpenCV     8
谁拥有OpenCV    9
下载和安装OpenCV    9

# ==========================================================================
# 标准格式2 如下 
# 特征 ：章序/节序 + 空格 + 标题 + 空格 + 页码 （空格用于区分各元素）
# 无 章节序 的 默认识别为 二级标题 ，若想设置为一级标题，请在前加 '@ '，
# 一般 需要区分的是 前言 目录 附录 参考文献 这些 
# 节序中有一个点 表二级标题(如 6.1 )，两个点 表三级标题(如 1.2.3)，以此类推
# ==========================================================================

第6章 支持向量机 121
6.1 间隔与支持向量 121
6.2 对偶问题 123
6.3 核函数 126
6.4 软间隔与正则化 129
6.5 支持向量回归 133
6.6 核方法 137
6.7 阅读材料 139
习题 141
休息一会儿 145
@ 参考文献 520

# ==========================================================================
#   建议使用 VSCode , EverEdit , Notepad++ , Sublime 等编辑器编辑 txt文件
# ==========================================================================
#
# —— 格式1 与 格式 2 取 其一 即可，用时替换非注释(#)部分,并删除不使用的格式 ——
# 
# ==========================================================================
"""


def generate_txtdemo():
    """
    生成 demo.txt 文件(目录样本文件)
    :param :无
    :return:无
    """
    demotxt = open("demo.txt", 'w+', encoding='UTF-8', errors='ignore')
    demotxt.write(demostr)
    demotxt.close()


def count_dot(str):
    """
    没有点是二级标题，1个点是二级标题，2个点是三级标题
    :param: str 
    :return: int 
    """
    n = 2
    for i in str:
        if i == '.':
            n += 1
    return n


def get_level(str):
    """
    :获取标题级别  带有'章'或者'@' 关键字的是一级标题，否则按照小数点记级别
    :param: string 
    :return: int   
    """
    level = 1
    if ('第' in str) and ('章' in str) or ('@' in str):
        level = 1
    else:
        level = count_dot(str)
    return level


def get_title(str):
    """
    获取标题 ： 章节 + 标题 
    :param : str 输入应是 一行数据 如：( 6.1 间隔与支持向量 121 )
    :return: str title
    """
    part = str.strip("@").split()  # delete @

    if len(part) == 2:
        return part[0]
    elif len(part) == 3:
        return part[0] + ' ' + part[1]
    else:
        return '0'  # error


def get_page(str):
    """
    获取该项页码
    :param : str
    :return: int page
    """
    page = str.split()[-1]
    temp=page
    if temp.strip().lstrip('-').isdigit():
    	return int(page)
    else:
	    return "该行目录错误: "+str


def add2pdf(pdffile, txtfile, offset):
    """
    添加目录到PDF,其中文件应为打开状态
    :param: pdffile , textfile , offset
    :return:pdffile
    """
    lines = txtfile.readlines()
    toc = []
    
    for line in lines:
        if line[0] == '#' or len(line.split()) == 0:
            continue
        level = get_level(line)
        title = get_title(line)
        if type(get_page(line))==type(1): #number
        	page = get_page(line)+ offset
        	toc.append([level, title, page])
        else:
	        return get_page(line)   # error str
        
    pdffile.setToC(toc)
    return pdffile
