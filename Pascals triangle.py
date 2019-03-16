a=int(input("Enter number of rows: "))
	c=1
	for i in range(0,a):
	    for s in range(0,a-i):
	        print(" ",end="") 
	    for j in range(0,i+1):
	        if(j==0 or i==0):
	            c=1   
	        else:
	            c=c*(i-j+1)/j
	        print(int(c), end=" ")
	    print('\n')
