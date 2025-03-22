import braintrust
from dotenv import load_dotenv
from braintrust import Eval, init_dataset

"""
This script is used to evaluate the performance of a prompt chain (2 prompts) but with structured output.
It uses the Braintrust API to invoke the prompts and dataset from the UI.

I've also included description and metadata to help in the eval script.

use this command to run the evaluation:
braintrust eval eval_dataset.py
"""

# Load environment variables from .env file
load_dotenv()

# Replace these with your actual project name
project_name = "workflow-glowing"

# Define the task function that chains the two prompts
def chain_task(input_data):
    # First prompt - generates initial content based on genre and context
    # The response is a structured dictionary with 'reason' and 'outline' fields
    story_outline_response = braintrust.invoke(
        project_name=project_name,
        slug="storyoutline-geminiflash001-so",
        input={
            "genre": input_data["genre"],
            "context": input_data["context"]
        }
    )
    
    # Extract the outline directly from the dictionary, if doesn't exist, return empty string
    story_outline = story_outline_response.get("outline", "")
    
    # Second prompt - refines or extends the first output
    final_story = braintrust.invoke(
        project_name=project_name,
        slug="story-4omini",
        input={
            "outline": story_outline
        }
    )
    
    # Return the final output for Braintrust
    return final_story

# Create and run the evaluation
eval_task = Eval(
    project_name,
    # Initialize the dataset from Braintrust UI
    data=init_dataset(project=project_name, name="story-input"),
    task=chain_task,
    scores=[],
    experiment_name="prompt_chain_evaluation_structured_output",
    # Note that you cannot add description. Not sure why. But you can add others like metadata.
    metadata={
        "model_1": "gemini-flash-001",
        "model_2": "4o-mini",
        "dataset": "story_input",
        "chain_length": 2
    }
)

# If you want to run the evaluation directly from this script
if __name__ == "__main__":
    eval_task.run()
