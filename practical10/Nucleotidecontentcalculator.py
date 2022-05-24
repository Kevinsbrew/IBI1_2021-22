
def dna_cal(DNA_strand): #set a function,parament : DNA_strand
    count_a_or_A=count_t_or_T=count_c_or_C=count_g_or_G=0 #Set the initial value
    for m in  range(len(DNA_strand)):# set a loop to check the whole strand
        if DNA_strand[m]=='a':
            count_a_or_A+=1
        elif DNA_strand[m]=='A':
            count_a_or_A+=1
        elif DNA_strand[m] == 't':
            count_t_or_T+= 1
        elif DNA_strand[m] == 'T':
            count_t_or_T += 1
        elif DNA_strand[m] == 'c':
            count_c_or_C += 1
        elif DNA_strand[m] == 'C':
            count_c_or_C += 1
        elif DNA_strand[m] == 'g':
            count_g_or_G += 1
        elif DNA_strand[m] == 'G':
            count_g_or_G += 1
    frequent_a=count_a_or_A/len(DNA_strand)#calculate the frequency
    frequent_t = count_t_or_T / len(DNA_strand)
    frequent_c = count_c_or_C / len(DNA_strand)
    frequent_g= count_g_or_G / len(DNA_strand)

    return print('frequent of A is',frequent_a,'\n','frequent of T is',frequent_t,'\n','frequent of C is',frequent_c,'\n','frequent of G is',frequent_g)

seq='accGTaAc'#example1
dna_cal(seq)


DNA_strand=input("please enter a dna strand:")#example2 ^o^
dna_cal(DNA_strand)


