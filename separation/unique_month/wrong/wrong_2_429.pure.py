def unique_month(month, possible_birthdays):
    all_month = ()
    repeat_month =()
    for date in possible_birthdays:
        if date[0] not in all_month:
            all_month += (date[0],)
        else:
            repeat_month += (date[0],)
    return month not in repeat_month 