# Read in membership data and convert to symbols to gene IDs
membership = []
with open("./data/protein_community_membership.csv", "r") as fp:
    for line in fp:
        if not line.startswith("symbol"):
            line = line.strip("\n")
            line = line.split(",")
            
            if gene_to_symbol[line[0]] is not None:
                membership.append([gene_to_symbol[line[0]], int(line[1])])

# Extract community IDs
communities = [comm[1] for comm in membership]
# Remove duplicates
communities = list(dict.fromkeys(communities))