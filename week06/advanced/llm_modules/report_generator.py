from llm_modules.paper_summarizer import summarize_text
from llm_modules.visual_extractor import extract_images_from_pdf
from monitoring.mlflow_tracking import log_summary_experiment
import time


def generate_final_report(paper_data: dict) -> dict:
    text = paper_data['text']
    file_path = paper_data.get('file_path')

    summary = summarize_text(text)
    visualizations = extract_images_from_pdf(file_path) if file_path else []

    html_content = f"<h1>논문 요약 리포트</h1><p>{summary}</p>"

    return {
        "summary": summary,
        "visualizations": visualizations,
        "html": html_content
    }




def generate_final_report_ii(paper_data: dict) -> dict:
    text = paper_data['text']
    file_path = paper_data.get('file_path')
    model_name = "gpt-4"
    start_time = time.time()

    summary = summarize_text(text, method="map_reduce")
    images = extract_images_from_pdf(file_path) if file_path else []

    log_summary_experiment(
        model_name=model_name,
        input_text=text,
        summary_text=summary,
        start_time=start_time,
        tags={"source": "streamlit_app", "file_name": getattr(file_path, 'name', 'unknown')}
    )

    return {
        "summary": summary,
        "visualizations": images,
        "html": f"<h1>논문 요약 리포트</h1><p>{summary}</p>"
    }
