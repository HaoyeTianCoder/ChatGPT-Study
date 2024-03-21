def unique_month(month, possible_birthdays):
    only_month = ()
    for i in possible_birthdays:
        if month in i:
            only_month = only_month + (i,)
    if len(only_month) == 1:
        return True
    else:
            return False