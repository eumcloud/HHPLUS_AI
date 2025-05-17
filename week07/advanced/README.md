# Custom Instruction-Tuning with GPT2

## 목표
- HuggingFace dataset이 아닌 **자체 corpus.json** 데이터를 활용한 GPT instruction-tuning 실험
- fine-tuned 모델 학습 및 wandb 기반 로깅 공유

## 파일 구성

| 파일 | 설명 |
|------|------|
| `corpus.json` | 직접 수집한 instruction-format corpus (100개 이상) |
| `dataset.py` | 데이터 로딩 및 전처리 |
| `train.py` | HuggingFace Trainer 기반 GPT2 fine-tuning |
| `requirements.txt` | 실행에 필요한 패키지 목록 |

## 학습 환경

- 모델: `gpt4`
- 학습 Epoch: 10
- Optimizer: Adam
- 로깅: wandb 연동

## wandb 학습 결과

- [링크](https://wandb.ai/eumcloud/instruction-tuning-custom/runs/abcdef123456)

## 🚀 실행 방법

```bash
pip install -r requirements.txt
python train.py --model_name=gpt2
