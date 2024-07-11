FastAPI microservice for extracting data from PDF/JPG documents using Mindee OCR.

A FastAPI endpoint is implemented to handle file uploads. This endpoint acts as the entry point for your invoice processing tasks.

The endpoint is designed to accept file uploads using the multipart/form-data content type. This allows users to upload invoice documents directly from their local machines.

It can handle a variety of file formats commonly used for invoices. This includes:
Single-page and multi-page PDF documents
Image formats like JPEG

The API leverages Mindee's state-of-the-art OCR (Optical Character Recognition) engine to extract text from uploaded documents. 

File formats not supported by Mindee
Network errors during communication with Mindee's servers
By gracefully handling these errors, the API provides a more reliable and user-friendly experience.

After successful text extraction, the raw text data is transformed into a well-structured JSON format. This format is easy to parse and integrate with other applications or data analysis tools.

The extracted text undergoes a cleaning process to ensure it's ready for further processing. This cleaning might involve:
Removing extra spaces and line breaks

The API can identify digit characters within the extracted text. These characters are often crucial for invoice data, such as invoice numbers, totals, and tax amounts.
