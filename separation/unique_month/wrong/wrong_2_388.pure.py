def unique_month(month, possible_birthdays):
    count = 0
    for month_day in possible_birthdays:
        mont = month_day[0]
        if month == mont:
            count+= 1
    return count == 1