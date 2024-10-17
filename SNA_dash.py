import streamlit as st
import plotly.io as pio

def show():
    # Load Plotly JSON file
    fig = pio.read_json("./Visualizations/Renewable_Energy_SNA.json")

    # Display the chart
    st.header("Social Network Analysis of Renewable Energy Consumption in Australia")
    
    # expander for detailed insight and analysis
    with st.expander("ℹ️ Click here to learn more"):
        st.markdown("""
        This Social Network Analysis (SNA) diagram visualizes the interactions between stakeholders relating to renewable energy consumption
        This Analysis was based upon Energy Consumer Sentiment Survey dataset along with the AEMO, AEMC, AER, and ECA stakeholder review reports. 
        The analysis focuses on 3 major factors:
            - Communication/Collaboration
            - Satisfaction
            - Trust

        For this Visualization we will utilizing a Centrality of Consumers approach where the Consumer node is placed in the middle and the
        other stakeholders are analyzed in relation to the consumers. the Node size to show the Overall rating of the nodes given by consumers. 
        the Overall rating is calculated by weighting the three factors with trust holding the most weight and satisfaction the least as it 
        relates to short term. he distance between nodes will be based on trust scores, where higher trust results in closer proximity to the 
        central node (Consumers). Node color will be used to represent satisfaction ratings, making it easy to distinguish stakeholders with 
        varying satisfaction levels.Lastly, edge weights and thickness will correspond to the communication score, highlighting the strength 
        of communication between different stakeholders, with the score being what the target node has attributed to the source node.
        

        Key Insights:
        - Utility Companies had the worst satisfaction score.  
        - Governments have lowest communication and Trust score among Consumers.
        - Governments had the worst overall score with Regulators having the best
        """)
    
    # Display the chart below the expander
    st.plotly_chart(fig, use_container_width=True)