import os
import random
import csv
from datetime import datetime, timedelta
import calendar

# Directorio donde se almacenarán las facturas
BASE_DIR = './facturas/'

# Lista de meses
MESES = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

# Lista de proveedores de ejemplo
PROVEEDORES = [
    "Proveedor A", "Proveedor B", "Proveedor C", "Proveedor D", "Proveedor E", 
    "Proveedor F", "Proveedor G", "Proveedor H", "Proveedor I", "Proveedor J"
]

# Lista de conceptos específicos
CONCEPTOS = ['Servicio de hosting', 'Compra de software', 'Consultoría TI', 'Desarrollo web', 'Mantenimiento de equipos']

# Función para generar una fecha aleatoria dentro de un mes
def generar_fecha_aleatoria(mes):
    year = datetime.now().year
    month = MESES.index(mes) + 1
    _, last_day = calendar.monthrange(year, month)
    primer_dia = datetime(year, month, 1)
    ultimo_dia = datetime(year, month, last_day)
    delta = ultimo_dia - primer_dia
    fecha_aleatoria = primer_dia + timedelta(days=random.randint(0, delta.days))
    return fecha_aleatoria.strftime('%d/%m/%Y')

# Función para generar una factura de forma aleatoria
def generar_factura(mes, numero_factura):
    fecha_factura = generar_fecha_aleatoria(mes)
    proveedor = random.choice(PROVEEDORES)
    concepto = random.choice(CONCEPTOS)
    importe = round(random.uniform(10.0, 1000.0), 2)
    moneda = "euros" if random.random() > 0.5 else "dolares"
    
    return {
        'fecha_factura': fecha_factura,
        'proveedor': proveedor,
        'concepto': concepto,
        'importe': importe,
        'moneda': moneda
    }

# Crear subcarpetas para cada mes y generar facturas
for mes in MESES:
    subcarpeta = os.path.join(BASE_DIR, mes)
    os.makedirs(subcarpeta, exist_ok=True)
    
    facturas_mes = []
    for i in range(5):  # Generamos 5 facturas por mes
        factura = generar_factura(mes, i + 1)
        facturas_mes.append(factura)
        
        # Guardar las facturas en un archivo CSV dentro de la subcarpeta correspondiente
        archivo_csv = os.path.join(subcarpeta, f"facturas_{mes}.csv")
        with open(archivo_csv, mode='a', newline='') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=factura.keys(), delimiter=';')
            if archivo.tell() == 0:
                writer.writeheader()
            writer.writerow(factura)
    
    print(f"Facturas generadas para el mes de {mes}")