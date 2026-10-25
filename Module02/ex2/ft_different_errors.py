def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")                      
    elif operation_number == 1:
        result = 10 / 0                 
    elif operation_number == 2:
        open("/non/existent/file")      
    elif operation_number == 3:
        result = "abc" + 5              
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    for value in range(5):
        print(f"Testing operation {value}...")
        try:
            garden_operations(value)
        except Exception as error:
            match error:
                case ValueError():
                    print(f"Caught ValueError: {error}")
                case ZeroDivisionError():
                    print(f"Caught ZeroDivisionError: {error}")
                case FileNotFoundError():
                    print(f"Caught FileNotFoundError: {error}")
                case TypeError():
                    print(f"Caught TypeError: {error}")
                case _:
                    raise
        else:
            print("Operation completed successfully")

    print("All error types tested successfully!")

if __name__ == "__main__":
    test_error_types()