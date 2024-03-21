def unique_month(month, possible_birthdays):
    a=0
    for i in range(len(possible_birthdays)):
        if month==possible_birthdays[i][0]:
            a+=1
    if a==1:
        return True
    else:
        return False