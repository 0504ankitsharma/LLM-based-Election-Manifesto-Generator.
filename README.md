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
```

###Install Dependencies

```sh
pip install -r requirements.txt
```

###Create a .env File

```sh
Create a .env file in the root directory with your OpenAI API key:

OPENAI_API_KEY=your_openai_api_key
```

###Run the Streamlit App

```sh
streamlit run main.py
```

