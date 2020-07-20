### 基于PyQt5实现的PDF工具箱

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

![image-20200720223727138](C:\Users\cherish\AppData\Roaming\Typora\typora-user-images\image-20200720223727138.png)

2. 添加目录

![image-20200720223933871](C:\Users\cherish\AppData\Roaming\Typora\typora-user-images\image-20200720223933871.png)

3. 文本增强

![image-20200720224009662](C:\Users\cherish\AppData\Roaming\Typora\typora-user-images\image-20200720224009662.png)

4. 拆分文档

![image-20200720224048371](C:\Users\cherish\AppData\Roaming\Typora\typora-user-images\image-20200720224048371.png)

5. 合并文档

![image-20200720224118804](C:\Users\cherish\AppData\Roaming\Typora\typora-user-images\image-20200720224118804.png)

### 4.步骤解析

1. 使用QT Designer 绘制界面(如上图) ，选择 `QDialog without Button`，拖拽控件，绘制后保存为`.ui`文件，我分别保存为`PDFTools.ui`   `add_UI.ui`   `enhance_UI.ui`   `merge_UI.ui`    `split_UI.ui`，绘制界面比较简单，但是`控件命名`应当添加适当的`前缀或后缀`加以区分。

2. 使用`pyuic5`命令将ui文件转换为python代码，切换到项目文件夹，输入

   ```bash
   pyuic5 PDFTools.ui -o PDFTools.py
   ```

   依次对界面代码进行转换，生成后的py文件无需手动更改，当再次生成时会完全覆盖。

3. 编写调用窗口和信号处理代码。pyqt延续了qt的设计思想，只要处理好信号与槽(可理解为触发事件与处理方法关联)，那么编写项目也会得心应手。在编写过程中可查看[qt类手册](https://doc.qt.io/qt-5/qtwidgets-module.html)，pyqt中的方法大多与QT C++同名，但是少了`丑陋的指针` `->`，使代码不那么扎眼。具体见代码解析

4. 推荐使用`ipython`对方法/类 进行测试

5. 如果需要可进行打包

   ```bash
   pyinstaller --onefile --windowed --icon=PDF.ico main.py
   ```

### 5.项目组成

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
   | spinBox     | valueChanged /editintFinished |
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

### 6.代码详见[Github](https://github.com/devxzh/PDFTools)

### 7.ToDo List

​	-[ ] 自定义样式表

​	-[ ] 自动爬取目录

​	-[ ] img2pdf

### 8.联系我： devxzh@qq.com

