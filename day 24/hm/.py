# nums = [2, 4, 6, 8, 10, 12, 14]
# print(nums[-7] * nums[-1])
# print(nums[2])   
# print(nums[-3]) 

# fruits = ["apple", "banana", "cherry", "grape", "kiwi", "orange"]
# print(fruits[2])   
# print(fruits[-3])

# words = ["dog" ,"most" ,"is" ,"angry" ,"running"  , "forest", "fast", "in" , "cat" ,"human", "very"]
# sentence1 = words[-11] + " " + words[-9] + " " + words[-7] + " " + words[-4] + " " + words[-6] + " " + words[-1] + " " + words[-5]
# print(sentence1) 

# sentence2 = words[0] + " " + words[2] + " " + words[4] + " " + words[7] + " " + words[5] + " " + words[10] + " " + words[6]
# print(sentence2)

# sentence3 = words[8] + " " + words[2] + " " + words[10] + " " + words[3]
# print(sentence3)

# animals = ["dog", "cat", "horse", "cow", "sheep", "goat"]
# index = int(input("შეიყვანე ინდექსი: "))

# if animals[index] == "cat":
#     print("შენ აირჩიე კატა")
# elif animals[index] == "goat":
#     print("შენ აირჩიე თხა")
# else:
#     print("სხვა ცხოველი აირჩიე")

# cities = ["ბათუმი", "თბილისი", "გორი", "ქუთაისი", "ოზურგეთი", "ჩოხატაური"]
# a = int(input("პირველი ინდექსი: "))
# b = int(input("მეორე ინდექსი: "))
# if a < b:
#     print(cities[a], cities[b])
# elif b < a:
#     print(cities[b], cities[a])
# else:
#     print(cities[a])

# list = input("შეიყვანე სიტყვა: ")
# if list[0] == "a":
#     print("სიტყვა იწყება a-თი")
# elif list[-1] == "z":
#     print("სიტყვა მთავრდება z-ით")
# else:
#     print("სიტყვა არც a-თი იწყება და არც z-ით მთავრდება")

# list = input("შეიყვანე სიტყვა: ")
# if list[0] == list[-1]:
#     print("პირველი და ბოლო ერთნაირია")
# else:
#     print("პირველი და ბოლო განსხვავებულია")

# letters = "agivorsbgitr"
# word1 = letters[1] + letters[0] + letters[1] + letters[0]
# print(word1)
# word2 = letters[6] + letters[0] + letters[7] + letters[0]
# print(word2)
# word3 = letters[7] + letters[0] + letters[11] + letters[2] + letters[4] + letters[1] + letters[6]
# print(word3)

# text = "giorgi"
# for i in text:
#     print(i)

# text = "giorgi"
# i = 0
# while i < len(text):
#     print(text[i])
#     i = i + 1


# list = [3,4,5,6,7,1,2,9,8,11]

# user = int(input("enter your num :"))
# if user > 0 and user < 10:
#     print(list[user])
# elif user < 0 or user > 10:
#     print("you entered negative or more than 10  number")