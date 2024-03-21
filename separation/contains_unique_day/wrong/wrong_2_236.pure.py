def contains_unique_day(month, possible_birthdays):
    days_in_month = []
    for i in range(len(possible_birthdays)):
        curr_month = possible_birthdays[i][0]
        curr_day = possible_birthdays[i][1]
        if curr_month == month:
            days_in_month.append(curr_day)
    for day in days_in_month:
        if unique_day(day, possible_birthdays):
            return True
    return False