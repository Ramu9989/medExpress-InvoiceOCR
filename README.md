# medExpress Invoice OCR

**Offline AI-Powered Invoice OCR and Document Extraction Service**

medExpress Invoice OCR is a Python-based document processing service designed for hospital management and pharmacy software. It uses PaddleOCR, PP-StructureV3 and FastAPI to process supplier invoices and extract structured information.

## Key Features

- Offline invoice processing.
- PDF and image upload support.
- OCR text recognition.
- Document layout analysis.
- Table recognition.
- Text coordinates and confidence scores.
- Structured JSON output.
- FastAPI REST API.
- Integration-ready for .NET 8 applications.
- Designed for manual verification before saving invoices.

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python 3.11 |
| OCR Framework | PaddleOCR |
| Advanced Document Engine | PP-StructureV3 |
| Deep Learning Framework | PaddlePaddle |
| API Framework | FastAPI |
| API Server | Uvicorn |
| Integration | ASP.NET Core .NET 8 |
| Database | Microsoft SQL Server |

## Project Structure

```text
InvoiceOCRService/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── invoice_extractor.py
│   ├── invoice_extractor_advance.py
│   └── schemas.py
│
├── uploads/
├── results/
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements

- Python 3.11
- Windows 10/11 or compatible Linux environment
- Minimum 8 GB RAM recommended for initial testing
- CPU or compatible NVIDIA GPU
- Internet connection for initial dependency and model downloads

After installation and model downloads, invoice inference can run offline.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Ramu9989/medExpress-InvoiceOCR.git

cd medExpress-InvoiceOCR
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

Windows:

```powershell
.\venv\Scripts\activate
```

Linux:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install --upgrade pip

pip install -r requirements.txt
```

For PP-StructureV3 document parsing dependencies, if they are not already included:

```bash
python -m pip install "paddleocr[doc-parser]"
```

## Run the Application

Start the FastAPI service from the project root:

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

For development with automatic reload:

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

## API Endpoints

### Health Check

**GET**

```text
http://127.0.0.1:8000/health
```

Checks whether the OCR service is running.

### Invoice Extraction

**POST**

```text
http://127.0.0.1:8000/api/invoice/extract
```

Content type:

```text
multipart/form-data
```

Parameter:

| Parameter | Type | Description |
|---|---|---|
| file | File | Invoice PDF or image |

Supported formats:

- PDF
- JPG
- JPEG
- PNG

### Swagger API Documentation

```text
http://127.0.0.1:8000/docs
```

Use Swagger UI to upload invoices and test the extraction endpoint.

## Invoice Extraction Workflow

```text
Supplier Invoice
       |
       v
FastAPI File Upload
       |
       v
PaddleOCR / PP-StructureV3
       |
       v
Text Recognition
       |
       v
Document Layout Analysis
       |
       v
Table Recognition
       |
       v
Structured Extraction
       |
       v
JSON Response
       |
       v
.NET 8 Invoice Review
       |
       v
Manual Approval
       |
       v
SQL Server Purchase Invoice
```

## Planned Invoice Data Extraction

### Supplier Details

- Supplier Name
- Supplier GSTIN
- Supplier Address
- Drug License Number

### Invoice Details

- Invoice Number
- Invoice Date
- Invoice Type
- Customer Name
- Customer GSTIN

### Medicine Details

- Manufacturer
- Medicine Name
- Product Code
- Pack Size
- Batch Number
- Expiry Date
- Quantity
- Free Quantity
- MRP
- Purchase Rate
- Discount
- GST Percentage
- HSN Code
- Item Amount

### Financial Details

- Subtotal
- Discount Amount
- CGST
- SGST
- IGST
- GST Amount
- Round Off
- Net Payable

## .NET 8 Integration

The FastAPI service is designed to communicate with the hospital management system through REST APIs.

The planned integration workflow:

1. .NET 8 uploads a supplier invoice to FastAPI.
2. Python processes the invoice.
3. FastAPI returns structured JSON.
4. .NET 8 displays extracted supplier and medicine details.
5. The user verifies medicine names, batches, expiry dates and financial values.
6. The user approves the invoice.
7. The approved purchase invoice is saved to SQL Server.

**Invoices must be reviewed and approved by an authorized user before being saved.**

## Model Information

The repository includes the following OCR implementations:

- PP-OCRv5 Mobile: lightweight text detection and recognition.
- PP-StructureV3: advanced document layout and table recognition.

The active engine depends on the extractor imported by `app/main.py`. Confirm the configured extractor before deployment.

Model files are downloaded and cached locally during initial setup. They should not be committed to GitHub.

## Security and Data Handling

- Do not commit supplier invoices or patient-related documents.
- Do not commit API credentials or environment files.
- Keep uploaded documents and generated results out of Git.
- Restrict access to the OCR API in production.
- Use HTTPS and appropriate authentication when connecting to hospital applications.
- Validate extracted financial data before posting transactions.

## Current Development Status

- [x] FastAPI service
- [x] Invoice upload API
- [x] PaddleOCR Mobile implementation
- [x] Initial GitHub repository
- [ ] PP-StructureV3 production testing
- [ ] Medicine table reconstruction
- [ ] Supplier and invoice field extraction
- [ ] GST and financial validation
- [ ] .NET 8 integration
- [ ] SQL Server purchase invoice integration
- [ ] Manual approval workflow

## Repository

GitHub: https://github.com/Ramu9989/medExpress-InvoiceOCR

## License

License and distribution terms to be determined.
