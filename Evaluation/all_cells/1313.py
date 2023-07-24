s = '가나다라마바사아자차카타파하'         # str타입 (유니코드)
utf8_string = s.encode('utf8')

f = open('utf8_string.txt', 'wb')  # write + binary
f.write(utf8_string)
f.close()