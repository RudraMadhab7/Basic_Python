'''num=int(input('enter the number'))
if num%2==0:
    print("given number is even")
else:
    print("given number is odd")'''
#add natural number using loop
'''num=0
sum=5
for i in range(num+1):
        sum+=i
        print(sum)'''
#Python program to print sum of N natural numbers
num=16
if num<0:
        print("enter the positive number")
else:
        sum=0
        while(num>0):
               sum=sum+num
               num=num-1
        print("the sum is",sum)