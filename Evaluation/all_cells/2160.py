import psycopg2
from goatools.obo_parser import GODag
from goatools.associations import read_ncbi_gene2go
from goatools.test_data.genes_NCBI_9606_ProteinCoding import GENEID2NT as gene_id_2_nt
from goatools.go_enrichment import GOEnrichmentStudy