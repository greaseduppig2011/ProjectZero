#Func
def intorfloat(question, response, typevar, appendresponse):
    varlist = []

    while len(varlist) < 2:
        answer = input(question)
        infvar = False
        try: 
            answer = typevar(answer)
            if answer <= 0:
                print(f"{response} that is more than 0")
            else:
                if infvar == True:
                    varlist.append(answer)
        except:
            if str(answer) == 'xxx':
                print("Exit Code activated.")
                exit()
            elif str(answer) == '':
                print("You have chosen infinite mode.")
                infvar = True
            else:
                print(f"{response}{appendresponse}.")


#Main
intorfloat('Input a float: ', 'Please enter a number', float, '')
intorfloat('Input an integer: ', 'Please enter an integer', int, ' (ie: a number which does have a decimal part)')