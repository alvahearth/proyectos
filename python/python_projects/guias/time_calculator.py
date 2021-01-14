def add_time(start, duration,day):
    x = start.split(":")
    start_hour = int(x[0])
    start_minutes = int(x[1].split(" ")[0])
    am_pm = x[1].split(" ")[1]
    
    y = duration.split(":")
    duration_hour = int(y[0])
    duration_minutes = int(y[1])
    
    days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    if day in days:
        x = day
    else:
        x = ""
    
    new_minutes = duration_minutes + start_minutes
    new_hour = start_hour + duration_hour
    if new_minutes >= 60:
        if new_hour >= 12:
            new_hour = (new_hour + 1) - 12
            if am_pm is "PM":
                am_pm = "AM"
            else:
                am_pm = "PM"
        if new_hour < 12:
            new_hour = (new_hour + 1)
            if am_pm is "PM":
                am_pm = "AM"
            else:
                am_pm = "PM"
        new_minutes = new_minutes - 60
        if new_minutes < 10:
            new_minutes = "0" + str(new_minutes)
    new_time = (str(new_hour)+":"+str(new_minutes))
    print(str(new_time)+" "+str(am_pm)+","+str(x))
    return new_time



add_time("10:43 PM","1:20","tuesday")