import requests
import time
import random
import json

with open("cookies.json",'r') as cookiesjson:
	cookies=json.load(cookiesjson)

with open("data/board.json",'r') as boardjson:
	board=json.load(boardjson)

cur=0

timeout=30

getheader={
        "refer":"https://www.luogu.org/paintBoard",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

def paint(x,y,col):
	global cur
	cur=(cur+1)%len(cookies)
	if cur==0:
		time.sleep(timeout)
	data={
		'x':x,
		'y':y,
		'color':col
	}
	headers={
                "refer":"https://www.luogu.org/paintBoard",
		"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
		"cookie":cookies[cur]
	}
	response = requests.post("https://www.luogu.org/paintBoard/paint",data=data,headers=headers)
	if response.json()['status']==200:
		print (cur,x,y,col)
		return 0
	return -1

getboard=requests.get("https://www.luogu.org/paintBoard/board",headers=getheader)

while True:
	r=random.randint(0,len(board)-1)
	x=board[r][0]
	y=board[r][1]
	col=board[r][2]
	if x*401+y<len(getboard.text) and int(getboard.text[x*401+y],32)!=col:
		while True:
			if cur==0:
				getboard=requests.get("https://www.luogu.org/paintBoard/board",headers=getheader)
			if paint(x,y,col)==0:
				break
