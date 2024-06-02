import streamlit as st
import langchain_helper
import os

# Set page title and favicon
st.set_page_config(page_title="Indian Lok Sabha Election Campaign Generator", page_icon="🇮🇳")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-image: linear-gradient(to bottom right, #5C258D, #4389A2);
        color: white;
    }
    .sidebar .sidebar-content .block-container {
        padding: 20px;
    }
    .sidebar .sidebar-content .block-container .stButton>button {
        background-color: #009688;
    }
    .sidebar .sidebar-content .stTextInput>div>div>input {
        background-color: #E0E0E0;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set the title of the app
st.title("Indian Lok Sabha Election Campaign Generator")

# Add input fields for user input
party = st.sidebar.text_input("Party Name")
candidate_name = st.sidebar.text_input("Candidate Name")
constituency = st.sidebar.text_input("Constituency")
campaign_focus = st.sidebar.text_input("Campaign Focus Point")

# Generate the campaign details when the button is clicked
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

# Add an option to view saved campaigns
if st.sidebar.checkbox("View Saved Campaigns"):
    saved_files = [file for file in os.listdir() if file.endswith("_campaign.txt")]
    if saved_files:
        selected_file = st.sidebar.selectbox("Select a campaign file", saved_files)
        with open(selected_file, "r") as file:
            st.text(file.read())
    else:
        st.sidebar.write("No saved campaigns found.")
