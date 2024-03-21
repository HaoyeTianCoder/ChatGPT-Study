def contains_unique_day(month, possible_birthdays):
    month_tuple=()
    for birthday in possible_birthdays:
        if month==birthday[0]:
            month_tuple+=(birthday,)
        else:
            continue
    for day in month_tuple:
        if unique_day(day[1], possible_birthdays)== True :
            return True
    return False