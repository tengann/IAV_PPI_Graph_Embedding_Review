========================================================================================================================
HPIDB: Positive control
Negatome 2.0 (http://mips.helmholtz-muenchen.de/proj/ppi/negatome/) : Negative control
[Downloaded Combined-stringent] ## A combined stringent non-interacting Protein dataset 
========================================================================================================================
1. HPIDB_pos_test_set.csv
Contains 1903 cleaned records (All proteins previously assigned an index in protein_list.csv)
PR8 (1803), Aichi (97), CA04 (3)
************************************************************************************************************************
2. negatome_human-human.csv
Contains 1143 unique Human-Human ProteinInteractions from Negatome 2.0 database 
(All proteins previously assigned an index in protein_list.csv)
************************************************************************************************************************
3. HPIDB_Negatome_testset.csv
Negatome -- All 1143 samples
HPIDB -- CA04 (3), Aichi (97) [All available in HPIDB]
PR8 [Randomly sampled, except PA (111), M1 (30) and PB1-F2 (13)]
# M2 - 112 samples
## Remaining 7 segments [i.e., PB2, PB1, HA, NP, NA, NS1, NS2] - (111 samples each) 
************************************************************************************************************************
4. HPIDB_Negatome_sampled.csv
Negatome -- randomly sampled 
HPIDB -- CA04 (3), Aichi (97) [All available in HPIDB]
PR8 [Randomly sampled, except M1 (30) and PB1-F2 (13)]
# HA, NS2, NP, PA - (33 each)  
# NA, PB2, NS1, PB1 - (34 each)
# M2 - 35
# M1 - 30 [All available in HPIDB]
# PB1-F2 - 13 [All available in HPIDB]
************************************************************************************************************************