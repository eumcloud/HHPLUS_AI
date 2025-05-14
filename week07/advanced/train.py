import argparse
import wandb
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from dataset import load_and_split_corpus, preprocess_function

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name", default="gpt2", type=str)
    parser.add_argument("--output_dir", default="./model", type=str)
    args = parser.parse_args()

    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
    tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(args.model_name)

    # Load and preprocess dataset
    train_dataset, valid_dataset = load_and_split_corpus("corpus.json")
    train_dataset = train_dataset.map(lambda x: preprocess_function(x, tokenizer), remove_columns=train_dataset.column_names)
    valid_dataset = valid_dataset.map(lambda x: preprocess_function(x, tokenizer), remove_columns=valid_dataset.column_names)

    # Setup wandb
    wandb.init(project="instruction-tuning-custom", name="gpt2-custom-instruction")

    # TrainingArguments
    training_args = TrainingArguments(
        output_dir=args.output_dir,
        per_device_train_batch_size=4,
        per_device_eval_batch_size=4,
        logging_steps=10,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        learning_rate=5e-5,
        num_train_epochs=3,
        weight_decay=0.01,
        report_to="wandb"
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=valid_dataset,
        tokenizer=tokenizer,
        data_collator=DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False),
    )

    trainer.train()

if __name__ == "__main__":
    main()
