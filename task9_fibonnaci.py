# initialise variables n, a and b and create an empty list fib_list

n= 50
a= 0
b= 1
fib_list= []

#iterate i to find out c 
#reassign variable a and b
#append value of c to the list
for i in range(0,51):
    fib = lambda c: a+b
    a=b
    b=fib
    fib_list.append(fib)

#print list
print(fib_list)