print("Question1")
def find_area(r):
    area=3.14*(r*r)
    return area
radius=float(input("Enter the value of radius"))
area_circle=find_area(radius)
print("Area of circle=%2f"%(area_circle))
print('*'*10)
print('\n')


print("Question2")
def perfect(n):
    sum=1
    i=2
    while i*i<=n:
        if n%i ==0:
            sum=sum+i+n/i
        i=i+1
    if(sum==n and n!=1):
        return True
    else:
        return False
print("Perfect Number")
n=2
for n in range(1000):
    if perfect(n):
        print(n,"is a perfect number")
print('*'*10)
print('\n')


print("Question3")
def timetable(n, times=1):
    if times <= 10:
        print(n, times, n*times)
        times=times+1
        timetable(n, times)
num=int(input("Enter Number"))
timetable(num)
print('*'*10)
print('\n')


print("Question4")
def power(base,pow1):
    if(pow1==1):
        return(base)
    if(pow1!=1):
        return(base*power(base,pow1-1))
base=int(input("Enter base: "))
pow1=int(input("Enter power value: "))
Result=power(base,pow1)
print(Result)
print('*'*10)
print('\n')


print("Question5")
def factorial(n):
    if(n <= 1):
        return 1
    else:
        return(n*factorial(n-1))
list1=[]
dict1={}
n = int(input("Enter number of elemets:"))
for i in range(n):
    num = int(input("Enter number:"))
    list1.append(num)
for j in list1:
    t=factorial(j)
    dict1[j]=t
print("Dictionary:")
for k,v in dict1.items():
    print(k,":",v)
