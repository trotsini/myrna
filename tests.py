from dna import DNA
import pytest

def bad_seq_raises_error():
    with pytest.raises(ValuError):
        DNA('ATB')



def test_complem_seq_works():
    assert DNA('GTC').complimentary_sequence == DNA('CAG')
    assert DNA('ATC').complimentary_sequence == DNA('TAG')

#if __name__=='__main__':      # what's below only active if not called as import module dna