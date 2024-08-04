from typing import List
from typing import Any

inform_state = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(
    info_state: List[dict[str, Any]], state_id: str = "EXECUTED"
) -> List[dict[str, Any]]:
    """Функция, которая принимает список словарей и опционально
    значение для ключа и возвращает новый список словарей,
    содержащий только те словари, у которых ключ
    соответствует указанному значению"""

    list_siate = []
    for key in info_state:
        if key.get("state") == state_id:
            list_siate.append(key)
    return list_siate


def sort_by_date(
    info_list: List[dict[str, Any]], revers_list: bool = True
) -> List[dict[str, Any]]:
    """Функция, которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание)"""

    sorted_list = sorted(info_list, key=lambda dat: dat["date"], reverse=revers_list)
    return sorted_list


if __name__ == "__main__":
    print(sort_by_date(inform_state))
    print(filter_by_state(inform_state))
