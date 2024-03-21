def unique_day(day, possible_birthdays):
    counter = 0
    for days in range(len(possible_birthdays)):
        if str(day) == possible_birthdays[days][1]:
            counter += 1
    return True if counter == 1 else False