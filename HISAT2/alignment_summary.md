
### Explanation of [HISAT2](https://ccb.jhu.edu/software/hisat2/index.shtml) summary statistics 

> HISAT2 is a fast and sensitive alignment program for mapping next-generation sequencing reads (both DNA and RNA) to a population of human genomes (as well as to a single reference genome).

> The below explanation was originally [posted](https://www.biostars.org/p/313264/#313355
) by me on [biostars.org](www.biostars.org)

The summary looks like this

```
HISAT2 summary stats:
            Total pairs: 11587225
                    Aligned concordantly or discordantly 0 time: 4464083 (38.53%)
                    Aligned concordantly 1 time: 2195620 (18.95%)
                    Aligned concordantly >1 times: 4877336 (42.09%)
                    Aligned discordantly 1 time: 50186 (0.43%)
            Total unpaired reads: 8928166
                    Aligned 0 time: 8019048 (89.82%)
                    Aligned 1 time: 304653 (3.41%)
                    Aligned >1 times: 604465 (6.77%)
            Overall alignment rate: 65.40%

```

### Description


**1. Total pairs: 11587225** 

Total reads = `11587225 * 2 = 23174450` (matches total number of reads in the sample)


**2. Aligned concordantly or discordantly 0 time: 4464083 (38.53%)**

These are unmapped reads :  `4464083 * 2 (paired end) = 8928166`

  

     ( 8928166 /  23174450 (Total reads) ) * 100 ~ 38.53%

**3. Aligned concordantly 1 time: 2195620 (18.95%)**

These are uniquely mapped reads : `2195620 * 2 (paired end) = 4391240`

   

    ( 4391240 /  23174450 (Total reads) ) * 100 ~ 18.95%

**4. Aligned concordantly >1 times: 4877336 (42.09%)**

These are multi mapped reads : `4877336 * 2  = 9754672`

    ( 9754672 /  23174450 (Total reads) ) * 100 ~ 42.09%

**5.Aligned discordantly 1 time: 50186 (0.43%)**

Discordant aligned : `50186 * 2 = 100372`

    ( 100372 /  23174450 (Total reads) ) * 100 ~ 0.43%

**6. Total unpaired reads: 8928166**

These are **not** paired reads

 - **Aligned 0 time: 8019048 (89.82%)**

    `(8019048 / 8928166 ) * 100 = 89.82%`  i.e. `89%` of the unpaired reads did not align at all

 - **Aligned 1 time: 304653 (3.41%)** 

    `(304653 / 8928166 ) * 100 = 3.41%`  i.e. `3.41%` of the unpaired reads aligned once

 - **Aligned >1 times: 604465 (6.77%)**

    `(604465 / 8928166 ) * 100 = 6.77%`  i.e. `6.77%` of the unpaired reads are multi mapped


**7. Overall alignment rate: 65.40%**

Calculation as explained below

#### PAIRED READS

Aligned concordantly 1 time: `(2195620 * 2 = 4391240)`
Aligned concordantly >1 times: `(4877336 * 2  = 9754672)`
Aligned discordantly 1 time: `(50186 * 2 = 100372)`

#### UNPAIRED READS

Aligned 1 time: `304653`
Aligned >1 times: `604465`

----------

Total = `4391240 + 9754672 +  100372 +  304653 +  604465 = 15155402`
    
Overall Alignment Rate = `(15155402 / 23174450) * 100 = 65.40%`
