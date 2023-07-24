# Remember to empty the 'challenge' directory before running this cell.

# Extract frames at 1s intervals -- the clip is 10s long
def frange(start, stop, step=1.):
    i = start
    while i < stop:
        yield i
        i += step

for ts in frange(3., 7.5, .5):
    clip2.save_frame("challenge/frame_" + str(ts) + ".jpg", t=ts)

files = os.listdir("challenge/")