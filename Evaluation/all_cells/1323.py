# 메모장을 여시고, 메모장에서 "가나다라마바사아자차카타파하" 를 입력하고,
# c:\dev 디렉토리에 저장

f = open('메모장.txt', 'rb')
data = f.read()
f.close()

data.decode('???')  # utf8, cp949