#set up lists containing calculated rations for plotting 
_ = [earningscost for earningscost in df0_10k_grouped['earnings_cost_ratio']]
_ = [earnings for earnings in df0_10k_grouped['earnings_growth_y6_y10']]
_ = [worthit for worthit in df0_10k_grouped['weighted_growth_to_tuition']]

_ = [earningscost for earningscost in df10_18k_grouped['earnings_cost_ratio']]
_ = [earnings for earnings in df10_18k_grouped['earnings_growth_y6_y10']]
_ = [worthit for worthit in df10_18k_grouped['weighted_growth_to_tuition']]

_ = [earningscost for earningscost in df18_32_grouped['earnings_cost_ratio']]
_ = [earnings for earnings in df18_32_grouped['earnings_growth_y6_y10']]
_ = [worthit for worthit in df18_32_grouped['weighted_growth_to_tuition']]

_ = [earningscost for earningscost in df32_grouped['earnings_cost_ratio']]
_ = [earnings for earnings in df32_grouped['earnings_growth_y6_y10']]
_ = [worthit for worthit in df32_grouped['weighted_growth_to_tuition']]