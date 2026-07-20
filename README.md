# Bioinformatics Practice

Learning bioinformatics from the ground up — command line, Python, and Biopython — by building small tools that work with real biological data.

## What's in here

- **hello.py** — first Python script
- **basics.py** — variables and basic Python syntax
- **gc_content.py** — calculates GC content of a single DNA sequence
- **multi_gc.py** — calculates GC content across multiple sequences using a loop
- **sequences.fasta** — sample FASTA file with test sequences
- **read_fasta.py** — parses FASTA files manually (no libraries)
- **fasta_gc.py** — combines FASTA parsing with GC content calculation
- **brca1.fasta** — real human BRCA1 mRNA sequence, downloaded from NCBI (accession NM_007294.4)
- **real_gc.py** — computes GC content of the real BRCA1 gene
- **biopython_gc.py** — same GC content tool, rewritten using Biopython
- **central_dogma.py** — demonstrates DNA transcription and translation using Biopython
- **brca1_protein.py** — translates the BRCA1 sequence into protein (naive version)
- **brca1_protein_fixed.py** — improved version that finds the correct reading frame before translating

## Tools used

- Python 3
- Biopython
- NCBI Entrez utilities (for downloading real sequence data)
- Git / GitHub

## What I'm learning next

- NGS pipeline tools (FastQC, samtools, alignment)
- Sequence alignment and phylogenetics
- Workflow managers (Snakemake/Nextflow)
## Pipeline progress

### Stage 1: Quality Control (FastQC)
- Downloaded real RNA-seq data (yeast, *S. cerevisiae*) from SRA accession SRR6357070
- Ran FastQC on raw reads (`sample.fastq`)
- Result: 50,000 reads, 101bp length, ~40% GC (matches expected yeast genome GC content)
- Quality assessment: high confidence across full read length, no trimming needed
- Report: `sample_fastqc.html`

**Next step:** align reads to the yeast reference genome
