import random
rps = ['rock', 'paper', 'scissors']

def ramdom_rps():
    return rps[random.randrange(0,3)]

def rps_func(in_rps, random_rps):
    if in_rps == random_rps: return 0
    else:
        if (random_rps == 'paper') & (in_rps == 'scissors'):
            return 1
        elif (random_rps == 'scissors') & (in_rps == 'rock'):
            return 1
        elif (random_rps == 'rock') & (in_rps == 'paper'):
            return 1
        else:
            return -1

def ramdom_rps_array(count):
    rps_array = []
    for num in range(count):
        rps_array.append(ramdom_rps())
    return rps_array

result_rps = ramdom_rps_array(3)
input_rps = ['rock', 'rock', 'paper']

for num in range(3):
    print("input: {}".format(input_rps[num]))
    print("ramdom: {}".format(result_rps[num]))
    print("result: {}".format(rps_func(input_rps[num], result_rps[num])))

# 가위 바위 보 게임을 10번 이상 실행하고 이긴 횟수와 평균을 구하시오!