#Func
def ageintcheck(name):
    while True:
        try:
            answer = int(input(f"How old are you {name}? "))
            if answer > 120:
                print(f"{name} is too old")
                return answer
            elif answer < 12:
                print(f"{name} is too young")
                return answer
            else:
                print(f"{name} has bought a ticket")
                return answer
        except:
            print('<Please enter an integer between 12 and 120>')



#Main
ageintcheck(input('Name: '))
ageintcheck(input('Name: '))
ageintcheck(input('Name: '))
ageintcheck(input('Name: '))
ageintcheck(input('Name: '))
ageintcheck(input('Name: '))