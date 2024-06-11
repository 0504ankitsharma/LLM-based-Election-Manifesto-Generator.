# Indian Election Manifesto Generator

## Overview

The Indian Election Manifesto Generator is a web application built with Streamlit and LangChain that generates election campaign details for Indian Lok Sabha elections. Utilizing OpenAI's GPT model, this application helps in creating campaign slogans, manifesto points, and constituency information based on user inputs.

## Features

- **User Input**: Enter party name, candidate name, constituency, and campaign focus point.
- **Campaign Generation**: Generate campaign slogans, manifesto points, and constituency information.
- **Data Privacy**: Secure storage of the OpenAI API key in a .env file, ignored in version control via .gitignore.
- **Dynamic UI**: Interactive and dynamic user interface provided by Streamlit for generating campaign details.

## Setup

### Clone the Repository

```sh
git clone https://github.com/yourusername/indian-election-campaign-generator.git

Install Dependencies

sh

pip install -r requirements.txt

Create a .env File

Create a .env file in the root directory with your OpenAI API key:

makefile

OPENAI_API_KEY=your_openai_api_key

Run the Streamlit App

sh

streamlit run main.py

Usage

    Input Details: Enter the required details in the sidebar (party name, candidate name, constituency, and campaign focus point).
    Generate Campaign: Click on the "Generate Campaign" button to create campaign details.
    View Results: See the generated campaign slogans, manifesto points, and constituency information on the main panel.
    Save Campaign: Optionally, save the campaign details to a text file.

Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

    Fork the repository.
    Create a new branch (git checkout -b feature-branch).
    Make your changes.
    Commit your changes (git commit -m 'Add some feature').
    Push to the branch (git push origin feature-branch).
    Open a pull request.
