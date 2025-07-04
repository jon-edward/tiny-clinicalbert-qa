"""
Concatenates and shuffles the "squad_v2" and "emrqa-msquad" datasets.
"""

import os
import sys
import uuid

from datasets import load_dataset, DatasetDict, concatenate_datasets


def save_concatenated_dataset(output_path: str):
    """
    Save the concatenated "squad" and "emrqa-msquad" datasets.

    Both are squad-style datasets, but there are structural differences that 
    need to be normalized before concatenation.
    """

    def normalize_for_concat(example: dict) -> dict:
        example["id"] = str(uuid.uuid4())  # id might be duplicated from concatenation, regenerate
        example["answers"]["answer_end"] = None  # exists in emrqa-msquad but not squad
        return example
    
    squad: DatasetDict = load_dataset("rajpurkar/squad_v2").map(normalize_for_concat, desc="Normalizing squad") # type: ignore
    emrqa: DatasetDict = load_dataset("Eladio/emrqa-msquad").map(normalize_for_concat, desc="Normalizing emrQA-msquad") # type: ignore

    train = concatenate_datasets([squad["train"], emrqa["train"]]).shuffle(seed=42)
    validation = concatenate_datasets([squad["validation"], emrqa["validation"]]).shuffle(seed=42)

    dataset = DatasetDict({"train": train, "validation": validation})
    dataset.save_to_disk(output_path)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_dataset.py <output_path>")
        exit(1)
    
    output_path = sys.argv[1]
    
    if not os.path.isdir(output_path):
        save_concatenated_dataset(output_path)
