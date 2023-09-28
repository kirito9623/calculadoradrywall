import streamlit as st

# Título de la aplicación
st.title("CALCULADORA DE MATERIALES Y COSTOS PARA DRYWALL")
st.subheader("by Roberto Gonzalez")

# Cantidad de metros cuadrados
metros_cuadrados = st.number_input("Ingrese la cantidad de M2 a calcular:", min_value=0.0, value=3.0, step=0.1)

# Mano de obra por metro cuadrado
mano_obra_por_metro = st.number_input("Costo Mano de obra x m2 (S/.):", min_value=0.0, value=10.0, step=1.0)

# Pintura por metro cuadrado
pintura_por_metro_cuadrado = st.number_input("Costo de Pintado x m2 (S/.):", min_value=0.0, value=5.0, step=0.5)

# Empaste por metro cuadrado
empaste_por_metro_cuadrado = st.number_input("Costo de Empastado x m2 (S/.):", min_value=0.0, value=7.0, step=0.5)

st.subheader("Instalaciones Eléctricas")

# Cantidad de mano de obra para la instalación de puntos de tomacorriente
cantidad_mano_obra_puntos_tomacorriente = st.number_input("Cantidad de tomacorrientes a instalar:", min_value=0, value=1)

# Cantidad de mano de obra para la instalación de interruptores
cantidad_mano_obra_interruptores = st.number_input("Cantidad de interruptores a instalar:", min_value=0, value=1)

# Cantidad de mano de obra para la instalación de puntos de iluminación
cantidad_mano_obra_puntos_iluminacion = st.number_input("Cantidad de luminarias a instalar:", min_value=0, value=1)

# Mano de obra para la instalación de puntos de tomacorriente por metro cuadrado
mano_obra_puntos_tomacorriente = st.number_input("Costo Unitario de instalación x Tomacorriente(S/.):", min_value=0.0, value=15.0, step=1.0)

# Mano de obra para la instalación de interruptores por metro cuadrado
mano_obra_interruptores = st.number_input("Costo Unitario de instalación x Interruptor (S/.):", min_value=0.0, value=12.0, step=1.0)

# Mano de obra para la instalación de puntos de iluminación por metro cuadrado
mano_obra_puntos_iluminacion = st.number_input("Costo Unitario de instalación x Luminaria (S/.):", min_value=0.0, value=20.0, step=1.0)

# Apartado de MATERIALES
st.write("## MATERIALES")

# Lista de materiales
materiales = [
    {
        "Material": "Plancha de Yeso RH(Resistente a la Humedad) de 1.22x2.44 m",
        "Cantidad": st.number_input("Cantidad de Planchas:", min_value=0, value=1),
        "Precio Unitario": st.number_input("Precio Unitario de Plancha de Yeso:", min_value=0.0, value=39.50, step=0.01),
    },
    {
        "Material": "Parante 89x38x0.45mm de 6 metros",
        "Cantidad": st.number_input("Cantidad de Parantes:", min_value=0, value=6),
        "Precio Unitario": st.number_input("Precio Unitario de Parante:", min_value=0.0, value=11.97, step=0.01),
    },
    {
        "Material": "Riel 90x25x0.45mm x 3 metros",
        "Cantidad": st.number_input("Cantidad de Rieles:", min_value=0, value=2),
        "Precio Unitario": st.number_input("Precio Unitario de Riel:", min_value=0.0, value=9.96, step=0.01),
    },
    {
        "Material": "Tornillos de Punta Fina 6mmx1\"",
        "Cantidad": st.number_input("Cantidad de Tornillos Punta Fina:", min_value=0, value=48),
        "Precio Unitario": st.number_input("Precio Unitario de Tornillos Punta Fina:", min_value=0.0, value=5.50, step=0.01),
    },
    {
        "Material": "Tornillos Wafer 8mmx1/2\"",
        "Cantidad": st.number_input("Cantidad de Tornillos Wafer:", min_value=0, value=26),
        "Precio Unitario": st.number_input("Precio Unitario de Tornillos Wafer:", min_value=0.0, value=5.00, step=0.01),
    },
]

