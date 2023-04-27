import pandas as pd
import os, glob
from Bio import SeqIO

import requests
from io import StringIO

def write_fasta():
    ## Concat virus .fasta sequences to single txt file
    proteinList = pd.read_csv('./data/IAV/raw/virus_uniprot.txt', delimiter='\t')
    uniProt_ID_df = proteinList['protein'].drop_duplicates()

    with open('./large_fasta.FASTA', 'w') as w_file:
        for i in uniProt_ID_df.index:
            uniProt_ID = uniProt_ID_df[i] #ID refers to UniProt ID column
            # print(uniProt_ID)
            page = requests.post("https://www.uniprot.org/uniprot/" + uniProt_ID + ".fasta")
            soup = ''.join(page.text)
            seq_records = StringIO(soup)
            pSeq = list(SeqIO.parse(seq_records,'fasta'))
            SeqIO.write(pSeq, w_file, 'fasta')

write_fasta()