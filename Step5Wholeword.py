#Func
def difficulty(difficulties, yesandno):
    while True:
        coffee = input('Do you like coffee? ')
        for item in yesandno:
            if coffee == item or coffee == item[0]:
                print('test')



#Main
difficulty(['easy', 'medium', 'hard'], ['yes', 'no'])