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

file_name=input("Enter the file name")
new_file = open("%s.fa" % file_name, 'w')  # open and write the file
for b in range(0,len(list_1)):#create a loop
    add_1 = re.findall(r'gene:.+?\s',list_1[b])
    fragments = len(re.findall(r'GAATTC', list_1[b]))+1
    edit_3 = re.sub(r'.+]', '', list_1[b])
    new_file.write(str(add_1))
    new_file.write('           ')
    new_file.write(str(fragments))
    new_file.write('\n')
    new_file.write(edit_3)
    new_file.write('\n')
new_file.close