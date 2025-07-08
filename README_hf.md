---
language: en
license: mit
tags:
  - question-answering
  - pytorch
  - bert
datasets:
  - rajpurkar/squad_v2
  - Eladio/emrqa-msquad
---

<!-- This README.md file is used to generate the README on https://huggingface.co/jon-t/tiny-clinicalbert-qa -->

# tiny-clinicalbert-qa

A lightweight, domain-adapted BERT model for clinical question answering, trained on a combination of [SQuAD v2](https://huggingface.co/datasets/rajpurkar/squad_v2) and [EMRQA-MSQuAD](https://huggingface.co/datasets/Eladio/emrqa-msquad) datasets.

Source code for the training script is available [on GitHub](https://github.com/jon-edward/tiny-clinicalbert-qa). See [eval_results.json](https://huggingface.co/jon-t/tiny-clinicalbert-qa/blob/main/eval_results.json) for evaluation results, and [train_results.json](https://huggingface.co/jon-t/tiny-clinicalbert-qa/blob/main/train_results.json) for training results.
