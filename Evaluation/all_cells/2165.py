obodag = GODag("./data/go.obo")
geneid2gos = read_ncbi_gene2go("./data/gene2go", taxids=[9606])

goeaobj = GOEnrichmentStudy(
        gene_id_2_nt.keys(), # human protein coding genes
        geneid2gos, # geneid/GO associations
        obodag, # Ontologies
        propagate_counts = False,
        alpha = 0.05, # default significance cut-off
        methods = ['fdr_bh']) # defult multipletest correction method