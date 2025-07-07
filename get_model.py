"""
Download the tiny-clinicalbert-qa model and tokenizer and save 
them to a tar.gz file
"""

import sys
import tarfile
import tempfile

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python get_model.py <output_path>")
        exit(1)

    from transformers import AutoModelForQuestionAnswering, AutoTokenizer
    
    out_path = sys.argv[1]

    if not out_path.endswith(".tar.gz"):
        out_path += ".tar.gz"
    
    model_id = "jon-t/tiny-clinicalbert-qa"

    with tempfile.TemporaryDirectory() as temp_dir:
        model = AutoModelForQuestionAnswering.from_pretrained(model_id)
        tokenizer = AutoTokenizer.from_pretrained(model_id)

        model.save_pretrained(temp_dir)
        tokenizer.save_pretrained(temp_dir)

        with tarfile.open(out_path, "w:gz") as tar:
            tar.add(out_path, arcname=".")
