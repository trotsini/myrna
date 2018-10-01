from genomics_demo.rna import RNA
import pytest

<<<<<<< HEAD
def test_bad_seq_raises_error():
    with pytest.raises(ValueError):
        RNA('TB')



def test_complem_seq_works():
    assert RNA('GUC').complementary_sequence == RNA('CAG')
    assert RNA('AUC').complementary_sequence == RNA('UAG')
=======
def test_bad_sequence_raises_error():
    with pytest.raises(ValueError):
        RNA('ATB')

def test_complimentary_sequence_works():
    assert RNA('GUC').complimentary_sequence == RNA('CAG')
    assert RNA('AUC').complimentary_sequence == RNA('UAG')

def test_reverse_sequence_works():
    assert RNA('GUCA').reverse_sequence == RNA('ACUG')
    assert RNA('ACUG').reverse_sequence == RNA('GUCA')

>>>>>>> cf0020488f9a3ca9b1eab6d8eaf3480bc3130a49
