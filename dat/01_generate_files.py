f = open("sorted","r")
a = []
for line in f:
	aux = line[:-1].split("\t")
	a.append(aux)
f.close()

#getting geneid and genesymbol
geneid2geneSymbol = []
print("a")
for data in a:
	if [data[0],data[2]] not in geneid2geneSymbol:
		geneid2geneSymbol.append([data[0],data[2]])

f = open("human_geneID_geneSymbol","w")
for d in geneid2geneSymbol:
	f.write(d[0]+"\t"+d[1]+"\n")
f.close()

transcript2ensembl = []

for data in a:
	transcript2ensembl.append([data[1],data[0]])
	
f = open("human_transcript_geneID","w")
for d in transcript2ensembl:
	f.write(d[0]+"\t"+d[1]+"\n")
f.close()

transcript2genesymbol = []
print("c")
for data in a:
	transcript2genesymbol.append([data[1],data[2]])
	
f = open("human_transcript_geneSymbol","w")
for d in transcript2genesymbol:
	f.write(d[0]+"\t"+d[1]+"\n")
f.close()
