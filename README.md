Indian Election Manifesto Generator

Overview

This project is a web application built with Streamlit and LangChain that generates election campaign details for Indian Lok Sabha elections. It utilizes OpenAI's GPT model to generate campaign slogans, manifesto points, and constituency information based on user inputs.
Features

    User Input: Users can input party name, candidate name, constituency, and campaign focus point.
    
    Campaign Generation: Upon user input, the application generates campaign slogans, manifesto points, and constituency information.
    
    Data Privacy: OpenAI API key is stored securely in a .env file and ignored in version control using .gitignore.
    
    Dynamic UI: The Streamlit app provides an interactive and dynamic user interface for generating campaign details.

Setup

    Clone the repository:

git clone https://github.com/yourusername/indian-election-campaign-generator.git

Install dependencies:

pip install -r requirements.txt

Create a .env file in the root directory with your OpenAI API key:

OPENAI_API_KEY=your_openai_api_key

Run the Streamlit app:

    streamlit run main.py

Usage

    Input the required details in the sidebar (party name, candidate name, constituency, and campaign focus point).
    
    Click on the "Generate Campaign" button to generate campaign details.
    
    View the generated campaign slogans, manifesto points, and constituency information on the main panel.
    
    Optionally, save the campaign details to a text file.

Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.s
