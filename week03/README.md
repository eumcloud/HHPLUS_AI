
# Multi-Genre Natural Language Inference (MNLI) 캐이스 모델 비교 보고서

## 1. 실험 개요

본 프로젝트는 **Multi-Genre Natural Language Inference (MNLI)** 태스크를 해결하기 위한 모델을 설계하고 학습시키는 실험을 수행.
MNLI는 두 문장(Premise와 Hypothesis)의 논리적 관계를 다음 세 가지 범주 중 하나로 분류하는 문제입니다.

- **Entailment**: 전제가 가설을 논리적으로 포함할 때 = 0
- **Neutral**: 전제와 가설이 논리적으로 무관할 때 = 1
- **Contradiction**: 전제와 가설이 논리적으로 모순될 때 = 2

해당 태스크를 통해 **Pre-trained BERT 모델을 fine-tuning하는 경우와**, **동일한 구조의 Non-pre-trained Transformer를 학습시킨 경우**의 성능 차이를 비교 분석하였다.

---

## 2. 데이터셋 및 전처리

### 2.1 데이터셋
- 출처: [Kaggle - Unlocking Language Understanding with the MultiNLI](https://www.kaggle.com/datasets/thedevastator/unlocking-language-understanding-with-the-multin)
- 사용 파일:
  - `train.csv` (학습용, 1,000 샘플)
  - `validation_matched.csv` (검증용, 1,000 샘플)

### 2.2 입력 구조
- 입력: `(premise, hypothesis)` 형태의 두 문장 쌍
- 출력: `0 (entailment), 1 (neutral), 2 (contradiction)` 중 하나의 정수 레이블

### 2.3 전처리
- Huggingface의 `AutoTokenizer`를 사용하여 토크나이징 수행
- 최대 길이 128로 패딩 및 트렁케이션
- `transformers.Dataset`을 활용하여 모델에 바로 입력 가능한 형태로 변환

---

## 3. 모델 설계

### 3.1 Pre-trained 모델 (BERT-base-uncased)
- 구조: Huggingface `AutoModelForSequenceClassification`
- 설정:
  - `num_labels=3` 설정
  - 사전 학습된 `bert-base-uncased` weight 로드
- 입력: `{'input_ids': [B, L], 'attention_mask': [B, L]}`
- 출력: `[B, 3]` (softmax logits)

### 3.2 Non-pre-trained 모델
- 구조는 BERT와 동일하나, 사전 학습 weight 없이 랜덤 초기화된 상태로 학습 시작
- 동일한 `config`를 사용하여 구조적 차이는 없음

---

## 4. 학습 설정 및 실험 환경

- 프레임워크: PyTorch, Huggingface Transformers
- 학습기: `Trainer` API 사용
- 하이퍼파라미터:
  - Epochs: 3
  - Batch size: 16 (train), 64 (eval)
  - Optimizer: AdamW
  - Weight decay: 0.01
  - Evaluation: 매 epoch마다 수행
- Loss: CrossEntropyLoss
- Metric: Accuracy

---

## 5. 실험 결과

### 5.1 정량적 비교

| 모델                        | Validation Accuracy | Validation Loss |
|-----------------------------|----------------------|------------------|
| Pre-trained BERT            | **0.84**             | **0.55**         |
| Non-pre-trained BERT        | 0.60                 | 0.80             |

### 5.2 시각화 결과

#### (1) Loss Curve
- 학습 도중 Pre-trained 모델은 빠르게 수렴하였으며, overfitting 없이 안정적인 loss 감소를 보였다.
- Non-pre-trained 모델은 loss 감소가 느리며, 일정 수준 이하로 감소하지 못함.

![Loss Curve](./loss_curve.png)

#### (2) Accuracy Plot
- Pre-trained 모델은 epoch마다 정확도가 안정적으로 상승했으며, 최종적으로 84%의 정확도를 기록하였다.
- Non-pre-trained 모델은 약 60% 수준에서 정체됨.

![Accuracy Plot](./accuracy_plot.png)

---

## 6. 분석 및 결론

본 실험은 Pre-trained BERT 모델을 fine-tuning할 경우, 같은 구조의 Transformer를 처음부터 학습하는 경우보다 훨씬 더 뛰어난 성능을 보임을 보여준다.

- **Pre-training의 효과**:
  - 언어적 문맥, 구조, 의미에 대한 사전 지식을 통해 학습 데이터가 적어도 빠른 수렴과 높은 정확도를 얻을 수 있다.
- **Non-pre-trained 모델의 한계**:
  - 같은 구조라도 초기 weight가 무작위일 경우, 수렴 속도가 매우 느리고 generalization이 어렵다.

따라서, 사전 학습된 언어 모델은 실전 NLP 태스크에서 효과적인 성능 향상 도구로 활용될 수 있으며, 특히 데이터가 제한적인 상황에서 더욱 큰 이점을 가진다.

---

## 7. 프로젝트 파일 구성

```
.
├── mnli_finetune.ipynb          # MNLI 실험 notebook
├── loss_curve.png               # Loss 시각화 결과
├── accuracy_plot.png            # Accuracy 시각화 결과
├── requirements.txt             # 설치 의존성 목록
└── README.md                    # 본 보고서
```

---

## 8. 실행 방법

```bash
# 필수 라이브러리 설치
pip install -r requirements.txt

# 또는 Jupyter Notebook 실행
jupyter notebook mnli_finetune.ipynb
```


