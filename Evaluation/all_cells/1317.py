# FileNotFoundError -> IOError 계열

# try:
#     f = open('utf8_string.txt', 'rt', encoding='utf8')
#     print(f.read())
#     1/0
# except IOError:
#     print('파일을 찾을 수 없습니다.')
# finally:
#     print('close 합니다.')
#     f.close()

try:
    with open('utf8_string.txt', 'rt', encoding='utf8') as f:
        print(f.read())
        1/0
except IOError:
    print('파일을 찾을 수 없습니다.')