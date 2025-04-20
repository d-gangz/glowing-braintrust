import braintrust
from dotenv import load_dotenv
from braintrust import traced, init_logger
# Import helper functions
from suggested_helper_functions import value_extractor, rag_data

load_dotenv()

# <ai_context>
# This file defines the main function `generate_suggested_response` which orchestrates calls to Braintrust prompts
# to generate a suggested response based on conversation history and other inputs.
# It imports helper functions `value_extractor` and `rag_data` from `suggested_helper_functions.py` to provide necessary context.
# Updated to be a generator function that yields streamed response chunks.
# </ai_context>

logger = init_logger(project="suggested-response")

project_name = "suggested-response"

def generate_suggested_response(
    salutation: str,
    last_name: str,
    conversation: str,
    current_date_time: str,
    unit_open_issues_max_limit: str,
):
    """
    Generates a suggested response based on conversation context and predefined guidelines, yielding chunks as they arrive.

    Args:
        salutation: The salutation for the guest (e.g., "Mr.", "Ms.").
        last_name: The last name of the guest.
        conversation: The conversation history.
        current_date_time: The current date and time.
        unit_open_issues_max_limit: The time limit for open issues.

    Yields:
        str: Chunks of the generated suggested response text.
    """

    extracted_values = value_extractor()

    # Prompt that generates a response based on the input of type string.
    open_issues_response = braintrust.invoke(
        project_name=project_name,
        slug="open-issues-handler-8ae1",
        input={
            "brand_customer_term": extracted_values["brand_customer_term"],
            "conversation": conversation,
            "current_date_time": current_date_time,
            "unit_name": extracted_values["unit_name"],
            "unit_open_issues_max_limit": unit_open_issues_max_limit,
            "unit_term": extracted_values["unit_term"],
        }
    )

    rag_data_output = rag_data(open_issues_response) # Pass the response, though it's not used yet

    """
    # Prompt that generates a response based on the input that is a json object like below.

    {
      "reason": "Guest's most recent message is in English.",
      "language": "English"
    }
    """
    language_selection_response = braintrust.invoke(
        project_name=project_name,
        slug="language-selection-handler-1bb5",
        input={
            "brand_customer_term": extracted_values["brand_customer_term"],
            "conversation": conversation,
            "unit_name": extracted_values["unit_name"],
        }
    )

    # Prompt that generates a suggested response based on the input of type string.
    generated_response = braintrust.invoke(
        project_name=project_name,
        slug="suggested-response-generator-f95c",
        input={
            "brand_communication_guidelines": extracted_values["brand_communication_guidelines"],
            "brand_customer_term": extracted_values["brand_customer_term"],
            "brand_response_guidelines": extracted_values["brand_response_guidelines"],
            "conversation": conversation,
            "current_date_time": current_date_time, # Use function input
            "knowledge_base": rag_data_output["knowledge_base"],
            "language": language_selection_response['language'], # Assuming language is in the language field
            "last_name": last_name, # Use function input
            "open_issues": open_issues_response, # The output is just a string. 
            "quick_replies": rag_data_output["quick_replies"],
            "salutation": salutation, # Use function input
            "unit_communication_guidelines": extracted_values["unit_communication_guidelines"],
            "unit_name": extracted_values["unit_name"],
            "unit_response_guidelines": extracted_values["unit_response_guidelines"],
            "unit_specific_information": extracted_values["unit_specific_information"],
            "unit_term": extracted_values["unit_term"]
        },
        stream=True
    )

    # Yield each chunk's data as it arrives
    for chunk in generated_response:
        if chunk.data:
            yield chunk.data # Yield the text data from the chunk

# Example usage with dummy data
if __name__ == "__main__":
    dummy_data = {
        "salutation": "Ms.",
        "last_name": "Chan",
        "conversation": (
            "[2025-01-03 13:45:03] Guest: 澄雲吃啥啊 \\n"
            "[2025-01-03 13:48:15] Guest: 澄雲吃什麼啊 \\n"
            "[2025-01-03 13:53:17] You: 下午好，Ms. Chan。澄雲提供單點菜單以供選擇。"
            "您可以在我們的Manor Club享用。若您需要更多資訊或協助，請隨時告訴我們。 \\n"
            "[2025-01-03 18:01:37] Guest: 澄云供应哪种类型的食物？ \\n"
            "[2025-01-03 18:02:19] You: 晚上好，Ms. Chan。澄云提供单点菜单，您可以在我们的Manor Club享用。"
            "若您需要更多信息或协助，请随时告知我们。 \\n"
            "[2025-01-05 13:26:42] Guest: What should I have for lunch at your hotel? \\n"
            "[2025-01-05 13:27:13] You: Good afternoon, Ms. Chan. For lunch at our hotel, you have a "
            "variety of options to choose from. You can enjoy a la carte dining at the Manor Club on the "
            "40th floor, or explore our diverse restaurant offerings on Level 5, including The Legacy House "
            "for refined Cantonese cuisine, Henry for American grill, Bayfare Social for Spanish tapas, "
            "Chaat for Indian cuisine, and XX for Western dishes. Additionally, on Level G, Blu House offers "
            "casual Italian cuisine, and MARMO Bistro serves French classics. Please let us know if you would "
            "like more information or assistance with reservations. \\n"
            "[2025-01-06 17:59:14] Guest: when the pool open? \\n"
        ),
        "current_date_time": "2025-01-06 17:59:26",
        "unit_open_issues_max_limit": "4 hours"
    }

    # Wrap the generator consumption in a traced function
    @traced(type="task", name="suggested response stream", metadata={"description": "Generate a suggested response based on conversation context and predefined guidelines."})
    def run_and_print_stream(data):
        suggested_response_generator = generate_suggested_response(
            salutation=data["salutation"],
            last_name=data["last_name"],
            conversation=data["conversation"],
            current_date_time=data["current_date_time"],
            unit_open_issues_max_limit=data["unit_open_issues_max_limit"]
        )

        # Print the streamed output chunk by chunk as yielded by the generator
        print("Streaming suggested response:")
        full_response_for_log = ""
        for chunk_data in suggested_response_generator: # Iterate over the generator
            print(chunk_data, end="", flush=True) # Print each chunk without newline, flush immediately
            full_response_for_log += chunk_data
        print() # Print a final newline
        # Return the full response so it's logged in the trace output
        return {"final_streamed_output": full_response_for_log}

    # Execute the traced function
    run_and_print_stream(dummy_data)