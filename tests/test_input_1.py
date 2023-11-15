from dummy.example_work import address_design_input_1


def test_input_1_with_text():
    assert address_design_input_1("text") is True


def test_input_1_without_text():
    assert address_design_input_1() is False
