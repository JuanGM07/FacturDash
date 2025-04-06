import os
import fitz
import re
import pandas as pd

FACTURAS_DIR = "facturas_pdf"

def cargar_facturas():
    data = []
    for file in os.listdir(FACTURAS_DIR):
        if file.endswith(".pdf"):
            path = os.path.join(FACTURAS_DIR, file)
            text = ""
            with fitz.open(path) as doc:
                for page in doc:
                    text += page.get_text()

            # Extraer datos del texto
            try:
                fecha = re.search(r"Fecha:\s*(\d{2}/\d{2}/\d{4})", text).group(1)
                proveedor = re.search(r"Proveedor:\s*(.*)", text).group(1).strip()
                concepto = re.search(r"Concepto:\s*(.*)", text).group(1).strip()
                importe = float(re.search(r"Importe:\s*([\d,.]+)", text).group(1).replace(",", "."))
                data.append({
                    "fecha_factura": pd.to_datetime(fecha, dayfirst=True),
                    "proveedor": proveedor,
                    "concepto": concepto,
                    "importe": importe
                })
            except Exception as e:
                print(f"Error procesando {file}: {e}")

    if not data:
        return None

    return pd.DataFrame(data)