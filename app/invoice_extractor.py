
import os
import json
import time

os.environ["PADDLE_PDX_ENABLE_MKLDNN_BYDEFAULT"] = "False"

from paddleocr import PaddleOCR

class InvoiceExtractor:

    def __init__(self):

        print("Loading PP-OCRv5 Mobile...")

        self.ocr = PaddleOCR(
            text_detection_model_name="PP-OCRv5_mobile_det",
            text_recognition_model_name="PP-OCRv5_mobile_rec",
            use_doc_orientation_classify=False,
            use_doc_unwarping=False,
            use_textline_orientation=False,
            device="cpu"
        )

        print("PP-OCRv5 Mobile loaded successfully.")

    def extract(self, file_path: str):

        start_time = time.perf_counter()

        results = self.ocr.predict(file_path)

        pages = []

        for page_number, result in enumerate(results, start=1):

            raw = result.json

            if isinstance(raw, str):
                raw = json.loads(raw)

            data = raw.get("res", raw)

            texts = data.get("rec_texts", [])
            scores = data.get("rec_scores", [])
            boxes = data.get("rec_boxes", [])

            lines = []

            for i, text in enumerate(texts):

                box = (
                    boxes[i].tolist()
                    if hasattr(boxes[i], "tolist")
                    else boxes[i]
                ) if i < len(boxes) else []

                score = (
                    float(scores[i])
                    if i < len(scores) else 0
                )

                lines.append({
                    "text": text,
                    "confidence": round(score, 4),
                    "box": box
                })

            pages.append({
                "pageNumber": page_number,
                "lines": lines
            })

        return {
            "totalPages": len(pages),
            "processingTimeSeconds": round(
                time.perf_counter() - start_time, 2
            ),
            "pages": pages
        }

invoice_extractor = InvoiceExtractor()