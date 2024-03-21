def contains_unique_day(month, possible_birthdays):
    tup_month_1 = ()
    tup_month_2 = ()
    for i in possible_birthdays:
        if month == i[0]:
            tup_month_1 = tup_month_1 + (i,)
        else:
            tup_month_2 = tup_month_2 + (i[1],)
    for j in tup_month_1:
        day = j[1]
        if day in tup_month_2:
            continue
        elif day not in tup_month_2:
            return True
    else:
        return False