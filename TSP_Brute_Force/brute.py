import time #this program's execution time is about 75s. a little long....
import itertools
import matplotlib.pyplot as plt
def distant(data): #calculate the distant
    total = 0
    i = -1
    while i < (len(data)-1):
        total += (((data[i][1] - data[i+1][1])**2 + (data[i][2] - data[i+1][2])**2))**0.5
        i += 1
    return total

def get_data(): #read data from readfile.txt
    name = input("Input file name: ")
    input_file = open(name,"r")
    raw = input_file.read() #raw store unorganized data
    raw = list(map(int, raw.split())) 
    i = 0
    data = [] #data store organized data
    while i < len(raw)-2:
        temp = (raw[i], raw[i+1], raw[i+2])
        data.append(temp)
        i += 3
    input_file.close()
    return data[0], data[1:]

def try_all(origin, data, best_distance): #run all possibility
    for i in data:
        temp = distant([origin,] + list(i))
        if best_distance > temp:
            best_distance = temp 
            best_order = [origin,] + list(i)
    return best_distance, best_order

def draw(x,y):
    fig = plt.figure()
    for i in range(len(x)):
        plt.scatter(int(x[i]),int(y[i]),s = 10,c = 'c')
    for i in range(len(x)-1):
        plt.plot([x[i],x[i+1]],[y[i],y[i+1]],c = 'r')
    
    plt.plot([x[0],x[len(x)-1]],[y[0],y[len(y)-1]],c = 'r')
    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.title("City sequence")
    fig.savefig("city_result.png")
    
 
def result(tim, best_distance, best_order):
    output = open("output.txt", 'w')
    print("Best Order: ", file = output, end = "")
    for i in best_order:
        print(i[0], end = " ", file = output)
    print("\nBest Distance:", best_distance, file = output)
    print("Execution Time (s):", tim, file = output)
    output.close()

time_start = time.time()
origin, data = get_data()
all_data = itertools.permutations(data)
best_distance, best_order = try_all(origin, all_data, 999)
time_end = time.time()
result(time_end - time_start, best_distance, best_order)

x = []
y = []
for i in best_order:
    x.append(i[1])
    y.append(i[2])
draw(x,y)