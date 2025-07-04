from functions.run_python import run_python_file


def test():
    result = run_python_file("calculator", "main.py")
    print("Result for getting file content:")
    print(result)
    print("")
    
    result = run_python_file("calculator", "tests.py")
    print("Result for getting file content:")
    print(result)
    print("")
    
    result = run_python_file("calculator", "../main.py")
    print("Result for getting file content:")
    print(result)
    print("")

    result = run_python_file("calculator", "nonexistent.py")
    print("Result for getting file content:")
    print(result)
    print("")

    # result = get_file_content("calculator", "main.py")
    # print("Result for getting file content:")
    # print(result)
    # print("")

    # result = get_file_content("calculator", "pkg/calculator.py")
    # print("Result for getting file content:")
    # print(result)
    # print("")

    # result = get_file_content("calculator", "/bin/cat")
    # print("Result for getting file content:")
    # print(result)
    # print("")

if __name__ == "__main__":
    test()
