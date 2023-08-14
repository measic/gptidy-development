image_url = 'http://cfile7.uf.tistory.com/image/26117F3E581EA5550BDC79'

image_data = requests.get(image_url).content

# f = open('twice.jpg', 'wb')
# f.write(image_data)
# f.close()

# open('twice.jpg', 'wb').write(image_data)