def contains_unique_day(month, possible_birthdays):
    days = ()
    true_false = ()
    for i in possible_birthdays:
        if month == i[0]:
            days += (i[1], )
    for j in days:
        if unique_day(j, possible_birthdays):
            true_false += ('True', )
        else:
            true_false += ('False', )
    if 'True' in true_false:
        return True
    return False