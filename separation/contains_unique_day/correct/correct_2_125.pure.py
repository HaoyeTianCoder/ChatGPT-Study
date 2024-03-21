def contains_unique_day(month, possible_birthdays):
    month_collection = ()
    outside_month_collection = ()
    for element in possible_birthdays:
        if element[0] == month:
            month_collection += (element, )
        else:
            outside_month_collection += (element, )
    for days in month_collection:
        count = 0
        for dates in outside_month_collection:
            if days[1] == dates[1]:
                count += 1
        if count == 0:
            return True
    return False