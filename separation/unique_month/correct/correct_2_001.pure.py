def unique_month(month, possible_birthdays):
    all_months = ()
    for i in possible_birthdays:
        all_months += (i[0],)
    return all_months.count(month) == 1