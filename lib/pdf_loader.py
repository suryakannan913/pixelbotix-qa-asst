import fitz  # PyMuPDF
import io
import pytesseract
from PIL import Image

def extract_text_from_image(image_data):
    """
    Extract text from an image using Tesseract OCR.
    """
    try:
        img = Image.open(io.BytesIO(image_data))
        text = pytesseract.image_to_string(img)
        return text.strip()
    except Exception as e:
        print(f"Error extracting text from image: {str(e)}")
        return ""

def load_pdf(file_path: str):
    doc = fitz.open(file_path)
    pages = []

    for num, page in enumerate(doc, start=1):
        # Extract text
        text = page.get_text("text")
        
        # Extract images
        image_texts = []
        image_list = page.get_images()
        for img_index, img in enumerate(image_list):
            try:
                xref = img[0]
                pix = fitz.Pixmap(doc, xref)
                
                # Convert to RGB if needed
                if pix.n - pix.alpha < 4:  # GRAY or RGB
                    try:
                        pix = fitz.Pixmap(fitz.csRGB, pix)
                    except:
                        # If conversion fails, try to get PNG directly
                        pass
                
                # Get image as PNG
                png_data = pix.tobytes("png") if pix.alpha == 0 else pix.tobytes("ppm")
                
                # Extract text from image
                img_text = extract_text_from_image(png_data)
                if img_text.strip():
                    image_texts.append(f"[Image {img_index + 1}] {img_text}")
            except Exception as e:
                # Skip problematic images silently
                continue
        
        # Combine text and image content
        combined_content = text.strip()
        if image_texts:
            combined_content += "\n" + "\n".join(image_texts)
        
        if combined_content.strip():
            pages.append({"page": num, "text": combined_content.strip()})

    return pages

