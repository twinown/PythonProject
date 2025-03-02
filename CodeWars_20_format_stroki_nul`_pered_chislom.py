def make_readable(seconds):
    hours = seconds//3600
    minutes = (seconds-hours*3600)//60
    sex  = seconds - (hours*3600) - (minutes*60)
    return f"{hours:02}:{minutes:02}:{sex:02}"

print(make_readable(60))