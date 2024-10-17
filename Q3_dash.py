import streamlit as st
import plotly.io as pio

def show():
    # Load Plotly JSON files
    fig = pio.read_json("./Visualizations/Australia_and_Japan_Consumption.json")
    fig1 = pio.read_json("./Visualizations/Australia_Hydro_and_Wind_renewables.json")
    fig2 = pio.read_json("./Visualizations/Japan_Hydro_and_Wind_renewables.json")

    # Display the top chart
    st.subheader("Renewable Energy Consumption projections for Australia and Japan")
    st.plotly_chart(fig, use_container_width=True)

    # Display columns
    st.subheader("Australia and Japan Solar and Hydro forecasts")
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        st.plotly_chart(fig2, use_container_width=True)