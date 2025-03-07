#Func
def YorN(question):
    while True:
        answer = input(question)
        answer = answer.lower()
        if answer[0] is 'y':
            return answer
        elif answer[0] is 'n':
            return answer
        else:
            print('Please enter either "Yes" or "No"')




#Main
print(YorN("question: "))