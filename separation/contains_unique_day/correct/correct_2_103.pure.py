def contains_unique_day(month, possible_birthdays):
    for x in range(len(days(month, possible_birthdays))):
        if unique_day(days(month, possible_birthdays)[x][1], possible_birthdays):
            return True
        elif unique_day(days(month, possible_birthdays)[len(days(month, possible_birthdays))-1][1], possible_birthdays) == False:
            return False