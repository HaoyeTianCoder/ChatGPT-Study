def contains_unique_day(month, possible_birthdays):
    for i in range(0,len(possible_birthdays)):
        if possible_birthdays[i][0] == month:
            if unique_day(possible_birthdays[i][1],possible_birthdays):
                return True
    else:
        return False            