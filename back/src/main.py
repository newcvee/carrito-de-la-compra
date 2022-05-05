
from pathlib import Path


def split_in_lines():
    source = Path.cwd() / "data" / "shopping-list.txt"
    content = source.read_text()
    text_list = content.splitlines()

    return text_list


def split_array_from_pipe(list_text):
    content = []

    for list in list_text:
        content.append(list.split("|"))

    return content


def list_to_dict(list_of_list_to_create_dict):

    key_dict = ['product', 'unit', 'price']
    list_of_dict = []
    for item in list_of_list_to_create_dict:
        dict_from_list = dict(zip(key_dict, item))
        list_of_dict.append(dict_from_list)

    return list_of_dict


def list_to_dict_with_new_key(dict_without_completed):

    for item in dict_without_completed:
        item["completed"] = False
        dict_with_completed = dict_without_completed

    return dict_with_completed


def main():

    separe = split_in_lines()
    split = split_array_from_pipe(separe)
    send_list_to_dict = list_to_dict(split)
    send_final_list = list_to_dict_with_new_key(send_list_to_dict)
    return send_final_list
