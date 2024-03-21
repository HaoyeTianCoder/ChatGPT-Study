def contains_unique_day(month, possible_birthdays):
    filtered_birthdays = tuple(filter(lambda x: x[0] == month,possible_birthdays))
    for day in tuple(map(lambda x: x[1], filtered_birthdays)):
        if unique_day(day, possible_birthdays):
            return True
    return False