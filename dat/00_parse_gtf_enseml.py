#19	havana	transcript	3283055	3289179	.	+	.	gene_id "ENSMUSG00000024829"; gene_version "12"; transcript_id "ENSMUST00000139844"; transcript_version "7"; gene_name "Mrpl21"; gene_source "ensembl_havana"; gene_biotype "protein_coding"; transcript_name "Mrpl21-203"; transcript_source "havana"; transcript_biotype "retained_intron"; transcript_support_level "1";
f = open("Mus_musculus.GRCm38.102.gtf","r")
sal = open("temp","w")
for line in f:
	if "gene_id" in line and "transcript_id" in line and "gene_name" in line:
		#getting gene ID
		geneID = line.split("gene_id \"")[1].split("\";")[0]
		#getting transcriptID
		transcriptID = line.split("transcript_id \"")[1].split("\";")[0]
		#if transcriptID not in transcriptIDs:
		#	transcriptIDs.append(transcriptID)
		#getting gene name
		geneName = line.split("gene_name \"")[1].split("\";")[0]
		sal.write(geneID+"\t"+transcriptID+"\t"+geneName+"\n")
		
sal.close()
f.close()
from os import system 
system ("sort -u temp >sorted")
