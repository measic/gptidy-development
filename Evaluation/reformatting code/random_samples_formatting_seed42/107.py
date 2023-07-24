rangelist = list(range(10))
print(list(rangelist))

for number in rangelist:
    # Check if number is one of
    # the numbers in the tuple.
    if number in [4, 5, 7, 9]:
        # "Break" terminates a for without
        # executing the "else" clause.
        break
    else:
        # "Continue" starts the next iteration
        # of the loop. It's rather useless here,
        # as it's the last statement of the loop.
        print(number)
        continue
else:
    # The "else" clause is optional and is
    # executed only if the loop didn't "break".
    pass # Do nothing