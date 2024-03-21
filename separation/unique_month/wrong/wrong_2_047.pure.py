def unique_month(month, possible_birthdays):
    month_count = 0
    for i in possible_birthdays:
        if month in i:
            month_count += 1
        if month_count > 1:
            return False
    return True