# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 09:18:18 2020
@author: cherish
"""

import fitz

def split_pdf_same_page(pathStr, page):
    """
    将pdf 拆分为 多个pdf文件，每page页为一部分
    :param: pathStr :pdf路径的字符串, page : int 分割区间
    :return: true
    """
    doc = fitz.open(pathStr)
    # doc1 = fitz.open() # 空 pdf 文件
    docPage = doc.pageCount
    if page > docPage or page ==0 :
        return "错误 : 页码超出范围，或 分割区间为0 !"

    num = docPage//page  # 可以拆成 page 页的部分
    for i in range(num):  # 0 到 num-1
        doc1 = fitz.open()  # 空 pdf 文件
        doc1.insertPDF(doc, from_page=page*i, to_page=page*(i+1)-1, start_at=-1)
        partName = '[part'+str(i)+'].pdf'
        newName = pathStr.replace(".pdf", partName)
        doc1.save(newName)
        doc1.close()

    surplus = docPage % page  # 最后少于 page 的部分
    if surplus != 0:
        doc1 = fitz.open()  # 空 pdf 文件
        doc1.insertPDF(doc, from_page=page*num, to_page=docPage-1, start_at=-1)
        partName = '[part'+str(num)+'].pdf'
        newName = pathStr.replace(".pdf", partName)
        doc1.save(newName)
        doc1.close()
    return "拆分成功"


def split_pdf_custom_page(pathStr, pageStr):
    """
    将pdf拆分为自定义页码的多个pdf文件
    :param: str ,pdf路径的字符串, pageStr: 自定义页码的字符串
    :return: Error page string / True
    """
    doc = fitz.open(pathStr)
    docPage = doc.pageCount
    pageStr = pageStr.replace('，', ',')  # 如果是中文逗号
    pageList = pageStr.split(",")

    for page in pageList:
        pse = page.split('-')  # page start and end
        ps = int(pse[0])
        pe = int(pse[0]) if len(pse) == 1 else int(pse[1])
        if ps > pe or pe > docPage:
            return "请检查>  "+ page + " 是否有误 !"  # error: page part

        doc1 = fitz.open()  # 创建 空pdf文件
        doc1.insertPDF(doc, from_page=ps-1, to_page=pe-1, start_at=-1)
        partName = '[page'+str(ps)+'-' + str(pe)+'].pdf'
        newName = pathStr.replace(".pdf", partName)
        doc1.save(newName)
        doc1.close()
    return "拆分成功"
