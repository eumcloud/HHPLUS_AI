# GPT Fine-tuning with Validation

## 프로젝트 개요

이 프로젝트는 HuggingFace의 `transformers` 라이브러리를 기반으로 GPT 계열 모델에 대해 fine-tuning을 수행하며, 학습 시 validation 데이터를 활용하여 `eval_loss`를 함께 측정하도록 구성되었습니다.

## 주요 기능

- HuggingFace Hub에서 사전 학습된 모델과 데이터셋을 로드
- Train/Validation 데이터셋 구성
- `Trainer`를 통해 fine-tuning 진행
- `wandb`를 이용한 학습 로그 시각화 및 공유
- `train_loss`, `eval_loss` 로깅 및 저장

## 실행 방법

다음 명령어를 통해 학습을 시작할 수 있습니다:

```bash
python train.py \
  --model_name_or_path=gpt4 \
  --dataset_name=<데이터셋 이름> \
  --output_dir=./gpt-finetune \
  --per_device_train_batch_size=2 \
  --per_device_eval_batch_size=2 \
  --evaluation_strategy=epoch \
  --num_train_epochs=3 \
  --logging_steps=100 \
  --save_strategy=epoch \
  --report_to=wandb
