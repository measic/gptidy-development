def function_def():
    try:
        10 / 0
    except ZeroDivisionError:
        print('Oops, invalid.')
    else:
        pass
    finally:
        print("We're done with that.")
function_def()