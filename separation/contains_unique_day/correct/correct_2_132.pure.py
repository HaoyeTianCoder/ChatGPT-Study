def contains_unique_day(month, possible_birthdays):
    this_month = filter(lambda x: x[0]==month,possible_birthdays)
    days_in_this_month = tuple(map(lambda x: x[1],this_month))
    for i in range(1,31):
        if unique_day(str(i),possible_birthdays) and str(i) in days_in_this_month:
            return True
    return False