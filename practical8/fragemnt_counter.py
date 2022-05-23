import re

seq = 'ATGCAATCGACTACGATCAATCGAGGGCC'
fragments=re.findall(r'GAATTC',seq)
print(len(fragments)+1) # extract all the string 'GAATTC' in seq , and count the extracted strings(to find how many fragments,plus one)




