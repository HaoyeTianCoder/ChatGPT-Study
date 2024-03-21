def contains_unique_day(month, possible_birthdays):
    relevant_dates= filter(lambda x: x[0] == month, possible_birthdays)
    days = map(lambda x: x[1], relevant_dates)
    times = 0
    for i in days:
        if unique_day(i, possible_birthdays):
            times = times+1
        else:
            continue
    if times==0:
        return False
    else:
        return True 