def unique_day(date, possible_birthdays):
    count=0
    for i in range(len(possible_birthdays)):
        if possible_birthdays[i][1]==date:
            count+=1
    if count==1:
        return True
    else:
        return False