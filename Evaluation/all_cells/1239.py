# Classify the test data
x_axis, y_axis = gen_line_vec(train_data, w, b, 0)

acc, miss = accuracy(c1.test, c2.test, w, b, 0)

print("-----LDA-----")
# print("The estimate overall mean is", mu_est)
print("The estimate overall covariance is", cov_est)

print("Learned weight w is", w)
print("Learned bias b is", b)

print("The accuracy is", acc)

#---PLOT---
fig2 = plt.figure(2,figsize=(8,8))
fig2.clf()
ax2  = fig2.add_subplot(111)
ax2.scatter(c1.test[:,0], c1.test[:,1], label="Class +1")
ax2.scatter(c2.test[:,0], c2.test[:,1], label="Class -1")
ax2.scatter(miss[:,0], miss[:,1], label="Misclassified",c="yellow")
ax2.plot(x_axis,y_axis,label="LDA Divider")
ax2.legend()
ax2.set_title("Fig 3. Classification accuracy(LDA)")
plt.show()