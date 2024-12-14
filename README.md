# DSGram: Dynamic Weighting Sub-Metrics for Grammatical Error Correction

## Introduction

**DSGram** is a novel evaluation framework designed to enhance the performance evaluation of Grammatical Error Correction (GEC) models, especially in the era of large language models (LLMs). Traditional reference-based evaluation metrics often fall short due to the inherent discrepancies between model-generated corrections and provided gold references. DSGram addresses this issue by introducing a dynamic weighting mechanism that integrates Semantic Coherence, Edit Level, and Fluency.

This repository contains the code and data associated with the paper: **"DSGram: Dynamic Weighting Sub-Metrics for Grammatical Error Correction in the Era of Large Language Models"** by Jinxiang Xie, Yilin Li, Xunjian Yin, and Xiaojun Wan.

![图片](https://github.com/jxtse/GEC_Metrics_LLM/blob/main/images/FlowChart.png)

## Repository Structure

- `Dataset/`: Contains the datasets used for evaluation, including human-annotated and LLM-simulated sentences.
  - `results/`: Directory to store the evaluation results.   
- `DSGram/`: Source code for implementing the DSGram evaluation framework.

![图片](https://github.com/jxtse/GEC_Metrics_LLM/blob/main/images/Example.png)

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
