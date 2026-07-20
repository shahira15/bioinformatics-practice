rule all:
    input:
        "variants.vcf"

rule fastqc:
    input:
        "sample.fastq"
    output:
        "sample_fastqc.html"
    shell:
        "fastqc {input}"

rule align:
    input:
        genome="yeast_genome.fasta",
        reads="sample.fastq"
    output:
        "aligned.sam"
    shell:
        "bwa mem {input.genome} {input.reads} > {output}"

rule sam_to_bam:
    input:
        "aligned.sam"
    output:
        "aligned.bam"
    shell:
        "samtools view -S -b {input} > {output}"

rule sort_bam:
    input:
        "aligned.bam"
    output:
        "aligned_sorted.bam"
    shell:
        "samtools sort {input} -o {output}"

rule index_bam:
    input:
        "aligned_sorted.bam"
    output:
        "aligned_sorted.bam.bai"
    shell:
        "samtools index {input}"

rule call_variants:
    input:
        genome="yeast_genome.fasta",
        bam="aligned_sorted.bam",
        bai="aligned_sorted.bam.bai"
    output:
        "variants.vcf"
    shell:
        "bcftools mpileup -f {input.genome} {input.bam} | bcftools call -mv -Ov -o {output}"
