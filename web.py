''' 
2048 vs AI Flask app

author: Sawyer
'''

from flask import Flask
from flask import render_template, redirect, request
from game2048 import *
import time

app = Flask(__name__)

users = 0
selfmodels = {}
selfcontrollers = {}
aimodels = {}
aicontrollers = {}
selfvsmodels = {}
selfvscontrollers = {}
aivsmodels = {}
aivscontrollers = {}
aivscounts = {}

max_count = {}

all_possible_tiles = []
for i in range(4):
	for j in range(4):
		all_possible_tiles.append(Tile(i+1, j+1, 2))


def reset_users():
	users = 0
	selfmodels = {}
	selfcontrollers = {}
	aimodels = {}
	aicontrollers = {}
	selfvsmodels = {}
	selfvscontrollers = {}
	aivsmodels = {}
	aivscontrollers = {}
	aivscounts = {}
	max_count = {}

def add_user():
	global users
	global selfmodels
	global selfcontrollers
	global selfcounts
	global aimodels
	global aicontrollers
	global aicounts
	global selfvsmodels
	global selfvscontrollers
	global selfvscounts
	global aivsmodels
	global aivscontrollers
	global aivscounts
	global max_count
	users+=1
	usernumber = users
	selfmodels[usernumber] = Model()
	selfcontrollers[usernumber] = Controller(selfmodels[usernumber])
	aimodels[usernumber] = Model()
	aicontrollers[usernumber] = AIcontroller(aimodels[usernumber])
	selfvsmodels[usernumber] = Model()
	selfvscontrollers[usernumber] = Controller(selfvsmodels[usernumber])
	aivsmodels[usernumber] = Model()
	aivscounts[usernumber] = 0
	aivscontrollers[usernumber] = AIcontroller(aivsmodels[usernumber])
	max_count[usernumber] = 1000

def get_time_interval(starttime):
	return time.time()-starttime

def get_time():
	return time.time()

@app.route('/', methods = ['POST', 'GET'])
def begin():
	add_user()
	return render_template('start.html', user=users)

@app.route('/ai/<user>', methods = ['POST', 'GET'])
def ai(user):
	global users
	user=int(user)
	if user > users:
		return redirect('/')
	user = int(user)
	global aimodels
	print max_count[user]
	return render_template('ai.html', aimodel=aimodels[user], time=time, user=user, all_possible_tiles=all_possible_tiles, max_time=max_count[user])

@app.route('/self/<user>', methods = ['POST', 'GET'])
def self(user):
	global users
	user=int(user)
	if user > users:
		return redirect('/')
	return render_template('self.html', model=selfmodels[user], user=user, all_possible_tiles=all_possible_tiles)

@app.route('/vs_ai/<user>/<timer>', methods = ['POST', 'GET'])
def vsai(user, timer):
	global users
	global max_count
	user=int(user)
	if user > users:
		return redirect('/')
	timer=int(timer)
	return render_template('vs_ai.html', model=selfvsmodels[user], aimodel=aivsmodels[user], user=user, time=timer, all_possible_tiles=all_possible_tiles, max_time = max_count[user])

@app.route('/self_human_move_up/<user>', methods = ['POST', 'GET'])
def up(user):
	#model update right
	global users
	user=int(user)
	if user > users:
		return redirect('/')
	selfcontrollers[user].move_up()
	return redirect('/self/'+str(user))

@app.route('/self_human_move_right/<user>', methods = ['POST', 'GET'])
def right(user):
	#model update right
	global users
	user=int(user)
	if user > users:
		return redirect('/')
	selfcontrollers[user].move_right()
	return redirect('/self/'+str(user))

@app.route('/self_human_move_left/<user>', methods = ['POST', 'GET'])
def left(user):
	#model update right
	global users
	user=int(user)
	if user > users:
		return redirect('/')
	selfcontrollers[user].move_left()
	return redirect('/self/'+str(user))

@app.route('/self_human_move_down/<user>', methods = ['POST', 'GET'])
def down(user):
	#model update right
	global users
	user=int(user)
	if user > users:
		return redirect('/')
	selfcontrollers[user].move_down()
	return redirect('/self/'+str(user))

@app.route('/vs_human_move_left/<user>/<timer>', methods = ['POST', 'GET'])
def vsleft(user, timer):
	#model update left
	global users
	global max_count
	user=int(user)
	if user > users:
		return redirect('/')
	selfvscontrollers[user].move_left()
	timer = int(timer)
	if timer>max_count[user]:
		aivscontrollers[user].move()
		timer = 0
	return redirect('/vs_ai/'+str(user)+'/'+str(timer))

@app.route('/vs_human_move_right/<user>/<timer>', methods = ['POST', 'GET'])
def vsright(user, timer):
	#model update left
	global users
	global max_count
	user=int(user)
	if user > users:
		return redirect('/')
	selfvscontrollers[user].move_right()
	timer = int(timer)
	if timer>max_count[user]:
		aivscontrollers[user].move()
		timer = 0
	return redirect('/vs_ai/'+str(user)+'/'+str(timer))

