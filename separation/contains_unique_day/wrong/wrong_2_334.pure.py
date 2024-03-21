def contains_unique_day(month, possible_birthdays):
    month_list = ()
    bday_list = possible_birthdays
    while len(bday_list)>0:
        if bday_list[0][0]==month:
            month_list = month_list + (bday_list[0],)
        bday_list = bday_list[1:]
    while len(month_list)>0:
        if unique_day(month_list[0][1],possible_birthdays):
            return True
        month_list = month_list[1:]
    return False