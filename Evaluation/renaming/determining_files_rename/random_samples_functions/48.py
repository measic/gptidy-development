import datetime

def function_def(start, n, total):
    now = datetime.datetime.now()
    diff = now - start
    secs = (total - n) * 1.0 * diff.seconds / (n + 1)
    ends = now + datetime.timedelta(seconds=secs)
    return ends.strftime('%H:%M:%S')