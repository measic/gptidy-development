def kwargs_func(arg1, **kwargs):
    print("kwargs is now a dictionary...\nType: %s\nContent: %s\n" % (type(kwargs), kwargs))

    print("Formal arg:", arg1)
    for key in kwargs:
        print("another keyword arg: %s: %s" % (key, kwargs[key]))
    
kwargs_func(arg1=1, myarg2="two", myarg3=3)