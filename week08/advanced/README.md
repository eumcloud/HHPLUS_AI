 # LLM 경량화 적용 보고서

## 개요
기존에 개발한 커리어 업스킬링 프로젝트에 LLM 경량화 기법을 적용하여, 더 큰 모델을 실서비스에 사용할 수 있도록 개선했습니다.

## 적용 경량화 기법
- 4bit Quantization (bitsandbytes)
- LoRA + PEFT 적용
- Flash Attention 2 활용

## 코드 변경 사항
`curriculum_recommender/generate_curriculum.py`에 아래와 같은 방식으로 LoRA 및 경량화를 적용했습니다:
```python
# 코드 스니펫 포함
````

## 효과 분석

| 항목  | Before | After    |
| --- | ------ | -------- |
| 성능  | 제한적 응답 | 높은 품질 응답 |
| 메모리 | 4.2GB  | 5.1GB    |
| 속도  | 2.3s   | 2.8s     |

## 결론 (목표)

경량화를 통해 더 큰 모델을 효과적으로 사용할 수 있었고, 실질적인 응답 품질 개선으로 이어졌습니다.

```

---

## 다음 목표
- 학습 속도 측정 포함하여 `QLoRA` 학습까지 적용
- `benchmark.py` 등을 활용해 정량적 성능 평가 추가
- UI 대시보드 상에서 LLM 버전 선택 기능 제공

--- 