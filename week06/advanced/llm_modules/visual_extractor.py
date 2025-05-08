import fitz  # PyMuPDF
import io
from PIL import Image

def extract_images_from_pdf(pdf_path: str) -> list:
    images = []
    doc = fitz.open(pdf_path)

    for page in doc:
        image_list = page.get_images(full=True)
        for img in image_list:
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image = Image.open(io.BytesIO(image_bytes))
            images.append(image)

    return images
