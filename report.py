def remove_none_values(dict: dict) -> dict:
    return {k: v for k, v in dict.items() if v is not None}


def sort_pages(dict: dict) -> list:
    dict_as_list = [(k, v) for k, v in dict.items()]
    dict_as_list.sort(key=lambda x: x[1], reverse=True)
    return dict_as_list
