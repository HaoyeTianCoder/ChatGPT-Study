def unique_day(day, possible_birthdays):
    count = 0
    for i in range(len(possible_birthdays)):
        if day == possible_birthdays[i][1]:
            count += 1
    if count > 1:
        return False
    else:
        return True