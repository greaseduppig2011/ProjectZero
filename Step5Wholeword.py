#Func
def difficulty1(yesandno):
    while True:
        coffee = input('Do you like coffee? ')
        coffee = coffee.lower()
        for item in yesandno:
            if coffee == item or coffee == item[0]:
                print(f"You chose '{item}'")
                return 'debug'
        print("Sorry please enter 'yes' or 'no")
def difficulty2(level):
    while True:
        level1 = input('Choose a level (Easy / Medium / Hard): ')
        level1 = level1.lower()
        for item in level:
            if level1 == item or level1 == item[0]:
                print(f"You chose '{item}'")
                return 'Nero Magnura'
        print("Sorry, please choose easy, medium, or hard")
def difficulty3(level):
    while True:
        level2 = input('Choose the next level (Easy/Medium/Hard): ')
        level2 = level2.lower()
        for item in level:
            if level2 == item or level2 == item[0]:
                print(f"You chose '{item}'")
                return 'debug'
        print('Sorry, please choose easy, medium, or hard')


#Main
difficulties = ['easy', 'medium', 'hard']
yesno = ['yes', 'no']
difficulty1(yesno)
difficulty2(difficulties)
difficulty3(difficulties)