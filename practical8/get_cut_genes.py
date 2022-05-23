import re


allsequence = open(r"C:\Users\14711\Downloads\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", 'r')
all_sequence = allsequence.read()
#open the fasta file(model:read)
edit_1 = re.sub(r'\n','',all_sequence)
edit_2 = re.sub(r'\r','',edit_1)
#delete all the LF and CR, avoid "GAATTC" sequence being ignored
split_sequence = re.split('(>)',edit_2)
#split by '>'
list_1 = []
#creat a list to put sequence with"GAATTC" into it
counts = len(split_sequence)
for i in range (0,counts):
    if 'GAATTC' in split_sequence[i]:
        list_1.append(split_sequence[i])
#use a loop to select the aim sequences
new_file = open('cut_genes.fa','w+')
#creat a new file to write

for b in range(0,len(list_1)):#create a loop
    add_1 = re.findall(r'gene:.+?\s',list_1[b])
    # extract the gene name
    edit_3 = re.sub(r'.+]', '', list_1[b])
    length_gene = str(len(edit_3))
    #delete every words except for the gene to calculate the length
    str_add_1= ''.join(add_1)#change name into string
    new_file.write(str_add_1)
    new_file.write(length_gene)
    new_file.write('\n')#add CR
new_file.close()

