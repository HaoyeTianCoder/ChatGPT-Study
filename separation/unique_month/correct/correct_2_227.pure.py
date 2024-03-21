def unique_month(month, possible_birthdays):
    a= tuple(filter(lambda birth_month: month == birth_month[0], possible_birthdays))
    return (len(a) ==1) 