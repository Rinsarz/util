def create_dates_list(date_from, date_to=None, n_days=None, step = 1):
    if date_to and n_days:
        raise ValueError("Only one argument between date2 and n_days should be specified")
    if n_days and n_days <= 0:
        raise ValueError("n_days should be more than 0")
    elif n_days:
        return [date_from + step/abs(step)* datetime.timedelta(days=x) for x in range(0, n_days, abs(step))]
    elif date_to:
        if date_from > date_to:
            return [date_from - datetime.timedelta(days=x) for x in range(0, (date_from-date_to).days, abs(step))]
        else:
            return [date_from + datetime.timedelta(days=x) for x in range(0, (date_to-date_from).days, abs(step))]
