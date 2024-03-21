def unique_day(day, possible_birthdays):
    counter = 0
    for i in range (len(possible_birthdays)):
        if day == possible_birthdays[i][1]:
            counter += 1
    if counter == 1:
        return True
    else:
        return False