from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize Google Gemini model
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

# Prompt template for summarization
template = PromptTemplate(
    input_variables=["input_text"],
    template="""
    You are an AI assistant. You will be given a text. Please summarize it concisely in 6-7 lines.

    Text:
    {input_text}

    Summary:
    """
)

chain = template | model

def chunk_text(text, max_chunk_size=1000):
    """Split long text into chunks of max_chunk_size characters without breaking words."""
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0

    for word in words:
        if current_length + len(word) + 1 <= max_chunk_size:
            current_chunk.append(word)
            current_length += len(word) + 1  # +1 for space
        else:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_length = len(word) + 1

    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks

def summarize(text):
    chunks = chunk_text(text)
    summaries = []
    for i, chunk in enumerate(chunks):
        print(f"Summarizing chunk {i+1}/{len(chunks)}...")
        result = chain.invoke({"input_text": chunk})
        summaries.append(result.content.strip())

    # Combine chunk summaries into one text for final summary
    combined_summary_text = " ".join(summaries)

    # Optionally, summarize the combined summary for brevity
    print("Summarizing combined summary...")
    final_result = chain.invoke({"input_text": combined_summary_text})

    return final_result.content.strip()

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python summarizer.py path_to_text_file.txt")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        sys.exit(1)

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    summary = summarize(text)
    print("\n=== Final Summary ===\n")
    print(summary)
