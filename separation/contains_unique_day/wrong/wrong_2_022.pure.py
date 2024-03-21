def contains_unique_day(month, possible_birthdays):
    birthday_list = tuple(filter(lambda x: x[0] == month, possible_birthdays))
    for i in tuple(map(lambda x: x[1], birthday_list)):
        if unique_day(i,possible_birthdays):
            return True
    return False