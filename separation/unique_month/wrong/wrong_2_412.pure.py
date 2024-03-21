def unique_month(month, possible_birthdays):
    count=0
    for i in range(len(possible_birthdays)):
        if possible_birthdays[i][0]==month:
            count+=1
    if count==1:
        return True
    else:
        return False