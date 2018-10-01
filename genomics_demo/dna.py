complimentary_nucleotides = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}


class DNA:
    def __init__(self, sequence: str):
        self.sequence = sequence
        if not self._check_validity():
            raise ValueError("Bad sequence. Sequences must only contain G, C, A, and T")

    def __eq__(self, other):
        return True if str(self) == str(other) else False

    def __str__(self):
        return self.sequence

    def __repr__(self):
        return "DNA(sequence='{}')".format(self.sequence)

    def _check_validity(self):
<<<<<<< HEAD
        are_good = (nucleotide.upper() in 'GCAT' for nucleotide in self.sequence)
        return True if all(are_good) else False
=======
        return all(nucleotide in 'GCAT' for nucleotide in self.sequence.upper())
>>>>>>> cf0020488f9a3ca9b1eab6d8eaf3480bc3130a49

    @property
    def complimentary_sequence(self):
        return DNA(''.join(complimentary_nucleotides[nt.upper()] for nt in self.sequence))

<<<<<<< HEAD
    @property
    def check_triplet(self):
        return DNA('{} codons'.format(len(self.sequence)/ 3))


#we ve got a module!
=======
>>>>>>> cf0020488f9a3ca9b1eab6d8eaf3480bc3130a49
