def unique_day(date, possible_birthdays):
    count = 0 
    for i in range (len(possible_birthdays)):
        if date == possible_birthdays[i][1]:
            count += 1 
        if count == 1:
            return True
        else: 
            return False 