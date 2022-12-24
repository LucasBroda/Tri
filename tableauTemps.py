from math import *
import random
import time
l=[]
for i in range(100):
    l.append(random.randint(0,100))

def triABulles(x):
    start = time.perf_counter()
    permut = True
    iteration = 0
    while permut == True:
        permut = False
        iteration += 1
        for j in range(len(x)-1):
            if x[j+1] < x[j]:
                permut = True
                tmp = x[j]
                x[j] = x[j+1]
                x[j+1] = tmp
    end = time.perf_counter()
    print(end-start)
    return x
print(l)

def tri_insertion(x):
	for i in range(len(x)):
		val = x[i]    
		j = i 
		while j>0 and x[j-1] > val: 
			x[j] = x[j - 1]  
			j = j - 1 
		x[j] = val 
	return x


def tri_en_selection(x):
	for i in range (len(x)):
		start = time.perf_counter()
		mini = i
	
		for j in range (i+1,(len(x))):
			t1 = time.time()
			if x[mini]>x[j]:
				mini = j
		
		tmp = x[i]
		x[i] = x[mini]
		x[mini] = tmp
		end = time.perf_counter()
		print(end-start)
	
	return x 

