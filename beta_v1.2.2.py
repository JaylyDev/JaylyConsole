import random

random.seed()   #Prepare random number generator

for loading in range(0, 100 + 1, 1):
    if loading == 25:
        for cooldown in range(0, 10 + 1, 1):
            print("Installing Console Communication Service")
    else:
        if loading == 50:
            for cooldown in range(0, 10 + 1, 1):
                print("Installing User Profile Service")
        else:
            if loading == 75:
                for cooldown in range(0, 10 + 1, 1):
                    print("Installing Software Service")
            else:
                print("")
print("Welcome to Flowgorithm")
while True:    #This simulates a Do Loop
    print("Please enter the username of this snapshot to open this document")
    loginstatus = "0"
    username = input()
    if username == "internal":
        while True:    #This simulates a Do Loop
            print("Please enter the password to open this document")
            passwordstatus = "0"
            password = input()
            if password == "password":
                print("Correct Password")
                print("Hello, " + username)
                print("Unlocking document infomations")
                passwordstatus = "1"
            else:
                print("Incorrect Password")
                passwordstatus = "0"
                loginstatus = "0"
            if not(passwordstatus == "0"): break   #Exit loop
        loginstatus = "1"
            else:
                loginstatus = "0"
                print("Incorrect Username")
    if not(loginstatus == "0"): break   #Exit loop
