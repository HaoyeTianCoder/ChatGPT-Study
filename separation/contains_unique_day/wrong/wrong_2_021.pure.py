def contains_unique_day(month, possible_birthdays):
    def contains_month(month, elem):
        return month == elem[0]
    pos_bd_containing_month = tuple(filter(lambda x: contains_month(month, x), possible_birthdays))
    for element in pos_bd_containing_month:
        if unique_day(element[1], possible_birthdays) == True:
            return True
    return False