assert is_valid_url("http://www.google.com/search?q=fuzzing")
assert not is_valid_url("xyzzy")