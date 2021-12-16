import csv
import sys
import os
import shutil
import requests
import argparse
import traceback
import time
import re
import concurrent.futures
import sqlite3



parser = argparse.ArgumentParser()
parser.add_argument('--file',help='input file conintaning requests',required=True,type=str)
args = parser.parse_args()


def sendtoslack(msg):
	t_data={}
	t_data['text']=msg
	data=json.dumps(t_data)
	res=requests.post("https://<SLACK-URL>",data=data,headers={"content-type":"application/json"})
	print('Sending to Slack[ hackerXcreed ]')


  
  ########## Common Functions ####################
  
def writetofile(file,msg):
	filename=file
	msg=str(msg)
	try:
		with open(filename,'a') as fh:
			fh.write(msg)
	except Exception as e:
		print(e)

def readfile(file):
	words=[]
	try:
		with open(file,'r') as fh:
			for line in fh:
				if len(line)>3:
					words.append(line.rstrip())
			if len(words)>1:
				return words
			else:
				return []
	except Exception as e:
		print(e)

	
		
def removeIfExists(i_file):
	if os.path.exists(i_file):
		os.remove(i_file)


def current_en_time():
	ts=time.time()
	xtime=time.ctime(ts)
	x=xtime.split(' ')
	f=x[3]+'-'+x[1]+'-'+x[4]
	return f



def removedupes(mylist):
	return list(dict.fromkeys(mylist))




################## Executing Shell Command #############3
def amass(domain):
	print('[~] Amass '+domain)
	cmd='./tools/amass/amass enum --passive -d '+domain+' -o amass_s.txt'
	subprocess.getoutput(cmd)
	s=readfile('amass_s.txt')
	removeIfExists('amass_s.txt')
	if len(s)>3:
		return s
	else:
		return []
  
  
  
  
  ##################### Start Coding Here ##########################
  
  
 
