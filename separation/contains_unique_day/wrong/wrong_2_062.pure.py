def contains_unique_day(month, possible_birthdays):
    month1 = filter(lambda x: x[0] == month, possible_birthdays)
    for birthday in month1:
        x = unique_day(birthday[1], possible_birthdays)
        if x == True:
            return True
    return False