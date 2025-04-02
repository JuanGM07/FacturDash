import os
import pandas as pd
import json
from flask import Flask, render_template
import plotly.express as px

app = Flask(__name__)

FACTURAS_DIR = "facturas"

def cargar_facturas():
    """Carga las facturas desde subcarpetas dentro de la carpeta 'facturas'."""
    all_files = []
    for root, dirs, files in os.walk(FACTURAS_DIR):
        for file in files:
            if file.endswith(".csv"):
                all_files.append(os.path.join(root, file))
    
    if not all_files:
        return None
    
    df_list = [pd.read_csv(f, delimiter=';', parse_dates=['fecha_factura'], dayfirst=True) for f in all_files]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

def generar_dashboard():
    df_total = cargar_facturas()
    if df_total is None:
        return None, None, 0, 0, 0, [], [], []
    
    total_facturas = len(df_total)
    total_importe = df_total["importe"].sum()
    gasto_promedio = total_importe / total_facturas if total_facturas else 0
    
    # Evolución mensual
    df_total['mes'] = df_total['fecha_factura'].dt.strftime('%Y-%m')
    gastos_mes = df_total.groupby('mes')["importe"].sum().reset_index()
    labels = gastos_mes["mes"].tolist()
    gastos = gastos_mes["importe"].tolist()
    fig_mes = px.bar(gastos_mes, x="mes", y="importe", title="Evolución Mensual de Gastos")
    
    # Gastos por proveedor
    gasto_proveedor = df_total.groupby("proveedor")["importe"].sum().reset_index()
    gasto_proveedor = gasto_proveedor.sort_values(by="importe", ascending=False).head(10)
    fig_proveedor = px.pie(gasto_proveedor, names="proveedor", values="importe", title="Gasto por Proveedor")
    
    # Facturas de mayor importe
    facturas_mayor_importe = df_total.sort_values(by="importe", ascending=False)[["fecha_factura", "importe"]].head(5).values.tolist()
    
    return fig_mes.to_json(), fig_proveedor.to_json(), total_facturas, total_importe, gasto_promedio, labels, gastos, facturas_mayor_importe

@app.route("/")
def index():
    fig_mes, fig_proveedor, total_facturas, total_importe, gasto_promedio, labels, gastos, facturas_mayor_importe = generar_dashboard()
    return render_template(
        "dashboard.html",
        total_facturas=total_facturas,
        total_importe=total_importe,
        gasto_promedio=gasto_promedio,
        fig_mes=fig_mes,
        fig_proveedor=fig_proveedor,
        labels=labels,
        gastos=gastos,
        facturas_mayor_importe=facturas_mayor_importe
    )

if __name__ == "__main__":
    app.run(debug=True)

