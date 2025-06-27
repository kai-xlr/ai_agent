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

    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

    schema_get_files_info = genai.types.FunctionDeclaration( # type: ignore
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=genai.types.Schema( # type: ignore
        type=genai.types.Type.OBJECT, # type: ignore
        properties={
            "directory": genai.types.Schema( # type: ignore # type: ignore
                type=genai.types.Type.STRING, # type: ignore # type: ignore
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
    schema_get_file_content = genai.types.FunctionDeclaration( # type: ignore
    name="get_file_content",
    description="Get the content of file in the specified directory, constrained to the working directory.",
    parameters=genai.types.Schema( # type: ignore
        type=genai.types.Type.OBJECT, # type: ignore
        properties={
            "directory": genai.types.Schema( # type: ignore # type: ignore
                type=genai.types.Type.STRING, # type: ignore # type: ignore
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
    schema_run_python_file = genai.types.FunctionDeclaration( # type: ignore
    name="run_file",
    description="Run a file in the specified directory, constrained to the working directory.",
    parameters=genai.types.Schema( # type: ignore
        type=genai.types.Type.OBJECT, # type: ignore
        properties={
            "directory": genai.types.Schema( # type: ignore # type: ignore
                type=genai.types.Type.STRING, # type: ignore # type: ignore
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
    schema_write_file = genai.types.FunctionDeclaration( # type: ignore
    name="write_file",
    description="Write a file in the specified directory, constrained to the working directory.",
    parameters=genai.types.Schema( # type: ignore
        type=genai.types.Type.OBJECT, # type: ignore
        properties={
            "directory": genai.types.Schema( # type: ignore # type: ignore
                type=genai.types.Type.STRING, # type: ignore # type: ignore
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
    
    available_functions = genai.types.Tool( # type: ignore
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)
    
    config=genai.types.GenerateContentConfig( # type: ignore
        tools=[available_functions], system_instruction=system_prompt
)

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=user_prompt,
        config=config,
    )

    if "--verbose" in args:
        print(f"User prompt: {user_prompt}")
        print("Prompt tokens:", response.usage_metadata.prompt_token_count) # type: ignore
        print("Response tokens:", response.usage_metadata.candidates_token_count) # type: ignore
        
    print("Response:")
    if response.function_calls:
        for function_call_part in response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(response.text)
    



if __name__ == "__main__":
    main()
