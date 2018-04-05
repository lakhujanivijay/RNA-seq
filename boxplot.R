library(reshape2)
library(ggplot2)
data=read.table("S3_vs_S6.txt", header=T, stringsAsFactors=F)

S3=log((data[,2] + 1),2)
S6=log((data[,3] + 1),2)



a<-data.frame( data$GeneID ,S3, S6, stringsAsFactors=F)
ex <- melt(a, id.vars=c("data.GeneID"))

colnames(ex) <- c("gene","samples","exprs")


ggplot(data=ex, aes(x=samples, y=exprs,fill=samples))+geom_boxplot(outlier.size=0.05,width=0.4, outlier.color="red")+ylab("log2(fpkm+1)") + expand_limits(x=0,y=-0.5) + ggsave("S3_vs_S6.png")
