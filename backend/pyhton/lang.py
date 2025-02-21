import os
from langchain.prompts import PromptTemplate
from langchain.schema import LLMResult
from langchain_community.chat_models import ChatOllama  # Use updated import
from langchain_core.runnables import RunnableLambda

# Define your Ollama model
ollama_model = "llama3.2:3b"

# Define the prompt template
prompt_template = """
You are a sustainability expert. Given the following information about a solar energy project, calculate the total carbon offset in kilograms (kg) for the project.

Project Details:
- Number of Solar Panels: {num_panels}
- Capacity per Panel (kWh): {capacity_per_panel}
- Capacity Factor: {capacity_factor}
- Carbon Emission Factor (kg CO2 per kWh): 0.9

Formula:
Energy Generated (kWh) = Number of Panels * Capacity per Panel * Capacity Factor
CO2 Offset (kg) = Energy Generated * Carbon Emission Factor

Provide only the numerical value for the carbon offset.
"""

# Initialize the LLM
llm = ChatOllama(model=ollama_model)

# Create a LangChain prompt
prompt = PromptTemplate(template=prompt_template, input_variables=["num_panels", "capacity_per_panel", "capacity_factor"])

# Define a function to run the model
def run_model(inputs):
    return llm.invoke(prompt.format(**inputs))

# Define input values for the project
inputs = {
    "num_panels": 1000,
    "capacity_per_panel": 300,
    "capacity_factor": 0.15
}

# Run the chain
carbon_offset = run_model(inputs)
print(f"Calculated Carbon Offset: {carbon_offset}")
