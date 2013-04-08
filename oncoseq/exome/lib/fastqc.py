'''
Created on Nov 2, 2011

@author: mkiyer
'''

SANGER_ENCODING = "Sanger / Illumina 1.9"
SOLEXA_ENCODING = "Illumina < 1.3"
ILLUMINA_13_ENCODING = "Illumina 1.3"
ILLUMINA_15_ENCODING = "Illumina 1.5"

ENCODING_VALUES = (SANGER_ENCODING, 
                   SOLEXA_ENCODING, 
                   ILLUMINA_13_ENCODING, 
                   ILLUMINA_15_ENCODING)
ENCODING_TO_QUAL_FORMAT = {SANGER_ENCODING: "sanger",
                           SOLEXA_ENCODING: "solexa",
                           ILLUMINA_13_ENCODING: "illumina",
                           ILLUMINA_15_ENCODING: "illumina"}

def get_most_common_read_length(fastqc_data_file):
    fileh = open(fastqc_data_file)
    for line in fileh:
        if line.startswith(">>Sequence Length Distribution"):
            break
    fileh.next()
    most_common_length = None
    most_common_count = 0
    for line in fileh:
        fields = line.strip().split('\t')
        length = int(fields[0])
        count = float(fields[1])
        if (count >= most_common_count):
            most_common_length = length
            most_common_count = count
    fileh.close()
    return most_common_length

def get_total_reads(fastqc_data_file):
    for line in open(fastqc_data_file):
        if not line: continue
        line = line.strip()
        if line.startswith("Total Sequences"):
            return int(line.split()[-1])

def get_fastq_encoding(fastqc_data_file):
    for line in open(fastqc_data_file):
        if not line: continue
        line = line.strip()
        if line.startswith("Encoding"):
            return line.split("\t")[-1]