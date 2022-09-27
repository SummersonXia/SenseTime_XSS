
from SenseTime_UI_child_log_analysis import Ui_Child_log_analysis
from SenseTime_Cabin_Service_multithread import loganalysis_thread
from PyQt5.QtWidgets import *


import time



class log_analysis_Window(QMainWindow,Ui_Child_log_analysis):
    def __init__(self,function,parent=None):
        #继承(QMainWindow,Ui_MainWindow)父类的属性
        super(log_analysis_Window,self).__init__(parent)
        #初始化界面组件
        self.function=function
        self.setupUi(self)

        self.setWindowTitle('LOG分析'+'-'+str(self.function[-1]))

        self.pushButton_log_analysis.clicked.connect(self.log_analyze)
        self.toolButton_gt_csv.clicked.connect(self.choose_gt)
        self.toolButton_log_folder.clicked.connect(self.choose_log_folder)
        self.toolButton_result_csv.clicked.connect(self.choose_result_csv)

    def log_analyze(self):
        # self.update_textBrowser(self.textBrowser,self.function[0])
        if len(self.function)==0:
            self.update_textBrowser(self.textBrowser, '请选择待分析功能')
        elif self.function[0]=='Static':
            self.update_textBrowser(self.textBrowser, time.strftime('%Y-%m-%d %H:%M:%S')+':静态手势分析开始...')
            self.analyze_log_ges = loganalysis_thread(
                function=self.function[0],
            gt_csv_path=self.lineEdit_gt.text(),
            log_folder=self.lineEdit_log_folder.text(),
            result_csv_path=self.lineEdit_result.text(),
            keyword = ["GESTURE_OK", "GESTURE_FIST", "GESTURE_V", "GESTURE_HEART", "GESTURE_PALM",
                                "GESTURE_OTHERS"],
            other_keyword = "|GESTURE_",
            thread_num = 2)
            self.analyze_log_ges.start()
            self.analyze_log_ges.signal_loganalysis.connect(self.diaglog_analyzelog)
            self.update_textBrowser(self.textBrowser,time.strftime('%Y-%m-%d %H:%M:%S') + ':log分析完成')
        elif self.function[0]=='Dynamic':
            self.update_textBrowser(self.textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':动态手势分析开始...')
            self.analyze_log_ged = loganalysis_thread(
                function=self.function[0],
                gt_csv_path=self.lineEdit_gt.text(),
                log_folder=self.lineEdit_log_folder.text(),
                result_csv_path=self.lineEdit_result.text(),
                keyword=["MJVS_GESTURE_PALM_WAVE_LEFT", "MJVS_GESTURE_PALM_WAVE_RIGHT", "MJVS_GESTURE_PALM_WAVE_UP",
                                  "MJVS_GESTURE_PALM_WAVE_DOWN", "MJVS_GESTURE_FOREFINGER_ROTATION_CLOCKWISE",
                                  "MJVS_GESTURE_FOREFINGER_ROTATION_ANTICLOCKWISE", "MJVS_GESTURE_DYNAMIC_OTHERS"],
                other_keyword="|MJVS_GESTURE_",
                thread_num=2)
            self.analyze_log_ged.start()
            self.analyze_log_ged.signal_loganalysis.connect(self.diaglog_analyzelog)
        elif self.function[0]=='OMS Action' or self.function[0]=='DMS Action':
            self.update_textBrowser(self.textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':危险动作分析开始...')
            self.analyze_log_action = loganalysis_thread(
                function=self.function[0],
                gt_csv_path=self.lineEdit_gt.text(),
                log_folder=self.lineEdit_log_folder.text(),
                result_csv_path=self.lineEdit_result.text(),
                keyword=["ACTION:Smoke","ACTION:Drink","ACTION:Call"],
                # drink_keyword="ACTION:Drink",
                other_keyword='',
                thread_num=2)
            self.analyze_log_action.start()
            self.analyze_log_action.signal_loganalysis.connect(self.diaglog_analyzelog)
        elif self.function[0]=='Drowsiness':
            self.update_textBrowser(self.textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':疲劳检测分析开始...')
            self.analyze_log_drowsiness = loganalysis_thread(
                function=self.function[0],
                gt_csv_path=self.lineEdit_gt.text(),
                log_folder=self.lineEdit_log_folder.text(),
                result_csv_path=self.lineEdit_result.text(),
                keyword=["DROWSINESS_LEVEL:Light", "DROWSINESS_LEVEL:Medium", "DROWSINESS_LEVEL:Heavy"],
                other_keyword='',
                thread_num=2)
            self.analyze_log_drowsiness.start()
            self.analyze_log_drowsiness.signal_loganalysis.connect(self.diaglog_analyzelog)
        elif self.function[0]=='GAZEAOI':
            self.update_textBrowser(self.textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':功能开发中...')
        elif self.function[0]=='Distraction':
            self.update_textBrowser(self.textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':分心检测分析开始...')
            self.analyze_log_distraction = loganalysis_thread(
                function=self.function[0],
                gt_csv_path=self.lineEdit_gt.text(),
                log_folder=self.lineEdit_log_folder.text(),
                result_csv_path=self.lineEdit_result.text(),
                keyword=["DISTRACTION_LEVEL:heavy", "DISTRACTION_LEVEL:medium", "DISTRACTION_LEVEL:light"],
                other_keyword='',
                thread_num=2)
            self.analyze_log_distraction.start()
            self.analyze_log_distraction.signal_loganalysis.connect(self.diaglog_analyzelog)
        elif self.function[0]=='Emotion':
            self.update_textBrowser(self.textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':OMS表情检测分析开始...')
            self.analyze_log_emotion = loganalysis_thread(
                function=self.function[0],
                gt_csv_path=self.lineEdit_gt.text(),
                log_folder=self.lineEdit_log_folder.text(),
                result_csv_path=self.lineEdit_result.text(),
                keyword=["EMOTION:Neutral","EMOTION:Positive","EMOTION:Negative"],
                other_keyword='',
                thread_num=2)
            self.analyze_log_emotion.start()
            self.analyze_log_emotion.signal_loganalysis.connect(self.diaglog_analyzelog)
        elif self.function[0] == 'Gender':
            self.update_textBrowser(self.textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':功能开发中...')
        elif self.function[0] == 'Age':
            self.update_textBrowser(self.textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':功能开发中...')
        elif self.function[0] == 'Child':
            self.update_textBrowser(self.textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':疲劳检测分析开始...')
            self.analyze_log_child = loganalysis_thread(
                function=self.function[0],
                gt_csv_path=self.lineEdit_gt.text(),
                log_folder=self.lineEdit_log_folder.text(),
                result_csv_path=self.lineEdit_result.text(),
                keyword={  # "PERSON_NUMBER:No_Person":0,
                    "CHILD:Person 0 is child": 1},
                other_keyword='',
                thread_num=2)
            self.analyze_log_child.start()
            self.analyze_log_child.signal_loganalysis.connect(self.diaglog_analyzelog)
        elif self.function[0] == 'PA':
            self.update_textBrowser(self.textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':功能开发中...')
        elif self.function[0] == 'FACEID':
            self.update_textBrowser(self.textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':功能开发中...')
        elif self.function[0] == 'Safety Seat':
            self.update_textBrowser(self.textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':功能开发中...')

    def choose_gt(self):
        self.gt_csv_file = QFileDialog.getOpenFileNames(QMainWindow(), '请选择gt文件', './',
                                                                "csv Files(*.csv)")
        self.lineEdit_gt.setText(self.gt_csv_file[0][0])
        # print(self.lineEdit_gt.text())

    def choose_log_folder(self):
        self.log_folder = QFileDialog.getExistingDirectory(QMainWindow(), '请选择log文件夹', './')
        self.lineEdit_log_folder.setText(self.log_folder)
        # print(self.log_folder)

    def choose_result_csv(self):
        self.result_csv_file = QFileDialog.getSaveFileName(QMainWindow(), "结果文件保存", "./",
                                                           "csv Files(*.csv)")
        self.lineEdit_result.setText(self.result_csv_file[0])
        # print(self.result_csv_file)
    def diaglog_analyzelog(self,str):
        self.update_textBrowser(self.textBrowser,time.strftime('%Y-%m-%d %H:%M:%S') + str)

    def update_textBrowser(self, textBrowser, addtext="..."):
        """
        文本框追加信息
        :param textBrowser: 文本框句柄
        :param addtext: 需要添加的文本
        :return:
        """
        textBrowser.append(addtext)  # 文本框逐条添加数据
        # textBrowser.append("\n")
        textBrowser.moveCursor(textBrowser.textCursor().End)  # 文本框显示到底部
        QApplication.processEvents()  # 刷新窗口