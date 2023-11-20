
import subprocess
import openai
import os
from dotenv import load_dotenv

load_dotenv()

def get_changed_code():
    diff = subprocess.check_output(['git', 'diff']).decode()
    return diff

def chunk_diff(diff, max_length):
    chunks = []
    current_chunk = ""
    for line in diff.split("\n"):
        if len(current_chunk) + len(line) > max_length:
            chunks.append(current_chunk)
            current_chunk = line
        else:
            current_chunk += line + "\n"
    if current_chunk:
        chunks.append(current_chunk)
    return chunks

def openai_code_review(chunks):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    feedback = ""
    for chunk in chunks:
        response = openai.Completion.create(
            engine="code-davinci-002",
            prompt="Review these code changes: \n\n" + chunk,
            max_tokens=150
        )
        feedback += response.choices[0].text.strip() + "\n\n"
    return feedback

def main():
    diff = get_changed_code()
    if not diff:
        print("No uncommitted changes.")
        return
    max_length = 1000  # Adjust as needed based on OpenAI's token limits
    chunks = chunk_diff(diff, max_length)
    feedback = openai_code_review(chunks)
    print("Code Review Feedback:\n", feedback)

if __name__ == "__main__":
    main()
