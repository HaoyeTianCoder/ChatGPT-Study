def contains_unique_day(month, possible_birthdays):
   birthday = ()
   for i in range(len(possible_birthdays)):
    if possible_birthdays[i][0] == month:
       birthday += possible_birthdays[i]
    for j in range(len(birthday)):
        return unique_day(birthday[i][1], possible_birthdays) 