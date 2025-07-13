def time_conversion(s):
    # Write your code here
    s = s.split(":")
    hour = s[0]
    mid = (hour == "12")
    if "AM" in s[-1]:                
        if mid:
            hour = "00"        
    else:                
        if not mid:
            hour = int(hour) + 12
    s = [str(hour)] + s[1:]        
    time = ":".join(s)[:-2]
    return time



x = "12:01:00AM"

print()

time_conversion(x)
x = "02:01:00AM"
time_conversion(x)
x = "11:01:00AM"
time_conversion(x)


x = "07:05:45PM"
time_conversion(x)
x = "11:05:45PM"
time_conversion(x)
x = "12:05:45PM"
time_conversion(x)