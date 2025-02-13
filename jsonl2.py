# -*- coding: utf-8 -*-
"""
Export an excel file based on a template to a jsonl for a LLM fine-tuning (so far tested on chatGPT and Mistral)
"""

import pandas as pd
import json

# Load the Excel file
file_path = "/jsonl_template.xlsx"  # Update with your file path
df = pd.read_excel(file_path)

# Ensure the expected columns exist
required_columns = ["prompt", "completion"]
if not all(col in df.columns for col in required_columns):
    raise ValueError(f"Missing required columns. Expected {required_columns}")

# Convert to JSONL format
output_file = "output.jsonl"
with open(output_file, "w", encoding="utf-8") as f:
    for _, row in df.iterrows():
        json.dump({"prompt": row["prompt"], "completion": row["completion"]}, f, ensure_ascii=False)
        f.write("\n")

print(f"Conversion complete. JSONL file saved as {output_file}")
