#Func
def intorfloat(question, response, typevar, appendresponse):
    varlist = []

    while len(varlist) < 2:
        try:
            answer = input(question)
            if answer > 0:
                varlist.append(answer)
            else:
                print(f"{response} that is more than 0")
        except:
            if str(answer) == 'xxx':
                print('Exit code activated')
                return
            print(f"{response}{appendresponse}. ")


#Main
intorfloat('Input a float: ', 'Please enter a number', float, '')
intorfloat('Input an integer: ', 'Please enter an integer', int, ' (ie: a number which does have a decimal part)')