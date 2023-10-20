#Prompt 3 
def rev_string(strng):
    if len(strng) == 0:
        return strng
    else:
        return rev_string(strng[1:]) + strng[0]
    
og_str = "You are doing your best"
revrs_str = rev_string(og_str)

print(revrs_str)