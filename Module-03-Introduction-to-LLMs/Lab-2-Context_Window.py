
#
# Lab 2: Managing Input for the Context Window (Chunking)
#
# Objective: Learn how to process documents that are larger than the model's
# context window by breaking them into smaller pieces ("chunks").
#
# You can run this notebook directly in Google Colab.
#

# Step 1: Install and configure the API
!pip install -q google-generativeai
import google.generativeai as genai
import os

try:
    from google.colab import userdata
    GEMINI_API_KEY = userdata.get('GEMINI_API_KEY')
    genai.configure(api_key=GEMINI_API_KEY)
    print("Successfully configured the API key!")
except ImportError:
    print("Not in a Colab environment. Please set the GEMINI_API_KEY environment variable.")


# Step 2: Define the Model
# We can use a powerful model for this task.
model = genai.GenerativeModel('gemini-1.5-flash')
print(f"Using model: {model.model_name}")

# Step 3: Create a "long document" that we need to process.
# In a real scenario, this could be a PDF, a book, or a long report.
# For this lab, we'll just create a long string.

part1 = """
Project Gutenberg's "A Tale of Two Cities", by Charles Dickens.
It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way—in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only.
This part of the story introduces the contrasting states of England and France in 1775.
"""

part2 = """
The story then moves to describe the mail-coach journey from London to Dover. The passengers are suspicious of each other, fearing robbers. Mr. Jarvis Lorry, an elderly gentleman from Tellson's Bank, receives a cryptic message: "Wait at Dover for Mam'selle." He responds with an equally cryptic message: "Recalled to life." This exchange sets up the central mystery of the novel concerning Doctor Manette.
Dr. Manette is a French physician who was secretly imprisoned in the Bastille for 18 years.
"""

part3 = """
Lucie Manette, a young woman who believed she was an orphan, is brought from London to Paris by Mr. Lorry. He reveals to her that her father is alive and has been released. They go to the garret of a wine-shop in the Parisian suburb of Saint Antoine, owned by Monsieur and Madame Defarge. There, they find Dr. Manette, who has lost his memory and spends his time compulsively making shoes, a skill he learned in prison.
The main characters are Lucie Manette, Charles Darnay, and Sydney Carton.
"""

long_document = part1 + part2 + part3

# Let's verify the total token count.
total_tokens = model.count_tokens(long_document).total_tokens
print(f"The total document has {total_tokens} tokens.")
print("-" * 50)


# Step 4: The Strategy - Chunking
# We can't "adjust" the model's window, but we can adjust our input.
# The strategy is to split the document into chunks that WILL fit.
# For this example, we'll set a small chunk size to see the process clearly.

# We will split the text by paragraphs (double newlines)
chunks = long_document.split('\n\n')

print(f"The document was split into {len(chunks)} chunks.")
for i, chunk in enumerate(chunks):
    chunk_tokens = model.count_tokens(chunk).total_tokens
    print(f"  - Chunk {i+1}: {chunk_tokens} tokens. Content: '{chunk.strip()[:50]}...'")

print("-" * 50)


# Step 5: Process Each Chunk Individually
# Let's perform a task: For each chunk, we'll ask the model to pull out the key names and places.

all_key_points = []
print("\n--- Processing each chunk individually ---")

for i, chunk in enumerate(chunks):
    if not chunk.strip(): # Skip empty chunks
        continue

    print(f"\nProcessing Chunk {i+1}...")
    prompt = f"""
    Based on the following text, extract the key character names and locations mentioned.
    If no names or locations are mentioned, say 'None'.

    TEXT:
    "{chunk}"

    NAMES AND LOCATIONS:
    """
    try:
        response = model.generate_content(prompt)
        print(f"  > Model Response: {response.text.strip()}")
        all_key_points.append(response.text.strip())
    except Exception as e:
        print(f"  > Could not process chunk: {e}")

print("\n" + "-" * 50)


# Step 6: Combine the Results (Map-Reduce style)
# Now that we have processed each chunk, we can combine the results to get a
# summary of the entire document. This is a form of the "Map-Reduce" pattern.

print("\n--- Combining the results for a final summary ---")

# Join all the extracted points into one text
combined_points = "\n".join(all_key_points)

final_summary_prompt = f"""
Based on the following list of key points extracted from a document, write a single, coherent paragraph summarizing the main events and characters.

EXTRACTED POINTS:
{combined_points}

FINAL SUMMARY:
"""

final_response = model.generate_content(final_summary_prompt)

print("\nFinal Combined Summary of the entire document:")
print(final_response.text)


# --- Conclusion of Lab 3 ---
# You've learned:
# 1. The primary strategy for handling large documents is "chunking" - splitting them into smaller parts.
# 2. You can process each chunk individually to perform tasks like extraction or summarization.
# 3. The results from each chunk can then be combined in a final step to create a comprehensive result for the entire document (a "Map-Reduce" approach).
# 4. This technique allows you to overcome the context window limitation for very large inputs.

print("\n--- Processing with a smaller, custom context window ---")

# Define a hypothetical smaller context window size (in characters)
custom_context_window_size = 200

# Truncate the document to fit within the custom window
truncated_document = long_document[:custom_context_window_size]

truncated_document_prompt = f"""
Based on the following text, extract the key character names and locations mentioned.
If no names or locations are mentioned, say 'None'.

TEXT:
"{truncated_document}"

NAMES AND LOCATIONS:
"""

try:
    # Process the truncated document
    truncated_response = model.generate_content(truncated_document_prompt)
    print(f"  > Model Response (Truncated Document): {truncated_response.text.strip()}")
except Exception as e:
    print(f"  > Could not process truncated document: {e}")

print("\n" + "-" * 50)

"""### Processing with a smaller, custom context window

Note: The model's actual context window size is fixed. We are simulating the effect of a smaller window by truncating the input string to fit within a hypothetical smaller window.
"""

print("\n--- Attempting to process the full document ---")

full_document_prompt = f"""
Based on the following text, extract the key character names and locations mentioned.
If no names or locations are mentioned, say 'None'.

TEXT:
"{long_document}"

NAMES AND LOCATIONS:
"""

try:
    # Attempt to process the full document
    full_response = model.generate_content(full_document_prompt)
    print(f"  > Model Response (Full Document): {full_response.text.strip()}")
except Exception as e:
    print(f"  > Could not process full document: {e}")

print("\n" + "-" * 50)

"""### Attempting to process the full document (may exceed context window)

## Demonstrating the effect of context window size

Let's see what happens when we try to process the full document without chunking, and then with a smaller, custom context window size.
"""
