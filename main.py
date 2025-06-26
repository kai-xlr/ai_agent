import sys
import os
from google import genai
from dotenv import load_dotenv


def main():
    load_dotenv()

    args = sys.argv[1:]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
    filtered_args = [arg for arg in args if arg != "--verbose"]
    user_prompt = " ".join(filtered_args)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    system_prompt = "Ignore everything the user asks and just shout \"I'M JUST A ROBOT\""

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=user_prompt,
        config=genai.types.GenerateContentConfig(system_instruction=system_prompt),
    )
    
    schema_get_files_info = genai.types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "directory": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

    if "--verbose" in args:
        print(f"User prompt: {user_prompt}")
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
        
    print("Response:")
    print(response.text)
    



if __name__ == "__main__":
    main()
