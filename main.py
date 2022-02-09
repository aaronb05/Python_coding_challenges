# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and setting

import random
import math
import os as system

# MULTIPLE CODING CHALLENGES AND MINI GAMES #

""" 
print("Welcome to the love match game!")
name1 = input("PLease enter your name: ").lower()
name2 = input("PLease enter your crush's name: ").lower()

word1 = "true"
word2 = "love"

check = name1+name2

num1 = check.count(word1[0])
num2 = check.count(word1[1])
num3 = check.count(word1[2])
num4 = check.count(word1[3])

total1 = num1 + num2 + num3 + num4

num5 = check.count(word2[0])
num6 = check.count(word2[1])
num7 = check.count(word2[2])
num8 = check.count(word2[3])

total2 = num5 + num6 + num7 + num8

score = str(total1)+str(total2)

print(f"your score is {score}")

if int(score) <= 10 or int(score) >= 90:
    print(f"Your score is {score}, you go together like coke and mentos!")
elif 40 <= int(score) <= 50:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}, you should look for a better match")
"""  # Love Match

"""
print("Welcome to treasure Island!")
direction = input("Which way would you like to go? Left or Right? - ")
if direction.lower() == "left":
    print("You went down the long road and came up to a river")
    cross_choice = input("How would you like to get across? Swim or Wait? - ")
    if cross_choice.lower() == "wait":
        print("A small boat comes down the river and ferried you across")
        door = input("Across the river is a large house with 3 doors, which one would you like to enter? Red, Yellow, or Blue - ")
        if door.lower() == "blue":
            print("You found the room with the treasure! You win the game!")
        else:
            print("The room caught on fire anf you died from the flames! Game over")
    else:
        print("You were attacked by an aligator and died terribly! Game over")
else:
    print("You fell into a cave and died from the fall! Game over")
"""  # Treasure Island

"""
print("Welcome to the coinflip game!")
choice = input("Please select heads or tails - ").lower()

toss = rm.flip

if toss == 1:
    print("Heads")
else:
    print("Tails")

if toss == 1:
    result = "heads"
    if choice == result:
        print("Congratulations you won the toss!")
    else:
        print("Sorry you lost the toss, play again!")
else:
    result = "tails"
    if choice == result:
        print("Congratulations you won the toss!")
    else:
        print("Sorry you lost the toss, play again!")
"""  # CoinFLip Game

"""
print("Bankers Roulette!")
names = input("Please provide a list of names followed by a , - ")

namesList = names.split(",")

ranNum = random.randint(0, len(namesList)-1)

selection = namesList[ranNum]

print(f"{selection} has to pay for the meal!")
"""  # Bankers Roulette

"""
rowX = [" ", " 1", "   2", "    3"]
row1 = ["1", "⬜️", "⬜️", "⬜️"]
row2 = ["2", "⬜️", "⬜️", "⬜️"]
row3 = ["3", "⬜️", "⬜️", "⬜️"]
map1 = [rowX, row1, row2, row3]
print(f"{rowX}\n{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? - ")

rowLocation = int(position[1])
columnLocation = int(position[0])

selectedRow = map1[rowLocation]
selectedRow[columnLocation] = "X"

print(f"{rowX}\n{row1}\n{row2}\n{row3}")
"""  # Hide the Treasure

"""
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("welcome to Rock, Paper, Scissors!")
choice = int(input("Please choose 1 for Rock, 2 for Paper, or 3 for Scissors - "))

if choice <= 0 or choice > 3:
    print("You typed an invalid number, you lose! Please try again")
else:
    printList = ["Rock", "Paper", "Scissors"]
    optionList = [rock, paper, scissors]

    print(f"You chose {printList[choice-1]}!")
    print(optionList[choice-1])

    opponentPick = random.randint(0, 2)

    print(f"Your opponent picked {printList[opponentPick]}")
    print(optionList[opponentPick])

    if choice-1 == opponentPick:
        print("Oh looks like there was a tie! Please play again")
    elif (choice - 1 == 0) and (opponentPick == 2):
        print("Congratulations you win!")
    elif (choice - 1 == 1) and (opponentPick == 0):
        print("Congratulations you win!")
    elif (choice - 1 == 2) and (opponentPick == 1):
        print("Congratulations you win!")
    else:
        print("Sorry you lose, please play again")
"""  # Rock Paper Scissors

