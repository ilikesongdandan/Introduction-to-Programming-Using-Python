number=eval(input('please input a number between 1 and 15 : '))
count=0
for i in range(1,number+1):
	print ('   '*(number-i),end='')
	for l in range(i,1,-1):
		print (format(l,'<3d'),end='')
	for l in range(1,i):
		print (format(l,'<3d'),end='')
	print (i)