# SEADECC-EDDG
Cooperative coevolutionary surrogate ensemble assisted differential evolution with efficient dual differential grouping for large-scale expensive optimization problems

## Abstract
This paper proposes a novel algorithm named surrogate ensemble assisted differential evolution with efficient dual differential grouping (SEADECC-EDDG) to deal with large-scale expensive optimization problems (LSEOPs) based on the CC framework. In the decomposition phase, our proposed EDDG inherits the framework of efficient recursive differential grouping (ERDG) and embeds the multiplicative interaction identification technique of Dual DG (DDG), which can detect the additive and multiplicative interactions simultaneously without extra fitness evaluation consumption. Inspired by RDG2 and RDG3, we design the adaptive determination threshold and further decompose relatively large-scale sub-components to alleviate the curse of dimensionality. In the optimization phase, the SEADE is adopted as the basic optimizer, where the global and the local surrogate model are constructed by generalized regression neural network (GRNN) with all historical samples and Gaussian process regression (GPR) with recent samples. Expected improvement (EI) infill sampling criterion cooperated with random search is employed to search elite solutions in the surrogate model. To evaluate the performance of our proposal, we implement comprehensive experiments on CEC2013 benchmark functions compared with state-of-the-art decomposition techniques. Experimental and statistical results show that our proposed EDDG is competitive with these advanced decomposition techniques, and the introduction of SEADE can accelerate the convergence of optimization significantly.

## Citation
@ARTICLE{Zhong:23,  
title={Cooperative coevolutionary surrogate ensemble-assisted differential evolution with efficient dual differential grouping for large-scale expensive optimization problems},  
author={Rui Zhong and Enzhi Zhang and Masaharu Munetomo},  
journal={Complex \& Intelligent System},  
volume={10},  
number={},  
pages={2129–2149},  
year={2023},  
doi={https://doi.org/10.1007/s40747-023-01262-6 },  
}

## Datasets and Libraries
CEC2013 large-scale optimization benchmarks are provided by the cec2013lsgo library. Surrogate models are provided by sklearn and pyGRNN libraries.

## Contact
If you have any questions, please don't hesitate to contact zhongrui[at]iic.hokudai.ac.jp
