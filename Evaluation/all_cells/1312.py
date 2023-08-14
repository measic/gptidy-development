f = open('utf8_string.txt', 'rb')  # read + binary
utf8_string = f.read()
f.close()

utf8_string.decode('utf8')  # utf8 -> unicode