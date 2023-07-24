# Run GO enrichment analysis for each community
comm_enrich_scores = []
for community in communities:
    subset = [gene[0] for gene in membership if gene[1] == community]

    # Exclude communities smaller than 5:
    if len(subset) > 5:
        goea_results = goeaobj.run_study(subset);
        sig_results = [result for result in goea_results if result.p_fdr_bh < 0.05]

        enriched_mem_ratios = []
        for res in sig_results:
            enriched_mem_ratios.append(res.ratio_in_study[0] / res.ratio_in_study[1])

        if len(enriched_mem_ratios):
            avg_enriched_ratio = sum(enriched_mem_ratios) / len(enriched_mem_ratios)
            comm_enrich_scores.append([community, avg_enriched_ratio])