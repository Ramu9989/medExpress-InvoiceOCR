
import os
import json
import time
from pathlib import Path

# Set before importing PaddleOCR
os.environ["PADDLE_PDX_ENABLE_MKLDNN_BYDEFAULT"] = "False"

from paddleocr import PPStructureV3


class InvoiceExtractor:

    def __init__(self):

        print("Loading PP-StructureV3...", flush=True)

        self.pipeline = PPStructureV3(
            use_doc_orientation_classify=False,
            use_doc_unwarping=False,
            use_textline_orientation=False,
            use_table_recognition=True,
            device="cpu"
        )

        print("PP-StructureV3 loaded successfully.", flush=True)

    def extract(self, file_path: str):

        start_time = time.perf_counter()

        print("Starting PP-StructureV3 prediction...", flush=True)

        results = self.pipeline.predict(file_path)

        pages = []

        for page_number, result in enumerate(results, start=1):

            raw = result.json

            if callable(raw):
                raw = raw()

            if isinstance(raw, str):
                raw = json.loads(raw)

            if not isinstance(raw, dict):
                raw = {"result": str(raw)}

            pages.append({
                "pageNumber": page_number,
                "structure": raw
            })

        elapsed = round(time.perf_counter() - start_time, 2)

        return {
            "engine": "PP-StructureV3",
            "totalPages": len(pages),
            "processingTimeSeconds": elapsed,
            "pages": pages
        }


invoice_extractor = InvoiceExtractor()
