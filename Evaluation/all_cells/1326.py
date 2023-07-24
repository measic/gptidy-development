with open('가사.txt', 'rt', encoding='utf8') as f:
    # print(f.read())  # 파일 전체 내용 읽기
#     for line in f.read().splitlines():
#         print(line)
    
    for line in f:
        print('#' + line.strip())  # 좌/우 화이트스페이스 제거