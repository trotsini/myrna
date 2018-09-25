from rna import RNA
import pytest

def test_bad_seq_raises_error():
    with pytest.raises(ValueError):
        RNA('TB')



def test_complem_seq_works():
    assert RNA('GUC').complementary_sequence == RNA('CAG')
    assert RNA('AUC').complementary_sequence == RNA('TAG')