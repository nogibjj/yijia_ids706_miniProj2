from main import add, subtract


def test_add():
    result = add(2, 3)
    assert result == 5, f"Expected 5, but got {result}"
    print("test_add passed")


def test_subtract():
    result = subtract(5, 3)
    assert result == 2, f"Expected 2, but got {result}"
    print("test_subtract passed")


if __name__ == "__main__":
    print("Running tests...")
    test_add()
    test_subtract()
