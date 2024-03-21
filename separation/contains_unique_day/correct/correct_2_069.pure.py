def contains_unique_day(month, possible_birthdays):
    specific_set = tuple(filter(lambda x: x[0] == month, possible_birthdays))
    get_days = tuple(map(lambda x: x[1],specific_set))
    ans = tuple(map(lambda x: unique_day(x,possible_birthdays),get_days))
    if True in ans:
        return True
    else:
        return False