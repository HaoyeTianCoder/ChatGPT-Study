def contains_unique_day(month, possible_birthdays):
    month_dates=filter_1(lambda x:True if x[0]==month else False, possible_birthdays)
    for date in month_dates:
        if unique_day(date[1],possible_birthdays):
            return True
        else:
            continue
    else:
        return False