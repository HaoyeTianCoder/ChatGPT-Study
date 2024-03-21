def contains_unique_day(month, possible_birthdays):
    counter = 0
    revised_list = keep_month(month,possible_birthdays)
    for i in revised_list:
        if unique_day(i[1], possible_birthdays) == True:
            return True
    return False 