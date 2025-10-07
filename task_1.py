def total_minutes(time_str):
    time_lst = time_str.replace(' ', ',').split(',')
    total_minutes = 0
    for time in time_lst:
        if 'h' in time:
            total_minutes += int(time[:-1]) * 60
        elif 'm' in time:
            total_minutes += int(time[:-1])
        else:
            total_minutes += int(time[:-1]) // 60
    return total_minutes

test_str = '1h 45m,360s,25m,30m 120s,2h 60s'
total_minutes_result = total_minutes(test_str)
print(total_minutes_result)