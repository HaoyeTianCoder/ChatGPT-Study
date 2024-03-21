def unique_month(month, possible_birthdays):
    flat_possible_birthdays=enumerate_tree(possible_birthdays)
    if flat_possible_birthdays.count(month) == 1:
        return True
    else:
        return False