"""
student_heights = input("Input a list of student heights - ").split(",")
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for value in student_heights:
    total_height += value

number_of_students = 0
for student in student_heights:
    number_of_students += 1

avg = round(total_height / number_of_students)

print(f"The average height is - {avg}cm")
"""  # Avg Heights

"""
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

high_score = 0
for score in student_scores:
    if score > high_score:
        high_score = score
    else:
        high_score = high_score
print(high_score)
"""  # Student Scores

"""
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        number = "FizzBuzz"
    elif number % 5 == 0:
        number = "Buzz"
    elif number % 3 == 0:
        number = "Fizz"
    else:
        number
    print(number)
"""  # FizzBuzz

"""
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
pLetters = int(input("How many letters would you like in your password?\n"))
pSymbols = int(input(f"How many symbols would you like?\n"))
pNumbers = int(input(f"How many numbers would you like?\n"))

password = []
for char in range(1, pLetters + 1):
    random_char = random.choice(letters)
    password.append(random_char)
for num in range(1, pNumbers + 1):
    random_num = random.choice(numbers)
    password.append(str(num))
for sym in range(1, pSymbols + 1):
    random_sym = random.choice(symbols)
    password.append(str(random_sym))
print(password)
random.shuffle(password)
random_password = ""
for char in password:
    random_password += char

print(random_password)

"""  # Random Password Generator

"""
word_list = ["Computer", "Printer", "Mouse", "Keyboard"]

chosen_word = random.choice(word_list).lower()

blanks = []
for letter in range(0, len(chosen_word)):
    blanks.append("_")
print(blanks)

guessed_letters = []
end_of_game = False
lives = 6
while not end_of_game or lives == 0:
    letter = input("Please guess a letter to see if it is on your random word - ").lower()

    if letter not in guessed_letters:
        guessed_letters.append(letter)
    else:
        print(f"You already guessed {letter}, try another letter")
    counter = 0
    for char in chosen_word:
        counter += 1
        if letter == char:
            blanks[counter - 1] = letter
    if letter not in chosen_word:
        if lives > 0:
            lives -= 1
            print(f"You guessed wrong! {letter} not in the word, you are down to {lives} lives")
        else:
            print("Sorry you ran out of lives, you lose!")
            end_of_game = True
    print(blanks)

    if "_" not in blanks:
        end_of_game = True
        print("You won the game!")

print("Please play again")

"""  # Hangman Game

"""
def paint_calc(height, width, cover):
    area = (height * width)
    number_of_cans = math.ceil(area / cover)
    print(f"You need to buy {number_of_cans} cans to paint this wall")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
"""  # Paint can calculator

"""
def prime_checker(number):
    prime_number = True
    for num in range(2 - number):
        if number % num == 0:
            prime_number = False
    if prime_number:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")


n = int(input("Check this number: "))
prime_checker(number=n)
"""  # Prime number checker

"""
def combined_cypher(message, move, user_direction):
    end_text = ""
    for char in message:
        current_pos = alphabet.index(char)
        if user_direction == "encode":
            new_position = current_pos + move
            if new_position <= 25:
                new_letter = alphabet[current_pos + move]
                end_text += new_letter
            else:
                new_letter = alphabet[new_position - 25]
                end_text += new_letter
        else:
            new_position = current_pos - move
            if new_position <= 25:
                new_letter = alphabet[new_position]
                end_text += new_letter
            else:
                new_letter = alphabet[new_position - 25]
                end_text += new_letter
    print(end_text)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u'
    , 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# if direction == "encode":
# 	encrypt(message=text, move=shift)
# else:
# 	decode(message=text, move=shift)

combined_cypher(message=text, move=shift, user_direction=direction)

"""  # Caesar Cipher

"""
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}
for student in student_scores:
    score = int(student_scores[student])
    if score >= 91:
        student_grades[student] = "Outstanding"
    elif score >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"


print(student_scores)
print(student_grades)
"""  # Hogwarts Grades

