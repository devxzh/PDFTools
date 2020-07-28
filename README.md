### 基于PyQt5实现的PDF工具箱

---

#### 功能：批量添加目录，增强图像，拆分pdf，合并pdf

---

### 前言

PDF 是一种便携，易查找的电子书，在学习工作中我们可能需要翻阅大量的参考书籍，实体书往往贵且笨重，如果需要经常翻阅，那么可以购置纸质书。但是大多数时候我们可能只是需要查阅书中的某一部分，如此电子书便具有不可比拟的优势，互联网上有者大量的电子书籍，且多数以`pdf`格式流传，其中一部分为文字版，一部分为扫描版。这些文件一般为自制的盗版书籍，往往缺少目录，或者扫描不清晰。以致索引困难，观感极差。

市面上也有很多`pdf编辑器`，如`Adobe Acrobat PDF`,`PDF Element`,`福昕PDF编辑器`等，但他们大多价格昂贵，且没有批量添加目录的功能，虽有OCR增强的功能，但是比较耗时，且在年迈的PC上容易卡死。此工具没有使用OCR，仅对扫描页面的图片逐一增强来改善PDF清晰度。

### 1. 使用模块

1. `pyqt5`，`pymupdf`，`python3.7` ，`qt designer` ，`QCandyUi`(可选)
2. 指定下载源。可后加`-i https://pypi.tuna.tsinghua.edu.cn/simple`，如

```powershell
pip3 install pymupdf -i https://pypi.tuna.tsinghua.edu.cn/simple
pip3 install pyqt5,pyqt5-tools
```

3. 在终端输入 `designer` 可启动 QT Designer
4. 注意：如果在电脑上已经安装过`Ananconda`，则`pyqt`版本过高可能会导致`Spyder`无法打开，此时请使用如下命令，更换版本，(不要频繁的使用conda update)

```
pip3 uninstall pyqt5
pip3 install pyqt5==5.12.0
```

版本号如果有误，终端会列出可安装的版本，选择其一输入即可

### 2. 编辑环境搭建

