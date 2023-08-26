fig = plt.figure(figsize=(16, 5))
ax = fig.add_subplot(121)
ax.axis('off')
ay = fig.add_subplot(122)
ay.axis('off')
P1 = Ps[0]
P2 = Ps[1]
K1 = Ks[0]
K2 = Ks[1]
Rt1 = Rts[0]
Rt2 = Rts[1]
annot1 = Annotations[0][0]
annot2 = Annotations[1][0]
indv_left = annot1[0]
variable_def = annot2[1]
lefthand_left = indv_left[1][0]
lefthand_right = variable_def[1][0]
ax.imshow(X[0, 0])
ax.scatter(lefthand_left[0], lefthand_left[1], color='red')
ay.imshow(X[1, 0])
ay.scatter(lefthand_right[0], lefthand_right[1], color='red')
plt.show()