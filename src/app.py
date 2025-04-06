import os
import pandas as pd
from flask import Flask, render_template
from datetime import datetime
from extractor import cargar_facturas

app = Flask(__name__)

FACTURAS_DIR = "facturas_pdf"

def generar_dashboard():
    df = cargar_facturas()
    if df.empty:
        return {}

    df['mes'] = df['fecha_factura'].dt.strftime('%Y-%m')
    
    # Métricas clave
    total_facturas = len(df)
    total_importe = df["importe"].sum()
    gasto_promedio = round(total_importe / total_facturas, 2)
    importe_max = df["importe"].max()
    importe_min = df["importe"].min()
    desviacion = round(df["importe"].std(), 2)
    total_proveedores = df["proveedor"].nunique()
    # Gastos por concepto
    gasto_concepto = df.groupby("concepto")["importe"].sum().reset_index()
    gasto_concepto = gasto_concepto.sort_values(by="importe", ascending=False).head(5)
    concepto_data = round(gasto_concepto[['concepto', 'importe']],2).values.tolist()  # Convertir a lista

    # Evolución mensual
    gastos_mes = df.groupby('mes')["importe"].sum().reset_index()
    labels_mes = gastos_mes["mes"].tolist()
    datos_mes = gastos_mes["importe"].tolist()

    # Gasto por proveedor
    gasto_proveedor = df.groupby("proveedor")["importe"].sum().reset_index()
    gasto_proveedor = gasto_proveedor.sort_values(by="importe", ascending=False).head(5)

    # Facturas más caras
    facturas_top = df.sort_values(by="importe", ascending=False)[["fecha_factura", "importe"]].head(5).values.tolist()

    return {
        "total_facturas": total_facturas,
        "total_importe": total_importe,
        "gasto_promedio": gasto_promedio,
        "importe_max": importe_max,
        "importe_min": importe_min,
        "desviacion": desviacion,
        "total_proveedores": total_proveedores,
        "labels_mes": labels_mes,
        "datos_mes": datos_mes,
        "gasto_proveedor": gasto_proveedor.values.tolist(),
        "facturas_top": facturas_top,
        "concepto_data":concepto_data
    }

@app.route("/")
def index():
    data = generar_dashboard()
    return render_template("dashboard.html", **data)

if __name__ == "__main__":
    app.run(debug=True)
