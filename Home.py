import streamlit as st

# Título de la aplicación
st.title("CALCULADORA DE MATERIALES PARA DRYWALL")
st.subheader("by Roberto Gonzalez")

# Cantidad de metros cuadrados
metros_cuadrados = st.number_input("Ingrese la cantidad de metros cuadrados a calcular:", min_value=0.0, value=3.0, step=0.1)

# Lista de materiales
materiales = [
    {
        "Material": "Plancha de Yeso RH(Resistente a la Humedad) de 1.22x2.44 m",
        "Cantidad": st.number_input("Cantidad de Planchas:", min_value=0, value=1),
        "Precio Unitario": st.number_input("Precio Unitario de Plancha de Yeso:", min_value=0.0, value=39.50, step=0.01),
    },
    {
        "Material": "Parante 89x38x0.45mm de 6 metro",
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

# Calcular el costo parcial de cada material y formatear números a dos decimales
for material in materiales:
    material["Parcial"] = "{:.2f}".format(material["Cantidad"] * material["Precio Unitario"])
    material["Precio Unitario"] = "{:.2f}".format(material["Precio Unitario"])

# Crear una lista de listas para la tabla dinámica
tabla_datos = [["Material", "Cantidad", "Precio Unitario", "Parcial"]]

# Llenar la lista de listas con los datos de los materiales
for material in materiales:
    tabla_datos.append([material["Material"], material["Cantidad"], material["Precio Unitario"], material["Parcial"]])

st.write("### RESULTADOS")

# Mostrar la tabla dinámica
st.table(tabla_datos)

# Calcular el costo total de los materiales
costo_total_materiales = sum(float(material["Parcial"]) for material in materiales)

# Calcular el costo total de los materiales por metro cuadrado
costo_por_metro_cuadrado = costo_total_materiales / (1.22 * 2.44)

# Mostrar el costo total de los materiales por metro cuadrado
st.write(f"**El costo total de los materiales por m2 ES: S/.{costo_por_metro_cuadrado:.2f}**")

# Calcular el costo total de los materiales con los precios actuales
costo_total_con_precios_actuales = costo_total_materiales * (metros_cuadrados / 3.0)

# Mostrar el costo total con precios actuales y la frase personalizada
st.subheader(f"**EL COSTO TOTAL DE {metros_cuadrados:.1f} m2 ES: S/.{costo_total_con_precios_actuales:.2f}**")