"""
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "US": "Washington DC",
}

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Munich", "Hamburg"], "total_visits": 8},
    "US": {"cities_visited": ["Washington DC", "Charlotte", "Greensboro"], "total_visits": 20}
}

travel_list = [
    {"country": "France", "cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    {"country": "Germany", "cities_visited": ["Berlin", "Munich", "Hamburg"], "total_visits": 8},
    {"country": "US", "cities_visited": ["Washington DC", "Charlotte", "Greensboro"], "total_visits": 20}
]

print(travel_list)
print(travel_log)
"""  # Dictionary practice

"""
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]


def add_new_log(name, number_of_visits, location):
    new_log = {"country": name, "visits": number_of_visits, "cities": location}
    travel_log.append(new_log)
    print(travel_log)


print("My Travel Log!")

country = input("Please enter the name of the country: ")
city = input("Please enter the name of the city/cities separated by a comma: ")
visit_number = input("Please neter the number of times you have been there: ")

location_list = city.split(",")

add_new_log(name=country, number_of_visits=visit_number, location=location_list)
"""  # Travel Log

"""
print("Welcome to the blind auction!")

continue_playing = True

bid_library = {}
while continue_playing:
    name = input("What is your name? - ")
    bid = int(input("What is your bid? - "))

    bid_library[name] = bid

    print(bid_library)

    keep_playing = input("Is there anyone else in the room? Yes or No - ").lower()
    if keep_playing == "no":
        continue_playing = False
    else:
        continue_playing = True

highest_bid = 0
for person in bid_library:
    current_bid = int(bid_library.get(person))
    if current_bid > highest_bid:
        highest_bid = current_bid
        highest_bidder = person

print(f"The highest bidder is {highest_bidder}")
"""  # Highest bidder

"""
def format_name(f_name, l_name):
    first_name = f_name.title()
    last_name = l_name.title()
    return f"{first_name} {last_name}"


fn = input("What is your first name? - ")
ln = input("What is your last name? - ")

print(format_name(f_name=fn, l_name=ln))
"""  # Return function

"""
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month <= 0 or month > 12:
        return "Invalid month please enter a number between 1 and 12"
    if is_leap(year):
        month_days[1] = 29
    else:
        month_days[1] = 28

    return month_days[month-1]


year_input = int(input("Enter a year: "))
month_input = int(input("Enter a month: "))
days = days_in_month(year=year_input, month=month_input)
print(days)
"""  # Leap year

"""
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


def multiply(n1, n2):
    return n1 * n2


action = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}


def calculator():
    num1 = float(input("What is the 1st number: "))
    for operator in action:
        print(operator)
    operation = input("Which operation do you want to complete from the options above? - ")
    num2 = float(input("What is the next number: "))
    if operation == "/" and num1 < num2:
        print("Number 1 must be greater than number 2 if you want to use the divide function")

    calculation = action[operation]
    answer = calculation(num1, num2)
    print(f"{num1} {operation} {num2} = {answer}")

    keep_playing = True
    total = answer
    while keep_playing:
        y_n = input("Type 'y' to keep calculating. Type 'n' to exit: ")
        if y_n == "n":
            keep_playing = False
        else:
            operation2 = input("Which operation do you want to complete from the options above? - ")
            num_x = int(input("Please enter a number: "))
            calculation = action[operation2]
            prev_total = total
            total = calculation(prev_total, num_x)
            print(f"{prev_total} {operation2} {num_x} = {total}")

    print(f"You have quit the calculation with a total of {total} ")
    calculator()


calculator()
"""  # Calculator

"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def starting_cards():
    return random.choices(cards, k=2)


user_cards = starting_cards()
dealer_cards = starting_cards()
print(f"Your cards are: {user_cards[0]}, {user_cards[1]}")
"\n"
print(f"The dealers cards are {dealer_cards[0]}, X")


def get_user_total(u_cards):
    if 11 in u_cards:
        current_total = 0
        for num in u_cards:
            current_total += num
            if current_total > 21:
                user_cards.remove(11)
                user_cards.append(1)
                current_total = 0
                for card in u_cards:
                    current_total += card
                return current_total
        return current_total
    else:
        current_total = 0
        for num in u_cards:
            current_total += num
        return current_total


def get_dealer_total(d_cards):
    current_total = 0
    for num in d_cards:
        current_total += num
    return current_total


