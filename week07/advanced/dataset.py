import json
from datasets import Dataset
from sklearn.model_selection import train_test_split

def load_and_split_corpus(path="corpus.json", test_size=0.2):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    train_data, valid_data = train_test_split(data, test_size=test_size, random_state=42)
    return Dataset.from_list(train_data), Dataset.from_list(valid_data)

def preprocess_function(example, tokenizer, max_length=512):
    prompt = f"### Instruction:\n{example['instruction']}\n"
    if example.get("input"):
        prompt += f"### Input:\n{example['input']}\n"
    prompt += "### Response:\n"
    full_text = prompt + example["output"]

    return tokenizer(full_text, truncation=True, padding="max_length", max_length=max_length)
