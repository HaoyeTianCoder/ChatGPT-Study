def unique_day(day, possible_birthdays):
    counter = 0
    result = 0
    while counter < len(possible_birthdays):
        date = possible_birthdays[counter][1]
        if date == day:
            result = result + 1
        counter = counter + 1
    if result > 1:
        return False
    return True