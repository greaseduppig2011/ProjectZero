#Func goes here
def make_statement(statement, decoration, lines):
    for i in range(int(lines/2) + (lines%2) -1 ): 
        print(f"{decoration * 3}{decoration * len(statement)}{decoration*3}")
    print(f"{decoration * 3}{statement}{decoration * 3}")
    for i in range(int(lines/2)):
        print(f"{decoration * 3}{decoration * len(statement)}{decoration*3}")
    


# Main code
make_statement("Programming is Fun!", "=", 3)
make_statement("Programming is Still Fun!", "*", 2)
make_statement("Emoji in Action", "🐎", 1)