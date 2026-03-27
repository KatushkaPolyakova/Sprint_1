some_time = '1h 45m,360s,25m,30m 120s,2h 60s'.split(",")
total_minutes = 0
for time in some_time:
    time_without_spaces = time.split()
    for time_2 in time_without_spaces:
        if 'h' in time_2:
            total_minutes += int(time_2.replace('h','')) * 60
        if 's' in time_2:
            total_minutes += int(time_2.replace('s','')) // 60
        if 'm' in time_2:
            total_minutes += int(time_2.replace('m',''))
print("Итого минут:" , total_minutes)
