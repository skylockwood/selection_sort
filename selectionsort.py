import random
import time
arr=[]
for x in xrange(0,10000):
	rand = int(random.random()*10000)
	arr.append(rand)

print arr
start = time.time()
place = 0
count = 0
for x in xrange(0,len(arr)):
	min = arr[x]
	minnum = place
	for i in xrange(place,len(arr)):
		if arr[i]<min:
			min=arr[i]
			minnum = i
			count+=1
	temp = arr[place]
	arr[place]=min
	arr[minnum] = temp
	place+=1
print arr, count
print ("---%s seconds---" % (time.time()-start))