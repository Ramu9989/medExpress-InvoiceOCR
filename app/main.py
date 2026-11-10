 
from fastapi import FastAPI, UploadFile, File, HTTPException
from pathlib import Path
from app.invoice_extractor import invoice_extractor
import uuid
import os
import traceback
import time

app = FastAPI(
    title="medExpress Invoice AI",
    version="1.0.0"
)

BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = BASE_DIR / "uploads"

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

ALLOWED_EXTENSIONS = {".pdf", ".jpg", ".jpeg", ".png"}


@app.get("/health")
def health():
    return {
        "success": True,
        "service": "medExpress Invoice OCR",
        "status": "running"
    }


@app.post("/api/invoice/extract")
def extract_invoice(file: UploadFile = File(...)):

    print("\n========== INVOICE REQUEST RECEIVED ==========", flush=True)

    extension = Path(file.filename or "").suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Only PDF, JPG, JPEG and PNG files are supported."
        )

    file_path = UPLOAD_DIR / f"{uuid.uuid4()}{extension}"

    try:
        start_time = time.perf_counter()

        print(f"File: {file.filename}", flush=True)

        print("Saving uploaded file...", flush=True)

        with file_path.open("wb") as buffer:
            while chunk := file.file.read(1024 * 1024):
                buffer.write(chunk)

        print("Upload completed.", flush=True)
        print("Starting OCR extraction...", flush=True)

        result = invoice_extractor.extract(str(file_path))

        elapsed = round(time.perf_counter() - start_time, 2)

        print("OCR extraction completed.", flush=True)
        print(f"Total processing time: {elapsed} seconds", flush=True)

        return {
            "success": True,
            "message": "Invoice extraction completed",
            "totalProcessingTimeSeconds": elapsed,
            "data": result
        }

    except HTTPException:
        raise

    except Exception as ex:

        print("\n========== INVOICE OCR ERROR ==========", flush=True)
        print(str(ex), flush=True)
        traceback.print_exc()
        print("=======================================\n", flush=True)

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )

    finally:
        file.file.close()

        if file_path.exists():
            os.remove(file_path)

        print("Temporary file cleanup completed.", flush=True)
