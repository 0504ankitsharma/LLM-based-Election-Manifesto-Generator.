import streamlit as st
import langchain_helper
import os

st.set_page_config(page_title="Election Manifesto and Constituency Detail Generator", page_icon="🇮🇳")

st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-image: linear-gradient(to bottom, #FF9933, #FFFFFF, #138808);
        color: #000000; 
    }
    .sidebar .sidebar-content .block-container {
        padding: 20px;
    }
    .sidebar .sidebar-content .block-container .stButton>button {
        background-color: #138808;
        color: #FFFFFF; 
    }
    .sidebar .sidebar-content .stTextInput>div>div>input {
        background-color: #FFFFFF; 
        color: #000000; 
    }
    .stTextInput>div>div>label {
        color: #000000; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

def generate_campaign_page():
    st.title("Indian Election Manifesto and Constituency Detail Generator")

    party = st.sidebar.text_input("Party Name")
    candidate_name = st.sidebar.text_input("Candidate Name")
    constituency = st.sidebar.text_input("Constituency")
    campaign_focus = st.sidebar.text_input("Campaign Focus Point")

    if st.sidebar.button("Generate Campaign"):
        if party and candidate_name and constituency and campaign_focus:
            response = langchain_helper.generate_campaign_details(party, candidate_name, constituency, campaign_focus)
            
            st.header(f"Campaign Slogan for {candidate_name} ({party})")
            st.subheader(response['campaign_slogan'].strip())
            
            manifesto_items = response['manifesto_items'].strip().split(",")
            st.write("**Key Manifesto Points**")
            for item in manifesto_items:
                st.write("-", item.strip())
            
            st.write("**Constituency Information**")
            st.write(response['constituency_info'].strip())
            
            # Save the generated content
            file_name = f"{candidate_name}_{party}_campaign.txt"
            with open(file_name, "w") as file:
                file.write(f"Campaign Slogan: {response['campaign_slogan'].strip()}\n")
                file.write("Key Manifesto Points:\n")
                for item in manifesto_items:
                    file.write(f"- {item.strip()}\n")
                file.write("\nConstituency Information:\n")
                file.write(response['constituency_info'].strip())
            
            st.success(f"Campaign details saved successfully as {file_name}!")
        else:
            st.error("Please fill in all the details.")

def view_saved_campaigns_page():
    saved_files = [file for file in os.listdir() if file.endswith("_campaign.txt")]
    if saved_files:
        selected_file = st.sidebar.selectbox("Select a campaign file", saved_files)
        with open(selected_file, "r") as file:
            st.text(file.read())
    else:
        st.sidebar.write("No saved campaigns found.")

page = st.sidebar.radio("Navigation", ["Generate Campaign", "View Saved Campaigns"])

if page == "Generate Campaign":
    generate_campaign_page()
elif page == "View Saved Campaigns":
    view_saved_campaigns_page()
