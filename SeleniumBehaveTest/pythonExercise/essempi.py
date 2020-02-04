import random
import pprint
# secretNumber = random.randint(1, 20)
# print("I am thinking of a number between 1 and 20.")
# print(secretNumber)
# for guessNumber in range(1, 7):
#     print("Take a guess")
#     guess = int(input())
#     if guess < secretNumber:
#         print("Your guess is too low")
#     elif guess > secretNumber:
#         print("'Your guess is too high")
#     else:
#         break
#     if guess == secretNumber:
#         print('Good job! You guessed my number in ' + str(int(guessNumber)) + ' guesses!')
#     else:
#             print("Nope")
# ----------------------------------------
# catName = []
# while True:
#     print("Enter name cat " + str(len(catName)+ 1)  + "(Or entter nothing)")
#     name = input()
#     if name == "":
#         break
#     catName.append(name)
# print('The cat name are:')
# for cat in catName:
#
#     print('  ' + cat)
# catName.sort(reverse=True)
# print(catName)
# # -------------------------------------------
# myPets = ['Zophie', 'Pooka', 'Fat-tail']
# print("Enter a pet name:")
# name = input()
# if name not in myPets:
#     print(name + " isn't in the list")
# else:
#     print("pet in the list " + name)
# .........................................
# birthday = {'Igor': '27 March ', 'Svitlana': '10 September'}
# print("insert your name")
# while True:
#     name = input()
#     if name == "":
#         break
#     if name in birthday:
#         print(birthday[name] + "is the birthday of" + name)
#     else:
#         print('I don-t know your birthday, please type your name')
#         newbirthday = input()
#         birthday[name] = newbirthday
#         print(birthday[name] + " is the birthday of" + name)
#     print(birthday)
#.....................................................
# color = {'colores': 'red', 'number': 88}

# for item, vel in color.items():
#     print('Key ' + item + ' Value is ' + str(vel))

# for item in color.keys():
#     print(item)

# for item in color.items():
#     print(item)
# print("I-m going to take " + str(color.get('number', 0)) + ' -s number')
#...........................................................................
# message = 'The setdefault() method is a nice shortcut to ensure that a key exists. Here is a short program that counts the number of occurrences of each letter in a string. Open the file editor window and enter the following code, '
# count = {}
# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] +1
# print(count)
# pprint.pprint(count)
# print(pprint.pformat(count))
# ......................................................
# allGuests = {'Alice': {'apples': 5, 'pretzels': 12}, 'Bob': {'ham sandwiches': 3, 'apples': 2}, 'Carol': {'cups': 3, 'apple pies': 1}}
# def totBrought(guests, it):
#     broughtItem = 0
#     for x, y in guests.items():
#         broughtItem = broughtItem + y.get(it, 0)
#     return broughtItem
# print('apples  ' + str(totBrought(allGuests, 'apples')))
#//////////////////////////////////////////////////////////////////////
