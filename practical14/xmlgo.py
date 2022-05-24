from xml.dom.minidom import parse
import xml.dom.minidom
from copy import deepcopy
import matplotlib.pyplot as plt
dom = xml.dom.minidom.parse(r'C:\Users\14711\Documents\WeChat Files\wxid_7pstdf75czk932\FileStorage\File\2022-05\go_obo.xml')
root = dom.documentElement
#print(root)

def remove_repetitition(dic):
    dic_edit = deepcopy(dic)
    for i in dic:

        dic_edit[i]= set(dic[i])
    return dic_edit
# this function will be used to remove the repetition of the childnodes in the dictionary value,so the length of the value represents the real number of childnodes


def generation_depth_plus_1(origin_dic):
    for b in origin_dic:
        for c in dictionary_copy[b]:
            if c in origin_dic:
                dictionary_copy[b].extend(origin_dic[c])
    return dictionary_copy
#in this function,  the childnodes will be checked in the one generation depth,only put the child of child into parents' value
term_all = root.getElementsByTagName('term')
#print(len(term_all))
origin_dic = {}
a=0
for term in term_all:#all the keys is a parent node, while values are child nodes
    if term.getElementsByTagName('is_a'):
        termid = term.getElementsByTagName('id')[0].childNodes[0].data
        len1=len(term.getElementsByTagName('is_a'))
        for a in range (len1):
            is_a=term.getElementsByTagName('is_a')[a].childNodes[0].data
            if is_a in origin_dic:
                origin_dic[is_a].append(termid)
            else:
                origin_dic[is_a] = [termid]
            a+=1
    a=0
dictionary_copy=deepcopy(origin_dic)
edit1_dic = generation_depth_plus_1(origin_dic)
edit2_dic=remove_repetitition(edit1_dic)
uncounted = len(term_all)-len(edit2_dic)
length_list=[]

for d in edit2_dic:
    len2=len(edit2_dic[d])
    length_list.append(len2)
#print(len(edit2_dic))
for e in range(uncounted):
    length_list.append(0)
#print(length_list)
id_list=[]
for term in term_all:
    DEFSTR = term.getElementsByTagName('defstr')[0].childNodes[0].data.upper()
    ID = term.getElementsByTagName('id')[0].childNodes[0].data
    if DEFSTR.count('TRANSLATION') >0:
        id_list.append(ID)
no_child_node = 0
id_list_2 = []
id_lenth_list=[]
for f in id_list:
    if f in origin_dic:
        id_list_2.append(edit2_dic[f])
    else:
        no_child_node=no_child_node+1
for g in range(0,no_child_node):
    id_lenth_list.append(0)
for h in id_list_2:
    id_lenth_list.append(len(h))
print('the total number of terms =', len(term_all))
print('mean of childNodes of all terms = ',sum(length_list)/len(length_list))
print('mean of childNodes associated with translation = ',sum(id_lenth_list)/len(id_lenth_list))
plt.boxplot(length_list,patch_artist=False,showfliers=True,showmeans=True,flierprops = {'marker':'o','markerfacecolor':'red','color':'black'})
plt.xlabel('the distribution of childNodes in all terms')
plt.show()
plt.boxplot(id_lenth_list,patch_artist=False,showfliers=True,showmeans=True,flierprops = {'marker':'o','markerfacecolor':'blue','color':'green'})
plt.xlabel('the distribution of childNodes in terms associated with translation')
plt.show()
print('comment:mean of childNodes of overall Gene Ontology is smaller than mean of childNodes associated with translation,')

#print(edit2_dic)












