#genomics demo workshop
THis is a module with demo functions related to genomics from a Python workshop

##Instalation
```
pip install git+https://github.com/trotsini/myrna/tree/irindemo/genomics_demo
```


##Usage

``python
from genomics_demo import DNA
dna_strand = DNA('AGTCAG') # Make a valid DNA seq
dna_strand.complementary_sequence  #outputs a complement
```