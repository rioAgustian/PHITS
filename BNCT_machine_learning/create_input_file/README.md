# Create $2^N$ PHITS Input File with 6 Parameters Using Sobol Sampling
- **[Rio Agustian Gilang Fernando]**

## What it does?
Make a paramater sweep for 6 variabels for PHITS input file.

## Why is it imporant?
Our main goal is to generate different beam shaping assembly configurations for machine learning dataset. In order to make this task easier, I created this code to outomate the paramater sweep.

## Why using sobol sampling?
Grid search is too long, random search not exploring sample good enough, latin hypercube hard to add more sample. 

## How to use?
Download `sobol_sampling.py` and `template.inp`. Change the value of `N` inside the `sobol_sampling.py`. Remember, sobol sampling performs the best when your sample is $2^N$.
