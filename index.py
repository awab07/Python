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

# cities=["Lahore", "karachi"]
# cities[0]="kalam"
# cities.append("malam jaba")
# cities.append("Kalam")
# cities.pop()
# cities.extend(["Sialkot","hyderbad"])
# cities2=["Sialkot","hyderbad"]
# cities.extend(cities2)
# print(cities)
# print(cities[0:5])
# print(cities[0]+ " " + cities[2])
# print(f"{cities[0]} {cities[2]}")
# print(cities[0::2])
# print(cities[0:])

# cities=["Lahore", "karachi","Faislabad"]
# cities.insert(1,"Kalam")
# cities.insert(2,"Sawat")
# cities.insert(3,("LHR", "mianwali"))
# cities.clear()
# del cities
# del cities[0]
# cities.remove("Lahore")
# city= cities.index("karachi")
# print(cities, city)
# print(len(cities))


# # First Task
# print("This is First Task")
# cities=["jarawala","Lahore","Faislabad"]
# number=["1"]
# cities.extend(["Lahore","Islamabad"])
# del number
# print(cities)
# # print(number)

# # Second Task
# print("This is Second Task:")
# cities=["jarawala","Lahore","Faislabad"]
# print("Number of Length of List:",cities)
# print("Number of indexes :",len(cities)-1)

# # Third Task
# print("This is Third Task:")
# cities=[]
# cities.extend(["Lahore"])
# cities.append(int(2))
# cities.append(float(2.00))
# print("Used Different Data Types in List:",cities)

# # Fourth Task
# print("This is Forth Task:")
# cities=[-2,-1,0,1,2,3,4,5,6,7]
# print("Numebr of list from -ve range:",cities[-10:])

# tup=("atif", "Amjad","Ali")
# tup=("Ali",)
# print(tup,type(tup))

# tup=("Ali", "Ahmad", "Ali","Ajaz")
# print(len(tup))
# print(tup[0::2])
# tup2=("Faraz",)
# # tup +=tup2 #tuple joining (unfamilia Method)
# tup= tup + tup2  #(familia Method)
# print(tup)
# y =list(tup)
# y[-1]= "hani"
# print(y)
# tup= tuple(y)
# print("Tuple", tup)

# y.append("Ali")
# print(y)
# tup = tuple(y)
# print(tup)

# tup=(1,2,3,4,"Hello", True)
# # print(tup)
# # for i in tup:
# #     print(i, type(i))

# # for i,j in enumerate(tup,start=10):
# #     print(i,j)
# # del tup
# # print(tup)

# i=0 
# while i< len(tup):
#     print(tup[i])
#     i= i+1

# tup=("Lahore", "Faisalbad","Sialkot"," Islamabad","Hyderbad")
# user=input("Enter the city to detect :")
# print( "Yes Found" if[i for i in tup if i==user] else "not Found")

# tup=("Lahore", "Faisalbad","Sialkot","Islamabad","Hyderbad")
# user=input("Enter the city to detect :")

# print("Yes Found" if user in tup else "Not Found")

tup=("A+", "A","B","C")
english=int(input("Enter the Marks of English :"))
urdu=int(input("Enter the Marks of Urdu :"))
math=int(input("Enter the Marks of Math :"))
isl=int(input("Enter the Marks of Isl :"))
pak=int(input("Enter the Marks of Pak Studies :"))
computer=int(input("Enter the Marks of computer :"))


Total= float((english+urdu+math+isl+pak+computer)/600*(100))
print("Total marks % :", Total)


if Total >= 80:
    print("Passed With", tup[0])
elif Total >= 70:
    print("Passed With", tup[1])
elif Total >= 60:
    print("Passed With", tup[2])
elif Total >= 50:
    print("Passed With", tup[3])
else:
    print("Fail")
    



# print("Yes Found" if user in tup else "Not Found")