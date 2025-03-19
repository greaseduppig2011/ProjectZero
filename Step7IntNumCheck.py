#Func
def intorfloat(question, response, typevar, appendresponse):
    varlist = []

    while len(varlist) < 2:
        answer = input(question)
        try: 
            answer = typevar(answer)
            if answer <= 0:
                print(f"{response} that is more than 0")
            else:
                varlist.append(answer)
        except:
            if str(answer) == 'xxx':
                print("Exit Code activated.")
                exit()
            print(f"{response}{appendresponse}.")


#Main
intorfloat('Input a float: ', 'Please enter a number', float, '')
intorfloat('Input an integer: ', 'Please enter an integer', int, ' (ie: a number which does have a decimal part)')