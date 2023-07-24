# train_data_1s.T.shape
#print("-----LDA-----")
#print("Bias:",b,"W:",w)
re = IRLS(train_data_1s)
print("-----LR-----")
print("Bias:",re[0])
print("Weight:",re[1:])
acc, miss = accuracy(c1.test, c2.test, re[1:], re[0 ], 0.5)
print("Accuracy", acc)

#---PLOT---
_x,_y = gen_line_vec(test_data, re[1:], re[0], 0.5)
f4 = plt.figure(4,figsize=(8,8))
f4.clf()
ax4 = f4.add_subplot(111)
ax4.scatter(c1.test[:,0], c1.test[:,1], label="Class +1")
ax4.scatter(c2.test[:,0], c2.test[:,1], label="Class -1")
ax4.scatter(miss[:,0],miss[:,1], label="Misclassificated", c="yellow")
ax4.plot(_x, _y, label='LR divider')
ax4.legend()
ax4.set_title("Fig 4. Classification accuracy(LR)")
plt.show()

# exit()