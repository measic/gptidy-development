# Create connection
conn = psycopg2.connect(database="vir_mirna", user="wkg", 
                        password="apples", host="localhost")

# Create cursor
cursor = conn.cursor()

# Query
cursor.execute("SELECT interactor_a_symbol, interactor_a_gene_id "
               "FROM protein_interaction ;")

results = cursor.fetchall()

# Make dict
gene_to_symbol = dict(results)

# Query - I want to query both interactors for my conversion dict
# to ensure that I am not missing anything
cursor.execute("SELECT interactor_b_symbol, interactor_b_gene_id "
               "FROM protein_interaction ;")

results = cursor.fetchall()

# Update dict
gene_to_symbol.update(dict(results))