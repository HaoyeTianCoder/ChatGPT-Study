def contains_unique_day(month, possible_birthdays):
    for i in range(len(possible_birthdays)):
        if possible_birthdays[i][0] == month and unique_day(possible_birthdays[i][1], possible_birthdays) == True:
            return True
    return False