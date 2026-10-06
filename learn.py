# ############################# Print ##########################
# -------------------------------------------------------------

# print(yfguygugbhbjuhbujh) #False
# print("Hello") # "" or ''
# print(110) #Allow Math
# print("133") #Doesn't Allow Math
# print(110 + 133)
# print("110" + 133) #False

# -------------------------------------------------------------



# -------------------------------------------------------------

# "" or '' : Str -> رشته کلمات | امکان عملیات ریاضی
# 123 : Int : Special type just for number | Allow Calculation
# 123.561663 : Float : اعداد اعشاری
# TRUE or FALSE : Boolean 

# -------------------------------------------------------------



# -------------------------------------------------------------

# print(type("Hello")) # <class 'str'>
# print(type("110")) # <class 'str'>
# print(type(110)) # <class 'int'>
# print(type(123.0124561)) #<class 'float'>
# print(type(False)) #<class 'bool'>

# -------------------------------------------------------------


# -------------------------------------------------------------

# Print -------------------> | + | - | * | / | ^ |
#  Int and Float
# print(2.56515656165156 * 3) #7.69546968495468
# print("2.56515656165156" + "AAAAAAAAAAAA3") #2.56515656165156AAAAAAAAAAAA3 -> Stick

# -------------------------------------------------------------
# ############################# Print ##########################


# ############################# Variable ##########################
# -------------------------------------------------------------

# test = True
# print(type(test))
# x = 2313465132
# y = x + 156465415616
# print("This is : ",x + 21654656 + y,"| Type of test : ", type(test))

# -------------------------------------------------------------
# ############################# Variable ##########################

# -------------------------

# جمع +
# تفریق -
# ضرب *
# توان  **
# تقسیم /
# (تقسیم کف)تقسیم براکتی  //
# باقیمانده %
# [2.5] = 2 | [-2.3] = -3

# -------------------------

# اولویت های ریاضی

# 1 : () LTR
# 2 : ** RLT
# 3 : * and / and // LRT
# 4 : + and - LRT

# -------------------------

# print((2+3)**2)
# print(2 + 3 ** 2)

# -------------------------

# print(2 + 3 * 2)
# print(2 + (3 * 2))
# same

# -------------------------

# Until Page 20-50

# -------------------------

# print(2 + 3 - 2)
# print(3 + 2 - 2)

# -------------------------

# int + int = int
# float + int = float
# float + float = float

# -------------------------

# print("Hello \nMy name is Amir")
# Hello 
# My name is Amir

# -------------------------

# print("Hello \t I am Amir")
# Hello 	 I am Amir

# -------------------------

# print("Hello \\ I am Amir")
# Hello \ I am Amir

# -------------------------

# print("Hello \" I am Amir ")
# Hello " I am Amir 

# -------------------------

# print("Hello \' I am Amir ")
# Hello ' I am Amir 

# -------------------------

# print("Hello \
# Amir \
# Test")
# Hello Amir Test

# -------------------------

# print("This is :", 3+7**2)
# This is : 52

# -------------------------

# str : '' & "" & """


# print("Hi I am "Amir" ")
# SyntaxError: invalid syntax. Perhaps you forgot a comma?

# print("Hi I am 'Amir' ")
# Hi I am 'Amir' 

# print("Hi I am \"Amir\" ")
# Hi I am "Amir" 

# print(""" Hello "Test" """)
# Hello "Test"

# ------------------------- 


# ==========INPUT==========

# name = input("what's your name? ")
# print(name)
# print(type(name))
# what's your name? Amir
# Amir
# <class 'str'>

# =========================

# first_num = input("Enter your first number : ")
# second_num = input("Thanks, Now Enter your second number : ")
# output = first_num + second_num
# print(type(first_num), type(second_num), type(output), output)

# Enter your first number : 8
# Thanks, Now Enter your second number : 3
# <class 'str'> <class 'str'> <class 'str'> 83

# =========================

# first_num = input("Enter your first number : ")
# second_num = input("Thanks, Now Enter your second number : ")
# output = int(first_num + second_num)
# print(type(first_num), type(second_num), type(output), output)

# Enter your first number : 5
# Thanks, Now Enter your second number : 69
# <class 'str'> <class 'str'> <class 'int'> 569

# =========================

# first_num = input("Enter your first number : ")
# second_num = input("Thanks, Now Enter your second number : ")
# output = int(first_num) + int(second_num)
# print(type(first_num), type(second_num), type(output), output)

# Enter your first number : 5
# Thanks, Now Enter your second number : 1
# <class 'str'> <class 'str'> <class 'int'> 6

# =========================

# first_num = input("Enter your first number : ")
# second_num = input("Thanks, Now Enter your second number : ")
# output = float(first_num) + float(second_num)
# print(type(first_num), type(second_num), type(output), output)

