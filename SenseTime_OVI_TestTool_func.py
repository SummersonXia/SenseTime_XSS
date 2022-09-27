import threading

from SenseTime_OVI_TestTool import Ui_MainWindow
from SenseTime_UI_child_MCU_Connection_settings_func import MCU_Connection_settings_Window
from SenseTime_UI_child_log_analysis_func import log_analysis_Window
from SenseTime_Cabin_Service_func_run_analysis import SenseAuto_Cabin_Service_run_analysis
from PyQt5.QtGui import *
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QBrush, QColor
from PyQt5.QtCore import Qt
from SenseTime_Cabin_Service_multithread import *

import csv

import time





class MainWindow(QMainWindow,Ui_MainWindow):
    # _signal=pyqtSignal(str)
    def __init__(self,parent=None):
        #继承(QMainWindow,Ui_MainWindow)父类的属性
        super(MainWindow,self).__init__(parent)
        #初始化界面组件
        self.setupUi(self)

        # menubar signal connection
        self.actionNew_Project.triggered.connect(self.make_project_file)
        self.actionOpen_Project.triggered.connect(self.open_project_file)
        self.action_openfile.triggered.connect(self.loaddata)
        self.action_savefile.triggered.connect(self.savedata)
        self.action_Functions.triggered.connect(self.expand_functions)
        self.action_loganalyze.triggered.connect(self.log_analysis)
        self.action_runSDK.triggered.connect(self.MCU_Connection_Settings)
        self.action_csv_result.triggered.connect(self.loaddata)
        self.action_display_statistics.triggered.connect(self.runAnalysis)

        # treeWidget signal connection
        self.treeWidget_functions.itemChanged.connect(self.treechild_state)

        # tabWidget signal connection
        self.tabWidget.tabCloseRequested.connect(self.close_tab)

        # treeView signal connection
        self.treeView.doubleClicked.connect(self.treeview_doubleclick)


        self.treeWidget_functions.topLevelItem(0).child(0).setCheckState(0, Qt.Unchecked)
        self.treeWidget_functions.topLevelItem(0).child(1).setCheckState(0, Qt.Unchecked)
        self.treeWidget_functions.topLevelItem(0).child(2).setCheckState(0, Qt.Unchecked)
        self.treeWidget_functions.topLevelItem(0).child(3).setCheckState(0, Qt.Unchecked)
        self.treeWidget_functions.topLevelItem(0).child(4).setCheckState(0, Qt.Unchecked)
        self.treeWidget_functions.topLevelItem(1).child(0).setCheckState(0, Qt.Unchecked)
        self.treeWidget_functions.topLevelItem(1).child(1).setCheckState(0,Qt.Unchecked)
        self.treeWidget_functions.topLevelItem(1).child(2).setCheckState(0, Qt.Unchecked)
        self.treeWidget_functions.topLevelItem(1).child(3).setCheckState(0, Qt.Unchecked)
        self.treeWidget_functions.topLevelItem(1).child(4).setCheckState(0, Qt.Unchecked)
        self.treeWidget_functions.topLevelItem(1).child(5).setCheckState(0, Qt.Unchecked)
        self.treeWidget_functions.topLevelItem(1).child(6).setCheckState(0, Qt.Unchecked)
        self.treeWidget_functions.topLevelItem(2).child(0).setCheckState(0, Qt.Unchecked)
        self.treeWidget_functions.topLevelItem(2).child(1).setCheckState(0, Qt.Unchecked)


        # palette = QPalette()
        # palette.setBrush(QPalette.Background, QBrush(QPixmap("./icon/SenseAuto.jpg")))
        # self.tabWidget.setStyleSheet("background-color:rgb(200, 200, 200)")
        self.setStyleSheet("background-color:rgb(130, 130, 130)")
        self.treeView.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.treeWidget_functions.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.dockWidget_4.setStyleSheet("background-color:rgb(140, 140, 140)")
        self.Dialog_textBrowser.setStyleSheet("background-color:rgb(255, 255, 255)")




    def loaddata(self):
        try:
            self.loaddata_csvpath = QFileDialog.getOpenFileNames(QMainWindow(), '请选择结果文件', './',
                                                                     "csv Files(*.csv)")
            self.loaddata_csvfile=open(self.loaddata_csvpath[0][0],'r')
            self.loaddata_csvfile_ls=self.loaddata_csvfile.readlines()
            # text_line=''
            # for line in self.loaddata_csvfile_ls:
            #     text_line+=line
            self.display_loaddata_csv(self.loaddata_csvpath[0][0], self.loaddata_csvfile_ls)
        except:
            pass


    def log_analysis(self):
        function=self.choosed_function
        print(function)
        if len(function)>0:
            self.log_analysis_child_window=log_analysis_Window(function,self)
            self.log_analysis_child_window.show()
        else:
            self.update_textBrowser(self.Dialog_textBrowser,time.strftime('%Y-%m-%d %H:%M:%S') + ':请选择分析功能')

    def savedata(self):
        pass

    def expand_functions(self):
        self.treeWidget_functions.expandAll()

    def make_project_file(self):
        self.new_project_path = QFileDialog.getExistingDirectory(QMainWindow(),'请选择项目文件夹','./')
        # print(self.new_project_path)
        try:
            os.makedirs(self.new_project_path+os.sep+'log')
        except:
            pass
        try:
            os.makedirs(self.new_project_path + os.sep + 'gt')
        except:
            pass
        try:
            os.makedirs(self.new_project_path + os.sep + 'result')
        except:
            pass
        try:
            os.makedirs(self.new_project_path + os.sep + 'SDK')
        except:
            pass
        try:
            os.makedirs(self.new_project_path + os.sep + 'video')
        except:
            pass
        self.treeview_project(self.new_project_path)

    def open_project_file(self):
        try:
            self.open_project_path = QFileDialog.getExistingDirectory(QMainWindow(), '请选择项目文件夹', './')
            self.treeview_project(self.open_project_path)
        except:
            pass

    def treeview_project(self,path):
        self.model = QFileSystemModel()
        self.project_root_path=path
        # print(self.project_root_path)
        self.model.setRootPath(self.project_root_path)
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(self.project_root_path))
        for col in range(1, 4):
            self.treeView.setColumnHidden(col, True)

    def treeview_doubleclick(self,Qmodelidx):
        clicked_file_path = self.model.filePath(Qmodelidx)
        if not os.path.isdir(clicked_file_path):
            if clicked_file_path.endswith('.csv'):
                self.read_csv(clicked_file_path)
            elif clicked_file_path.endswith('txt'):
                self.read_txt(clicked_file_path)
            else:
                self.update_textBrowser(self.Dialog_textBrowser,time.strftime('%Y-%m-%d %H:%M:%S') + ':暂不支持该格式文件')
        else:
            pass

    def read_txt(self,file_path):
        self.txt_csv_file=open(file_path,'r').readlines()
        txt_line=''
        for line in self.txt_csv_file:
            txt_line+=line
        self.display_loaddata_txt(file_path,txt_line)

    def read_csv(self,file_path):
        csv_file=open(file_path,'r').readlines()
        self.display_loaddata_csv(file_path, csv_file)


    def treechild_state(self,item,column):
        self.choosed_function=[]
        if item.checkState(column)==Qt.Checked:
            self.choosed_function.append(item.text(column))


    def runAnalysis(self):
        print(self.choosed_function)
        run_analysis=SenseAuto_Cabin_Service_run_analysis(self.loaddata_csvfile_ls)
        if len(self.choosed_function)<1:
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':请选择功能')
        elif len(self.loaddata_csvfile_ls)<1:
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':请选择有效结果文件')

        elif len(self.choosed_function)==1 and len(self.loaddata_csvfile_ls)>0 and self.choosed_function[0]=='DMS Action':
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':DMS Action 结果分析中...')
            res_oms_action = []
            res_run_analysis = run_analysis.analyze_DMS_Action()
            header_line = [' ', 'TP', 'FN', 'FP', 'TN', 'P', 'N', 'Sum', 'TPR', 'FPR', 'PRE']
            res_sm_all_line = res_run_analysis[0][0]
            res_sm_wgh_line = res_run_analysis[0][1]
            res_dr_all_line = res_run_analysis[1][0]
            res_dr_wgh_line = res_run_analysis[1][1]
            res_ca_all_line = res_run_analysis[2][0]
            res_ca_wgh_line = res_run_analysis[2][1]
            res_oms_action.append(header_line)
            res_oms_action.append(res_sm_all_line)
            res_oms_action.append(res_sm_wgh_line)
            res_oms_action.append(res_dr_all_line)
            res_oms_action.append(res_dr_wgh_line)
            res_oms_action.append(res_ca_all_line)
            res_oms_action.append(res_ca_wgh_line)
            self.display_result_csv(res_oms_action, 'dms action')
            self.update_textBrowser(self.Dialog_textBrowser,time.strftime('%Y-%m-%d %H:%M:%S') + ':数据分析完成')

        elif len(self.choosed_function)==1 and len(self.loaddata_csvfile_ls)>0 and self.choosed_function[0]=='Distraction':
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':DMS分心检测 结果分析中...')
            res_dist = []
            res_run_analysis = run_analysis.analyze_Distraction()
            header_line = [' ', 'TP', 'FN', 'FP', 'TN', 'P', 'N', 'Sum', 'TPR', 'FPR', 'PRE']
            res_ori_line = res_run_analysis
            res_dist.append(header_line)
            res_dist.append(res_ori_line)
            self.display_result_csv(res_dist, 'distraction')
            self.update_textBrowser(self.Dialog_textBrowser,time.strftime('%Y-%m-%d %H:%M:%S') + ':数据分析完成')

        elif len(self.choosed_function)==1 and len(self.loaddata_csvfile_ls)>0 and self.choosed_function[0]=='Drowsiness':
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':DMS疲劳检测 结果分析中...')
            res_drow = []
            res_run_analysis = run_analysis.analyze_Drowsiness()
            header_line = [' ', 'TP', 'FN', 'FP', 'TN', 'P', 'N', 'Sum', 'TPR', 'FPR', 'PRE']
            res_ori_line = res_run_analysis[0]
            res_wgh_line = res_run_analysis[1]
            res_drow.append(header_line)
            res_drow.append(res_ori_line)
            res_drow.append(res_wgh_line)
            self.display_result_csv(res_drow, 'drowsiness')
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':数据分析完成')

        elif len(self.choosed_function)==1 and len(self.loaddata_csvfile_ls)>0 and self.choosed_function[0]=='GAZEAOI':
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':功能开发中...')
            run_analysis.analyze_GAZEAOI()

        elif len(self.choosed_function)==1 and len(self.loaddata_csvfile_ls)>0 and self.choosed_function[0]=='OMS Action':
            self.update_textBrowser(self.Dialog_textBrowser,
                                    time.strftime('%Y-%m-%d %H:%M:%S') + ':OMS Action 结果分析中...')
            res_oms_action = []
            res_run_analysis = run_analysis.analyze_OMS_Action()
            header_line = [' ', 'TP', 'FN', 'FP', 'TN', 'P', 'N', 'Sum', 'TPR', 'FPR', 'PRE']
            res_sm_all_line = res_run_analysis[0][0]
            res_sm_wgh_line = res_run_analysis[0][1]
            res_ca_all_line = res_run_analysis[1][0]
            res_ca_wgh_line = res_run_analysis[1][1]
            res_oms_action.append(header_line)
            res_oms_action.append(res_sm_all_line)
            res_oms_action.append(res_sm_wgh_line)
            res_oms_action.append(res_ca_all_line)
            res_oms_action.append(res_ca_wgh_line)
            self.display_result_csv(res_oms_action, 'oms action')
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':数据分析完成')

        elif len(self.choosed_function)==1 and len(self.loaddata_csvfile_ls)>0 and self.choosed_function[0]=='Age':
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':OMS年龄检测 结果分析中...')
            res_age = []
            res_run_analysis = run_analysis.analyze_Age()
            header_line = [' ', 'right', 'wrong', 'invalid', 'Sum', 'PRE']
            res_line = res_run_analysis
            res_age.append(header_line)
            res_age.append(res_line)
            self.display_result_csv(res_age, 'age')
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':数据分析完成')

        elif len(self.choosed_function)==1 and len(self.loaddata_csvfile_ls)>0 and self.choosed_function[0]=='Gender':
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':OMS性别检测 结果分析中...')
            res_gender = []
            res_run_analysis = run_analysis.analyze_Gender()
            header_line = [' ', 'right', 'wrong', 'invalid', 'Sum', 'PRE']
            res_line = res_run_analysis
            res_gender.append(header_line)
            res_gender.append(res_line)
            self.display_result_csv(res_gender, 'gender')
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':数据分析完成')

        elif len(self.choosed_function)==1 and len(self.loaddata_csvfile_ls)>0 and self.choosed_function[0]=='Child':
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':DMS疲劳检测 结果分析中...')
            res_child = []
            res_run_analysis = run_analysis.analyze_Child()
            header_line = [' ', 'TP', 'FN', 'FP', 'TN', 'P', 'N', 'Sum', 'TPR', 'FPR', 'PRE']
            res_ori_line = res_run_analysis[0]
            res_wgh_line = res_run_analysis[1]
            res_child.append(header_line)
            res_child.append(res_ori_line)
            res_child.append(res_wgh_line)
            self.display_result_csv(res_child, 'child')
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':数据分析完成')

        elif len(self.choosed_function)==1 and len(self.loaddata_csvfile_ls)>0 and self.choosed_function[0]=='PA':
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':OMS乘客位置 结果分析中...')
            res_pa = []
            res_run_analysis = run_analysis.analyze_PA()
            header_line = [' ', 'right', 'wrong', 'invalid', 'Sum',  'PRE']
            res_line = res_run_analysis
            res_pa.append(header_line)
            res_pa.append(res_line)
            print(res_pa)
            self.display_result_csv(res_pa, 'position')
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':数据分析完成')

        elif len(self.choosed_function)==1 and len(self.loaddata_csvfile_ls)>0 and self.choosed_function[0]=='Emotion':
            self.update_textBrowser(self.Dialog_textBrowser,
                                    time.strftime('%Y-%m-%d %H:%M:%S') + ':OMS Emotion 结果分析中...')
            res_emotion = []
            res_run_analysis = run_analysis.analyze_Emotion()
            header_line = [' ', 'TP', 'FN', 'FP', 'TN', 'P', 'N', 'Sum', 'TPR', 'FPR', 'PRE']
            res_pos_line = res_run_analysis[0]
            res_calm_line = res_run_analysis[1]
            res_neg_line = res_run_analysis[2]
            res_emotion.append(header_line)
            res_emotion.append(res_pos_line)
            res_emotion.append(res_calm_line)
            res_emotion.append(res_neg_line)
            self.display_result_csv(res_emotion, 'emotion')
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':数据分析完成')

        elif len(self.choosed_function)==1 and len(self.loaddata_csvfile_ls)>0 and self.choosed_function[0]=='Safety Seat':
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':OMS安全座椅 结果分析中...')
            res_ss = []
            res_run_analysis = run_analysis.analyze_Safetyseat()
            header_line = [' ', 'TP', 'FN', 'FP', 'TN', 'P', 'N', 'Sum', 'TPR', 'FPR', 'PRE']
            res_ori_line = res_run_analysis[0]
            res_wgh_line = res_run_analysis[1]
            res_ss.append(header_line)
            res_ss.append(res_ori_line)
            res_ss.append(res_wgh_line)
            self.display_result_csv(res_ss, 'safety seat')
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':数据分析完成')

        elif len(self.choosed_function)==1 and len(self.loaddata_csvfile_ls)>0 and self.choosed_function[0]=='FACEID':
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':功能开发中...')
            run_analysis.analyze_Faceid()

        elif len(self.choosed_function)==1 and len(self.loaddata_csvfile_ls)>0 and self.choosed_function[0]=='Static':
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':Static Gesture 结果分析中...')
            # print(run_analysis.analyze_Ges())
            res_ges=[]
            res_run_analysis=run_analysis.analyze_Ges()
            header_line=[' ','TP','FN','FP','TN','P','N','Sum','TPR','FPR','PRE']
            res_ori_line = res_run_analysis[0]
            res_wgh_line = res_run_analysis[1]
            res_ges.append(header_line)
            res_ges.append(res_ori_line)
            res_ges.append(res_wgh_line)
            self.display_result_csv(res_ges,'static gesture')
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':数据分析完成')

        elif len(self.choosed_function)==1 and len(self.loaddata_csvfile_ls)>0 and self.choosed_function[0]=='Dynamic':
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':Dynamic Gesture 结果分析中...')
            # print(run_analysis.analyze_Ged())
            res_ged = []
            res_run_analysis = run_analysis.analyze_Ged()
            header_line = [' ', 'TP', 'FN', 'FP', 'TN', 'P', 'N', 'Sum', 'TPR', 'FPR', 'PRE']
            res_ori_line = res_run_analysis[0]
            res_wgh_line = res_run_analysis[1]
            res_ged.append(header_line)
            res_ged.append(res_ori_line)
            res_ged.append(res_wgh_line)
            self.display_result_csv(res_ged, 'dynamic gesture')
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':数据分析完成')

        else:
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':请选择单一功能')

    def display_loaddata_txt(self,file_path,text):
        self.tab_add=QWidget()
        self.addTab_textBrowser=QTextBrowser()
        self.addTab_textBrowser.setText(text)
        self.layout_add=QHBoxLayout()
        self.layout_add.addWidget(self.addTab_textBrowser)
        self.tab_add.setLayout(self.layout_add)
        self.tabWidget.addTab(self.tab_add,file_path.strip('.csv').split('/')[-1])
        tabCount=self.tabWidget.count()
        self.tabWidget.setCurrentIndex(tabCount-1)

    def display_loaddata_csv(self,file_path,csv_file):
        table_add=QTableWidget()
        n_row = len(csv_file)
        # print(n_row)
        n_col = len(csv_file[0].strip('\n').split(','))
        # print(n_col)
        table_add.setColumnCount(n_col)
        table_add.setRowCount(n_row)
        for i in range(n_row):
            for j in range(n_col):
                table_add.setItem(i, j, QTableWidgetItem(str(csv_file[i].split(',')[j])))
        self.tabWidget.addTab(table_add, file_path.strip('.csv').split('/')[-1])
        tabCount=self.tabWidget.count()
        self.tabWidget.setCurrentIndex(tabCount-1)

    def display_result_csv(self, result_list,function):
        table_add = QTableWidget()
        n_row = len(result_list)
        n_col = len(result_list[0])
        # print(result_list)
        table_add.setColumnCount(n_col)
        table_add.setRowCount(n_row)
        for i in range(n_row):
            for j in range(n_col):
                table_add.setItem(i, j, QTableWidgetItem(str(result_list[i][j])))
        self.tabWidget.addTab(table_add, 'result-'+function)
        tabCount = self.tabWidget.count()
        self.tabWidget.setCurrentIndex(tabCount - 1)


    def display_analysis_result(self,txt_lines):
        self.tab_add = QWidget()
        self.addTab_textBrowser = QTextBrowser()
        self.addTab_textBrowser.setText(txt_lines)
        self.layout_add = QHBoxLayout()
        self.layout_add.addWidget(self.addTab_textBrowser)
        self.tab_add.setLayout(self.layout_add)
        self.tabWidget.addTab(self.tab_add, 'result')
        tabCount = self.tabWidget.count()
        self.tabWidget.setCurrentIndex(tabCount - 1)



    def close_tab(self,index):
        self.tabWidget.removeTab(index)



    def MCU_Connection_Settings(self):
        dialog_window= MCU_Connection_settings_Window(self)
        dialog_window.show()


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

