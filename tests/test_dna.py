from genomics_demo.dna import DNA
import pytest

<<<<<<< HEAD
def test_bad_seq_raises_error():
    with pytest.raises(ValueError):
        DNA('ATB')



def test_complem_seq_works():
    assert DNA('GTC').complimentary_sequence == DNA('CAG')
    assert DNA('ATC').complimentary_sequence == DNA('TAG')

def test_triplet_works():
    assert DNA('GTCAAATTTGGG').check_triplet == DNA('4 codons')

#if __name__=='__main__':      # what's below only active if not called as import module dna
#every funct should start with test_
=======
def test_bad_sequence_raises_error():
    with pytest.raises(ValueError):
        DNA('ATB')

def test_complimentary_sequence_works():
    assert DNA('GTC').complimentary_sequence == DNA('CAG')
    assert DNA('ATC').complimentary_sequence == DNA('TAG')
>>>>>>> cf0020488f9a3ca9b1eab6d8eaf3480bc3130a49