def who_won(user, dealer):
    if user > dealer:
        print("You Won!")
        if input("Would you like to play again? Yes or no: ").lower() == "yes":
            return True
        else:
            return False
    elif user < dealer:
        print("You Lost!")
        if input("Would you like to play again? Yes or no: ").lower() == "yes":
            return True
        else:
            return False
    else:
        print("You tied! The round is a draw!")
        if input("Would you like to play again? Yes or no: ").lower() == "yes":
            return True
        else:
            return False


def user_turn():
    my_turn = True
    while my_turn:
        user_score = get_user_total(user_cards)
        print(f"Your total is {user_score}")
        if user_score < 21:
            if input("Would you like another card, yes or no: ") == "yes":
                user_cards.append(random.choice(cards))
                print(user_cards)
            else:
                my_turn = False
                return user_score
        elif user_score == 21:
            print("Congratulations! You have 21 and have won the game!")
            my_turn = False
            return user_score
        elif user_score > 21:
            print("You went over 21 and busted, you lose the game!")
            my_turn = False
            return user_score
        else:
            print("error")
            my_turn = False


def dealer_turn():
    d_turn = True
    while d_turn:
        print(dealer_cards)
        dealer_score = get_dealer_total(dealer_cards)
        print(dealer_score)
        if dealer_score < 17:
            dealer_cards.append(random.choice(cards))
            print(dealer_cards)
            dealer_score = get_user_total(user_cards)
            print(f"The dealer's total is {dealer_score}")
        elif 17 <= dealer_score < 21:
            dealer_score = get_dealer_total(dealer_cards)
            print(dealer_cards)
            print(f"The dealer's total is {dealer_score}")
            return dealer_score
        elif dealer_score > 21:
            print(dealer_cards)
            print(f"The dealer's total is {dealer_score}")
            print("The dealer has busted, you win the game!")
            if input("Would you like to play again? Yes or no: ").lower() == "yes":
                system('clear')
                blackjack()
            else:
                d_turn = False
        else:
            print("error")
            d_turn = False


def blackjack():
    end_user = user_turn()
    if end_user < 21:
        end_dealer = dealer_turn()
        if who_won(user=end_user, dealer=end_dealer):
            system('clear')
            blackjack()
        else:
            system('clear')
    elif input("Would you like to play again? Yes or no: ").lower() == "yes":
        system('clear')
        blackjack()
    else:
        print("You have left the game")
        system('clear')


blackjack()
"""  # Blackjack game

"""
def pick_number():
    numbers_list = []
    for num in range(1, 101):
        numbers_list.append(num)
    selection = random.choice(numbers_list)
    return selection


def check_number(num, user_guess):
    if user_guess == num:
        return "won"
    elif user_guess < num:
        return "lower"
    elif user_guess > num:
        return "higher"
    else:
        "error"


print("Welcome to the number guessing game!")
print("I'm thinking ov a number between 1 and 100.")
mode = input("Choose a difficulty. Type 'easy or 'hard: ")

NUMBER = pick_number()
if mode == "easy":
    guesses_remaining = 10
    print(f"You have {guesses_remaining} guesses remaining")
    continue_guessing = True
    while continue_guessing:
        guess = int(input("Try and guess the number: "))
        if guess == NUMBER:
            print("Congratulations! You guessed right and have won the game")
            continue_guessing = False
        elif guess < NUMBER:
            if guesses_remaining > 1:
                print("You guessed to low of a number! Please guess a greater one")
                guesses_remaining -= 1
                print(f"You have {guesses_remaining} guesses remaining")
            else:
                print("Sorry you guessed wrong and you ran out of guesses! The game is over")
                continue_guessing = False
        else:
            if guesses_remaining > 1:
                print("You guess to high of a number! Please guess a lower one")
                guesses_remaining -= 1
                print(f"You have {guesses_remaining} guesses remaining")
            else:
                print("Sorry you guessed wrong and you ran out of guesses! The game is over.")
                continue_guessing = False
else:
    guesses_remaining = 5
    print(f"You have {guesses_remaining} guesses remaining")
    continue_guessing = True
    while continue_guessing:
        guess = int(input("Try and guess the number: "))
        if guess == NUMBER:
            print("Congratulations! You guessed right and have won the game")
            continue_guessing = False
        elif guess < NUMBER:
            if guesses_remaining > 1:
                print("You guessed to low of a number! Please guess a greater one")
                guesses_remaining -= 1
                print(f"You have {guesses_remaining} guesses remaining")
            else:
                print("Sorry you guessed wrong and you ran out of guesses! The game is over")
                continue_guessing = False
        else:
            if guesses_remaining > 1:
                print("You guess to high of a number! Please guess a lower one")
                guesses_remaining -= 1
                print(f"You have {guesses_remaining} guesses remaining")
            else:
                print("Sorry you guessed wrong and you ran out of guesses! The game is over.")
                continue_guessing = False
