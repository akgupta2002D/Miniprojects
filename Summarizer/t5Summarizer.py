# Import necessary libraries
from transformers import T5Tokenizer, T5ForConditionalGeneration


def summarize_text(text):
    """
    Summarize the given text using T5 transformer model.

    Parameters:
    - text (str): The text to summarize.

    Returns:
    - str: The summarized text.
    """

    # Initialize the tokenizer and model from the pre-trained 't5-small' version.
    # You can replace 't5-small' with other versions like 't5-base', 't5-large', 't5-3b', or 't5-11b' for better results.
    tokenizer = T5Tokenizer.from_pretrained('t5-base')
    model = T5ForConditionalGeneration.from_pretrained('t5-base')

    # Prepend the prefix "summarize: " to the text as T5 requires task-specific prefixes
    text = "summarize: " + text

    # Encode the text into tensor of tokens
    input_ids = tokenizer.encode(
        text, return_tensors="pt", max_length=512, truncation=True)

    # Generate the summary output tokens with the model
    summary_ids = model.generate(input_ids, max_length=150, min_length=40,
                                 length_penalty=2.0, num_beams=4, early_stopping=True)

    # Decode the summary tokens to a string
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary


# Example text to summarize
text = "The history of natural language processing (NLP) generally started in the 1950s, although work can be found from earlier periods. In 1950, Alan Turing published an article titled 'Computing Machinery and Intelligence' which proposed what is now called the Turing Test as a criterion of intelligence."

# Summarize the text
summary = summarize_text(text)

# Print the summarized text
print(summary)
