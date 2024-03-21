def contains_unique_day(month, possible_birthdays):
    daysinmonth =()
    for i in possible_birthdays:
        if month in i:
            daysinmonth += (i[1],)
    for j in daysinmonth:
        if unique_day(j, possible_birthdays):
            return True   
    return False 