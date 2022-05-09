# 2022 May 09 Monty Hall Problem by Python
# Version 0.1

print('Monty Hall Problem - Offline 6')
print('2022-May-09')

#모듈 import
import random as rd

# host, player 자료형 int 처리
host = 999
player = 999

# 선택할 문의 종류
doorNum = [0, 1, 2]

print('Stage Start!!\nPlay Time(starts from 1)\n')
#print(f'Before : host : {host} / player : {player}')

# Stage Two
def stageTwo(h2, p2):
	print('====== Stage Two ======')
	del doorNum[p2] 
	#플레이어가 선택한 것 제외
	p2 = rd.choice(doorNum) 
	#남은 것에서 선택
	if (h2 == p2):
		print(f'host : {host} / player : {player} => Same. Stage Two SUCESS!')
	elif (h2 != p2):
		print(f'host : {host} / player : {player} => FAILED')

# Stage One
def stageOne(h1, p1):
	print('====== Stage One ======')
	if(h1 == p1):
		print(f'host : {host} / player : {player} => Same. Stage One SUCESS!')
	elif(h1 != p1):
		print('Stage One Failed. Go to Stage Two')
		stageTwo(h1, p1)

# play times
for i in range(10):
	print(f'Play Time : {i+1}')
	host = rd.randrange(0,2)
	player = rd.randrange(0,2)
	stageOne(host, player)
	#host, player = 999, 999
	print()

print('Done')
