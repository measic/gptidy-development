plt.figure(figsize=(12,24))

plt.subplot(4, 2, 1)    #パレットを4行2列に分割し，一番左上に以下のプロットを描く
plt.plot(alpha[0:14000], u1_z[0:14000], c='black')
plt.title('thigh (up single stairs)')
plt.xlabel('angle [deg]')
plt.ylabel('angular velocity [deg/sec]')
plt.grid()

plt.subplot(4, 2, 2)
plt.plot(beta[0:14000], u2_z[0:14000],  c='black')
plt.title('lower leg (up single stairs)')
plt.xlabel('angle [deg]')
plt.ylabel('angular velocity [deg/sec]')
plt.grid()

plt.subplot(4, 2, 3)
plt.plot(alpha[14000:28000], u1_z[14000:28000], c='black')
plt.title('thigh (down single stairs)')
plt.xlabel('angle [deg]')
plt.ylabel('angular velocity [deg/sec]')
plt.grid()

plt.subplot(4, 2, 4)
plt.title('lower leg (down single stairs)')
plt.xlabel('angle [deg]')
plt.ylabel('angular velocity [deg/sec]')
plt.plot(beta[14000:28000], u2_z[14000:28000],  c='black')
plt.grid()

plt.subplot(4, 2, 5)
plt.plot(alpha[51000:63000], u1_z[51000:63000], c='black')
plt.title('thigh (up double stairs)')
plt.xlabel('angle [deg]')
plt.ylabel('angular velocity [deg/sec]')
plt.grid()

plt.subplot(4, 2, 6)
plt.plot(beta[51000:63000], u2_z[51000:63000],  c='black')
plt.title('lower leg (up double stairs)')
plt.xlabel('angle [deg]')
plt.ylabel('angular velocity [deg/sec]')
plt.grid()

plt.subplot(4, 2, 7)
plt.plot(alpha[63000:75000], u1_z[63000:75000], c='black')
plt.title('thigh (down double stairs)')
plt.xlabel('angle [deg]')
plt.ylabel('angular velocity [deg/sec]')
plt.grid()

plt.subplot(4, 2, 8)    #パレットを4行2列に分割し，一番右下に以下のプロットを描く
plt.title('lower leg (down double stairs)')
plt.xlabel('angle [deg]')
plt.ylabel('angular velocity [deg/sec]')
plt.plot(beta[63000:75000], u2_z[63000:75000],  c='black')
plt.grid()