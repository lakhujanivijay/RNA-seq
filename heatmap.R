library(pheatmap)
data <- read.csv("S3_S6.txt", sep="\t",header=TRUE, stringsAsFactors=F)
rnames <- paste(sprintf("% 20s",data[,1]),"\t",data[,2])
mat_data <- data.matrix(data[,3:ncol(data)])
rownames(mat_data) <- rnames
png("S3_vs_S6.png", width=3100,height=2000, res=315, pointsize=12)
pheatmap(mat_data,color=colorRampPalette(c("red","yellow","grey","blue","green"))(60),cluster_cols=FALSE,fontsize = 8,cellwidth=30,cellheight=8, cluster_rows = TRUE, display_numbers=F)
dev.off()
