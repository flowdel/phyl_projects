
# coding: utf-8

# In[1]:

import re
from Bio import SeqIO


# In[ ]:

gff_file = open('/Volumes/Element/BI/proj4/tiho.gff', 'r')

# create one string
string = ''
for i in gff_file:
    string = string+i
string = string.replace('[', '{')
string = string.replace(']', '}')

# find all protein sequences
match = re.findall("{[^}]+}", string)

proteins = []
for prot in match:
    prot = prot.replace('\n# ', '')
    prot = prot.replace('{', '')
    prot = prot.replace('}', '')
    proteins.append(prot)

gff_file.close()


# In[57]:

len(proteins)


# In[56]:

# write fasta file with proteins
w = open('/Users/Adele/Documents/proteins.fasta', 'w')
i = 0
for prot in proteins:
    i+=1
    w.write('>')
    w.write(str(i))
    w.write(' protein')
    w.write('\n')
    w.write(prot)
    w.write('\n')
w.close()


# In[73]:

# search peptides in proteins
proteins = SeqIO.parse('/Volumes/Element/BI/proj4/proteins.fasta', 'fasta')
peptides = SeqIO.parse('/Volumes/Element/BI/proj4/peptides.fa', 'fasta')
proteins_seq = [i.seq for i in proteins]
peptides_seq = [i.seq for i in peptides]
found_proteins = []
for i in peptides_seq:
    for j in proteins_seq:
        a = j.find(i)
        if a != -1 and j not in found_proteins:
            found_proteins.append(j)


# In[90]:

# write proteins in which we've found peptides
w = open('/Users/Adele/Documents/needed_proteins.fasta', 'w')
i = 0
for j in found_proteins:
    i+=1
    w.write('>')
    w.write(str(i))
    w.write(' needed protein')
    w.write('\n')
    w.write(str(j))
    w.write('\n')
w.close()

