from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Ensure the environment variable is set
openai_api_key = os.getenv('OPENAI_API_KEY')
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")

os.environ['OPENAI_API_KEY'] = openai_api_key

llm = OpenAI(temperature=0.7)

def generate_campaign_details(party, candidate, constituency, focus):
    # Chain 1: Campaign Slogan
    prompt_template_slogan = PromptTemplate(
        input_variables=['party', 'candidate', 'focus'],
        template="I am {candidate} running an election campaign for the {party} party in India with a focus on {focus}. Suggest a catchy campaign slogan for this."
    )

    slogan_chain = LLMChain(llm=llm, prompt=prompt_template_slogan, output_key="campaign_slogan")

    # Chain 2: Manifesto Items
    prompt_template_manifesto = PromptTemplate(
        input_variables=['campaign_slogan', 'party', 'candidate', 'focus'],
        template="""Based on the campaign slogan "{campaign_slogan}" and the focus area of {focus}, suggest some key points for the {party} party's manifesto for {candidate}'s campaign. Return it as a comma-separated string."""
    )

    manifesto_chain = LLMChain(llm=llm, prompt=prompt_template_manifesto, output_key="manifesto_items")

    # Chain 3: Constituency Information
    prompt_template_constituency = PromptTemplate(
        input_variables=['constituency'],
        template="Provide some important information and key issues about the constituency of {constituency}."
    )

    constituency_chain = LLMChain(llm=llm, prompt=prompt_template_constituency, output_key="constituency_info")

    chain = SequentialChain(
        chains=[slogan_chain, manifesto_chain, constituency_chain],
        input_variables=['party', 'candidate', 'constituency', 'focus'],
        output_variables=['campaign_slogan', 'manifesto_items', 'constituency_info']
    )

    response = chain({'party': party, 'candidate': candidate, 'constituency': constituency, 'focus': focus})

    return response
