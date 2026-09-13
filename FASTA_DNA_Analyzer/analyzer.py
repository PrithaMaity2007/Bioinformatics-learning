from Bio import SeqIO
from Bio.Seq import Seq
import csv
input_file = "sample.fasta"
output_file = "results.csv"
results = []
for record in SeqIO.parse(input_file, "fasta"):
    seq = record.seq
    name = record.id

    complement = seq.complement()
    reverse_complement = seq.reverse_complement()
    transcription = seq.transcribe()

    trim_length = len(seq) - (len(seq) % 3)
    translation = seq[:trim_length].translate()

    gc_content = seq.count("G") + seq.count("C")
    gc_content = round(gc_content/len(seq) * 100, 2)

    print(f"\n---{name}---")
    print("sequence:", seq)

    results.append([name, str(seq), str(complement), ...])

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Sequence", "Complement", "Reverse_Complement", "Transcription","Translation", "GC_Content(%)"])
        writer.writerows(results)
