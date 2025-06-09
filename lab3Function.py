from itertools import permutations
import random


def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return None, None


chickens, rabbits = solve(35, 94)
if chickens is not None:
    print(f"Chickens: {chickens}, Rabbits: {rabbits}")
else:
    print("No solution found.")


def converter(Farh):
    result = (Farh-32)*(5/9)
    print(result)


number = float(input("please insert your desired number? "))
converter(number)


def converter(numbeer):
    result = number/28.3494
    print(result)


number = float(input("please insert a number? "))
converter(number)

name = input("Hello, what is your name? ")
number = random.randint(1, 20)
print(f"well {name} Im thinking a name between 1 and 20 \n Take a guess")

counter = 0
numberPlayer = -1
while numberPlayer != number:
    numberPlayer = int(input("Your guess: "))

    if numberPlayer == number:
        print('You Win')
    elif abs(numberPlayer - number) <= 5:
        print('You are so close')
    else:
        print('Not close')
    counter += 1


my_list = []
num = int(input("write a number? "))

for i in range(num):
    num2 = int(input("insert another number? "))
    my_list.append(num2)

for i in range(len(my_list)):
    print(my_list[i]*"*")


# Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):


def List():
    n = int(input("Please input how many numbers you want to enter: "))
    numbers = []
    for i in range(n):
        num = int(input(f"Please input number {i+1}: "))
        numbers.append(num)
    for i in range(len(numbers)):
        if numbers[i] == 0 and numbers[i+1] == 0 and numbers[i+2] == 7:
            print("found")
            break


List()


def List():
    n = int(input("Please input how many numbers you want to enter: "))
    numbers = []
    for i in range(n):
        num = int(input(f"Please input number {i+1}: "))
        numbers.append(num)
    for i in range(len(numbers)):
        if numbers[i] == 3 and numbers[i+1] == 3:
            print("found")
            break


List()


name = input("write a string? ")
reversed_string = name[::-1]
if name == reversed_string:
    print("YES")
else:
    print("NO")


def recursive():
    name = input("please insert a string? ")
    perm_set = set(permutations(name))
    print(f"\n permuation of '{name}': ")
    for p in sorted(perm_set):
        print(''.join(p))


recursive()


def is_prime(number):
    check = False

    for i in range(2, number-1):
        if number % i == 0:
            check = True
            break

        if check == False:
            print(number)


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

for i in list:
    is_prime(i)


def Sentence():
    sentence = input("Enter a sentence")
    words = sentence.split()
    reversed_sentence = ' ' .join(words[::-1])
    return reversed_sentence


print(Sentence())


def uniq(my_new):
    my_new = []
    for item in my_list:
        if item not in my_new:
            my_new.append(item)
    print(my_new)


num = int(input('Please insert a number'))
my_list = []

for i in range(num):
    num2 = int(input("please insert your numbers? "))
    my_list.append(num2)

uniq(my_list)
