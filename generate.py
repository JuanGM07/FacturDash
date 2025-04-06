import os
import random
import calendar
from datetime import datetime
from fpdf import FPDF

# Crear directorio para guardar PDFs
output_dir = "facturas_pdf"
os.makedirs(output_dir, exist_ok=True)

# Ruta a la fuente
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = os.path.join(BASE_DIR,"src", "static", "fonts", "DejaVuSans.ttf")

# Verificar si la fuente existe
assert os.path.exists(FONT_PATH), f"No se encontró la fuente en {FONT_PATH}"

# Datos ficticios
proveedores = ["Amazon", "IKEA", "Carrefour", "Mercadona", "Leroy Merlin"]
conceptos = ["Compra de suministros", "Material de oficina", "Reparaciones", "Servicios", "Renovaciones"]

class PDF(FPDF):
    def header(self):
        self.set_font("DejaVu", "", 14)
        self.cell(0, 10, "Factura", ln=True, align='C')

def generar_facturas():
    for mes in range(1, 13):
        for i in range(2):  # Dos facturas por mes
            proveedor = random.choice(proveedores)
            concepto = random.choice(conceptos)
            importe = round(random.uniform(100, 1000), 2)
            dia = random.randint(1, calendar.monthrange(2023, mes)[1])
            fecha = datetime(2023, mes, dia).strftime("%d/%m/%Y")

            pdf = PDF()
            pdf.add_font("DejaVu", "", FONT_PATH, uni=True)  # REGISTRAR PRIMERO
            pdf.set_font("DejaVu", "", 12)
            pdf.add_page()  # AHORA sí puedes agregar la página

            pdf.cell(100, 10, txt=f"Fecha: {fecha}", ln=True)
            pdf.cell(100, 10, txt=f"Proveedor: {proveedor}", ln=True)
            pdf.cell(100, 10, txt=f"Concepto: {concepto}", ln=True)
            pdf.cell(100, 10, txt=f"Importe: {importe} €", ln=True)

            filename = f"factura_{mes:02d}_{i+1}.pdf"
            pdf.output(os.path.join(output_dir, filename))

generar_facturas()
print("Facturas generadas en:", output_dir)
