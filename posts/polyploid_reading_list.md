# All things polyploid

This is a (aperiodically updated) reading list where I put scientific papers on the topic of polyploid SNP calling and genomic predictions. 

For each entry I try to paste the most interesting bits, either for future reference or just so that I can recall what the paper is about. The number in square brackets is the year of publication.

Contributions are welcome :)

* [2020] [Evaluation of variant calling tools for large plant genome re-sequencing](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-020-03704-1)
  * Methodology review
  * "Based on the concordance and receiver operating characteristic (ROC), the Samtools/mpileup variant calling tool with BWA-mem mapping of raw sequence reads outperformed other tests"
* [2022] [Alfalfa genomic selection for different stress-prone growing regions](https://acsess.onlinelibrary.wiley.com/doi/full/10.1002/tpg2.20264)
  * Genomic regressions, comparing several representations of the same genotypes: diploid call, tetraploid call, allele ratios (i.e. A/(A+a) )
  * In-house pipeline:
  	* align, filtering -> dDocent
  	* variant calling -> freebayes ("naive" config just to obtain allele counts)
 	* filters: biallelic SNPs only, minimum depth of 6 or 20 reads -> bcftools
  	* actual calling -> updog R package
* [2018] [Development and Applications of a High Throughput Genotyping Tool for Polyploid Crops: Single Nucleotide Polymorphism (SNP) Array](https://www.frontiersin.org/articles/10.3389/fpls.2018.00104/full)
	* review, nice intro on the polyploid topic (history, role in agriculture, neopolyploids), problems with SNP discovery, features of SNP array technology, Illumina vs. Affymetrix comparison
	* table with all the available (at the time) SNP array for polyploid species
	* "Ploidy is a significant factor impacting SNP qualities and validation rates of SNP markers in SNP arrays... This review presents a complete overview of SNP array development and applications in polypoid crops, which will benefit the research in molecular breeding and genetics of crops with complex genomes"
	* "There are two types of SNPs: transition SNPs such as A/G, T/C, and transversion SNPs such as A/T, C/G, A/C, and T/G. For SNP array development, the transition SNP type is preferred and transversion SNPs, INDELs, or multiple allelic SNPs are typically excluded (Bianco et al., 2016; Clarke et al., 2016). Particularly, A/T or C/G SNPs are eliminated, as these types require two probes, while other SNP types require just one probe for genotyping"
	* "So far, there are two software, fitTetra and ClusterCall, written for tetraploids, which can call five genotypes. Another software, SuperMASSA, was written for all ploidies (so far only successfully reported in sugarcane)."
* [2023] [Polyploid SNP Genotyping Using the MassARRAY System](https://link.springer.com/protocol/10.1007/978-1-0716-3024-2_7)
  * focus on MassARRAY, as an alternative to GBS
  * The paper extends the base MassARRAY/Sequenom protocol from diploids to polyploids, plus brief discussion on the related softwares
  * "the MassARRAY platform (Sequenom Inc.), based on matrix-assisted laser desorption/ionization time-of-flight (MALDI-TOF) spectrometry, is widely recognized for its ability to perform accurate SNP genotyping analyses. It generates spectra with two signals for each heterozygous locus, and the ratio between these signals can beused to provide the relative abundance of alleles."
  * MassARRAY requires two subsequent PCRs (the second one known as iPLEX reaction)
  * "The assay’s design relies on prior knowledge of the sequences where the SNPs of interest are located and the ability to find an adequate set of primers in this region."
	
## NGS Polyploid-oriented pipelines

* [2020] [fast-GBS v2](https://pubmed.ncbi.nlm.nih.gov/33006480/)
	* paper behind paywall :(
	* wiki & software: https://bitbucket.org/jerlar73/fast-gbs_v2/wiki/Home
	* requires reference genome, possibly paired with companion software 
	[SGR extractor](https://bitbucket.org/jerlar73/srg-extractor/src/master/) to
	create a "skinny" reference genome with only the parts interested by reduced
	representation
	* main softwares needed: sabre (demultiplex), cutadapt (trimming), bwa (alignment),
	  samtools & vcftools (various manipulations), platypus (variant calling), beagle (imputation)
	* python based, as of Feb 2023 supports only 2.7+, I tested with Python3 and received too many errors to be able to successfully install
* [2018] [UGbs-Flex](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6003085/)
	* does not require reference genome
	* python + perl based
	* wiki & software: https://devoslab.franklinresearch.uga.edu/scripts-used-gbs-pipeline
	* no preprocessing, in the paper they use Stacks (demultiplexing) and FASTX Toolkit (trimming), Flash (overlapping forward/reverse reads)
	* reference genome via clustering (ustacks/cstacks from the Stacks suite)
	* internally using bowtie (alignment), gatk (SNP calling)
	* they claim to be superior to GBS-SNP-CROP pipelines (more SNPs retained)
	* nice work on genetic map reconstruction (they work without reference genome)
	* optimization of the wetlab part of GBS (choice of restriction enzyme, size selection...)
* [2019] [PolyRAD](https://academic.oup.com/g3journal/article/9/3/663/6026786?login=false)
	* wiki & software: https://github.com/lvclark/polyRAD
	* R package
	* "The polyRAD software imports read depth from several existing pipelines, and outputs continuous or discrete numerical genotypes suitable for analyses such as genome-wide association and genomic prediction."
	* main competitor: updog (R package)
	* "Initially, SNP discovery is performed by other software such as TASSEL (Glaubitz et al. 2014) or Stacks (Catchen et al. 2013), with or without a reference genome, then allelic read depth is imported into polyRAD from those pipelines or the read counting software TagDigger (Clark and Sacks 2016)."
	* "*c* is the cross-contamination rate [...] estimated by including a negative control in library preparation, i.e., of the set of ligation reactions with barcoded adapters, one that has no genomic DNA added. The sequence read depth for this blank barcode is then divided by the mean read depth of non-blank barcodes in order to estimate c. Our model assumes c to be constant across loci, under the assumption that most errors are due to contamination during library preparation. In practice we have found c to typically be 1/1000 (unpublished data), and expect it to be more substantial than errors arising from the sequencing technology, which will tend to produce haplotypes not found elsewhere in the data set."
	* "Bayesian genotype estimation allows correction of genotyping errors in diploids and polyploids, i.e., when an individual is truly heterozygous but only one allele was sequenced, or when an individual appears heterozygous due to sequencing error or contamination but is truly homozygous."

## To be investigated (stuff that I haven't read, yet)

* [2022] [A joint learning approach for genomic prediction in polyploid grasses](https://www.nature.com/articles/s41598-022-16417-7)
* [2015] [Polyploidy and genome evolution in plants](https://www.sciencedirect.com/science/article/pii/S0959437X15001185?casa_token=LAet5jlt-KgAAAAA:5BZNAFkkq4ij0kGhz4VUzrxhbzfUSY8L9pns29BHQJ_ha9avGT0bkZtCM2xEDevuBgtw_1sh8ns)
* [2022] [A joint learning approach for genomic prediction in polyploid grasses](https://www.nature.com/articles/s41598-022-16417-7)
* [2022] [Recent Advances and Applicability of GBS, GWAS, and GS in Polyploid Crops](https://onlinelibrary.wiley.com/doi/abs/10.1002/9781119745686.ch15)
  * contacted the authors, requested full text
* [Robust and efficient software for reference-free genomic diversity analysis of genotyping-by-sequencing data on diploid and polyploid species](https://onlinelibrary.wiley.com/doi/abs/10.1111/1755-0998.13477)
  * contacted the authors, requested full text
  * there's also [the preprint](https://www.biorxiv.org/content/10.1101/2020.11.28.402131v1.full.pdf)
* [2015] [Single Nucleotide Polymorphism Identification in Polyploids: A Review, Example, and Recommendations](https://www.cell.com/molecular-plant/pdf/S1674-2052(15)00130-6.pdf)
  * review
* [2022] [Stack Mapping Anchor Points (SMAP): a versatile suite of tools for read-backed haplotyping](https://www.biorxiv.org/content/10.1101/2022.03.10.483555v1.abstract)
  * preprint only
* [2013] [A Next-Generation Sequencing Method for Genotyping-by-Sequencing of Highly Heterozygous Autotetraploid Potato](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0062355)
* [2019] [Genomic Prediction of Autotetraploids; Influence of Relationship Matrices, Allele Dosage, and Continuous Genotyping Calls i Phenotype Prediction](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6469427/)
* [2021] [Genomic Selection in an Outcrossing Autotetraploid Fruit Crop: Lessons From Blueberry Breeding](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8236943/)
* [2019] [Genomic Selection with Allele Dosage in Panicum maximum Jacq](https://academic.oup.com/g3journal/article/9/8/2463/6026834?login=false)
* [2018] [Genotyping Polyploids from Messy Sequencing Data](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6218231/)
* [2019] [On the accuracy of genomic prediction models considering multi-trait and allele dosage in Urochloa spp. interspecific tetraploid hybrids](https://link.springer.com/article/10.1007/s11032-019-1002-7)
* [2012] [Efficient Exact Maximum a Posteriori Computation for Bayesian SNP Genotyping in Polyploids](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0030906)
* [2017] [GBS-based single dosage markers for linkage and QTL mapping allow gene mining for yield-related traits in sugarcane](https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-016-3383-x)
* [2014] [Development of an Alfalfa SNP Array and Its Use to Evaluate Patterns of Population Structure and Linkage Disequilibrium](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0084329)
  * SNP array for alfalfa
* [2016] [Genome-Wide SNP Calling from Genotyping by Sequencing (GBS) Data: A Comparison of Seven Pipelines and Two Sequencing Technologies](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0161333)
* [2023] [Sequencing and Assembly of Polyploid Genomes](https://link.springer.com/protocol/10.1007/978-1-0716-2561-3_23)
	* protocol details

