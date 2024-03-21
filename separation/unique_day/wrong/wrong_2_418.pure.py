def unique_day(date, possible_birthdays):
    for i in range(len(possible_birthdays)):
        if date==possible_birthdays[i]:
            return True
        else:
            return False