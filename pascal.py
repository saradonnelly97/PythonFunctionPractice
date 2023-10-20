#Prompt 5
def pascal(n):
    for line in range(n):
        current_val = 1 
        for i in range(line + 1):
            print(current_val, end = " ")

            current_val = current_val * (line - 1) // (i + 1)
    print()

n = 5
pascal(2)