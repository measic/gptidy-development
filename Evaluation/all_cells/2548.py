%%writefile SSAnova.R

rawRTData <- read.csv('SS_ANOVA_RT.csv')
install.packages("psych",repos='https://mirrors.nics.utk.edu/cran/')
install.packages("ez",repos='https://mirrors.nics.utk.edu/cran/')
library(psych)
library(ez)

rawRTData$subject = as.factor(rawRTData$subject)
rawRTData$run = as.factor(rawRTData$run)
rawRTData$trialtype = as.factor(rawRTData$trialtype)

SS_RT_runANOVA <- ezANOVA(data=as.data.frame(rawRTData),
                                  dv=rt,
                                  wid=subject,
                                  within=.(run, trialtype),
                                  detailed=TRUE)
print(SS_RT_runANOVA)

rawACCData <- read.csv('SS_ANOVA_ACC.csv')

rawACCData$subject = as.factor(rawACCData$subject)
rawACCData$run = as.factor(rawACCData$run)
rawACCData$trialtype = as.factor(rawACCData$trialtype)

SS_ACC_runANOVA <- ezANOVA(data=as.data.frame(rawACCData),
                                  dv=acc,
                                  wid=subject,
                                  within=.(run, trialtype),
                                  detailed=TRUE)
print(SS_ACC_runANOVA)