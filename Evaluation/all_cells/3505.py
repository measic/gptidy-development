def args_func(arg1, *args):
    print("Formal arg:", arg1)
    for a in args:
        print("additioanl arg:", a)

args_func(1, "two", 3, [1, 2, 3])