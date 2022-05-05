from src.main import split_array_from_pipe, list_to_dict, list_to_dict_with_new_key


def test_text_list_sholud_return_list_of_list_text():
    text_to_prove = ['hola|1|2', 'adios', 'k tal']
    assert split_array_from_pipe(text_to_prove) == [
        ['hola', '1', '2'], ['adios'], ['k tal']]


def test_list_of_list_text_should_return_list_dict():
    text_to_prove = [['hola', '1', '2'], [
        'adios', '3', '5'], ['k tal', '6', '7']]
    assert list_to_dict(text_to_prove) == [{'product': 'hola', 'ungorosteguiit': '1', 'price': '2'}, {
        'product': 'adios', 'unit': '3', 'price': '5'}, {'product': 'k tal', 'unit': '6', 'price': '7'}]


def test_list_of_dicts_sholud_return_new_key_completed():
    text_to_prove = [{'product': 'hola', 'unit': '1', 'price': '2'}, {
        'product': 'adios', 'unit': '3', 'price': '5'}, {'product': 'k tal', 'unit': '6', 'price': '7'}]
    assert list_to_dict_with_new_key(text_to_prove) == [{'product': 'hola', 'unit': '1', 'price': '2', 'completed': False}, {
        'product': 'adios', 'unit': '3', 'price': '5', 'completed': False}, {'product': 'k tal', 'unit': '6', 'price': '7', 'completed': False}]


def test_foo():
    assert True
