
def take(num,lyst):
	rlist=[]
	if num>0 :
		for i in range(0,num) :
			rlist.append(lyst[i])
		return rlist		
	else :
		for i in range(len(lyst)+num,len(lyst)) :
			rlist.append(lyst[i])
		return rlist		

names=['Deep','Venky','Harsh','Srijan','Mama']


def drop(num,lyst):
	slist=[]
	if num>0 :
		for i in range(num,len(lyst)) :
			slist.append(lyst[i])
		return slist
	else :
		for i in range(0,len(lyst)+num) :
			slist.append(lyst[i])
		return slist

#taking first three names
somenames=take(3,names)
print(somenames)

#taking last three names
somenames=take(-3,names)
print(somenames)

#dropping first three names
names=drop(3,names)
print(names)

#dropping last three names
names=drop(-3,names)
print(names)


