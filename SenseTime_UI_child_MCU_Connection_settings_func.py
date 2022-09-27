
from SenseTime_Cabin_Service_multithread import runSDK_thread
from SenseTime_UI_child_MCU_Connection_settings import Ui_Child_MCU_Connection_settings
# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *


import time



class MCU_Connection_settings_Window(QMainWindow,Ui_Child_MCU_Connection_settings):

    def __init__(self,parent=None):
        #继承(QMainWindow,Ui_MainWindow)父类的属性
        super(MCU_Connection_settings_Window,self).__init__(parent)
        #初始化界面组件
        self.setupUi(self)

        self.setWindowTitle('测试配置与运行')

        self.pushButton_connection_server.clicked.connect(self.ConnecttoHost)
        self.pushButton_connection_mcu.clicked.connect(self.ConnecttoMcu)
        self.pushButton_runtest.clicked.connect(self.runtest)
        self.toolButton_gt.clicked.connect(self.gt_choose)
        self.toolButton_sh.clicked.connect(self.sh_choose)
        self.toolButton_log.clicked.connect(self.log_choose)
        self.toolButton_video.clicked.connect(self.video_choose)
        self.radioButton_ftp_mcu.toggled.connect(lambda :self.lineEdit_port_mcu.setText('21'))
        self.radioButton_sftp_mcu.toggled.connect(lambda :self.lineEdit_port_mcu.setText('22'))



    def ConnecttoHost(self):
        IP_server = self.lineEdit_ip_server.text()
        port_server = self.lineEdit_port_server.text()
        usr_server = self.lineEdit_user_server.text()
        pwd_server = self.lineEdit_pwd_server.text()
        self.session_server=self.connect_SFTP(IP_server,port_server,usr_server,pwd_server)
        # print(self.session_server)
        # stdin, stdout, stderr=self.session_server.exec_command('ls')
        # print(stdout.read().decode('utf-8'))

    def ConnecttoMcu(self):
        self.IP_MCU = self.lineEdit_ip_mcu.text()
        self.port_MCU = int(self.lineEdit_port_mcu.text())
        self.usr_MCU = self.lineEdit_user_mcu.text()
        self.pwd_MCU = self.lineEdit_pwd_mcu.text()
        try:
            self.session_mcu_ftp=connector_ftp_ssh(ip=self.IP_MCU,usr=self.usr_MCU,pwd=self.pwd_MCU)
            self.update_textBrowser(self.textBrowser_MCU_connection,
                                time.strftime('%Y-%m-%d %H:%M:%S') + ': ' + '控制器ftp连接成功')
            self.update_textBrowser(self.textBrowser_MCU_connection,
                                time.strftime('%Y-%m-%d %H:%M:%S') + ': ' + '控制器ssh连接成功')
        except Exception as ex:
            self.update_textBrowser(self.textBrowser_MCU_connection,
                                    time.strftime('%Y-%m-%d %H:%M:%S') + ': ' + str(ex))




    def gt_choose(self):
        self.gt_csvpath = QFileDialog.getOpenFileNames(QMainWindow(), '请选择gt文件', './',
                                                                 "csv Files(*.csv)")
        self.gt_csvfile=open(self.gt_csvpath[0][0],'r')
        self.lineEdit_gt.setText(self.gt_csvpath[0][0])


    def sh_choose(self):
        self.sh_path = QFileDialog.getOpenFileNames(QMainWindow(), '请选择Sh文件', './',
                                                       "Sh Files(*.sh)")
        self.lineEdit_sh.setText(self.sh_path[0][0])

    def log_choose(self):
        self.log_path = QFileDialog.getExistingDirectory(QMainWindow(),'请选择log文件夹','./')
        self.lineEdit_log.setText(self.log_path)

    def video_choose(self):
        self.video_path = QFileDialog.getExistingDirectory(QMainWindow(), '请选择视频文件夹', './')
        self.lineEdit_video.setText(self.video_path)

    def runtest(self):
        if self.radioButton_local.isChecked() and self.radioButton_ftp_mcu.isChecked():
            self.checkBox_video.setChecked(False)
            self.checkBox_gt.setChecked(False)
            self.checkBox_sdk.setChecked(False)
            self.checkBox_log.setChecked(False)
            self.checkBox_sh.setChecked(False)
            # self.session_mcu_ssh.exec_command('ls')
            gt_csv_path = self.lineEdit_gt.text()
            if os.path.exists(gt_csv_path) and gt_csv_path!='':
                self.checkBox_gt.setChecked(True)
            if self.lineEdit_sdk.text()[-1]!='/':
                sdk_path = self.lineEdit_sdk.text()+'/'
            else:
                sdk_path=self.lineEdit_sdk.text()

            stdin,stdout,stderr=self.session_mcu_ftp.ssh.exec_command('cd '+sdk_path+'&& pwd')
            ret=stdout.read().decode().strip('\n')
            ret+='/'

            if ret==sdk_path:
                self.checkBox_sdk.setChecked(True)
            else:
                self.update_textBrowser(self.textBrowser_MCU_connection,
                                        time.strftime('%Y-%m-%d %H:%M:%S') + ': sdk路径不存在' )
                self.checkBox_sdk.setChecked(False)

            sh_path = self.lineEdit_sh.text()

            if os.path.exists(sh_path) and sh_path!='':
                self.checkBox_sh.setChecked(True)

            video_path = self.lineEdit_video.text().replace(os.sep,'\\')+'\\'
            if os.path.exists(self.lineEdit_video.text()) and self.lineEdit_video!='':
                self.checkBox_video.setChecked(True)

            log_path = self.lineEdit_log.text()+'\\'
            if os.path.exists(self.lineEdit_log.text()) and self.lineEdit_log!='':
                self.checkBox_log.setChecked(True)

            ip = self.IP_MCU
            usr = self.usr_MCU
            pwd = self.pwd_MCU
            if gt_csv_path=='' or sdk_path=='' or sh_path=='' or video_path=='' or log_path=='':
                self.update_textBrowser(self.textBrowser_MCU_connection,
                                        time.strftime('%Y-%m-%d %H:%M:%S') + ': ' + '测试配置路径不可为空')

            elif self.checkBox_sdk.isChecked() and self.checkBox_gt.isChecked() and self.checkBox_sh.isChecked() and \
                    self.checkBox_video.isChecked() and self.checkBox_log.isChecked():
                self.task_runsdk = runSDK_thread(gt_csv_path=gt_csv_path, sdk_path=sdk_path, sh_path=sh_path,
                                                 video_path=video_path,
                                                 log_path=log_path, ip=ip, usr=usr, pwd=pwd)
                self.task_runsdk.start()
                self.task_runsdk.signal_runSDK.connect(self.diaglog_runsdk)

        elif self.radioButton_server.isChecked():
            print('sftp')
        else:
            print('请选择数据源')

    def diaglog_runsdk(self,str):
        self.update_textBrowser(self.textBrowser_MCU_connection,
                                time.strftime('%Y-%m-%d %H:%M:%S') + ': ' + str)


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
