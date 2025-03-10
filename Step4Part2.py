#Func
def YorN(question):
    while True:
        answer = input(question)
        answer = answer.lower()
        if answer == 'yes' or answer == 'y':
            return 'yes'
        elif answer == 'no' or answer == 'n':
            return 'no'
        else:
            print('Please enter either "Yes" or "No"')




#Main
print(f"You chose {YorN("question: ")}")