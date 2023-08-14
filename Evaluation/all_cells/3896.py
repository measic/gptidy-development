# Circular plot of insertions in the genome. 
iCol = qual_palette[1]
eCol = qual_palette[9]
nCol = qual_palette[3]
aCol = qual_palette[7]

fig = plt.figure(figsize=(10,10),frameon=False)
ax=fig.add_axes([0,0,1,1], polar=True)

plt.ylim(0,8)

mapped_ins = total_pool_df.pos.notnull()
all_insertions = total_pool_df[mapped_ins].pos.values
bins = range(0, int(all_insertions.max()) + 1000, 1000)

hist, bins = np.histogram(all_insertions, bins=bins)
heights = ((hist/max(hist))*3)+5
ax.vlines(bins, [5]*len(all_insertions),heights, colors=iCol,linewidth=0.5)

mask_essentials = essentiality_df.essentiality == 'essential'
mask_amb = essentiality_df.essentiality == 'ambiguous'
mask_nonessential = essentiality_df.essentiality == 'nonessential'

essentials = essentiality_df[mask_essentials]
essentials_pos = essentials.begin

length = len(essentials)
ax.vlines(essentials_pos, [4.8]*length,[4.3]*length, colors=eCol,linewidth=0.5)
ax.axis('off')


size = [4]*3
dat=np.array([mask_essentials.sum(), mask_amb.sum(), mask_nonessential.sum()])
widths=dat/sum(dat)*2*np.pi
datleft=np.append(0,np.cumsum(widths)[:-1])
ax.bar(left=datleft,width=widths,bottom=0,height=size,color=[eCol,aCol,nCol],
       edgecolor='w', linewidth=1, align="edge")

lw=7
perc=(dat/sum(dat))*100
legend_elements = [matplotlib.lines.Line2D([0], [0], color=iCol, lw=lw, label='Insertions'),
                   matplotlib.lines.Line2D([0], [0], color=eCol, lw=lw, label='Essential Genes: '+str(round(perc[0],2))+'% '+str(dat[0])),
                  matplotlib.lines.Line2D([0], [0], color=aCol, lw=lw, label='Ambiguous genes: '+str(round(perc[1],2))+'% '+str(dat[1])),
                  matplotlib.lines.Line2D([0], [0], color=nCol, lw=lw, label='Nonessential Genes: '+str(round(perc[2],2))+'% '+str(dat[2])),]
ax.legend(handles=legend_elements, handlelength=0.3,loc=[0.4,1.1])

plt.savefig('fig1/fig1B.eps', format='eps', bbox_inches='tight')
plt.show()