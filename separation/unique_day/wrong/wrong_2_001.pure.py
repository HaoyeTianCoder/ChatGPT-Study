def unique_day(day, possible_birthdays):
    for i in range (len(possible_birthdays)):
        if possible_birthdays[i][1] == day:
            for j in range (i + 1, len(possible_birthdays)):
                if possible_birthdays[j][1] == day:
                    return False
    return True