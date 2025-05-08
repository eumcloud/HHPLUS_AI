import kfp
from kfp import dsl
from kfp.components import load_component_from_file

@dsl.pipeline(
    name="LLM 논문 요약 리포트 생성",
    description="PDF → 요약 + 시각화 리포트 생성 파이프라인"
)
def paper_summary_pipeline(pdf_path: str):
    extract_text_op = load_component_from_file('kfp/components/extract_text.yaml')
    summarize_op = load_component_from_file('kfp/components/summarize.yaml')
    extract_visuals_op = load_component_from_file('kfp/components/extract_visuals.yaml')
    report_op = load_component_from_file('kfp/components/generate_report.yaml')

    text_task = extract_text_op(pdf_path)
    summary_task = summarize_op(text_task.output)
    visuals_task = extract_visuals_op(pdf_path)
    report_task = report_op(summary_task.output, visuals_task.output)
