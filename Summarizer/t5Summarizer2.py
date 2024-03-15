# Import necessary libraries
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


def summarize_text_with_t5(text):
    """
    Summarizes text using Google's T5 model.

    Parameters:
    - text (str): The text to summarize.

    Returns:
    - str: The summarized text.
    """

    # Initialize the tokenizer and model for 't5-base'
    tokenizer = AutoTokenizer.from_pretrained('t5-base')
    model = AutoModelForSeq2SeqLM.from_pretrained('t5-base')

    # Prepare the text for summarization (prefix with "summarize: ")
    prep_text = "summarize: " + text

    # Tokenize the text
    inputs = tokenizer.encode(
        prep_text, return_tensors='pt', max_length=512, truncation=True)

    # Generate summary tokens
    summary_ids = model.generate(
        inputs, max_length=150, min_length=80, length_penalty=5.0, num_beams=2)

    # Decode and return the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary


# Example text
text = """The Solar System is a vast and intricate ensemble of celestial bodies, dominated by the Sun, a G-type main-sequence star that contains almost 99.9% of the system's total mass. It includes eight planets, their moons, and countless smaller bodies such as dwarf planets, asteroids, comets, and meteoroids. The planets, ordered by their distance from the Sun, are Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune. Each planet has its unique characteristics and moons, contributing to the diversity of the Solar System. For instance, Earth is the only planet known to support life, while Jupiter, the largest planet, boasts a massive 79 moons. The Solar System is also home to two major asteroid belts, with the main asteroid belt lying between Mars and Jupiter, serving as a boundary between the inner rocky planets and the outer gas giants. Beyond Neptune lies the Kuiper Belt, a region filled with icy bodies and dwarf planets such as Pluto, marking the edge of our Solar System before it fades into the interstellar medium. This cosmic neighborhood offers a glimpse into the processes that governed the formation and evolution of planetary systems, making it a focal point of scientific research and exploration."""

# Generate summary
summary = summarize_text_with_t5(text)

# Print the summarized text
print(summary)
