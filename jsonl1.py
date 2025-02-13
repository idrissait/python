# -*- coding: utf-8 -*-
"""
Create a excel template formated in a way it can be later on tranformed into a jsonl for LLM fine-tuning
"""
import pandas as pd

# Create a sample dataframe with a template structure
data = {
    "prompt": [
        "a",
        "b?",
        "c"
    ],
    "completion": [
        "A",
        "B.",
        "C"
    ]
}

df = pd.DataFrame(data)

# Save as an Excel file
file_path = "/Users/XXXXXXX/.spyder-py3/jsonl_template.xlsx"  # Update with your file path
df.to_excel(file_path, index=False)

# Provide the file for download
file_path
