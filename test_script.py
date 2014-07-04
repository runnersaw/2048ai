''' 
2048 vs AI Flask app

author: Sawyer
'''

from flask import Flask
from flask import render_template, redirect, request
import time
from game2048 import *

app = Flask(__name__)

global aistarttime
global vsstarttimes
aistarttime = None
vsstarttime = None
print aistarttime
print time.time()

def get_time_interval(starttime):
	return time.time()-starttime

def get_time():
	return time.time()

def begin(starttime):
	if starttime == None:
		starttime = time.time()
	print get_time_interval(starttime)

if __name__ == '__main__':
	model = Model()
	print model.row_collapse_right_or_down([2,4,4,4])
