def contains_unique_day(month, possible_birthdays):
    counter = 0
    while counter < len(possible_birthdays):
        get_month = possible_birthdays[counter][0]
        if get_month == month:
            test_date = possible_birthdays[counter][1]
            if unique_day(test_date, possible_birthdays) == True:
                return True
        counter = counter + 1
    return False 