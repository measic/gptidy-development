if not(os.path.isdir(''.join((letters_dir)))):
    os.mkdir(''.join((letters_dir)))

for i,e in enumerate(data_chars):
    for j in range(5):
        if not(os.path.isdir(''.join((letters_dir,'/',labels[i][j],'/')))):
            os.mkdir(''.join((letters_dir,'/',labels[i][j],'/')))
        cv2.imwrite(''.join((letters_dir,'/',labels[i][j],'/',str(i),'.png')),e[j])