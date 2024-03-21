def contains_unique_day(month, possible_birthdays):
    tuple_with_unique_day=filter(lambda x:unique_day(x[1],possible_birthdays)==True,possible_birthdays)
    month_with_unique_day=map(lambda x:x[0],tuple_with_unique_day)
    return month in month_with_unique_day