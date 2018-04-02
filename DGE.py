import argparse, math, xlwt

parser = argparse.ArgumentParser(description='Program to generate gene regulation table')
parser.add_argument("-t","--treated", help="[infile] name of abundance file for treated sample", required=True)
parser.add_argument("-c","--control", help="[infile] name of abundance file for control sample", required=True)
parser.add_argument("-f","--table", help="[outfile] suffix for fpkm table", required=True)
parser.add_argument("-o","--out", help="[outfile] suffix for final out files", required=True)

args = parser.parse_args()

fpkm_dict1, fpkm_dict2 = {}, {}
gene_names1, gene_names2 = [], []
excel_summary = args.out+".xls"
rows, Up, Down, NotExpressed = 0, 0, 0, 0	
sample_name1=str(args.treated.split(".")[0])
sample_name2=str(args.control.split(".")[0])


with open(args.treated) as treated,  open(args.control) as control:

        first_line1 = treated.readline()
        for line in treated:
            line = line.strip().split("\t")
            gene_names1.append(line[0])
            gene_name, fpkm = line[0], line[7]
            fpkm_dict1[gene_name] = fpkm

        first_line2 = control.readline()
        for line in control:
            line = line.strip().split("\t")
            gene_names2.append(line[0])
            gene_name, fpkm = line[0], line[7]
            fpkm_dict2[gene_name] = fpkm

treated.close()
control.close()

all_genes = sorted(list((set(gene_names1) & set(gene_names2))))

known_genes=[x for x in all_genes if not x.startswith('MSTRG')]

with open(args.table + ".txt", 'w') as fpkm_table:
    fpkm_table.write("Gene_name" + "\tFPKM_" + sample_name2 + "\tFPKM_" + sample_name1 + "\n")
    for i in range(len(all_genes)):
        fpkm_table.write(all_genes[i]+"\t"+fpkm_dict2[all_genes[i]]+"\t"+fpkm_dict1[all_genes[i]]+"\n")
fpkm_table.close()


outfile = open((args.out + ".txt"),'w')

with open(args.table + ".txt") as fpkm_table:
    outfile.write("GeneID\tFPKM_" + sample_name2 + "\tFPKM_" + sample_name1 + "\tfold_change\tlog2_foldChange\tRegulation\n")
    for line in fpkm_table:
        if not "Gene" in line:
            if not "MSTRG" in line:               
                line_array = line.rstrip().split("\t")
                fpkm_sum = float(line_array[1]) + float(line_array[2])
                if fpkm_sum != 0:
                    if float(line_array[1]) > 0 and float(line_array[2]) > 0:
                        fold_change = float(line_array[2]) / float(line_array[1])
                        log2foldchange = math.log(fold_change,2)
                        line_array.append(str(fold_change))
                        line_array.append(str(log2foldchange))
                        if log2foldchange > 0: 
                            line_array.append("Upregulated")
                        else:
                            line_array.append("Downregulated")
                        outfile.write("\t".join(line_array[:]) + "\n")
                    else:
                        line_array.extend(["N.A","N.A","N.A"])
                        outfile.write("\t".join(line_array[:]) + "\n")
                else:
                    NotExpressed+=1
                    continue
            line_array=[]

outfile.close()

header_style = xlwt.easyxf('font: name Liberation Sans, bold True; pattern: fore_colour aqua, pattern solid;borders: left thin,right thin, top thin, bottom thin')

content_style = xlwt.easyxf('font: name Liberation Sans; borders: left thin,right thin, top thin, bottom thin')

summary = xlwt.Workbook(encoding="utf-8")
ws = summary.add_sheet('Master')


with open(args.out + ".txt") as outfile:
    for line in outfile:
        if 'Upregulated' in line:
            Up+=1
        if 'Downregulated' in line:
            Down+=1              
        line=line.strip().split("\t")
        for cols in range(0,len(line)):
            if not 'GeneID' in line:
                ws.write(rows, cols, line[cols], content_style)
            else:
                ws.write(rows, cols, line[cols], header_style)
        rows+=1

summary.save(excel_summary)

print "\nKnown genes:\t\t\t" + str(len(known_genes))
print "Upregulated:\t\t\t" + str(Up)
print "Downregulated:\t\t\t" + str(Down)
print "Genes not expressed at all:\t" + str(NotExpressed) + "\n"
