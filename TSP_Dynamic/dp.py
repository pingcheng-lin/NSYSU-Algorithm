import time #produce program's execution time
import matplotlib.pyplot as plt #draw picture
import numpy as np
import math
def initialize(): #初始化
    unused = []
    for i in range(city_num): 
        unused.append(1)
    unused.append(0)
    return unused

def distant(data, city_num): #calculate all fundamental distant
    two = np.zeros((city_num, city_num))
    for i in range(city_num):
        for j in range(city_num):
            two[i, j] = math.pow(math.pow(data[i][1] - data[j][1], 2) + math.pow(data[i][2] - data[j][2], 2), 0.5)
    return two

def get_data(): #read data from readfile.txt
    name = input("Input file name: ")
    input_file = open(name,"r")
    raw = input_file.read() #raw store unorganized data
    raw = list(raw.split()) 
    i = 0 #counter
    data = [] #data store organized data
    while i < len(raw)-2:
        temp = (raw[i], int(raw[i+1]), int(raw[i+2]))  #將城市名、x座標、y座標存入temp
        data.append(temp)
        i += 3
    input_file.close()
    return data

def move(sum, num):  #把特定位置num的compare改成1
    compare = []
    for i in range(sum):
        compare.append(0)
    compare[sum - num - 1] = 1
    return compare

def flip(suffer): # 1->0,0->1
    for i in range(len(suffer)):
        if suffer[i]:
            suffer[i] = 0
        else:
            suffer[i] = 1
    return suffer

def transfer(num, unused): #list binary transfer to decimal number
    total = 0
    for i in range(num+1):
        total += unused[i] * int(math.pow(2, num-i))
    return total   

def one_to_one(un, compare): # 比較unused與compare,兩者皆為1時,unused存1,其餘為0
    for i in range(city_num + 1):
        if un[i] == 1 and compare[i] == 1:
            un[i] = 1
        else:
            un[i] = 0
    return un

def cmp(a, b): #比較兩個list，當有1個參數一樣，return true
    for i in range (len(a)):
        if a[i] == 1 and b[i] == 1:
            return 1
    return 0

def dynamic(unused, origin): #dynamic programming 
    total = transfer(city_num, unused)
    if shortest[total][origin] != 0:
        return shortest[total][origin]
    compare = move(city_num + 1, city_num)
    if compare == unused: #判斷走完全部city
        return two_city[0][origin]
    smallest = 999999
    for i in range(city_num): #遞迴進入dynamic programming
        compare = move(city_num + 1, i)  #要移動的bit 
        if cmp(compare, unused):  #將所有可能都跑過
            current = two_city[i][origin] + dynamic(one_to_one(unused[:], flip(compare)), i) 
            if smallest > current:
                smallest = current
                route[total][origin] = i
    shortest[total][origin] = smallest
    return shortest[total][origin]
    
def draw(x,y): #畫成圖
    fig = plt.figure()
    for i in range(len(x)):
        plt.scatter(int(x[i]), int(y[i]), s = 10, c = 'c')
    for i in range(len(x)-1):
        plt.plot([x[i], x[i+1]], [y[i], y[i+1]], c = 'r')
    
    plt.plot([x[0], x[len(x)-1]], [y[0], y[len(y)-1]], c = 'r')
    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.title("City sequence")
    fig.savefig("city_result.png")
    
 
def result(tim, best_distance, best_order):
    output = open("output.txt", 'w')
    print("Best Order: ", file = output, end = "")
    for i in best_order:
        print(i[0], end = " ", file = output) #i[0]為城市名
    print("\nBest Distance:", best_distance, file = output)
    print("Execution Time (s):", tim, file = output)
    output.close()

time_start = time.time() #計時開始
data = get_data()

city_num = len(data) #city數量
unused = initialize()
two_city = distant(data, city_num)
route = np.zeros((int(math.pow(2, city_num+1)),city_num)) #儲存與init最佳距離的city
shortest = np.zeros((int(math.pow(2, city_num+1)),city_num)) #目前最短距離
best_distance = dynamic(unused, 0) #全部city走完的最佳距離

time_end = time.time() #計時終止

origin = 0 #原點
counter = 1 
unused = initialize() #初始化
best_order = [data[0]] #存到訪城市最佳順序
while counter <= city_num - 1: 
    total = transfer(city_num, unused)
    temp = int(route[total][origin])
    best_order.append(data[temp])
    origin = int(route[total][origin])
    compare = flip(move(city_num + 1, origin))
    unused = one_to_one(unused, compare)
    counter += 1

result(time_end - time_start, best_distance, best_order) #印出結果

x = []  
y = []
for i in best_order:
    x.append(i[1]) 
    y.append(i[2])
draw(x,y) 