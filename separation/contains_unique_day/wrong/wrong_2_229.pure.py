def contains_unique_day(month, possible_birthdays):
    for each_day_in_month in filter(lambda x: x[0] == month, possible_birthdays):
        if unique_day(each_day_in_month[1], possible_birthdays) == True:
            res = True
        else:
            res = False
    return res