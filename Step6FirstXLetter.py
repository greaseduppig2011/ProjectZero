#Func
def firstxletter(question, answers):
    singleletter = 0
    while True:
        method = input(question)
        method = method.lower()
        for item in answers:
            if method == item:
                return f"You chose '{item}'"
            elif method[0] == item[0]:
                singleletter = singleletter + 1
                singleletterstring = item
        if singleletter == 1:
            return f"You chose '{singleletterstring}'"
        elif singleletter > 1:
            if len(method) > 1:
                for item in answers:
                    if method[1] == item[1]:
                        return f"You chose '{item}'"
        print(f'Sorry, please enter {answers[0]} or {answers[1]}')



#Main
payment = ['cash', 'credit']
print(firstxletter('Do you like coffee? ', ['yes', 'no']))
print(firstxletter('Payment: ', payment))
print(firstxletter('Payment: ', payment))