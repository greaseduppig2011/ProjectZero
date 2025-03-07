def not_blank(question):
    while True:
        response = input(question)

        if len(response) < 1:
            print("Sorry, this can't be Blank.")
        else:
            return response
#Main code
who = not_blank("Please enter your name: ")
print(f"Hello {who}")