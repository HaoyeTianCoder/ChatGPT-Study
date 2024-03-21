def unique_day(day, possible_birthdays):
    count = 0
    for month_day in possible_birthdays:
        date = month_day[1]
        if day == date:
            count+= 1
    return count == 1