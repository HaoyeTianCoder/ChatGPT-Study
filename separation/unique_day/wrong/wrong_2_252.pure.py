def unique_day(date, possible_birthdays):
    counter = 0
    for i in range(len(possible_birthdays)):
        if possible_birthdays[i][1] == day:
            counter += 1
    if counter == 1:
        return True
    else:
        return False