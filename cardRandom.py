import random
names_string = input("give every buddies names,seperated by comma.")
names = names_string.split(",")
# split() used todivides a string into seperat list
num_items = len(names)
random_choice= random.randint(0,num_items-1)
person_who_pay = names[random_choice]
print(person_who_pay + " " +"is going to pay today")

