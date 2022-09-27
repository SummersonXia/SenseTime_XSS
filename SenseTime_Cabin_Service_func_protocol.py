
import os
import time
import paramiko
from ftplib import FTP
import ftplib



class ftp_client():
    def __init__(self,ip,usr,pwd):
        self.ip=ip
        self.usr=usr
        self.pwd=pwd
        self.connect_FTP()


    def connect_FTP(self):
        self.ftp = FTP(
            host=self.ip,
            user=self.usr,
            passwd=self.pwd
        )
        self.ftp.login()


    def push_file(self, mcu_video_path,file_handler_video):

        self.ftp.storbinary('STOR ' + mcu_video_path, file_handler_video)



    def pull_file(self, mcu_log_path,file_handler_log):
        self.ftp.retrbinary('RETR ' + mcu_log_path, file_handler_log)


class connector_ftp_ssh():
    def __init__(self,ip,usr,pwd):
        self.ip=ip
        self.usr=usr
        self.pwd=pwd

        self.ftp=ftp_client(ip=self.ip,usr=self.usr,pwd=self.pwd)
        self.ssh=self.connect_SSH(ip=self.ip,usr=self.usr,pwd=self.pwd)

    def connect_SSH(self, ip, usr, pwd):

        print(ip, usr, pwd)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.load_system_host_keys()
        ssh.connect(hostname=ip, username=usr, password=pwd, port=22)
        return ssh

    def run_command(self,command):
        stdin, stdout, stderr = self.ssh.exec_command(command)
        return stdout.readlines()


    def run(self,remote_log_path,local_log_path):

        self.ftp.pull_file(remote_log_path,local_log_path)

