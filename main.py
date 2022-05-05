import random
# Lists Exercise
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# How to pick a random name, using a random index based on the number of items in the list
# How to get the random name and the output "Name is going to buy the meal today!"
#Solition 1
print(names)
num_items = len(names)
all_names = random.randint(0, num_items -1)
text_names = str(all_names)
print(text_names + "is going to pay for the meal today!")

#Solution 2
# print(names)
# print(random.choice(names), "will be paying the bill for the meal today =D !")
# Names = ["John", "David", "James", "Max", "Zebra"]