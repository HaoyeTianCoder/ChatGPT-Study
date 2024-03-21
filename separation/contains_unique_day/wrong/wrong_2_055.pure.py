def contains_unique_day(month, possible_birthdays):
    month_tuple = ()
    for i in range(0,len(possible_birthdays)):
        if possible_birthdays[i][0] == month:
            month_tuple = month_tuple + (possible_birthdays[i][1],)
    for x in month_tuple:
        for i in range(0,len(possible_birthdays)):
            if x == possible_birthdays[i][1]:
                return False
            else:
                return True