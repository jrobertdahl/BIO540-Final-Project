Steps to reproduce:

Python3 is required to run the main script.

For the required data preprocessing, you will need to install breseq (bowtie2 and R are required dependencies). The commands included in this file assume the breseq and gdtools binaries are located in ~/breseq/bin. If breseq is installed in a different location, be sure to adjust the path accordingly.

Download the REL606 GenBank file. Copy the genomic sequence out of the GenBank file and save it into a .txt file. This will be used for order_index.py.

Use NCBI's Run Browser to search for the SRA Run Accessions listed below. Download the fastq from the FASTA/FASTQ Download tab.

Next, follow these steps to generate the plain text genome sequence file needed for the order_index.py algorithm:

./breseq/bin/breseq -r path/to/REL606.gbk -j 8 path/to/downloaded/fastq/XXXXXXXXX-YYK.fastq.gz -o path/to/desired/output/location/XXXXXXXXX-YYK

Replace the XXXXXXXXX with the SRR ID, and the YY with the generation number (which is in thousands). Example: SRR098027-33k 

This can take a while and range from several minutes to nearly an hour.

The output file from the previous process is then incorporated in this command, which generates the fasta file:

./breseq/bin/gdtools APPLY -r path/to/REL606.gbk path/to/desired/output/location/XXXXXXXXX-YYK/output/output.gd -o path/to/final/output/location/XXXXXXXXX-YYK/gdtools_output_XXXXXXXXX-YYK.fasta

Finally, duplicate the fasta file, remove the accession number from the first line, and change the file extension to .txt. Now we have a .txt file whose only contents are the genome nucleotide sequence, as required by order_index.py.

Now simply change the file path on line 9 of order_index.py as needed and run the script for the REL606 .txt file and subsequent generation .txt files. Analyze as desired.

Use NCBI's RunBrowser https://trace.ncbi.nlm.nih.gov/Traces/?view=run_browser&display=metadata to find the following SRRs:

ara-3
SRR098285 (20k)
SRR098286 (20k)
SRR098289 (31.5k)
SRR098032 (32k)
SRR098042 (32k)
SRR098043 (32k)
SRR098027 (33k)
SRR098034 (34k)
SRR098035 (34k)
SRR098036 (36k)
SRR098037 (36k)
SRR098038 (38k)
SRR098039 (38k)
SRR098029 (40k)
SRR098030 (40k)

ara-6
SRR12340686 (50k)
SRR12340691 (50k)
SRR12340695 (50k)
SRR12340704 (50k)

ara+4
SRR12340689 (50k)
SRR12340694 (50k)
SRR12340698 (50k)
SRR12340707 (50k)






