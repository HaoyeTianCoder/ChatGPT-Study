def contains_unique_day(month, possible_birthdays):
    for i in range(len(possible_birthdays)):
        if month == possible_birthdays[i][0]:    
            day = possible_birthdays[i][1]
            check = unique_day(day, possible_birthdays)
            if check == True:
                return True
    return False