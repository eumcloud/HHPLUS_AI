import mlflow
import time
import hashlib

def log_summary_experiment(model_name: str, input_text: str, summary_text: str, start_time: float, tags: dict = {}):
    """MLflow에 요약 실험 정보를 기록"""
    duration = time.time() - start_time
    input_hash = hashlib.md5(input_text.encode()).hexdigest()

    with mlflow.start_run(run_name=f"Summary-{model_name}-{input_hash[:6]}"):
        mlflow.set_tag("task", "paper_summary")
        mlflow.set_tag("model_name", model_name)

        for k, v in tags.items():
            mlflow.set_tag(k, v)

        mlflow.log_param("input_length", len(input_text.split()))
        mlflow.log_param("model", model_name)
        mlflow.log_metric("summary_length", len(summary_text.split()))
        mlflow.log_metric("duration_sec", round(duration, 2))

        mlflow.log_text(summary_text, "summary_output.txt")
