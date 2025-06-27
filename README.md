# TEXT SUMMARIZATION TOOL

COMPANY: CODTECH IT SOLUTIONS

*NAME*: Keerthi K

*INTERN ID*: CT06DG2158

*DOMAIN*: Artificial Intelligence 

*DURATION*: 6 WEEEKS

*MENTOR*: NEELA SANTOSH

## Project Overview
This project presents a complete, beginner-friendly yet powerful tool for summarizing lengthy articles and research papers using the latest advancements in Natural Language Processing (NLP).
Built with Python, the tool integrates Google's Gemini model via LangChain, and provides both a command-line interface and a web-based interface using Streamlit. 
The goal is to take long, dense text inputs and return clean, clear, and concise summaries in various styles and lengths.
The project addresses a growing real-world need: with the massive volume of digital content today—research papers, blogs, reports, news, and technical documentation—people need ways to quickly grasp the key ideas without reading every word. This tool uses AI to make that possible.

## Tools & Technologies Used
Tool	                                         Purpose
Python	                                     Main programming language
LangChain	                                   For prompt templates and chaining logic with LLMs
Google Gemini (via langchain-google-genai)	 The AI model used for summarization
Streamlit	                                   For building a fast and interactive web interface
dotenv (python-dotenv)	                     Securely loads API keys from a .env file
Git + GitHub	                               Version control and code hosting
Virtual Environment (venv)	                 Isolates project dependencies
Text File Input	                             Accepts .txt files for offline text summarization

## How the Project Works (Architecture)
1. Text Input
Users can either:
Paste or type their text directly into a Streamlit app, or
Pass a .txt file through a command-line script.
2. Prompt Design
The tool uses a PromptTemplate that defines how the AI should summarize the input. It includes variables for:
The paper/topic name
The desired explanation style (e.g., Beginner-Friendly, Technical)
The desired length (Short, Medium, Long)
3. Chunking Long Texts
If the input text is very long, the script splits it into smaller chunks (~1000 characters each) so it fits within the model’s input limits. Each chunk is summarized individually.
4. Model Interaction
The ChatGoogleGenerativeAI class from langchain-google-genai connects to Google Gemini, sending each chunk’s prompt and receiving its summary.
5. Summary Merging
Once all chunks are summarized, the tool combines them and sends that combined text back to the model for a final, high-level summary.
6. Output Display
The result is printed in the terminal (CLI version) or shown on the Streamlit interface for end-users.

## Future Improvements
Add file upload support (PDF, DOCX).
Deploy the Streamlit app on a public server (like Streamlit Cloud).
Integrate summarization metrics like ROUGE or BLEU.
Add memory or vector-based document storage.
Let users select different models (e.g., OpenAI, Claude).


