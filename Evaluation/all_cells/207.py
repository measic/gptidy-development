img[0:100, 0:100] = img[300:400, 400:500]
img[0:100, 100:200] = img[200:300, 300:400]
img[0:100, 200:300] = img[250:350, 350:450]
img[0:100, 300:400] = img[300:400, 400:300:-1]
img[0:100, 400:500] = img[400:300:-1, 300:400]
img[0:100, 500:600] = img[400:300:-1, 400:300:-1]
img[0:100, 600:700] = img[200:400:2, 300:500:2]
img[100:300:2, 0:200:2] = img[300:400, 300:400]
# 貼四個圖形
img[101:300:2, 0:200:2] = img[200:300, 300:400]
img[100:300:2, 1:200:2] = img[300:400, 400:500]
img[101:300:2, 1:200:2] = img[200:300, 400:500]
# 行列互換 hint:(keyword transpose, .T)
img[300:500, 0:200]=np.transpose(img[200:400, 300:500], axes=[1,0,2])
# 旋轉九十度 
img[100:300, 500:700]=img[300:500, 0:200][:, ::-1]
# 綠色的圓圈
img[100:200, 200:300, 1]  = img[300:400, 400:500, 0]
img[100:200, 300:400, :2] = img[300:400, 300:400, :2]
plt.imshow(img, interpolation='bilinear')
