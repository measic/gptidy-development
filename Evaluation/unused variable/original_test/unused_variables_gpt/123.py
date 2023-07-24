if __name__=='__main__':
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib
    %matplotlib inline

    x = -Q_training['Ras.Stat']
    y = Q_training['NPM1.3542']
    z = -Q_training['FIBRINOGEN']
    area = Q_training['PCA_Sq_38']*25+75 # 0 to 15 point radiuses
    colors = Q_training['resp.simple']

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel(x.name)
    ax.set_ylabel(y.name)
    ax.set_zlabel(z.name)
    ax.scatter(x, y, z,s=area, c=colors,cmap=matplotlib.cm.coolwarm_r)
    #Blue is 1 and red is 0
    plt.show()