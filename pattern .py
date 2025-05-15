#right angle triangle

#step 1:Take input
print("Half pyramid patternof stars(*):")
n=int(input("enter number of rows: "))

#step 2:outer loop to handle the rows
for i in range(n):
    #step 3:inner loop to handle number of columns
    for j in range(i+1):
        #Step 4:display result
        print("* ",end="")
    print()


#FLOYDS TRIANGLE


#take input
rows=int(input("please enter the total number of rows: "))
number=1  #initialise by 1

print("Floyds triangle")
#outer loop for rows
for i in range(1,rows+1):
    #inner loop for columns
    for j in range(1,i+1):
        #display result
        print(number,end=" ")
        number=number+1
    print()

#DIAMOND PATTERN

#upper part
#take input
rowsize=int(input("enter the number of rows you want: "))
if rowsize%2==0:#conditions
    halfdiamrow =int(rowsize/2)
else:
    halfdiamrow=int(rowsize/2)+1
space =halfdiamrow-1

#loop for upper part
for i in range(1,halfdiamrow+1):#loop for rows
    for j in range (1,space+1):#loop for columns
        print(end=" ")
#loop for lower part
    space=space-1
    num=1
    for j in range (2*i-1):
        print(end=str(num))
    #incrementingnumber at each column
        num = num+1
    print()
space=1
#loop for lower part
for i in range(1,halfdiamrow):#loop for row
    for j in range(1,space+1): #loop for columns
        print(end=" ")
    space = space+1
    num=1
    for j in range(1,2*(halfdiamrow-i)):
        print(end=str(num))#Display result
        #incrementing number at each column
        num = num+1
    print()
