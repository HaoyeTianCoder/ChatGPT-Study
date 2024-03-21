def unique_day(day, possible_birthdays):
    result = 0
    for i in range(len(possible_birthdays)):
        if day in possible_birthdays[i]:
            result += 1
    if result == 1:
        return True
    else:
        return False