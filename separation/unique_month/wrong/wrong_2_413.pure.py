def unique_month(month, possible_birthdays):
    for dates in possible_birthdays:
        if month in dates:
            return False
        else:
            return True