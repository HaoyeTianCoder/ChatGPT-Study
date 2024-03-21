def unique_day(day, possible_birthdays):
    a = 0
    for i in range(len(possible_birthdays)):
        if day == possible_birthdays[i][1]:
            a += 1
    if a == 1:
        return True
    else:
        return False