def unique_month(month, possible_birthdays):
    lenth=len(possible_birthdays)
    count=0
    for i in range(0,lenth):
        if month==possible_birthdays[i][0]:
            count=count+1
    if count==1:
        return True
    else:
        return False