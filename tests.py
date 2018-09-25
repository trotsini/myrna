from dna import DNA

if __name__=='__main__':      # what's below only active if not called as import module dna
    try:
        assert DNA('ATB')
    except ValueError:
        pass
    assert DNA('GTC').complimentary_sequence == DNA('CAG')
    assert DNA('ATC').complimentary_sequence == DNA('TAG')
    assert DNA('ATC').complimentary_sequence == 'TAG'
    print('it worked')
