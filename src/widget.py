from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(my_card: str) -> str:
    """Функция, которая обрабатывает информацию как о картах,
    так и о счетах"""

    if len(my_card.split()[-1]) == 16:
        new_my_card = get_mask_card_number(my_card.split()[-1])
        result = f"{my_card[:-16]}{new_my_card}"
        return result
    elif len(my_card.split()[-1]) == 20:
        new_my_card = get_mask_account(my_card.split()[-1])
        result = f"{my_card[:-20]}{new_my_card}"
        return result


def get_date(old_date: str) -> str:
    """Функция, которая принимает на вход строку с датой в формате
    "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" """

    new_date = old_date[0:10].split("-")
    return ".".join(new_date[::-1])


if __name__ == "__main__":
    print(mask_account_card("Maestro 7000792289606361"))
    print(get_date("2024-03-11T02:26:18.671407"))