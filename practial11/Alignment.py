import pandas as pd

DLX5_MOUSE = 'MTGVFDRRVPSIRSGDFQAPFPTSAAMHHPSQESPTLPESSATDSDYYSPAGAAPHGYCSPTSASYGKALNPYQYQYHGVNGSAAGYPAKAYADYGYASPYHQYGGAYNRVPSATSQPEKEVAEPEVRMVNGKPKKVRKPRTIYSSFQLAALQRRFQKTQYLALPERAELAASLGLTQTQVKIWFQNKRSKIKKIMKNGEMPPEHSPSSSDPMACNSPQSPAVWEPQGSSRSLSHHPHAHPPTSNQSPASSYLENSASWYPSAASSINSHLPPPGSLQHPLALASGTLY'
RandomSeq  = 'GDYHNIYEMQSTDNDVIIVLCESYWQNRYWCGYKQNCIFEDSSLFAPSEVDWAVNGYPPYRAVNMHKYEYDYATPTPQKMMWWHLPIWSWHFWGWNIRTWDILTNSGNTMGFCYCAWVCNLPCMILCHARFAFSTDKKPFSVHTFIIKICHTQPALAVTEPNADSCCMIFPLIGKSYCHTCGTWDFYPNEVKYQFNFSAATQYENVIYIFHHICQDVRRGCTDIELNHFWMSHHVANRKLENIVGYRAILRFIGSKCAQNMRSLFAHPWQSFQDHKEYDWHGNLGLNWP'
DLX5_HUMAN = 'MTGVFDRRVPSIRSGDFQAPFQTSAAMHHPSQESPTLPESSATDSDYYSPTGGAPHGYCSPTSASYGKALNPYQYQYHGVNGSAGSYPAKAYADYSYASSYHQYGGAYNRVPSATNQPEKEVTEPEVRMVNGKPKKVRKPRTIYSSFQLAALQRRFQKTQYLALPERAELAASLGLTQTQVKIWFQNKRSKIKKIMKNGEMPPEHSPSSSDPMACNSPQSPAVWEPQGSSRSLSHHPHAHPPTSNQSPASSYLENSASWYTSAASSINSHLPPPGSLQHPLALASGTLY'
blosum = pd.read_excel(r'C:\Users\14711\Downloads\BLOSUM.xlsx%3FglobalNavigation=false.xlsx') #read the sequences of Mouse,human, random sequence and BLOSUM matrix
order="ARNDCQEGHILKMFPSTWYVBZX"
def cal_score(DLX5_HUMAN,DLX5_MOUSE): #define a function to calculate the score
    list_1 = list(DLX5_HUMAN) #put the protein sequence into the list
    list_2 = list(DLX5_MOUSE)
    i=0
    score_sum=0
    for i in range (0,len(list_1)):
        A=order.find(list_1[i])#transform the letter to an int
        B=order.find(list_2[i])
        i=i+1
        score = blosum.iloc[A , B + 1]
        score_sum=score_sum+score
    return score_sum
print('score1 =',cal_score(DLX5_HUMAN,DLX5_MOUSE))
print('score2 =',cal_score(DLX5_HUMAN,RandomSeq))
print('score3 =',cal_score(DLX5_MOUSE,RandomSeq))

def aliment(seq1,seq2): #define a function to calculate the distance
    edit_distance=0
    for i in range(0,len(seq1)):
        if seq1[i]!=seq2[i]:#if the protein is different,add a distance
            edit_distance+=1
    return edit_distance
print('distance =',aliment(DLX5_HUMAN,DLX5_MOUSE),'rate =',1-aliment(DLX5_HUMAN,DLX5_MOUSE)/len(DLX5_HUMAN))
print('distance =',aliment(DLX5_HUMAN,RandomSeq),'rate =',1-aliment(DLX5_HUMAN,RandomSeq)/len(DLX5_HUMAN))
print('distance =',aliment(DLX5_MOUSE,RandomSeq),'rate =',1-aliment(DLX5_MOUSE,RandomSeq)/len(DLX5_HUMAN))