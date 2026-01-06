def add_time(start, duration, start_day=None):
    # ----- parse start time -----
    time_part, period = start.split()
    start_hour, start_min = map(int, time_part.split(':'))

    # convert start to 24-hour “absolute minutes”
    if period == "PM" and start_hour != 12:
        start_hour += 12
    if period == "AM" and start_hour == 12:
        start_hour = 0
    start_total_minutes = start_hour * 60 + start_min

    # ----- parse duration -----
    dur_hour, dur_min = map(int, duration.split(':'))
    dur_total_minutes = dur_hour * 60 + dur_min

    # ----- add and compute days passed -----
    end_total_minutes = start_total_minutes + dur_total_minutes
    days_later = end_total_minutes // (24 * 60)
    end_total_minutes = end_total_minutes % (24 * 60)

    # back to hour/min and AM/PM
    end_hour_24 = end_total_minutes // 60
    end_min = end_total_minutes % 60

    if end_hour_24 == 0:
        end_hour = 12
        end_period = "AM"
    elif 1 <= end_hour_24 < 12:
        end_hour = end_hour_24
        end_period = "AM"
    elif end_hour_24 == 12:
        end_hour = 12
        end_period = "PM"
    else:  # 13–23
        end_hour = end_hour_24 - 12
        end_period = "PM"

    # ----- build base result (time) -----
    new_time = f"{end_hour}:{end_min:02d} {end_period}"

    # ----- handle day of week if provided -----
    if start_day:
        days = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
        start_day_index = days.index(start_day.capitalize())
        end_day_index = (start_day_index + days_later) % 7
        end_day = days[end_day_index]
        new_time += f", {end_day}"

    # ----- append day-later info -----
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time
