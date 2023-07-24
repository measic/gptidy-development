plt.figure(figsize=(12,6))
rv_plot2(theta, omega, alpha, u1_z, 8000, 9000, 
         title1='knee flexion (up single stair)', title2='thigh (up single stair)', 
         redrange=[8625, 8725])

plt.figure(figsize=(12,6))
rv_plot2(theta, omega, alpha, u1_z, 22000, 23000, 
         title1='knee flexion (down single stair)', title2='thigh (down single stair)', 
         redrange=[22010, 22100])

plt.figure(figsize=(12,6))
rv_plot2(theta, omega, alpha, u1_z, 56000, 58000,
        title1='knee flexion (up double stair)', title2='thigh (up double stair)', 
        redrange=[56625, 56700])

plt.figure(figsize=(12,6))
rv_plot2(theta, omega, alpha, u1_z, 66000, 68000,
        title1='knee flexion (down double stair)', title2='thigh (down double stair)', 
        redrange=[66475, 66530])