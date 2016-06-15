sentence="Hey deep nirmal How are yOu"
count=0 

for letter in sentence :
	if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u' :
		count=count+1

print("The num of vowels are :"+str(count))