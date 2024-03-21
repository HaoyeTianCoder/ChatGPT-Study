def unique_month(month, possible_birthdays):
    i=0
    count=0
    while i<=len(possible_birthdays):
        if possible_birthdays[i][0]==month:
            count+=1
            i+=1
    if count==1:
        return True
    else:
        return False