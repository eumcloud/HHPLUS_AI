from llm_modules.paper_summarizer import summarize_text
from llm_modules.visual_extractor import extract_images_from_pdf

def run_summary_pipeline(text: str, pdf_path: str = None) -> dict:
    summary = summarize_text(text)
    visuals = extract_images_from_pdf(pdf_path) if pdf_path else []

    return {
        "summary": summary,
        "visualizations": visuals
    }
