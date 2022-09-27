from PyQt5.QtCore import QThread,pyqtSignal
from SenseTime_Cabin_Service_func_protocol import *
from SenseTime_Cabin_Service_func_log_analysis import *

class runSDK_thread(QThread):
    #  通过类成员对象定义信号对象
    signal_runSDK = pyqtSignal(str)

    def __init__(self, gt_csv_path,sdk_path,sh_path,video_path,log_path,ip,usr,pwd):

        ## 初始化函数
        super(runSDK_thread, self).__init__()
        self.gt_csv_path=gt_csv_path
        self.sdk_path=sdk_path
        # self.command_line=command_line
        self.sh_path=sh_path
        self.video_path=video_path
        self.log_path=log_path
        self.ip=ip
        self.usr=usr
        self.pwd=pwd

    def run(self):
        self.connector_mcu = connector_ftp_ssh(ip=self.ip, usr=self.usr, pwd=self.pwd)
        file_handler_sh=open(self.sh_path,'rb')
        self.connector_mcu.ftp.push_file(self.sdk_path+'runtest.sh',file_handler_sh)
        file_handler_sh.close()
        with open(self.gt_csv_path,'r') as csv_path:
            gt_lines=csv_path.readlines()
            count=0
            for line in gt_lines:
            # print(line)
                if '\xef\xbb\xbf' in line:
                    line = line.replace('\xef\xbb\xbf', '')
                raw_log = self.log_path.replace(os.sep,'\\')+'\\'+line.strip('\n')+'.log'
                if os.path.exists(raw_log):
                    continue

                video_name=line.strip('\n').split(',')[0]
                if not os.path.exists(self.video_path+video_name):
                    continue
                try:
                    file_handler_video=open(self.video_path+video_name,'rb')
                    self.connector_mcu.ftp.push_file(self.sdk_path+'test.mp4',file_handler_video)
                    file_handler_video.close()
                    self.signal_runSDK.emit('推送视频->'+video_name+'完成')
                except Exception as ex:
                    self.signal_runSDK.emit(str(ex))
                try:
                    self.connector_mcu.run_command('sh '+self.sdk_path+'runtest.sh')
                except Exception as ex:
                    self.signal_runSDK.emit(str(ex))
                try:
                    with open(self.log_path+video_name+'.log','wb') as file_handler_log:
                        self.connector_mcu.ftp.pull_file(self.sdk_path+'result.log',file_handler_log.write)
                        file_handler_log.close()
                    count += 1
                    self.signal_runSDK.emit('第{}个视频测试完成'.format(count))
                    self.signal_runSDK.emit('*'*50)
                except Exception as ex:
                    self.signal_runSDK.emit(str(ex))
            self.signal_runSDK.emit('测试完成')


class loganalysis_thread(QThread):
    signal_loganalysis = pyqtSignal(str)
    def __init__(self, function,log_folder, gt_csv_path, result_csv_path, thread_num,keyword,other_keyword):
        ## 初始化函数
        super(loganalysis_thread, self).__init__()
        self.function=function
        self.log_folder=log_folder
        self.gt_csv_path=gt_csv_path
        self.result_csv_path=result_csv_path
        self.thread_num=thread_num
        self.keyword=keyword
        self.other_keyword=other_keyword

    def run(self):
        if self.function=='DMS Action' or self.function=='OMS Action':
            try:
                analyzelog=LogAnalyzer_action(
                    gt_csv_path=self.gt_csv_path,
                    log_folder=self.log_folder,
                    result_csv_path=self.result_csv_path,
                    action_keyword_list=self.keyword,
                    thread_num=2)
                analyzelog.analyze_log_all()
                self.signal_loganalysis.emit(':log分析完成')
            except Exception as ex:
                self.signal_loganalysis.emit(str(ex))

        elif self.function=='Static':
            try:
                analyzelog=LogAnalyzer_ges(
                    gt_csv_path=self.gt_csv_path,
                    log_folder=self.log_folder,
                    result_csv_path=self.result_csv_path,
                    gesture_sequence=self.keyword,
                    other_gesture_keyword=self.other_keyword,
                    thread_num=2)
                analyzelog.analyze_log_all()
                self.signal_loganalysis.emit(':log分析完成')
            except Exception as ex:
                self.signal_loganalysis.emit(str(ex))

        elif self.function == 'Dynamic':
            try:
                analyzelog = LogAnalyzer_ged(
                    gt_csv_path=self.gt_csv_path,
                    log_folder=self.log_folder,
                    result_csv_path=self.result_csv_path,
                    gesture_sequence=self.keyword,
                    other_gesture_keyword=self.other_keyword,
                    thread_num=2)
                analyzelog.analyze_log_all()
                self.signal_loganalysis.emit(':log分析完成')
            except Exception as ex:
                self.signal_loganalysis.emit(str(ex))

        elif self.function == 'Emotion':
            try:
                analyzelog = LogAnalyzer_emotion(
                    gt_csv_path=self.gt_csv_path,
                    log_folder=self.log_folder,
                    result_csv_path=self.result_csv_path,
                    emotion_keyword_list=self.keyword,
                    thread_num=2)
                analyzelog.analyze_log_all()
                self.signal_loganalysis.emit(':log分析完成')
            except Exception as ex:
                self.signal_loganalysis.emit(str(ex))

        elif self.function == 'Distraction':
            try:
                analyzelog = LogAnalyzer_distraction(
                    gt_csv_path=self.gt_csv_path,
                    log_folder=self.log_folder,
                    result_csv_path=self.result_csv_path,
                    dist_keyword_list=self.keyword,
                    thread_num=2)
                analyzelog.analyze_log_all()
                self.signal_loganalysis.emit(':log分析完成')
            except Exception as ex:
                self.signal_loganalysis.emit(str(ex))

        elif self.function == 'Drowsiness':
            try:
                analyzelog = LogAnalyzer_drowsiness(
                    gt_csv_path=self.gt_csv_path,
                    log_folder=self.log_folder,
                    result_csv_path=self.result_csv_path,
                    drow_keyword_list=self.keyword,
                    thread_num=2)
                analyzelog.analyze_log_all()
                self.signal_loganalysis.emit(':log分析完成')
            except Exception as ex:
                self.signal_loganalysis.emit(str(ex))

        elif self.function == 'Child':
            try:
                analyzelog = LogAnalyzer_drowsiness(
                    gt_csv_path=self.gt_csv_path,
                    log_folder=self.log_folder,
                    result_csv_path=self.result_csv_path,
                    child_keyword_dic=self.keyword,
                    thread_num=2)
                analyzelog.analyze_log_all()
                self.signal_loganalysis.emit(':log分析完成')
            except Exception as ex:
                self.signal_loganalysis.emit(str(ex))
