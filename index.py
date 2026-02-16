# num=2
# num2=3
# print(num + num2 )


# name="Awab"
# print(name)

# numfirst=3
# print(numfirst)

# n = "45 Nabeel"
# print(n,type(n))

# type casting

# number= input("enter your number: ")
# print(number,type(number))
# number=int(number)
# print(number,type(number))

# number= int(input("enter your number: "))
# print(number,type(number))

# number= float(input("enter your number: "))
# print(number,type(number))

# number=44
# if number=="44":
#     print("yes you are right")
# else:
#     print("enter wrong value")

# marks=99
# if marks==90:
#     print("yes you are passed")
# elif marks==99:
#     print("hurry ! you are passed in good number")
# else:
#     print("enter wrong value")



# edu = int(input("Enter your Education: "))
# hei = float(input("Enter your Height: "))
# aGe = int(input("Enter your Age: "))

# if edu == 12 and hei == 5.7 and aGe == 18:
#     print("Pass")
# else:
#     print("Fail")

# if aGe>17 and edu>11:
#     print("pass")
# elif edu>11 and hei>5.6 :
#     print("pass")
# elif aGe>17 and hei>5.6:
#     print("pass")
# else:
#     print("fail")

# if (aGe>17 and edu>11) or (edu>11 and hei>5.6) or (aGe>17 and hei>5.6):
#     print("pass")
# else:
#     print("fail")

# num=10
# match(num):
#     case 0:
#         print("none")
#     case 1:
#         print("Ok")
#     case _1:
#         print("hello")

# n = (input("Enter the Table you want to print: "))
# for n in range(2, 101, 2):   # even numbers from 2 to 100
#     if n * n > 100:
#         break
#     print(f"{n}*{n}={n*n}")


# number = int(input("Enter the table to be printed: "))
# for i in range(2, 21, 2):   # even numbers: 2, 4, 6, ..., 20
#     print(f"{number} x {i} = {number * i}")

# Primitive example 

# name1="Ali"
# name2=name1
# name2="Ahmad"
# print(name1,name2)

# name1=["Ali"]
# name2=name1
# name2[0]="Ahmad"
# print(name1,name2)


# names = ["namdeem","farz","ali","ahmad","saad","usman"]
# print(names)

# names = list("namdeem", "Faraz", "Saad")
# print(names)

# names = list(("Ali", "Ahmad","Usman"))
# print(names)

cities=["Lahore", "karachi"]
# cities[0]="kalam"
cities.append("malam jaba")
cities.append("Kalam")
cities.pop()
# cities.extend(["Sialkot","hyderbad"])
cities2=["Sialkot","hyderbad"]
cities.extend(cities2)
print(cities)
# print(cities[0:5])
# print(cities[0]+ " " + cities[2])
print(f"{cities[0]} {cities[2]}")
