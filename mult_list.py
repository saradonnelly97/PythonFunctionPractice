#Prompt 2
def mult_list(num):
    if not num:
        return 1
    else:
        return num[0] * mult_list(num[1:])
    
ex_list = [2,2,2]
prod = mult_list(ex_list)
print(prod)