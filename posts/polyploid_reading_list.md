# All things polyploid

This is a (aperiodically updated) reading list where I put articles, posts and notes on the topic of polyploid SNP calling and genomic predictions. Contributions are welcome.

* [2020] [Evaluation of variant calling tools for large plant genome re-sequencing](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-020-03704-1)
  * Methodology review
  * "Based on the concordance and receiver operating characteristic (ROC), the Samtools/mpileup variant calling tool with BWA-mem mapping of raw sequence reads outperformed other tests"
* [2022] [Alfalfa genomic selection for different stress-prone growing regions](https://acsess.onlinelibrary.wiley.com/doi/full/10.1002/tpg2.20264)
  * In-house pipeline:
  	* align, filtering -> dDocent
  	* variant calling -> freebayes ("naive" config just to obtain allele counts)
 	* filters: biallelic SNPs only, minimum depth of 6 or 20 reads -> bcftools
  	* actual calling -> updog R package
  * using also allele ratios for predictions, i.e. A/(A+a)
* [2018] [Development and Applications of a High Throughput Genotyping Tool for Polyploid Crops: Single Nucleotide Polymorphism (SNP) Array](https://www.frontiersin.org/articles/10.3389/fpls.2018.00104/full)
	* review, nice intro on the polyploid topic (history, role in agriculture, neopolyploids), problems with SNP discovery, features of SNP array technology
	* "Ploidy is a significant factor impacting SNP qualities and validation rates of SNP markers in SNP arrays... This review presents a complete overview of SNP array development and applications in polypoid crops, which will benefit the research in molecular breeding and genetics of crops with complex genomes"
	
## To be investigated

* [2015] [Polyploidy and genome evolution in plants](https://www.sciencedirect.com/science/article/pii/S0959437X15001185?casa_token=LAet5jlt-KgAAAAA:5BZNAFkkq4ij0kGhz4VUzrxhbzfUSY8L9pns29BHQJ_ha9avGT0bkZtCM2xEDevuBgtw_1sh8ns)
* [2022] [A joint learning approach for genomic prediction in polyploid grasses](https://www.nature.com/articles/s41598-022-16417-7)
* [2023] [Polyploid SNP Genotyping Using the MassARRAY System](https://link.springer.com/protocol/10.1007/978-1-0716-3024-2_7)
  * contacted the authors, requested full text
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