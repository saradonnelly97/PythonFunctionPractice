#Prompt 4
def num_within(num, start, end):
    if start <= num <= end:
        return True
    else: 
        return False
    
print(num_within(6,5,7))
print(num_within(10,3,7))