f = open("sorted","r")
prefix = "mouse"
a = []
for line in f:
	aux = line[:-1].split("\t")
	a.append(aux)
f.close()

#getting geneid and genesymbol
geneid2geneSymbol = []
for data in a:
	if [data[0],data[2]] not in geneid2geneSymbol:
		geneid2geneSymbol.append([data[0],data[2]])

f = open(prefix+"_geneID_geneSymbol","w")
for d in geneid2geneSymbol:
	f.write(d[0]+"\t"+d[1]+"\n")
f.close()

transcript2ensembl = []

for data in a:
	transcript2ensembl.append([data[1],data[0]])
	
f = open(prefix+"_transcript_geneID","w")
for d in transcript2ensembl:
	f.write(d[0]+"\t"+d[1]+"\n")
f.close()

transcript2genesymbol = []
for data in a:
	transcript2genesymbol.append([data[1],data[2]])
	
f = open(prefix+"_transcript_geneSymbol","w")
for d in transcript2genesymbol:
	f.write(d[0]+"\t"+d[1]+"\n")
f.close()

#mouse_geneSymbol_geneID'
geneSymbol2geneID = []
for data in a:
	if [data[2],data[0]] not in geneSymbol2geneID:
		geneSymbol2geneID.append([data[2],data[0]])
	
f = open(prefix+"_geneSymbol_geneID","w")
for d in geneSymbol2geneID:
	f.write(d[0]+"\t"+d[1]+"\n")
	f.write(d[0].lower()+"\t"+d[1].lower()+"\n")
	f.write(d[0].upper()+"\t"+d[1].upper()+"\n")
f.close()
