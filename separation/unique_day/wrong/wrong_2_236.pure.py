def unique_day(day, possible_birthdays):
    days = [possible_birthdays[i][1] for i in range(len(possible_birthdays))]
    if days.count(day) > 1:
        return False
    return True