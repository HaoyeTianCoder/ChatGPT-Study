def unique_month(month, possible_birthdays):
    months = ()
    for all_months in possible_birthdays:
        months = months + (all_months[0],)
        i = 0
        for all_months in months:
            if all_months == month:
                i = i+1
    if i == 1:
        return True
    else:
        return False