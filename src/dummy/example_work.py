
def address_design_input_1(text: str = None) -> bool:
    """
    Dummy demo behaviour, returns whether a text has been entered or not, and prints the text if it exists
    :param text: text to print
    :return: True if text has been given to the function
    """
    if not text:
        return False
    print(f"You entered: {text}")
    return True
