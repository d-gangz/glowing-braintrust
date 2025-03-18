import braintrust
from dotenv import load_dotenv
from braintrust import Eval

"""
This script is used to evaluate the performance of a prompt chain (2 prompts).
It uses the Braintrust API to invoke the prompts from the UI.

use this command to run the evaluation:
braintrust eval eval_prompts.py
"""

# Load environment variables from .env file
load_dotenv()

# Replace these with your actual project name
project_name = "workflow-glowing"

# Define the dataset with genre and context for testing
dataset = [
    {
        "input": {
            "genre": "science fiction",
            "context": "space exploration in the distant future"
        }
    },
    {
        "input": {
            "genre": "romance",
            "context": "two people from different backgrounds meet in a small town"
        }
    },
    {
        "input": {
            "genre": "thriller",
            "context": "mysterious disappearances in a quiet suburban neighborhood"
        }
    }
]

# Define the task function that chains the two prompts
def chain_task(input_data):
    # First prompt - generates initial content based on genre and context
    # Note that braintrust.invoke returns a string, not a dictionary.
    story_outline = braintrust.invoke(
        project_name=project_name,
        slug="storyoutline-geminiFlash001",
        input={
            "genre": input_data["genre"],
            "context": input_data["context"]
        }
    )
    
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
    # lambda is used to lazily load the dataset. This is particularly useful when your dataset is large, as it prevents loading the entire dataset into memory until it's actually needed during evaluation. It's a common pattern in Braintrust to wrap datasets with a lambda.
    data=lambda: dataset,
    task=chain_task,
    scores=[],
    experiment_name="prompt_chain_evaluation"
)

# If you want to run the evaluation directly from this script
if __name__ == "__main__":
    eval_task.run()
