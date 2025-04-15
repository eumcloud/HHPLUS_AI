import json
import sys

def clean_widgets_metadata(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb_data = json.load(f)

    if 'metadata' in nb_data and 'widgets' in nb_data['metadata']:
        print("Removing 'metadata.widgets'...")
        del nb_data['metadata']['widgets']
    else:
        print("'metadata.widgets' not found. No changes made.")

    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(nb_data, f, indent=2)
    print(f"Updated notebook saved to: {notebook_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python remove_widgets.py good_student.ipynb")
    else:
        clean_widgets_metadata(sys.argv[1])
