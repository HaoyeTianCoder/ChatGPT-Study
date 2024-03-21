def contains_unique_day(month, possible_birthdays):
    def monthfilter(birthday):
        if birthday[0]==month:
            return True
        else:
            return False
    possible = tuple(filter(monthfilter,possible_birthdays))