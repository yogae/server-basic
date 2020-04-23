import json
# # 복합문제

test = [
    {
        "name": "younghyun",
        "score": [32, 43, 60, 32],
        "num": 0
    },
    {
        "name": "jihyun",
        "score": [100, 90, 80, 100],
        "num": 1
    },
    {
        "name": "eunjae",
        "score": [43, 70, 70, 30],
        "num": 2
    }
]

# # 세사람의 각각의 평균값과 천체 평균값을 구하는 함수는 만드시오! 
# # 반환값 예시: 
# # {
# #   "totalAvg": 100,
# #   "eachAvg": [
# #       {
# #           "num": 0,
# #           "avg": 100
# #       },
# #       {
# #           "num": 1,
# #           "avg": 100
# #       },
# #       {
# #           "num": 2,
# #           "avg": 100
# #       }
# #    ]
# # }
# #

def avg_func(score_array):
    return sum(score_array) / len(score_array)

def make_test_func(test_array):
    each_array = []
    total_array = []
    for student in test_array:
        total_array.extend(student["score"])
        each_array.append({
            "num": student["num"],
            "avg": avg_func(student["score"])
        })
    return {
        "totalAvg": avg_func(total_array),
        "eachAvg": each_array
    }

print(json.dumps(make_test_func(test), indent=2))