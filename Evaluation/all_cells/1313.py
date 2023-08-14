s = '가나다라마바사아자차카타파하'         # str타입 (유니코드)

# f = open('utf8_string.txt', 'wb')  # write + binary
# utf8_string = s.encode('utf8')
# f.write(utf8_string)
# f.close()

f = open('utf8_string.txt', 'wt', encoding='utf8')  # write + binary
f.write(s)
f.close()

f = open('utf8_string.txt', 'rt', encoding='utf8')
unicode_string = f.read()
print(unicode_string)   # str타입 (유니코드)
f.close()