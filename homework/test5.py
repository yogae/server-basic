import random
rps = ['rock', 'paper', 'scissors']

def ramdom_rps():
    num = random.randrange(0,3)
    return rps[num]

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
        rps = ramdom_rps()
        rps_array.append(rps)
    return rps_array
# print(ramdom_rps())

input_result = ramdom_rps_array(10)
random_computer_result = ramdom_rps_array(10)

for num in range(10):
    print('~~~~~~')
    print("input: " + input_result[num])
    print("ramdom: " + random_computer_result[num])
    print("result: " + str(format(rps_func(input_result[num], random_computer_result[num]))))

# 가위 바위 보 게임을 10번 이상 실행하고 이긴 횟수와 확률을 구하시오!







# try_count = 1000
# result_rps = ramdom_rps_array(try_count)
# input_rps = ramdom_rps_array(try_count)

def win_count_func(count):
    win_count = 0
    for num in range(count):
        result = rps_func(input_rps[num], result_rps[num])
        if result > 0: win_count = win_count + 1;
    return win_count;

def win_persent(win_count, count):
    return win_count / try_count

win = win_count_func(try_count)

print("win: {}".format(win))
print("percent: {}".format(win_persent(win, try_count)))