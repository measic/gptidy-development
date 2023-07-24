# Aggregate statistics for the two replicate sequencings of our Hnea library.
print('genome size: %d bp' % genome_size_bp)

print()
print('First replicate TN-Seq Mapping:')

mask = pool_df1.pos.notnull()
insertions_rep1 = pool_df1[mask].pos.values
n_ins_rep1 = len(insertions_rep1)
ins_rate_rep1 = (n_ins_rep1 / genome_size_bp)

print('rep1 number of insertions: %d' % n_ins_rep1)
print('rep1 insertion/bp: %.2f' % ins_rate_rep1)
print('rep1 bp/insertion: %.2f' % (genome_size_bp / n_ins_rep1))
print('Average insertions per gene rep1: %.2f' % rep_df1.inserts.mean())

print()
print('Second replicate TN-Seq Mapping:')

mask = pool_df2.pos.notnull()
insertions_rep2 = pool_df2[mask].pos.values
n_ins_rep2 = len(insertions_rep2)
ins_rate_rep2 = (n_ins_rep2 / genome_size_bp)

print('rep2 number of insertions: %d' % n_ins_rep2)
print('rep2 insertion/bp: %.2f' % ins_rate_rep2)
print('rep2 bp/insertion: %.2f' % (genome_size_bp/n_ins_rep2))

print('Average insertions per gene rep1: %.2f' % rep_df2.inserts.mean())