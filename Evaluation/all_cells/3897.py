# Making Panel B

fig,ax = plt.subplots(figsize=(10,10), frameon=False)

plt.ylim(0,0.8)
ys = [0.2,0.4,0.6]
regions = [(0, 8000+500),
           (348299-3000, 350747+3000),
           (428269-6850, 430257)]
essentiality_colors = {
    'essential': qual_palette[9],
    'nonessential': qual_palette[3],
    'ambiguous': qual_palette[7]}
short_names = {
    'HNEAP_RS00015': 'dnaA', 
    'HNEAP_RS00020': 'DNAP III $\\beta$',
    'HNEAP_RS00025': 'recF',
    'HNEAP_RS00030': 'topoisomerase',
    'HNEAP_RS00035': 'lemA', 
    'HNEAP_RS00040': 'unk.',
    'HNEAP_RS01690': '30S',
    'HNEAP_RS01695': '50S',
    'HNEAP_RS01700': '50S',
    'HNEAP_RS01705': 'secY',
    'HNEAP_RS01710': '30S',
    'HNEAP_RS01715': '30S',
    'HNEAP_RS01720': '30S',
    'HNEAP_RS01725': 'RNAP $\\alpha$',
    'HNEAP_RS01730': '50S',
    'HNEAP_RS01735': 'unk.',
    'HNEAP_RS01740': 'uvrB',
    'HNEAP_RS02010': 'poly-P-ase',
    'HNEAP_RS02015': 'fba',
    'HNEAP_RS02020': 'pyk',
    'HNEAP_RS02025': 'pgk',
    'HNEAP_RS02030': 'gapdh',
    'HNEAP_RS02035': 'tkt'
}
insert_color = qual_palette[1]

# Arrow parameters
width = 0.05
headwidth = 0.085
height = 1e-5
head_scale = 0.2
len_per_bp = 1e-4

for y, region in zip(ys, regions):
    region_start, region_end = region
    region_length = region_end - region_start

    genes_in_region = essentiality_df[(essentiality_df.begin >= region_start) & 
                                      (essentiality_df.end <= region_end)]
    insert_in_region = total_pool_df[(total_pool_df.pos >= region_start) & 
                                     (total_pool_df.pos <= region_end)]

    for gene_idx in genes_in_region.index:
        gene = genes_in_region.loc[gene_idx]
        gene_name = short_names[gene.locusId]
        gene_length = gene.length_rep1
        gene_essentiality = essentiality_df.loc[gene_idx].essentiality
        length = gene_length * len_per_bp
        head_length = length*head_scale
        if length > 0.03:
            head_length = 0.03
        c = essentiality_colors[gene_essentiality]
        
        gene_start = gene.begin
        gene_end = gene.end
        gene_strand = gene.strand

        if gene_strand == '+':
            start = (gene_start - region_start)*len_per_bp
            genePic = matplotlib.patches.FancyArrow(
                start, y, length, 0,
                width=width, length_includes_head=True,
                head_width=headwidth, head_length=head_length, fill=True, facecolor=c)
            ax.add_artist(genePic)
            plt.text(start+length/2, y-0.07, gene_name, ha='center', fontsize=14)
        else:
            start = (gene_end - region_start) * len_per_bp
            genePic = matplotlib.patches.FancyArrow(
                start, y, -length, 0,
                width=width, length_includes_head=True,
                head_width=headwidth,
                head_length=head_length, fill=True,facecolor=c)
            ax.add_artist(genePic)
            plt.text(start-length/2, y-0.07, gene_name, ha='center', fontsize=14)
        print(gene.desc)

    poses = (insert_in_region.pos - region_start) * len_per_bp
    n_positions = len(poses)
    
#     bottoms = [y+height+headwidth/2 + 0.045]*n_positions
#     tops = bottoms + (height*insert_in_region.n_total)
#     plt.vlines(poses, bottoms, tops, colors='k')

    bottoms = np.array([y+height+headwidth/2+0.01]*n_positions)
    tops = bottoms + 0.03
    plt.vlines(poses, tops, bottoms, colors=insert_color, linewidth=0.75)
    
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.tight_layout()

plt.savefig('fig1/fig1C.eps', format='eps', bbox_inches='tight')
plt.show()