def unique_month(month, possible_birthdays):
    counter = 0
    for i in range (len(possible_birthdays)):
        if month == possible_birthdays[i][0]:
            counter += 1
    if counter == 1:
        return True
    else:
        return False