# AG News 텍스트 분류 보고서 with DistilBERT 

본 과제는 AG News 데이터셋을 기반으로, 사전 학습된 DistilBERT 모델을 활용하여 뉴스 기사 분류 문제를 해결하는 것을 목표로 합니다. 주요 구현 내용은 다음과 같습니다.

---

## ✅ 구현 항목 체크리스트

- [x] AG_News dataset 준비
  - `fancyzhx/ag_news` Huggingface dataset 로드
  - `collate_fn` 함수 내 truncation 관련 코드 제거
- [x] Classifier 출력, 손실 함수, 정확도 함수 변경
  - `nn.CrossEntropyLoss` 사용
  - `TextClassifier` 출력 차원을 4로 수정
  - 정확도 계산 함수 수정 (`torch.argmax`)
- [x] 학습 결과 report
  - 각 epoch마다 train loss 출력
  - 최종 모델의 test accuracy report 포함

---

## 1. 데이터셋 준비

- `fancyzhx/ag_news` 데이터셋을 Huggingface Datasets 라이브러리를 통해 로드
- tokenizer는 `distilbert-base-uncased`에 적합한 DistilBERTTokenizer 사용
- `collate_fn` 함수에서 truncation 관련 항목 제거

```python
tokenizer(texts, padding=True).input_ids
```

---

## 2. 모델 구조

- 사전 학습된 DistilBERT 모델을 encoder로 사용
- 마지막 `[CLS]` 토큰의 representation을 활용하여 분류 수행
- 출력 차원을 4로 조정하여 4개의 카테고리 분류 문제로 설정
- Encoder는 freeze, 마지막 linear classifier만 학습

```python
self.classifier = nn.Linear(768, 4)
```

---

## 3. 학습 설정 및 손실 함수

- 손실 함수: `nn.CrossEntropyLoss` (multi-class classification용)
- 옵티마이저: `Adam`
- 학습 epoch 수: 20

---

## 4. 학습 및 정확도 결과

- 각 epoch마다 train loss를 출력
- 최종 test accuracy 출력 포함

예시 출력:
```
Epoch   0 | Train Loss: 0.9243 | Train Acc: 0.823 | Test Acc: 0.817
Epoch   1 | Train Loss: 0.6311 | Train Acc: 0.867 | Test Acc: 0.862
...
Epoch  19 | Train Loss: 0.3024 | Train Acc: 0.931 | Test Acc: 0.920
=========> Final Test acc: 0.920
```

---

## 5. 학습 결과 시각화

- 각 epoch마다의 Loss 및 Accuracy 그래프 첨부

![Training Curve](./week03/plot/loss_accuracy_plot.png)

---

## 6. 실행 방법

```bash
pip install tqdm boto3 requests regex sentencepiece sacremoses datasets
python run_classifier.py
```

또는 Jupyter Notebook 실행 후 순차적으로 실행.

---

## 7. 참고 사항

- tokenizer의 truncation 옵션은 명시적으로 제거
- 전체 문장 사용이 목표이므로 자르지 않고 입력 처리
- DistilBERT는 최대 입력 길이 512를 초과하는 입력은 자동으로 처리

--- 

## 🔗 GitHub 링크

[참고](https://github.com/yourusername/AGNews-DistilBERT-Classifier)
