# DSGram: Dynamic Weighting Sub-Metrics for Grammatical Error Correction

## Introduction

**DSGram** is a novel evaluation framework designed to enhance the performance evaluation of Grammatical Error Correction (GEC) models, especially in the era of large language models (LLMs). Traditional reference-based evaluation metrics often fall short due to the inherent discrepancies between model-generated corrections and provided gold references. DSGram addresses this issue by introducing a dynamic weighting mechanism that integrates Semantic Coherence, Edit Level, and Fluency.

This repository contains the code and data associated with the paper: **"DSGram: Dynamic Weighting Sub-Metrics for Grammatical Error Correction in the Era of Large Language Models"** by Jinxiang Xie, Yilin Li, Xunjian Yin, and Xiaojun Wan.

![图片](https://github.com/jxtse/GEC_Metrics_LLM/blob/main/images/FlowChart.png)

## Paper Abstract

Evaluating the performance of GEC models has become increasingly challenging due to the divergence between LLM-based corrections and gold references. Traditional metrics often fail to capture these nuances, leading to unreliable evaluations. DSGram introduces a dynamic weighting mechanism that incorporates Semantic Coherence, Edit Level, and Fluency to provide a more robust evaluation. Using the Analytic Hierarchy Process (AHP) in conjunction with LLMs, DSGram dynamically adjusts the weights of these criteria based on the evaluation context, resulting in a more nuanced and effective evaluation framework. Experimental results on datasets like CoNLL-2014 and BEA-2019 demonstrate the effectiveness of DSGram.

## Key Contributions

- Introduction of new sub-metrics for GEC evaluation, optimizing past metrics and adding an evaluation of over-editing.
- A dynamic weighting-based GEC evaluation method integrating AHP with LLMs to determine the relative importance of different evaluation criteria.
- Development of datasets incorporating human annotations and LLM-simulated sentences from CoNLL-2014 and BEA-2019 test sets.

## Repository Structure

- `data/`: Contains the datasets used for evaluation, including human-annotated and LLM-simulated sentences.
- `src/`: Source code for implementing the DSGram evaluation framework.
  - `evaluation.py`: Main script for performing evaluations using DSGram.
  - `metrics.py`: Definitions of the Semantic Coherence, Edit Level, and Fluency metrics.
  - `ahp.py`: Implementation of the Analytic Hierarchy Process for dynamic weight calculation.
  - `utils.py`: Utility functions for data processing and scoring.
- `results/`: Directory to store the evaluation results.

## Citation

If you use DSGram in your research, please cite the following paper:

```bibtex
@article{xie2024dsgram,
  title={DSGram: Dynamic Weighting Sub-Metrics for Grammatical Error Correction in the Era of Large Language Models},
  author={Jinxiang Xie and Yilin Li and Xunjian Yin and Xiaojun Wan},
  journal={arXiv preprint arXiv:XXXX.XXXX},
  year={2024}
}
```

# Tech Used
 ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=azure-devops&logoColor=white)