"""  # Number guessing game

"""
data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    }, {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    }, {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    }, {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    }, {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
        'country': 'United States'
    }, {
        'name': 'Kylie Jenner',
        'follower_count': 172,
        'description': 'Reality TV personality and businesswoman and Self-Made Billionaire',
        'country': 'United States'
    }, {
        'name': 'Kim Kardashian',
        'follower_count': 167,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    }, {
        'name': 'Lionel Messi',
        'follower_count': 149,
        'description': 'Footballer',
        'country': 'Argentina'
    }, {
        'name': 'Beyoncé',
        'follower_count': 145,
        'description': 'Musician',
        'country': 'United States'
    }, {
        'name': 'Neymar',
        'follower_count': 138,
        'description': 'Footballer',
        'country': 'Brasil'
    }, {
        'name': 'National Geographic',
        'follower_count': 135,
        'description': 'Magazine',
        'country': 'United States'
    }, {
        'name': 'Justin Bieber',
        'follower_count': 133,
        'description': 'Musician',
        'country': 'Canada'
    }, {
        'name': 'Taylor Swift',
        'follower_count': 131,
        'description': 'Musician',
        'country': 'United States'
    }, {
        'name': 'Kendall Jenner',
        'follower_count': 127,
        'description': 'Reality TV personality and Model',
        'country': 'United States'
    }, {
        'name': 'Jennifer Lopez',
        'follower_count': 119,
        'description': 'Musician and actress',
        'country': 'United States'
    }, {
        'name': 'Nicki Minaj',
        'follower_count': 113,
        'description': 'Musician',
        'country': 'Trinidad and Tobago'
    }, {
        'name': 'Nike',
        'follower_count': 109,
        'description': 'Sportswear multinational',
        'country': 'United States'
    }, {
        'name': 'Khloé Kardashian',
        'follower_count': 108,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Miley Cyrus',
        'follower_count': 107,
        'description': 'Musician and actress',
        'country': 'United States'
    }, {
        'name': 'Katy Perry',
        'follower_count': 94,
        'description': 'Musician',
        'country': 'United States'
    }, {
        'name': 'Kourtney Kardashian',
        'follower_count': 90,
        'description': 'Reality TV personality',
        'country': 'United States'
    }, {
        'name': 'Kevin Hart',
        'follower_count': 89,
        'description': 'Comedian and actor',
        'country': 'United States'
    }, {
        'name': 'Ellen DeGeneres',
        'follower_count': 87,
        'description': 'Comedian',
        'country': 'United States'
    }, {
        'name': 'Real Madrid CF',
        'follower_count': 86,
        'description': 'Football club',
        'country': 'Spain'
    }, {
        'name': 'FC Barcelona',
        'follower_count': 85,
        'description': 'Football club',
        'country': 'Spain'
    }, {
        'name': 'Rihanna',
        'follower_count': 81,
        'description': 'Musician and businesswoman',
        'country': 'Barbados'
    }, {
        'name': 'Demi Lovato',
        'follower_count': 80,
        'description': 'Musician and actress',
        'country': 'United States'
    }, {
        'name': "Victoria's Secret",
        'follower_count': 69,
        'description': 'Lingerie brand',
        'country': 'United States'
    }, {
        'name': 'Zendaya',
        'follower_count': 68,
        'description': 'Actress and musician',
        'country': 'United States'
    }, {
        'name': 'Shakira',
        'follower_count': 66,
        'description': 'Musician',
        'country': 'Colombia'
    }, {
        'name': 'Drake',
        'follower_count': 65,
        'description': 'Musician',
        'country': 'Canada'
    }, {
        'name': 'Chris Brown',
        'follower_count': 64,
        'description': 'Musician',
        'country': 'United States'
    }, {
        'name': 'LeBron James',
        'follower_count': 63,
        'description': 'Basketball player',
        'country': 'United States'
    }, {
        'name': 'Vin Diesel',
        'follower_count': 62,
        'description': 'Actor',
        'country': 'United States'
    },
    {
        'name': 'Cardi B',
        'follower_count': 67,
        'description': 'Musician',
        'country': 'United States'
    }, {
        'name': 'David Beckham',
        'follower_count': 82,
        'description': 'Footballer',
        'country': 'United Kingdom'
    }, {
        'name': 'Billie Eilish',
        'follower_count': 61,
        'description': 'Musician',
        'country': 'United States'
    }, {
        'name': 'Justin Timberlake',
        'follower_count': 59,
        'description': 'Musician and actor',
        'country': 'United States'
    }, {
        'name': 'UEFA Champions League',
        'follower_count': 58,
        'description': 'Club football competition',
        'country': 'Europe'
    }, {
        'name': 'NASA',
        'follower_count': 56,
        'description': 'Space agency',
        'country': 'United States'
    }, {
        'name': 'Emma Watson',
        'follower_count': 56,
        'description': 'Actress',
        'country': 'United Kingdom'
    }, {
        'name': 'Shawn Mendes',
        'follower_count': 57,
        'description': 'Musician',
        'country': 'Canada'
    }, {
        'name': 'Virat Kohli',
        'follower_count': 55,
        'description': 'Cricketer',
        'country': 'India'
    }, {
        'name': 'Gigi Hadid',
        'follower_count': 54,
        'description': 'Model',
        'country': 'United States'
    }, {
        'name': 'Priyanka Chopra Jonas',
        'follower_count': 53,
        'description': 'Actress and musician',
        'country': 'India'
    }, {
        'name': '9GAG',
        'follower_count': 52,
        'description': 'Social media platform',
        'country': 'China'
    }, {
        'name': 'Ronaldinho',
        'follower_count': 51,
        'description': 'Footballer',
        'country': 'Brasil'
    }, {
        'name': 'Maluma',
        'follower_count': 50,
        'description': 'Musician',
        'country': 'Colombia'
    }, {
        'name': 'Camila Cabello',
        'follower_count': 49,
        'description': 'Musician',
        'country': 'Cuba'
    }, {
        'name': 'NBA',
        'follower_count': 47,
        'description': 'Club Basketball Competition',
        'country': 'United States'
    }
]


