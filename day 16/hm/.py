# int(input("enter your age: "))
# if num > 0:
#     print("ეს რიცხვი დადებითი რიცხვია")
# elif num < 0:
#     print("ეს რიცხვი უარყოფითი რიცხვია")
# else:
#     print("ეს რიცხვი ნულია")

# age = int(input("შეიყვანეთ თქვენი ასაკი: "))
# if 0 <= age <= 12:
#     print("ბავშვი ხარ")
# elif 13 <= age <= 19:
#     print("მოზარდი/თინეიჯერი ხარ")
# elif 20 <= age <= 64:
#     print("ზრდასრული ხართ")
# elif 65 <= age <= 120:
#     print("ხანში შესული ხართ")
# elif age < 0:
#     print("არასწორი ინფო")
# else:
#     print("გურუ ან ჯადოქარი")

#      password guesser

# my_password = 4444
# attempts = 0
# while True:
#     user = int(input("guess my password :"))
#     attempts = attempts + 1 
#     if my_password == user:
#         print("correct")
#         break
#     elif user == "nah strong password :":
#         print("no more attepmts")
#         break
#     else:
#         print("no correct")
# print(("სულ ცდების რაოდენობა :", attempts))

# user_1 = int(input("first: "))
# user_2 = int(input("second: "))
# user_3 = int(input("third: "))
# if user_1 >= user_2 and user_1 >= user_3:
#     print("უდიდესი რიცხვია:", user_1)
# elif user_2 >= user_1 and user_2 >= user_3:
#     print("უდიდესი რიცხვია:", user_2)
# else:
#     print("უდიდესი რიცხვია: ",user_3)

user = (input("enter what day is it :"))
if user == 1:
    print("ორშაბათი")
elif user == 2:
    print("სამშაბათი")
elif user == 3:
    print("ოთხშაბათი")
elif user == 4:
    print("ხუთშაბათი")
elif user == 5:
    print("პარასკევი")
elif user == 6:
    print("შაბათი")
elif user == 7:
    print("კვირა")
else:
    print("i dont know")




    

