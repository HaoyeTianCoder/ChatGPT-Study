def unique_day(day, possible_birthdays):
    count, result = 0, 0
    for count in range(0, len(possible_birthdays)):
        if day == possible_birthdays[count][1]:
            result = result + 1
        else:
            continue
    if result == 1:
        return True
    else:
        return False