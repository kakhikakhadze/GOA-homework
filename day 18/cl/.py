# user1 = int(input("enter first num :"))
# user2 = int(input("enter second num :"))
# user3 = int(input("enter third num :"))

# if user1 == user2 == user3:
#     print("yvela tolia")
# elif user1 == user3:
#     print("esec tolia")
# elif user2 == user3:
#     print("isev tolia")
# elif user1 == user2:
#     print("tolia")
# else:
#     print("arcerti ar aris toli")


name = input("enter your name :")

if name == "admin":
    password = input("გთხოვთ, შეიყვანეთ ადმინის პაროლი: ")
    if password == "adminpassword123":
        print("სალამი ადმინ")
    else:
        print("წვდომა არ გაქვს")
else:
    print("სალამი მომხმარებელო")