1. IDE：[PyCharm Edu](https://www.jetbrains.com/pycharm-edu/)  ，[Spyder](https://www.spyder-ide.org/) ，[VS Code + Python 插件](https://code.visualstudio.com/)

2. 上述工具择其一即可，其中PyCharm 配置后可一体化开发 [配置教程-博客园](https://www.cnblogs.com/lsdb/p/9122425.html)，[配置教程-知乎](https://zhuanlan.zhihu.com/p/52920094)

3. 我没有配置，逐一进行

4. | 用途                    | 工具/方法                     |
   | ----------------------- | ----------------------------- |
   | 绘制用户界面 (UI)       | QT Designer                   |
   | UI转Python代码          | pyuic5                        |
   | 编写Python 代码         | PyCharm / VS Code             |
   | 执行代码                | python3.7 (PyCharm / VS Code) |
   | 打包为可执行文件 (可选) | pyinstaller                   |

### 3.工具箱功能概述

1. 主界面 (使用QCandyUi美化后的截图)

![imageMain.png](https://i.loli.net/2020/07/21/sQMa94oV1qOmLj2.png)

2. 添加目录

![imageAdd.png](https://i.loli.net/2020/07/21/YzNgBd8yThGVv7e.png)

3. 文本增强

![imageEnhance.png](https://i.loli.net/2020/07/21/1SVjMAOD3idRWBP.png)

4. 拆分文档

![imageSplit.png](https://i.loli.net/2020/07/21/XLI1RNDyof5OQtb.png)

5. 合并文档

![imageMerge.png](https://i.loli.net/2020/07/21/tpxkQFmwI5LSMh1.png)

### 4.步骤解析

1. 使用QT Designer 绘制界面(如上图) ，选择 `QDialog without Button`，拖拽控件，绘制后保存为`.ui`文件，我分别保存为`PDFTools.ui`   `add_UI.ui`   `enhance_UI.ui`   `merge_UI.ui`    `split_UI.ui`，绘制界面比较简单，但是`控件命名`应当添加适当的`前缀或后缀`加以区分。

2. 使用`pyuic5`命令将ui文件转换为python代码，切换到项目文件夹，输入

   ```bash
   pyuic5 PDFTools.ui -o PDFTools.py
   ```

   依次对界面代码进行转换，生成后的py文件无需手动更改，当再次生成时会完全覆盖。

3. 编写调用窗口和信号处理代码。pyqt延续了qt的设计思想，只要处理好信号与槽(可理解为触发事件与处理方法关联)，那么编写项目也会得心应手。在编写过程中可查看[qt类手册](https://doc.qt.io/qt-5/qtwidgets-module.html)，pyqt中的方法大多与QT C++同名，但是少了`丑陋的指针` `->`，使代码不那么扎眼。具体见代码解析

4. 推荐使用`ipython`在命令行窗口对方法/类 进行测试

5. ~~如果需要可进行打包~~ (生成的文件可能无法直接运行)

   ```bash
   pyinstaller --onefile --windowed --icon=PDF.ico main.py
   ```

### 5.项目组成(四个`callxxx.py`均可独立运行)

1. 代码组成 

   ```
   --------窗口信号处理----------
   main.py
   callAdd.py
   callEnhance.py
   callSplit.py
   callMerge.py
   --------窗口界面布局----------
   PDFTools.py
   add_UI.py
   enhance_UI.py
   split_UI.py
   merge_UI.py
   --------PDF处理函数----------
   addFunctins.py
   enhanceFunctions.py
   splitFunctions.py
   ```

2. 用到的QT控件信号， 通过 connect 可关联方法

   | 控件        | 信号                          |
   | ----------- | ----------------------------- |
   | pushButton  | clicked                       |
   | spinBox     | valueChanged /editingFinished |
   | Slider      | sliderMoved / valueChanged    |
   | radioButton | toggled                       |
   | lineEdit    | textChanged                   |
   | checkBox    | stateChanged                  |
   | comboBox    | currentIndexChanged           |

3. 用到的QT控件方法 ，大多数控件都有setText() 和text() 方法，不一一列举

   | 控件        | 方法               |
   | ----------- | ------------------ |
   | textEdit    | setText()  /text() |
   | lineEdit    | setText() / text() |
   | checkBox    | isChecked()        |
   | tableWidget | setItem()          |
   | spinBox     | setReadOnly()      |
   | lineEdit    | setReadOnly        |

4. `pymupdf`中的方法

   | 名称      | 描述                |
   | --------- | ------------------- |
   | open      | 打开文件(pdf，图片) |
   | save      | 保存                |
   | setToC    | 设置目录            |
   | getPixmap | 获取本页的图片      |
   | insertPDF | 插入PDF             |
   | close     | 关闭                |
   | pageCount | 获取页码（属性）    |
   | getToC    | 获取目录            |

5. `os` ，`PIL` 中的方法

   | 方法                  | 描述                   |
   | --------------------- | ---------------------- |
   | open                  | 打开txt                |
   | write                 | 写入txt                |
   | close                 | 关闭文本               |
   | strip                 | 删除指定符号           |
   | split                 | 根据指定符号分割字符串 |
   | len                   | 计算长度，数量         |
   | range                 | 连续的数               |
   | replace               | 替换指定字符串         |
   | os.getcwd()           | 获取当前文件路径       |
   | os.path.exists()      | 是否存在文件夹         |
   | os.makedirs()         | 创建文件夹             |
   | os.remove()           | 删除文件               |
   | Image.open            | 打开图片               |
   | ImageEnhance.Contrast | 增强方法               |

6. `demo.txt` 该文件是存放目录的文件，要求和格式见下，在打开`添加目录`窗口的同时会自动生成该文件

   ```txt
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
   ```


### 7.结语

第一次使用`pyqt5`写一个完整的项目，用时大概六天。前期绘制界面一天。后期逐一完善各个功能四天，写文档，改bug一天。最大的感受就是Python语法友好，轮子很全。本次项目也是熟悉pyqt的过程。写完本应用基本掌握了常用的控件，信号，槽。整体而言，使用pyqt5编写一些小工具还是很方便的。至于执行效率，一般的小项目基本体现不出来。

PyQt5优点：相较于QT Creator，python代码比较优雅；相较于 C# Winform/WPF ，python拥有较多的库。可用样式表`setStyleSheet`美化控件

缺点：QT Designer 可设置参数偏少，需要使用代码设置，控件不够美观，打包文件偏大，推荐直接运行脚本。

### 8.参考

- [pymupdf](https://pymupdf.readthedocs.io/en/latest/#)
- [qt class](https://doc.qt.io/qt-5/qtwidgets-module.html)
- [Qt5 Python GUI Programming Cookbook 2018](https://www.amazon.com/Qt5-Python-Programming-Cookbook-cross-platform/dp/1788831004)

### 9.ToDo List

	- [ ] 自定义样式表
	- [ ] 自动爬取目录
	- [ ] img2pdf

### 联系我： devxzh@qq.com

