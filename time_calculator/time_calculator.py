def add_time(start, duration, week_day=None):

    # set all initial values
    days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day_count = 0
    day_period = 0

    c = 0 # count value for days_of_week
    if week_day:
        week_day = week_day.lower()
        # matching given day of the week(if exists)
        for match in days_of_week:
            c += 1
            # stop if found
            if match == week_day:
                break

    # get time and day period from first function argument
    time, period = start.split()

    # increase value if given time is in the afternoon
    if period == "PM":
        day_period = 1

    # get integer of values to have it calculated later
    time = [int(time) for time in time.split(':')]
    to_add = [int(to_add) for to_add in duration.split(':')]

    # set list of calculated new time
    expected_time = list()
    expected_time.append(time[0] + to_add[0])
    expected_time.append(time[1] + to_add[1])

    # if there's more minutes than can be, add an hour and reset minutes
    while expected_time[1] > 59:
        expected_time[0] += 1
        expected_time[1] -= 60

    # if there's more hours than can be, change the day period and reset hours
    while expected_time[0] > 11:
        expected_time[0] -= 12
        day_count += 1
        day_period += 1

    # quick maths to get actual day number from 12h system
    day_count = int(day_count / 2 + 0.5)

    # get correct index to the list
    new_day_index = (c + day_count) - 1
    while new_day_index > 6:
        new_day_index -= 7

    # get weekday
    new_day = days_of_week[new_day_index]
    new_day = new_day.capitalize()

    # get day period
    if day_period % 2 == 0:
        day_period = "AM"
    else:
        day_period = "PM"

    # do not count whole day if period changed just from AM to PM
    if day_count == 1 and day_period == "PM":
        day_count = 0

    # correctly format expected time
    if expected_time[0] == 0:
        expected_time[0] = 12

    if len(str(expected_time[1])) < 2:
        expected_time[1] = f"0{expected_time[1]}"

    # different return statements for different cases
    standard_return = f"{expected_time[0]}:{expected_time[1]} {day_period}"
    if week_day:
        standard_return = standard_return + f", {new_day}"

    if day_count > 0:
        if day_count == 1:
            return standard_return + " (next day)"
        else:
            return standard_return +  f" ({day_count} days later)"

    else:
        return standard_return
