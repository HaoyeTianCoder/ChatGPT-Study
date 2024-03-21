def unique_day(date, possible_birthdays):
    lenth=len(possible_birthdays)
    count=0
    for i in range(0,lenth):
        if date==possible_birthday[i][1]:
            count=count+1
    if count==1:
        return True
    else:
        return False