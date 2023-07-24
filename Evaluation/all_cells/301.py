# ------------- Best probability Bar chart -----------------#
bestProb_plot <- function(best_A, best_B ){
        names <-c("A", "B")
        prob_list = c(best_A, best_B)
        yy <- barplot(prob_list ,main="Chance of B outperforming A", width = 1, horiz=TRUE,names.arg=names,las=1, 
                xlab = "Percent")
        ## Add text at top of bars
        text(y = yy,  x = prob_list, label = prob_list, pos = 2, cex = 0.8)

}