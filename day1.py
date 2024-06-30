#How will you remove last object from a list?
# list=[1,2,3,4,5]
# list.pop()
# print(list)


# 1) Swap 2 variable without using 3rd variable. (Give minimum three solutions)
# a= 27
# b= 12 
# print("a :-",a,"b :-",b)

# a,b=b,a
# print("a",a, "b",b)



# 3) Accept a number from the user - if it is divisible by 3 print “Three” , if it is divisible by 7 print “Seven” and
# if it is divisible by both 3 & 7, print “Three - Seven”.

# num=int(input("Enter a number  :-"))
# if num % 3 == 0 and num % 7 ==0 :
#     print("Three - seven")
# elif num % 3==0:
#     print("Three")
# elif num % 7 ==0:
#     print("seven")
# else:
#     print("number is not divisible bye three or seven ")



# 4)Accept a number from the user and check if it is odd or even number (Hint: use % operator).

# num=int(input("Enter a number  :- "))
# if num%2==0:
#     print("Number is even ")
# else:
#     print("Number is odd ")




# 5. Accept a number from the user check if it is odd or even number (Do not use % operator).
# num=int(input("Enter a number :- "))
# if (num & 1)== 0:
#     print("number is even ")
# else:
#     print("number id odd ")


# 6. Accept principal amount, rate of interest and years of investment then find the simple interest.
# principal_amt=int(input("Enter principal amt :-"))
# rate=int(input("Enter rate of interest  :-"))
# year=int(input("Enter year  :-"))

# def simple_intrest(principal_amt,rate,year):
#     print(((principal_amt*rate*year)/100))
    
# simple_intrest(principal_amt,rate,year)



# 8. Accept 10 numbers from the user and calculate their sum. (Do not use array).
# sum=0
# for i in range(1,11):
#     num=int(input(f"Enter {i} numbers"))
#     sum+=num
# print("Sum of 10 numbers :- ",sum)



# 9) Accept a number from the user and find the factorial of the number.
# def factorial(num):
#     fact=1
#     for i in range(1,num+1):
#         fact*=i
#     return fact

# fact=factorial(num=int(input("Enter a number :- ")))
# print(fact)



# 10. Accept 10 numbers from the user and count how many are positive, negative or zero.
# positive=0
# negative=0
# zero=0
# for i in range(10):
#     num=int(input("Enter numbers :-"))
#     if num ==0:
#         zero+=1
#     elif num > 0:
#         positive+=1
#     elif num < 0:
#         negative+=1
#     else:
#         print("please enter numeric value :-")

# print("Positive numbers :- ",positive,
#       "negative numbers :- ",negative,
#       "zeros :-",zero)




# 11. Accept a number from the user and calculate the sum of the digits of the number.
    
# num=int(input("Enter a number :-"))
# str_num=str(num)

# sum=0
# for i in range(len(str_num)+1):
#     sum+=int(i)
# print(sum)


# 12. Accept a number from the user and reverse it. Accept a number from the user and check if it is
# palindrome number or not.

# num=int(input("Enter a number :-"))

# num1=str(num)
# rev=num1[::-1]

# if num1 == rev:
#     print("Enter number is pallindrome")
# else:
#     print("Enter number is not palindrome")







# 13. Accept a number from the user and print a table for that number.
# num=int(input("Enter a number you want to print its table :-"))
# for i in range(1,11):
#     print(num,'X',i,num*i)




# 14. Accept a number from the user check if it is special number or not?
# Example: 145
# 1! =1
# 4!=1*2*3*4 5!=1*2*3*4*5
# Sum of the factorials is (1+24+120=145)

#ANS:-

# def factorial(int_num):
#     fact=1
#     for j in range(1,int_num+1):
#         fact*=j
#     return fact

# sum_of_fact=0
# num=int(input("Enter a number  :-"))
# str_num=str(num)
# for i in str_num:
#     int_num=int(i)
#     sum_of_fact+=factorial(int_num)

# if num == sum_of_fact:
#     print("Enter number is speecial ")
# else:
#     print("Enter number is not special")
# print(sum_of_fact)













# #decorators functoion 
# def decorator(fun):
#     def wrapper ():
#         print("Trasaction has been started ")
#         dnyaensh()
#         print("Trasaction ended ")
#     return wrapper


# def dnyaensh():
#     print("Hii Dnyanesh")

# decorator(dnyaensh)()