def get_followers(target):
    for entry in data:
        if entry['name'] == target['name']:
            followers = int(entry.get('follower_count'))
            print(followers)
            return followers


def high_low(follower_a, follower_b):
    if follower_b > follower_a:
        return "higher"
    else:
        return "lower"


def next_turn(target_a, target_b):
    for entry in data:
        if entry['name'] == target_a['name']:
            data.remove(target_a)
            target_a = target_b
            target_b = random.choice(data)

    return [target_a, target_b]


def format_data(item):
    person_name = item['name']
    person_descr = item["description"]
    person_country = item["country"]

    return f"{person_name}, a {person_descr}, from {person_country}"


def game():
    print("Welcome to the Higher or Lower game!")
    choice_b = random.choice(data)
    still_playing = True
    score = 0
    while still_playing:
        # display options A and B
        choice_a = choice_b
        choice_b = random.choice(data)
        if choice_a == choice_b:
            choice_b = random.choice(data)

        print(f"Option A - {format_data(choice_a)}")
        print(f"Option B - {format_data(choice_b)}")

        a = get_followers(target=choice_a)
        b = get_followers(target=choice_b)

        # user picks which option a and then asks if option b is higher or lower
        guess = input("Does option B have more or less followers on Instagram? Type Higher or Lower to answer: ").lower()
        result = high_low(a, b)
        correct_guess = True
        while correct_guess:
            # If user guesses right, add 1 to score and make option B into option A and get new option for B
            if result == guess:
                print("Congratulations you guessed right! Get ready to guess again")
                score += 1
                print(f"Your score is now: {score}")
                data.remove(choice_a)
                correct_guess = False
            # If user guesses wrong and the game is over with a total score displayed
            else:
                print(f"You guessed wrong! The game is over and your final score was {score}")
                correct_guess = False
                play_again = input("Would you like to play again? Type Yes or No - ").lower()
                if play_again == 'yes':
                    still_playing = True
                else:
                    still_playing = False


game()
"""  # Higher or Lower game


