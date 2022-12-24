#!/usr/bin/env python
import random
import time 

Liste = []
#First, we define the attribute Liste"


for i in range (10):
	entier_aleatoire = random.randint(1,10)
	Liste.append(entier_aleatoire)
	#Here, we are doing a loop with values who are not higher than 10, and 10 times in a row
	#we will put a random value between 1 and 10 in the attribute "Liste"
	
def tri_en_selection(x):
	for i in range (len(x)):
		start = time.perf_counter()
		mini = i
		#First, we want to know the minimal value
	
		for j in range (i+1,(len(x))):
			t1 = time.time()
			if x[mini]>x[j]:
				mini = j
		
		tmp = x[i]
		x[i] = x[mini]
		x[mini] = tmp
		end = time.perf_counter()
		print(end-start)
		#So here, we are doing a comparison between all the elements of the attribute "Liste"
		#we are just changing the position of the elements depending on their values
		#(if the value of one element is the smallest of the higher one)
	
	
print(Liste)

	
