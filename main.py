import random
# Lists Exercise
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# How to pick a random name, using a random index based on the number of items in the list
# How to get the random name and the output "Name is going to buy the meal today!"
print(names)
print(random.choice(names), "will be paying the bill for the meal today =D !")
# Names = ["Lenovo", "MSI", "ASUS", "RAZER", "ACER"]