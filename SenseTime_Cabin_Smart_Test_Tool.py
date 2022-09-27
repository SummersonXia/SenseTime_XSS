"""
视频标注工具
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from SenseTime_OVI_TestTool_func import *


import cgitb
import warnings

cgitb.enable(format="text")



warnings.filterwarnings('ignore')


if __name__ == "__main__":
    #创建QApplication 固定写法
    app = QApplication(sys.argv)
    # 实例化界面
    window = MainWindow()
    window.setStyleSheet("#MainWindow{background-color:rgb(150, 150, 150)}")
    # icon = QIcon()
    # icon.addPixmap(QPixmap('.\\sensetime.ico'), QIcon.Normal, QIcon.Off)
    window.setWindowIcon(QIcon(':/sensetime.ico'))
    # window.setWindowIcon(QIcon('SenseAuto.jpg'))
    #显示界面
    window.show()
    #阻塞，固定写法
    sys.exit(app.exec_())

