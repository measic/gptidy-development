'''Plot function for nuclides yield'''

def plot_nuclides(fpy):
    
    from matplotlib import pyplot as plt # import the pyplot function of the matplotlib package
    (fig, ax) = plt.subplots(figsize=(18,7))

    ax.plot(range(len(fpy)), [nc.yield_percent for nc in fpy], 
            '-.',color='black', marker='o',markersize=10)
    
    ax.set_xlabel('Nuclide',fontsize=18)
    ax.set_ylabel(r'Yield [%]',fontsize=18)
    
    plt.xticks(range(0,len(fpy),2),[nc.name for nc in fpy][::2],rotation=70,fontsize=12)

    ax.set_xlim((-1,len(fpy)))
    
    # create a twin y axis to reconfigure the top x axis
    ay1 = ax.twiny()
    ay1.set_xlim(ax.get_xlim())
    #ay1.xaxis.tick_top()
    ay1.set_xticks([])
    ay1.set_xticks(range(1,len(fpy),2),[nc.name for nc in fpy][1::2])
    ay1.set_xticklabels([nc.name for nc in fpy][1::2],minor=True,fontsize=12,rotation=70)

    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    
    plt.title('Cumulative (Decayed) Fission Products (>1% Yield)',fontsize=22)
    ax.grid(True)
    #plt.yscale('log')
    plt.show()

    return