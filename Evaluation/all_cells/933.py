pd.DataFrame(X).shift(1)[:10]
# So shift basically takes the input array and shift them down by specified
# number of rows in the table