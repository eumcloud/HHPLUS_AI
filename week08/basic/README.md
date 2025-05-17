# LoRA Rank 변화에 따른 성능 분석 실험 보고서

## 실험 목표

Low-Rank Adaptation (LoRA) 방식에서 `rank (r)` 값을 변화시켜가며 모델 학습을 진행하고, 이 변화가 성능(Loss), 학습 속도, 메모리 사용량에 어떤 영향을 주는지를 비교 분석한다.

## 실험 환경

- 모델: `facebook/opt-350m`
- 데이터셋: `sahil2801/CodeAlpaca-20k`
- 라이브러리: `peft`, `transformers`, `accelerate`, `torch`, `wandb`
- LoRA 적용 대상 모듈: `torch.nn.Linear`
- SFTTrainer 설정:
    ```python
    trainer = SFTTrainer(
        model,
        train_dataset=dataset,
        args=SFTConfig(output_dir="/tmp/clm-instruction-tuning", max_seq_length=128),
        formatting_func=formatting_prompts_func,
        data_collator=collator,
    )
    ```

## 실험 설정

- `lora_r` 값: 8, 128, 256
- `lora_alpha`: 32
- `lora_dropout`: 0.1

모든 실험은 Deepspeed 없이 수행되었으며, 동일한 랜덤 시드를 설정하여 실험의 일관성을 유지하였다.

## 결과

| LoRA Rank (`r`) | 최종 Loss (wandb) | 평균 학습 속도 (it/s) | 최대 메모리 사용량 (GPU) |
|------------------|------------------|-------------------------|----------------------------|
| 8                | 1.234            | 4.91                    | 1.6 GB                     |
| 128              | 1.019            | 3.15                    | 3.2 GB                     |
| 256              | 0.984            | 2.47                    | 5.1 GB                     |

메모리 사용량 측정 코드:
```python
print('Max Alloc:', round(torch.cuda.max_memory_allocated(0)/1024**3, 1), 'GB')
