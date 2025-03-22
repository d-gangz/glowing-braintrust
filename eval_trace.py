import braintrust
from dotenv import load_dotenv
from braintrust import Eval, init_dataset, traced
import random
import time

"""
This script is used to evaluate the performance of a prompt chain (2 prompts) but with structured output.
It uses the Braintrust API to invoke the prompts and dataset from the UI.

I've also included description and metadata to help in the eval script.

use this command to run the evaluation:
braintrust eval eval_trace.py
"""

# Load environment variables from .env file
load_dotenv()

# Replace these with your actual project name
project_name = "workflow-glowing"

@traced(type="function", metadata={"description": "Generate a random context for the story with a 1-second delay."})
def generate_random_context():
    """Generate a random context for the story with a 1-second delay."""
    contexts = [
        "In a world where shadows come alive at midnight",
        "On a space station orbiting a dying star",
        "During the last day before technology permanently stops working"
    ]
    
    # Add a 1-second delay to simulate processing time
    time.sleep(1)
    
    selected_context = random.choice(contexts)
    
    return selected_context

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
    
    # Generate a random context with a delay
    random_context = generate_random_context()
    
    # Second prompt - refines or extends the first output
    final_story = braintrust.invoke(
        project_name=project_name,
        slug="story-4omini-xtra",
        input={
            "outline": story_outline,
            "context": random_context
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
    experiment_name="prompt_chain_trace",
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
