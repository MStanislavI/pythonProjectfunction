_liste_dicte_ = [
    {"id": "41428829", "state": "EXECUTED", "date": "2019-07-03T18:35:29.312384"},
    {"id": "939719570", "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": "594226727", "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": "615064591", "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(_liste_dicte_: list, state: str = "EXECUTED") -> list:
    """Функция, фильтрующая список словарей по ключу state"""
    filtered_list = []
    for item in _liste_dicte_:
        if item.get("state") == state:
            filtered_list.append(item)
    return filtered_list


def sort_by_date(_liste_dicte_: list, type_sort: bool = True) -> list:
    """Функция, фильтрующая список словарей по дате"""
    return sorted(_liste_dicte_, key=lambda x: x["date"], reverse=type_sort)


print(sort_by_date(_liste_dicte_))