print("Hello, " + username)
print("Unlocking document infomations")
while True:    #This simulates a Do Loop
    print("Select an appication")
    print("Type '/play calculator' to use Calculator.")
    print("Type '/play trivia' to play Trivia.")
    print("Type '/play 8ball' to ask 8ball.")
    print("Type '/play rps' to play Rock, Paper, Scissors.")
    print("or Type '/stop' to stop the program.")
    selector = input()
    if selector == "/play calculator":
        selected = 1
        print("Select an operation:")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Comparsation")
        print("6.Weight conversion")
        operation = input()
        if operation == "1":
            selected = 1
            print("Enter first number: ")
            number1 = int(input())
            print("Enter second number: ")
            number2 = int(input())
            answer = number1 + number2
            print("The answer is " + str(answer))
        else:
            if operation == "2":
                selected = 1
                print("Enter first number: ")
                number1 = int(input())
                print("Enter second number: ")
                number2 = int(input())
                answer = number1 - number2
                print("The answer is " + str(answer))
            else:
                if operation == "3":
                    selected = 1
                    print("Enter first number: ")
                    number1 = int(input())
                    print("Enter second number: ")
                    number2 = int(input())
                    answer = number1 * number2
                    print("The answer is " + str(answer))
                else:
                    if operation == "4":
                        selected = 1
                        print("Enter first number: ")
                        number1 = int(input())
                        print("Enter second number: ")
                        number2 = int(input())
                        answer = float(number1) / number2
                        print("The answer is " + str(answer))
                    else:
                        if operation == "5":
                            selected = 1
                            while True:    #This simulates a Do Loop
                                print("Select a choice")
                                print("1.The largest value")
                                print("2.The smallest value")
                                choice = input()
                                if choice == "1":
                                    chosen = 1
                                    print("Enter first number: ")
                                    number1 = int(input())
                                    print("Enter second number: ")
                                    number2 = int(input())
                                    if number1 >= number2:
                                        answer = number1
                                        print("The answer is " + str(answer))
                                    else:
                                        if number2 >= number1:
                                            answer = number2
                                            print("The answer is " + str(answer))
                                        else:
                                            print("Invalid input")
                                else:
                                    if choice == "2":
                                        chosen = 1
                                        print("Enter first number: ")
                                        number1 = int(input())
                                        print("Enter second number: ")
                                        number2 = int(input())
                                        if number1 <= number2:
                                            answer = number1
                                            print("The answer is " + str(answer))
                                        else:
                                            if number2 <= number1:
                                                answer = number2
                                                print("The answer is " + str(answer))
                                            else:
                                                print("Invalid input")
                                    else:
                                        print("Invalid Input")
                                        chosen = 0
                                if not(chosen == 0): break   #Exit loop
                        else:
                            if operation == "6":
                                selected = 1
                                while True:    #This simulates a Do Loop
                                    print("Select a choice")
                                    print("1.Pounds to killograms")
                                    print("2.Killograms to pounds")
                                    choice = input()
                                    if choice == "1":
                                        chosen = 1
                                        print("Enter the weight in pounds: ")
                                        lbs = int(input())
                                        if lbs >= 0:
                                            answer = lbs / 2.205
                                            print("The weight which is measured in killograms is: " + str(answer))
                                        else:
                                            print("Invalid Input")
                                    else:
                                        if choice == "2":
                                            chosen = 1
                                            print("Enter the weight in killograms: ")
                                            kgs = int(input())
                                            if kgs >= 0:
                                                answer = kgs * 2.205
                                                print("The weight which is measured in pounds is: " + str(answer))
                                            else:
                                                print("Invalid Input")
                                        else:
                                            print("Invalid Input")
                                            chosen = 0
                                    if not(chosen == 0): break   #Exit loop
                            else:
                                print("Invalid Input")
                                selected = 0
        selected = 0
    else:
        if selector == "/play trivia":
            print("Trivia: Type 'Start' if you are ready")
            selected = 1
            activate = input()
            while activate != "Start":
                print("Type 'Start' if you are ready")
                activate = input()
            print("1. Enter a number greater than 10")
            a = int(input())
            while a <= 10:
                print("Enter a number greater than 10")
                a = int(input())
            print("Well done.")
            print("2. Enter a negative number")
            a = int(input())
            while a >= 0:
                print("Enter a negative number")
                a = int(input())
            print(str(a) + " is negative")
            print("3. What is the Answer to the Ultimate Question of Life, the Universe, and Everything?")
            a = int(input())
            while a != 42:
                print("That is incorrect, try again")
                a = int(input())
            print("Well done")
            print("4. What is your favourite football team?")
            b = input()
            while b != "Liverpool":
                print("That is incorrect, try again")
                b = input()
            print("Me too!")
            secretNumber = int(random.random() * 10)
            print("Guess the correct number between 0 and 9")
            a = int(input())
            while a != secretNumber:
                print("That is incorrect, try again")
                a = int(input())
            print("Congratulations! You have guessed the right number!")
            secretNumber = int(random.random() * 100)
            print("Guess the correct number between 0 and 100")
            a = int(input())
            while a != secretNumber:
                if a >= secretNumber:
                    print("Your guess is too high, try again!")
                else:
                    print("Your guess is too low, try again!")
                a = int(input())
            print("Congratulations! You have guessed the right number again!")
            selected = 0
        else:
            if selector == "/play 8ball":
                while True:    #This simulates a Do Loop
                    randomNum = int(random.random() * 15) + 1
                    print("Ask 8 Ball - Make your everyday decisions easier!")
                    question = input()
                    if randomNum == 1:
                        print("As I see it, yes.")
                    else:
                        if randomNum == 2:
                            print("It is certain.")
                        else:
                            if randomNum == 3:
                                print("Ask again later.")
                            else:
                                if randomNum == 4:
                                    print("Yes.")
                                else:
                                    if randomNum == 5:
                                        print("It is decidedly so.")
                                    else:
                                        if randomNum == 6:
                                            print("Concentrate and ask again.")
                                        else:
                                            if randomNum == 7:
                                                print("Outlook not so good.")
                                            else:
                                                if randomNum == 8:
                                                    print("Cannot predict now.")
                                                else:
                                                    if randomNum == 9:
                                                        print("Better not tell you now.")
                                                    else:
                                                        if randomNum == 10:
                                                            print("Yes – definitely.")
                                                        else:
                                                            if randomNum == 11:
                                                                print("Very doubtful.")
                                                            else:
                                                                if randomNum == 12:
                                                                    print("My sources say no.")
                                                                else:
                                                                    if randomNum == 13:
                                                                        print("You may rely on it.")
                                                                    else:
                                                                        if randomNum == 14:
                                                                            print("No.")
                                                                        else:
                                                                            print("Signs point to yes.")
                    while True:    #This simulates a Do Loop
                        print("Do you want to ask again? Answer in 'yes ' or 'no'.")
                        doYouWantToPlayAgain = input()
                        if doYouWantToPlayAgain == "yes":
                            againinput = 1
                            again = 1
                        else:
                            if doYouWantToPlayAgain == "no":
                                againinput = 2
                                again = 0
                            else:
                                print("Invalid Input")
                                againinput = 0
                        if not(againinput == 0): break   #Exit loop
                    if not(again == 1): break   #Exit loop
                selected = 0
            else:
                if selector == "/play rps":
                    selected = 1
                    while True:    #This simulates a Do Loop
                        while True:    #This simulates a Do Loop
                            print("Rock, Paper, Scissors?")
                            answer = int(input())
                            if answer == "Rock":
                                playerAnswer = 1
                                playerSelected = 1
                            else:
                                if answer == "Paper":
                                    playerAnswer = 2
                                    playerSelected = 1
                                else:
                                    if answer == "Scissors":
                                        playerAnswer = 3
                                        playerSelected = 1
                                    else:
                                        print("That's not a valid play. Check your spelling!")
                                        playerSelected = 0
                            if not(playerSelected == 0): break   #Exit loop
                        programAnswer = int(random.random() * 3) + 1
                        
                        # 1.Rock
                        # 2.Paper
                        # 3.Seissors
                        if playerAnswer == 1:
                            if programAnswer == 1:
                                print("It's a tie!")
                            else:
                                if programAnswer == 2:
                                    print("You won!")
                                else:
                                    if programAnswer == 3:
                                        print("You lost!")
                        else:
                            if playerAnswer == 2:
                                if programAnswer == 1:
                                    print("You lost!")
                                else:
                                    if programAnswer == 2:
                                        print("It's a tie!")
                                    else:
                                        if programAnswer == 3:
                                            print("You won!")
                            else:
                                if playerAnswer == 3:
                                    if programAnswer == 1:
                                        print("You won!")
                                    else:
                                        if programAnswer == 2:
                                            print("You lost!")
                                        else:
                                            if programAnswer == 3:
                                                print("It's a tie!")
                                else:
                                    print("ProgramAnswer.statement error")
                        while True:    #This simulates a Do Loop
                            print("Do you want to ask again? Answer in 'yes ' or 'no'.")
                            doYouWantToPlayAgain = input()
                            if doYouWantToPlayAgain == "yes":
                                againinput = 1
                                again = 1
                            else:
                                if doYouWantToPlayAgain == "no":
                                    againinput = 2
                                    again = 0
                                else:
                                    print("Invalid Input")
                                    againinput = 0
                            if not(againinput == 0): break   #Exit loop
                        if not(again == 1): break   #Exit loop
                    selected = 0
                else:
                    if selector == "/script python.beta-testing.miscellaneous.release_v1.2.1":
                        
                        # This command should be only knowledged by the program developer. The user running this command has activated 'Developer Mode'.
                        selected = 1
                        print("This program has activated 'Developer Mode' by " + str(name) + ".")
                        print("Enter the password of script.python.beta-testing.miscellaneous.release_v1.2.1.password")
                        print("Warning: Developer Mode will deactivated if the user typed the wrong password.")
                        scriptPassword = input()
                        
                        # scriptPassword = "4ebec206-b475-43e7-b92a-36c6ce228525"
                        if scriptPassword == "4ebec206-b475-43e7-b92a-36c6ce228525":
                            print("Welcome Admin to script.python.beta-testing")
                            print("Please select an appication.")
                            print("Type '/script developer.program.test_in_python_1' for Developer Program #1")
                            print("Type '/script developer.program.test_in_python_2' for Developer Program #2")
                            print("Type '/script developer.program.test_in_python_1' for Developer Program #3")
                            print("Type '/script developer.program.test_in_python_2' for Developer Program #4")
                            scriptSelector = input()
                            if scriptSelector == "/script developer.program.test_in_python_1":
                                
                                    # Insert program test in python #1
                                    print ("Enter a whole number and I'll square it.")
                                    number = int(input())
                                    answer = number * number
                                    print(answer)
                            else:
                                if scriptSelector == "/script developer.program.test_in_python_2":
                                    
                                    # Insert program test in python #2
                                    print ("Enter a word.")
                                    word = input()
                                    print (word + word + word)
                                else:
                                    if scriptSelector == "/script developer.program.test_in_python_3":
                                    
                                        # Insert program test in python #3
                                        # Selection is a decision within a computer program when the program decides what to do next based on the results of an event. In Flowgorithm, we implement Selection using an if diamond.
                                        #2. Create a new flowchart in Flowgorithm that tells the user whether they should wear shorts or not. First, ask the user for the current temperature. If the temperature is greater than 20 then tell them to wear shorts, otherwise tell them not to wear shorts.
                                        print ("What's the current temperature?")
                                        temperature = int(input())
                                        if temperature >= 20: 
                                            print ("Wear shorts.")
                                        else: 
                                            print ("Don't wear shorts.")
                                    else:
                                        if scriptSelector == "/script developer.program.test_in_python_4":

                                            # Insert program test in python #4
                                            # If they are under 13, tell them they are too young for social media. If they are over 13, tell them they are old enough for most social media. Be sure to test that both outputs work correctly.
                                            print ("What's your age?")
                                            age = int(input())
                                            if age < 13: 
                                                print ("You are too young for social media.")
                                            else: 
                                                print ("You are old enough for most social media.")
                                        else:
                                            if scriptSelector == "/script developer.program.test_in_python_5":
                                    
                                                # Insert program test in python #5
                                                # Update your code so that the program asks the user how much their suitcase weighs. If it weighs more than 23kg then tell them there will be a $50 charge. Otherwise, tell them there is no charge. Either way, then tell them to have a great day.
                                                print ("How much your suitcase weighs? " + "(Answer in kg.)")
                                                kg = float(input())
                                                if kg >= 23: 
                                                    print ("There will be a $50 charge.") 
                                                else:
                                                    print ("There is no charge," + "have a great day.")
                                            else:
                                                if scriptSelector == "/script developer.program.test_in_python_6":
                                    
                                                    # Insert program test in python #6
                                                    # Update your code so the program asks the user for their current temperature (this could be a decimal number!). If their temperature is over 39.4 tell them to go to the hospital. Otherwise, if their temperature is over 37.6 tell them to rest. Otherwise, tell them they’re fine. Be sure to test that all three outputs work correctly.
                                                    print ("What is your current temperature? " + "(Answer in degree calcius.)")
                                                    temperature = float(input())
                                                    if temperature >= 39.4: 
                                                        print ("Go to the hospital!")
                                                    else: 
                                                        if temperature >= 37.6: 
                                                            print ("Go take some rest.")
                                                        else: print ("You're fine.")
                                                else:
                                                    if scriptSelector == "/script developer.program.test_in_python_7":
                                    
                                                        # Insert program test in python #7
                                                        # a program that determines a letter grade for a given score – A for 90 and above, B for 80 and above, C for 70 and above and F for anything below 70. Here’s the code for such a program:
                                                        print ("What's your score?")
                                                        score = int(input())
                                                        if score >= 90:
                                                            print('A') 
                                                        else: 
                                                            if score >= 80: 
                                                                print('B') 
                                                            else: 
                                                                if score >= 70:
                                                                    print('C')
                                                                else: 
                                                                    print('F')
                                                    else:
                                                        if scriptSelector == "/script developer.program.test_in_python_8":
                    
                                                            # Insert program test in python #8
                                                            print ("What is your current temperature? " + "(Answer in degree calcius.)")
                                                            temperature = float(input())
                                                            if temperature >= 39.4:
                                                                print ("Go to the hospital!") 
                                                            elif temperature >= 37.6:
                                                                print ("Go take some rest.") 
                                                            else: print ("You're fine.")
                                                        else:
                                                            if scriptSelector == "/script developer.program.test_in_python_9":
                    
                                                                # Insert program test in python #9
                                                                print ("Say a number") 
                                                                number = int(input()) 
                                                                if number > 0: 
                                                                    print ("The number is positive")
                                                                elif number < 0: 
                                                                    print ("The number is negative")
                                                                else:
                                                                    print ("The number is zero")
                                                            else:
                                                                if scriptSelector == "/script developer.program.test_in_python_10":

                                                                    # Insert program test in python #10
                                                                    # Write a program to convert temperatures to and from Celsius and Fahrenheit. First, ask the user to enter a temperature. Then ask the user to enter whether that temperature is in C or F. You should then output the conversion. Be sure to test several temperatures of each type (you can use Google to check that your conversions are correct).
                                                                    # Formula Hints: if C is a temp in Celsius then the corresponding Fahrenheit temperature is C*1.8 – 32; if F is a temp in Fahrenheit, then the corresponding Celsisus temperature is 5*(F-32)/9
                                                                    print ("Enter a temperature")
                                                                    temperature = float(input())
                                                                    print ("What do you want to convert the temperature to?")
                                                                    print ("Type 'C' for Celeius, 'F' for Fahrenheit.")
                                                                    conversion = (input())
                                                                    if conversion == "C": 
                                                                        output = 5*(temperature-32)/9
                                                                        print (output)
                                                                    elif conversion == "F":
                                                                        output = temperature*1.8+32
                                                                        print (output)
                                                                    else: 
                                                                        print ("Invalid Input.")
                                                                else:
                                                                    if scriptSelector == "/script developer.program.test_in_python_11":

                                                                        # Insert program test in python #11
                                                                        # Write a program that determines whether a given year is a leap year. A leap year is a multiple of 4, and if it is a multiple of 100, it must also be a multiple of 400. Test with several years and use Google to check if you’re correct. [Hint: the % operator in Python calculates the remainder when dividing so for example 10%3 is 1 because when you divide 10 by 3 it goes it 3 times with a remainder of 1; 10 %2 is 0 because when you divide 10 by 2 it goes in 5 times with no remainder; you can test if something is a multiple of a number by checking if the remainder is 0].
                                                                        print ("Enter a year if the given year is a leap year.")
                                                                        year = int(input())
                                                                        if (year % 4) == 0:
                                                                            if (year % 100) == 0:
                                                                                if (year % 400) == 0: 
                                                                                    print("{0} is a leap year".format(year))
                                                                                else:
                                                                                    print("{0} is not a leap year".format(year))
                                                                            else: 
                                                                                print("{0} is a leap year".format(year))
                                                                        else: 
                                                                            print("{0} is not a leap year".format(year))
                                                                    else:
                                                                        if scriptSelector == "/script developer.program.test_in_python_12":

                                                                            # Insert program test in python #12
                        else:
                                print("Invalid script.python.beta-testing.miscellaneous.release_v1.2.1.developer_mode.scriptSelection")
                                selected = 0
                    else:
                        if selector == "/stop":
                            print("Stopping services")
                            selected = 1
                        else:
                            print("Invalid Input")
                            selected = 0
    if not(selected == 0): break   #Exit loop
