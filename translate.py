#importing libraries

import sys 
import argparse
import time

#defining functions
def done():
	print ("Done (Date: "+str(time.strftime("%y/%m/%d"))+" Time: "+str(time.strftime("%H:%M:%S"))+")")
	exit()


	
if __name__ == "__main__":


	print("\n\n#############################################")
	print("##                                         ##")
	print("##            trasformEnsembl              ##")
	print("##              version 3.0                ##")
	print("##        Data taken from Ensembl          ##")
	print("##          for Human and Mouse            ##")
	print("##              (GRCh38/mm10)              ##")
	print("##                                         ##")
	print("##               Created by                ##")
	print("##     Sebastian Contreras-Riquelme        ##")
	print("##     Search me on github as Cold7        ##")
	print("##        Question or suggestions          ##")
	print("##               write me                  ##")
	print("##  contrerasriquelme.sebastian@gmail.com  ##")
	print("#############################################\n\n")
	
	#checking python version
	if (sys.version_info < (3, 0)):
		print("You are using a python version lower than 3.0. Please use python3 to execute this script. Exiting")
		exit()

	#input
	parser = argparse.ArgumentParser()
	parser.add_argument("-O", "--organism", help="Organism to use. Default: human", default="human", choices=['human','mouse'])
	parser.add_argument("-l", "--list", help="File with geneID/transcriptID/geneSymbol list.", required=True)
	parser.add_argument("-i", "--input_data", help="Input data type. Default: geneID", choices=['geneID','transcriptID','geneSymbol'], default="geneID")
	parser.add_argument("-o", "--output_data", help="Output data type. It can not be equal to input_data. Default: geneSymbol", choices=['geneID','transcriptID','geneSymbol'], default="geneSymbol")
	parser.add_argument("-f","--output_file", help="Output file to save results. Default = ./output", default="./output")
	
	args = parser.parse_args()


	print("Starting translate.py (Date: "+str(time.strftime("%y/%m/%d"))+" Time: "+str(time.strftime("%H:%M:%S"))+") using the following parameters:")
	print("  Organism: "+args.organism)
	print("  List: "+args.list)
	print("  Input Data: "+args.input_data)
	print("  Output Data: "+args.output_data)
	print("  Output File: "+args.output_file)
	print("\n")

	if args.input_data == args.output_data:
		print("Input format can not be the same for Output format. Exiting...")
		done()

	#selecting file to use
	fileToOpen = "./dat/"+args.organism+"_"+args.input_data+"_"+args.output_data
	data = []
	file = open(fileToOpen,"r")
	for line in file:
		dat = line[:-1].split("\t")
		data.append(dat)
	file.close()
	
	List = open(args.list,"r")
	final = []
	notSyn = []
	file = open(args.output_file,"w")
	for line in List:
		if line != "\n":
			gene = line[:-1].split("\t")[0]
			flag = False
			for d in data:
				if d[0] == gene:
					file.write(d[1]+"\t"+gene+"\n")
					flag = True
			if flag == False:
				notSyn.append(gene)
	file.close()
	if len(notSyn) != 0:
		print("  Not found synonyms for the following genes")
		for item in notSyn:
			print("    "+item)
	print("\n\n")
	done()
	

