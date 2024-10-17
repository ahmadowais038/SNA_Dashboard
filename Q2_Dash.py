import streamlit as st
import plotly.io as pio

def show():
    # Load Plotly JSON files
    fig = pio.read_json("./Visualizations/Concerns_about_cost.json")
    fig1 = pio.read_json("./Visualizations/AUS_Solar_Pannel_adoption.json")
    fig2 = pio.read_json("./Visualizations/Concerns_about_environment.json")
    fig3 = pio.read_json("./Visualizations/AUS_Concerns_about_Future_energy.json")
    fig4 = pio.read_json("./Visualizations/AUS_reasons_for_switching.json")

    st.header("Consumer Insights for Australia")
    
    # Display the top chart
    st.plotly_chart(fig, use_container_width=True)

    # Display columns
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig3, use_container_width=True)
    with col2:
        st.plotly_chart(fig4, use_container_width=True)

    col3, col4 = st.columns(2)
    with col3:
        st.plotly_chart(fig2, use_container_width=True)
    with col4:
        st.plotly_chart(fig1, use_container_width=True)