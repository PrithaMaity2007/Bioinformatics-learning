from Bio.Seq import Seq
my_dna = Seq("ATGCGTACGTAGCTAG")
print("DNA Sequence:", my_dna)
print("Complement:", my_dna.complement())
print("Reverse Complement:", my_dna.reverse_complement())
print("Transcription:", my_dna.transcribe())
print("Translation:", my_dna.translate())