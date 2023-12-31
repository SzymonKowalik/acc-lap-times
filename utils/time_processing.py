import re
from datetime import datetime as dt


def to_date(text):
    return dt.strptime(text, '%d.%m.%Y').date()


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


def time_to_txt(time, as_diff=False):
    if time == '-':
        return time
    if as_diff:
        sign = '+' if time < 0 else '-'
    time = abs(time)
    m, s = divmod(time, 60)
    print(m, s)
    if m < 60:
        if as_diff:
            return f"{sign}{int(m)}:{s:0>4.1f}"
        return f"{int(m)}:{s:0>4.1f}"
    else:
        h, m = divmod(m, 60)
        if as_diff:
            return f"{sign}{int(h)}:{int(m):0>2}:{s:0>4.1f}"
        return f"{int(h)}:{int(m):0>2}:{s:0>4.1f}"
