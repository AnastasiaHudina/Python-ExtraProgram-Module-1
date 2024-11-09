import json


FILENAME = "input.json"

# TODO решите задачу
def task() -> float:
    list1=[]
    a=0
    with open(FILENAME) as f:
        json_data = json.load(f)
    score_values = [item1["score"] for item1 in json_data]
    weight_values = [item2["weight"] for item2 in json_data]
    for i in range(len(score_values)):
        list1.append(score_values[i]*weight_values[i])
    for g in range(len(list1)):
        a = a+list1[g]
    return round(a,3)
print(task())
