from fastapi import FastAPI, File, UploadFile, HTTPException
from mindee import Client, product
import uvicorn
from mindee import Client, PredictResponse, product




def parse_invoice_pdf(file_path):


    mindee_client = Client(api_key="f663365e1c54409be6447257c3a14013")


    input_doc = mindee_client.source_from_path(file_path)

    result: PredictResponse = mindee_client.parse(product.InvoiceV4, input_doc)
    final_result= {}
    for i, page in enumerate(result.document.inference.pages):
        current_page={}
        invoice_number = page.prediction.invoice_number
        total_amount= page.prediction.total_amount
        total_net= page.prediction.total_net
        total_tax = page.prediction.total_tax
        # print(invoice_number)
        # print(type(invoice_number), type(total_amount), type(total_net), type(total_tax))
        current_page["invoice_number"]= invoice_number
        current_page["total_amount"]=total_amount
        current_page["total_net"] = total_net
        current_page["total_tax"] =total_tax
        final_result[i+1]=current_page
    return final_result
    


