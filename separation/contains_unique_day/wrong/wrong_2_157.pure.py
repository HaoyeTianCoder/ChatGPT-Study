def contains_unique_day(month, possible_birthdays):
    date=()
    for mon in possible_birthdays:
        if month ==mon[0]:
            date+=(mon,)
        else:
            date=date
    days=()
    for day in date:
        days+=(day[1],)
    y=()
    for x in days:
        if unique_day(x, possible_birthdays)==True:
            y+=(x,)
        else:
            y=y
    if y==():
        return False
    else:
        return True 