#conditions
#if-condition by using comparision operators
#<,>,<=,>=,!=,==
'''a=2
b=4
if a<b:
    print("true")

a=2
b=4
if a>b:
    print("false")

a=10
b=15
if a<=b:
    print("true")

a=8
b=3
if a>=b:
    print("greater")

a=2
b=4
if a!=b:
    print("true")

a=4
b=2
if a==b:
    print("false")

a=4
b=4
if a==b:
    print("true")

a=int(input("a value: "))
b=int(input("b value: "))
if a>b:
    print("greater")

a=int(input("a value: "))
if a>40:
    print("greater")

a=input("data: ")
if a=="python":
    print("correct")

a=input("name: ")
if a!="mahe":
    print("valid")'''

#if-condition by using logical operators
#and, or, not
'''a=5
b=9
if a<b and b>a:
    print("a is smaller than b")

a=7
b=11
if a<=b and b>=a:
    print("a is smaller than b")

a=5
b=6
if a!=b and b==a:
    print("equal")

a=20
b=30
if a<b or b>a:
    print("true")

a=50
b=60
if a<=b or b>=a:
    print("ture")

a=20
b=30
if a!=b or b==a:
    print("not equal")

a=4
b=8
if not a<b:
    print("true")

a=4
b=8
if not a>b:
    print("true")

a=int(input("enter a value: "))
b=int(input("enter b value: "))
if a<b or b>a:
    print("true")'''

#if-condition by using identify operators
#is, is not
'''a=7
if type(a) is int:
    print("a is integer")

a=7
if type(a) is not int:
    print("a is integer")

a="mahesh"
if type(a) is str:
    print(a)

a="mahesh"
if type(a) is not str:
    print(a)

a=5.2
if type(a) is float:
    print("a is float")

a=5.2
if type(a) is not float:
    print("a is float")

a=5+9j
if type(a) is complex:
    print("a is complex")

a=5+9j
if type(a) is not complex:
    print("a is complex")

a=True
if type(a) is bool:
    print("a is boolean")

a=True
if type(a) is not bool:
    print("a is boolean")

a= int(input("Enter the value: "))
if type(a) is int:
    print(a)

a= int(input("Enter the value: "))
if type(a) is not int:
    print(a)'''

#if-condition by using membership operators
#in, not in
'''a=[2,3,5,6]
if 3 in a:
    print("3 is in a")

a=[2,3,5,6]
if 3 not in a:
    print("3 is in a")

a=(2,3,5,6)
if 7 in a:
    print("7 is in a")

a=[10,20,30,40,50]
b=int(input("Enter the value: "))
if b in a:
    print("the value is: ",b)'''




