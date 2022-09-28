import  os
if __name__ == '__main__':
    from PyInstaller.__main__ import run
    opts=['SenseTime_Cabin_Smart_Test_Tool.py','-F','-w','-i=C:\\Users\\xiasensen\\PycharmProjects\\pyqt_testtools_Sensetime - phase3\\sensetime.ico']
    run(opts)