# Enter your first number : 8
# Thanks, Now Enter your second number : 3
# <class 'str'> <class 'str'> <class 'float'> 11.0

# =========================

# num = float(input("Enter your number : "))
# print(int(num))

# Enter your number : 8.65146514651
# 8

# =========================
# 7 > 4 True
# 7 < 4 False

# True = 1
# print(True)
# SyntaxError: cannot assign to True

# x > y : x بزرگتر از y
# X < y : x  کوچکتر از y
# x >= y : x بزرگتر یا مساوی y
# x <= y : x کوچکتر یا مساوی y
# * چهار مورد بالا تقدم برابر دارند *

# x == y : x برابر است با y
# x != y : x مخالف y
#  ! در این دو مورد نیز تقدم باهم برابر است ولی از چهار مورد بالا سطح کمتری دارند !

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #

# print('Enter 2 int, and I will tell you',
# 'teh relationship they satisfy')

# # * Read Number 1 *
# number1 = int(input('Enter Your First Number : '))

# * Read Number 2 *
# number2 = int(input('Enter Your Second Number : '))

# if number1 == number2:
#     print(number1, "is equal to", number2)
    
# if number1 != number2:
#     print(number1, "is not equal to", number2)
    
# if number1 < number2:
#     print(number1, "is less than", number2)
    
# if number1 > number2:
#     print(number1, "is greater than", number2)
    
# if number1 <= number2:
#     print(number1, "is less than or equal", number2)
    
# if number1 >= number2:
#     print(number1, "is greater than or equal" , number2)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #

# a = 3
# b = 5
# c = 7
# if a != b or b > c :
#     print("True")

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #

# ???????????????????????????????????????????????? #

# اولویت های ریاضی

# 1 : () LTR
# 2 : ** RLT
# 3 : * and / and // LRT
# 4 : + and - LRT
# 5 : <= and < and >= and > LTR
# 6 : != and == LTR
# 7 : = RTL

# ???????????????????????????????????????????????? #

# ************************************************ #

""" Find th minimum of 3 values """

# number1 = int(input("Enter Your First NUmber : ")) 
# number2 = int(input("Enter Your Second NUmber : ")) 
# number3 = int(input("Enter Your Third NUmber : ")) 

# minimum = number1

# if number2 < minimum :
#     minimum = number2
    
# if number3 < minimum :
#     minimum = number3
    
# print('Minimum Value Is', minimum)

# ************************************************ #

""" Find th minimum of 3 values """

# number1 = int(input("Enter Your First NUmber : ")) 
# number2 = int(input("Enter Your Second NUmber : ")) 
# number3 = int(input("Enter Your Third NUmber : ")) 

# print('Minimum Value Is', min(number1,number2,number3))

# ************************************************ #

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #

# grade = 40

# if grade >= 60 :
#     print("Passed")
    
# if grade < 60 :
#     print("Failed")
    
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #

# grade = 80

# if grade >= 60 :
#     print("Passed")
    
# else :
#     print("Failed")

# ------------------------------------------------ #

# grade = 80
# result = ('Passed!' if grade >= 60 else 'Failed')
# print(result)
        
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #

# grade = float(input("Enter Your Grade : "))

# if grade >= 90:
#     print("A")
    
# elif grade >= 80:
#     print("B")
    
# elif grade >= 70:
#     print("C")
    
# elif grade >= 60:
#     print("D")
    
# else:
#     print("Failed")

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #

# product = 51

# while product <= 50:
#     product = product * 3
    
# print(product)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #

# for char in "Program":
#     print(char, end='  ')
    
# P  r  o  g  r  a  m  

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #

# print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", end=',')
# print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", end='#####')
# print("ccccccccccccccccccccccccccccccccccc")

# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa,bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb#####ccccccccccccccccccccccccccccccccccc

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #

# print(10, 20, 30, sep=" $ ")

# 10 $ 20 $ 30

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #

# total = 0

# for num in [2, 5, 8, 0]:
#     total = total + num
    
# print(total)


# total = 0

# for num in [2, 5, 8, 0]:
#     total += num
    
# print(total)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #

# for counter in range(11):
#     print(counter, end="    ")
    
# 0    1    2    3    4    5    6    7    8    9    10    
    
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #

# TODO #############################################

# c = c + 7 >>>>>>>>>>> c += 7
# d = d - 4 >>>>>>>>>>> d -= 4
# e = e * 5 >>>>>>>>>>> e *= 5
# f = f ** 3 >>>>>>>>>> f **= 3
# g = g / 2 >>>>>>>>>>> g /= 2
# g = g // 2 >>>>>>>>>> g //= 2
# h = h % 9 >>>>>>>>>>> h %= 9

# TODO #############################################
