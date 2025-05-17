from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments
from datasets import load_dataset
import argparse
import wandb

# 1. 인자 파싱
parser = argparse.ArgumentParser()
parser.add_argument('--model_name_or_path', type=str, required=True)
parser.add_argument('--dataset_name', type=str, required=True)
parser.add_argument('--output_dir', type=str, required=True)
parser.add_argument('--per_device_train_batch_size', type=int, default=2)
parser.add_argument('--per_device_eval_batch_size', type=int, default=2)
parser.add_argument('--evaluation_strategy', type=str, default='epoch')
parser.add_argument('--num_train_epochs', type=int, default=3)
parser.add_argument('--logging_steps', type=int, default=100)
parser.add_argument('--save_strategy', type=str, default='epoch')
parser.add_argument('--report_to', type=str, default='wandb')
args = parser.parse_args()

# 2. wandb 초기화
wandb.init(project="gpt-finetune", name=args.model_name_or_path)

# 3. 모델과 토크나이저 로드
tokenizer = AutoTokenizer.from_pretrained(args.model_name_or_path)
model = AutoModelForCausalLM.from_pretrained(args.model_name_or_path)

# 4. 데이터셋 로드 및 전처리
datasets = load_dataset(args.dataset_name)
def tokenize_function(examples):
    return tokenizer(examples['text'], truncation=True, padding='max_length')
tokenized_datasets = datasets.map(tokenize_function, batched=True)

# 5. TrainingArguments 설정
training_args = TrainingArguments(
    output_dir=args.output_dir,
    per_device_train_batch_size=args.per_device_train_batch_size,
    per_device_eval_batch_size=args.per_device_eval_batch_size,
    evaluation_strategy=args.evaluation_strategy,
    num_train_epochs=args.num_train_epochs,
    logging_steps=args.logging_steps,
    save_strategy=args.save_strategy,
    report_to=args.report_to,
    logging_dir='./logs',
)

# 6. Trainer 정의 및 학습 시작
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets['train'],
    eval_dataset=tokenized_datasets['validation'],
)
trainer.train()
