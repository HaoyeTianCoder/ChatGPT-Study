def unique_day(day, possible_birthdays):
    flat_possible_birthdays=enumerate_tree(possible_birthdays)
    if flat_possible_birthdays.count(day) == 1:
        return True
    else:
        return False