# Materiales relacionados con la electricidad
materiales_electricidad = [
    {
        "Material": "Cable eléctrico 12 AWG",
        "Cantidad": st.number_input("Cantidad de Cable 12 AWG (metros):", min_value=0, value=50),
        "Precio Unitario": st.number_input("Precio Unitario de Cable 12 AWG (S/. por metro):", min_value=0.0, value=2.50, step=0.01),
    },
    {
        "Material": "Tomacorrientes",
        "Cantidad": st.number_input("Cantidad de Tomacorrientes:", min_value=0, value=5),
        "Precio Unitario": st.number_input("Precio Unitario de Tomacorrientes (S/. por unidad):", min_value=0.0, value=4.00, step=0.01),
    },
    {
        "Material": "Interruptores",
        "Cantidad": st.number_input("Cantidad de Interruptores:", min_value=0, value=5),
        "Precio Unitario": st.number_input("Precio Unitario de Interruptores (S/. por unidad):", min_value=0.0, value=3.50, step=0.01),
    },
    {
        "Material": "Luminarias",
        "Cantidad": st.number_input("Cantidad de Luminarias:", min_value=0, value=8),
        "Precio Unitario": st.number_input("Precio Unitario de Luminarias (S/. por unidad):", min_value=0.0, value=12.00, step=0.01),
    },
]

# Agregar materiales de electricidad a la lista de materiales existente
materiales.extend(materiales_electricidad)

# Calcular el costo parcial de cada material y formatear números a dos decimales
for material in materiales:
    material["Parcial"] = material["Cantidad"] * material["Precio Unitario"]
    material["Precio Unitario"] = "{:.2f}".format(material["Precio Unitario"])
    material["Parcial"] = "{:.2f}".format(material["Parcial"])

# Calcular el costo de la mano de obra
costo_mano_obra = mano_obra_por_metro * metros_cuadrados
costo_mano_obra_puntos_tomacorriente = mano_obra_puntos_tomacorriente * cantidad_mano_obra_puntos_tomacorriente
costo_mano_obra_interruptores = mano_obra_interruptores * cantidad_mano_obra_interruptores
costo_mano_obra_puntos_iluminacion = mano_obra_puntos_iluminacion * cantidad_mano_obra_puntos_iluminacion

# Crear listas para la tabla de costos de mano de obra
mano_de_obra_table = [
    ["Concepto", "Cantidad", "Costo Unitario (S/.)", "Costo Parcial (S/.)"],
    ["Mano de Obra por m2", metros_cuadrados, mano_obra_por_metro, "{:.2f}".format(costo_mano_obra)],
    ["Mano de Obra para Tomacorrientes", cantidad_mano_obra_puntos_tomacorriente, mano_obra_puntos_tomacorriente, "{:.2f}".format(costo_mano_obra_puntos_tomacorriente)],
    ["Mano de Obra para Interruptores", cantidad_mano_obra_interruptores, mano_obra_interruptores, "{:.2f}".format(costo_mano_obra_interruptores)],
    ["Mano de Obra para Iluminación", cantidad_mano_obra_puntos_iluminacion, mano_obra_puntos_iluminacion, "{:.2f}".format(costo_mano_obra_puntos_iluminacion)]
]

# Calcular el costo total de la mano de obra
costo_total_mano_de_obra = sum(float(row[3]) for row in mano_de_obra_table[1:])

# Crear listas para la tabla de costos de materiales
materiales_table = [
    ["Material", "Cantidad", "Precio Unitario (S/.)", "Costo Parcial (S/.)"],
]

for material in materiales:
    materiales_table.append([material["Material"], material["Cantidad"], material["Precio Unitario"], material["Parcial"]])

# Calcular el costo total de los materiales
costo_total_materiales = sum(float(material["Parcial"]) for material in materiales)

# Crear una tabla dinámica para los costos de mano de obra
st.write("## RESUMEN DE MANO DE OBRA")
st.table(mano_de_obra_table)

# Crear una tabla dinámica para los costos de materiales
st.write("## RESUMEN DE MATERIALES")
st.table(materiales_table)

# Mostrar el costo total de mano de obra y materiales
st.write("## RESULTADOS")
st.subheader(f"**Costo Total de Mano de Obra : S/.{costo_total_mano_de_obra:.2f}**")
st.subheader(f"**Costo Total de Materiales para {metros_cuadrados:.1f} m2 es: S/.{costo_total_materiales:.2f}**")

# Calcular el costo total del proyecto
costo_total_proyecto = costo_total_mano_de_obra + costo_total_materiales

# Mostrar el costo total del proyecto
st.subheader(f"**COSTO TOTAL DEL PROYECTO: S/.{costo_total_proyecto:.2f}**")
