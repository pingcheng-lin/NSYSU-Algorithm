import time #produce program's execution time
import matplotlib.pyplot as plt #draw picture
import random
import math
import sys
def get_data(): #read data from readfile.txt
    name = input("Input file name: ")
    input_file = open(name,"r")
    raw = input_file.read() #raw store unorganized data
    raw = list(raw.split()) 
    i = 0 #counter
    data = [] #data store organized data
    while i < len(raw)-2:
        temp = (raw[i], float(raw[i+1]), float(raw[i+2]))  #將城市名、x座標、y座標存入temp
        data.append(temp)
        i += 3
    input_file.close()
    return data

def distant(data): #計算總路徑長
    total = 0
    for i in range(len(data)-1):
        total += math.pow(math.pow(data[i][1] - data[i+1][1], 2) + math.pow(data[i][2] - data[i+1][2], 2), 0.5)
    return total

def create_two_int():
    while 1:
        a_city = random.randint(1, len(data)-2)
        b_city = random.randint(1, len(data)-2)
        if a_city >= b_city:
            continue
        return a_city, b_city

def swap(data, distance, a_city, b_city):
    temp_data = data[:]
    temp_data[a_city], temp_data[b_city] = temp_data[b_city], temp_data[a_city]
    temp_distance = distant(temp_data)
    return temp_data, temp_distance

def sa(data):
    data.append(data[0]) #list前後皆原點
    distance = distant(data) #計算總長
    tempeture_current = 1000 #初始化溫度
    tempeture_end = 1e-5
    while tempeture_current > tempeture_end: #執行直到降到一定溫度
        a_city, b_city = create_two_int()
        temp_data, temp_distance = swap(data, distance, a_city, b_city) #嘗試更好的路徑
        diff = temp_distance - distance
        zero_to_one = random.uniform(0, sys.maxsize)/ (sys.maxsize+1)
        if diff < 0 or math.exp(-diff/tempeture_current) > zero_to_one: #看是否新路徑比較優 或 可以接受較差解
            distance = temp_distance
            data = temp_data
        tempeture_current *= 0.99999 #降溫
    data = data[0:-1]
    return distance, data
 
def result(tim, best_distance, best_order): #印出結果
    output = open("output.txt", 'w')
    print("Best Order: ", file = output, end = "")
    for i in best_order:
        print(i[0], end = " ", file = output) #i[0]為城市名
    print("\nBest Distance:", best_distance, file = output)
    print("Execution Time (s):", tim, file = output)
    output.close()

def draw(best_order): #畫圖
    x = []  
    y = []
    for i in best_order:
        x.append(i[1]) 
        y.append(i[2])
    fig = plt.figure()
    for i in range(len(x)):
        plt.scatter(int(x[i]), int(y[i]), s = 10, c = 'c')
    for i in range(len(x)-1):
        plt.plot([x[i], x[i+1]], [y[i], y[i+1]], c = 'r')
    plt.plot([x[0], x[len(x)-1]], [y[0], y[len(y)-1]], c = 'r')

    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.title("City sequence")
    fig.savefig("city result.png")

if __name__ == "__main__":
    time_start = time.time() #計時開始
    data = get_data() #讀入資料
    best_distance, best_order = sa(data) #執行sa
    draw(best_order) #畫圖
    time_end = time.time() #計時終止
    result(time_end - time_start, best_distance, best_order) #印出結果
