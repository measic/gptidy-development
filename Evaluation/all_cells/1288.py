#set up lists containing calculated rations for plotting 
earningscost10k = [earningscost for earningscost in df0_10k_grouped['earnings_cost_ratio']]
earningsgrowth10k = [earnings for earnings in df0_10k_grouped['earnings_growth_y6_y10']]
weighted_growth10k = [worthit for worthit in df0_10k_grouped['weighted_growth_to_tuition']]

earningscost10k_18k = [earningscost for earningscost in df10_18k_grouped['earnings_cost_ratio']]
earningsgrowth10k_18k = [earnings for earnings in df10_18k_grouped['earnings_growth_y6_y10']]
weighted_growth10k_18k = [worthit for worthit in df10_18k_grouped['weighted_growth_to_tuition']]

earningscost18k_32k = [earningscost for earningscost in df18_32_grouped['earnings_cost_ratio']]
earningsgrowth18k_32k = [earnings for earnings in df18_32_grouped['earnings_growth_y6_y10']]
weighted_growth18k_32k = [worthit for worthit in df18_32_grouped['weighted_growth_to_tuition']]

earningscost32k = [earningscost for earningscost in df32_grouped['earnings_cost_ratio']]
earningsgrowth32kk = [earnings for earnings in df32_grouped['earnings_growth_y6_y10']]
weighted_growth32k = [worthit for worthit in df32_grouped['weighted_growth_to_tuition']]