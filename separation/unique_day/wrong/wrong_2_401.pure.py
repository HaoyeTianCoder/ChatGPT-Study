def unique_day(date, possible_birthdays):
    i=0
    count=0
    while i <= len(possible_birthdays):
        if possible_birthdays[i][1]==date:
            count+=1
            i+=1
    if count==1:
        return True
    else:
        return False