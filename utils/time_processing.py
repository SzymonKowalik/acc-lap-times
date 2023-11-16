import re


def txt_to_time(text):
    if text == '-':
        return text
    if text.count(':') == 1:
        m, s = re.split(r':', text)
        time_in_s = (float(m) * 60) + float(s)
    else:
        h, m, s = re.split(r':', text)
        time_in_s = (float(h) * 3600) + (float(m) * 60) + float(s)
    return time_in_s


def time_to_txt(time):
    if time == '-':
        return time
    m, s = divmod(time, 60)
    if m < 60:
        return f"{int(m)}:{s:0>4.1f}"
    else:
        h, m = divmod(m, 60)
        return f"{int(h)}:{int(m):0>2}:{s:0>4.1f}"
