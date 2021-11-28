# -*- coding: utf-8 -*-
#@Author：Susy.huang
#@time :2021/7/19 10:34

import paramiko  #alt+enter

class SSH():
	def __init__(self, host, port, user, passwd):
		self.host = host
		self.port = port
		self.user = user
		self.passwd = passwd
		self.length = 0
		self.ssh = paramiko.SSHClient()
		self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		try:
			self.ssh.connect(self.host,self.port,self.user,self.passwd)
		except Exception as error:
			print ('Exception:', error)

	def Execmd(self,exe_cmd):
		stdin, stdout, stderr = self.ssh.exec_command(exe_cmd, get_pty = True)
		return stdout.read()
