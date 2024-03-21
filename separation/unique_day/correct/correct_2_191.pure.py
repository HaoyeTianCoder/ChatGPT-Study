def unique_day(day, possible_birthdays):
    n = len(possible_birthdays)
    result = 0
    for counter in range(n):
        if day == possible_birthdays[counter][1]:
            result = result + 1
    return result == 1