@app.route('/vs_human_move_down/<user>/<timer>', methods = ['POST', 'GET'])
def vsdown(user, timer):
	#model update left
	global users
	global max_count
	user=int(user)
	if user > users:
		return redirect('/')
	selfvscontrollers[user].move_down()
	timer = int(timer)
	if timer>max_count[user]:
		aivscontrollers[user].move()
		timer = 0
	return redirect('/vs_ai/'+str(user)+'/'+str(timer))

@app.route('/vs_human_move_up/<user>/<timer>', methods = ['POST', 'GET'])
def vsup(user, timer):
	#model update left
	global users
	global max_count
	user=int(user)
	if user > users:
		return redirect('/')
	selfvscontrollers[user].move_up()
	timer = int(timer)
	if timer>max_count[user]:
		aivscontrollers[user].move()
		timer = 0
	return redirect('/vs_ai/'+str(user)+'/'+str(timer))

@app.route('/ai_move/<user>', methods = ['POST', 'GET'])
def aimove(user):
	#aimodel update
	global aicontrollers
	global users
	global max_count
	user=int(user)
	if user > users:
		return redirect('/')
	aicontrollers[user].move()
	return redirect('/ai/'+str(user))

@app.route('/vs_ai_move/<user>/<timer>', methods = ['POST', 'GET'])
def vsaimove(user, timer):
	#aimodel update
	global aicontrollers
	global users
	global max_count
	user=int(user)
	if user > users:
		return redirect('/')
	aivscontrollers[user].move()
	return redirect('/vs_ai/'+str(user)+'/'+str(timer))
	
@app.route('/reset-ai/<user>', methods=['POST', 'GET'])
def reset_ai(user):
	global aimodels
	global aicontrollers
	user=int(user)
	aimodels[user] = Model()
	aicontrollers[user] = AIcontroller(aimodels[user])
	return redirect('/ai/'+str(user))
	
@app.route('/reset-self/<user>', methods=['POST', 'GET'])
def reset_self(user):
	global selfmodels
	global selfcontrollers
	user=int(user)
	selfmodels[user] = Model()
	selfcontrollers[user] = Controller(selfmodels[user])
	return redirect('/self/'+str(user))
	
@app.route('/reset-vs/<user>', methods=['POST', 'GET'])
def reset_aivs(user):
	global aivsmodels
	global aivscontrollers
	global selfvscontrollers
	global selfvsmodels
	user=int(user)
	aivsmodels[user] = Model()
	aivscontrollers[user] = AIcontroller(aivsmodels[user])
	selfvsmodels[user] = Model()
	selfvscontrollers[user] = Controller(selfvsmodels[user])
	return redirect('/vs_ai/'+str(user)+'/0')

@app.route('/ai-super-slow/<user>', methods=['POST', 'GET'])
def ai_super_slow(user):
	global max_count
	user = int(user)
	max_count[user] = 2000
	print max_count[user]
	return redirect('/ai/'+str(user))

@app.route('/ai-slow/<user>', methods=['POST', 'GET'])
def ai_slow(user):
	global max_count
	user = int(user)
	max_count[user] = 1250
	print max_count[user]
	return redirect('/ai/'+str(user))

@app.route('/ai-mid/<user>', methods=['POST', 'GET'])
def ai_mid(user):
	global max_count
	user = int(user)
	max_count[user] = 1000
	print max_count[user]
	return redirect('/ai/'+str(user))

@app.route('/ai-fast/<user>', methods=['POST', 'GET'])
def ai_fast(user):
	global max_count
	user = int(user)
	max_count[user] = 750
	print max_count[user]
	return redirect('/ai/'+str(user))

@app.route('/ai-super-fast/<user>', methods=['POST', 'GET'])
def ai_super_fast(user):
	global max_count
	user = int(user)
	max_count[user] = 250
	print max_count[user]
	return redirect('/ai/'+str(user))

@app.route('/vs-ai-super-slow/<user>', methods=['POST', 'GET'])
def vs_ai_super_slow(user):
	global max_count
	user = int(user)
	max_count[user] = 2000
	return redirect('/vs_ai/'+str(user)+'/0')

@app.route('/vs-ai-slow/<user>', methods=['POST', 'GET'])
def vs_ai_slow(user):
	global max_count
	user = int(user)
	max_count[user] = 1250
	return redirect('/vs_ai/'+str(user)+'/0')

@app.route('/vs-ai-mid/<user>', methods=['POST', 'GET'])
def vs_ai_mid(user):
	global max_count
	user = int(user)
	max_count[user] = 1000
	return redirect('/vs_ai/'+str(user)+'/0')

@app.route('/vs-ai-fast/<user>', methods=['POST', 'GET'])
def vs_ai_fast(user):
	global max_count
	user = int(user)
	max_count[user] = 750
	return redirect('/vs_ai/'+str(user)+'/0')

@app.route('/vs-ai-super-fast/<user>', methods=['POST', 'GET'])
def vs_ai_super_fast(user):
	global max_count
	user = int(user)
	max_count[user] = 250
	return redirect('/vs_ai/'+str(user)+'/0')

@app.route('/about/<user>', methods=['POST', 'GET'])
def about(user):
	return render_template('about.html', user=user)

if __name__ == '__main__':
	reset_users()
	app.run()