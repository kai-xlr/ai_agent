from functions.write_file import write_file


def test():
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Result for getting file content:")
    print(result)
    print("")
    
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("Result for getting file content:")
    print(result)
    print("")
    
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
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
