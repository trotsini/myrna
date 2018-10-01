<<<<<<< HEAD
complementary_nucleotides = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
=======
complimentary_nucleotides = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
>>>>>>> cf0020488f9a3ca9b1eab6d8eaf3480bc3130a49


class RNA:
    def __init__(self, sequence: str):
        self.sequence = sequence
        if not self._check_validity():
            raise ValueError("Bad sequence. Sequences must only contain G, C, A, and U")

    def __eq__(self, other):
        return True if str(self) == str(other) else False

    def __str__(self):
        return self.sequence

    def __repr__(self):
        return "RNA(sequence='{}')".format(self.sequence)

    def _check_validity(self):
        are_good = (nucleotide.upper() in 'GCAU' for nucleotide in self.sequence)
        return True if all(are_good) else False

    @property
<<<<<<< HEAD
    def complementary_sequence(self):
        return RNA(''.join(complementary_nucleotides[nt.upper()] for nt in self.sequence))
=======
    def complimentary_sequence(self):
        return RNA(''.join(complimentary_nucleotides[nt.upper()] for nt in self.sequence))

    @property
    def reverse_sequence(self):
        return RNA(''.join(reversed(self.sequence)))

>>>>>>> cf0020488f9a3ca9b1eab6d8eaf3480bc3130a49


