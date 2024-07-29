def get_mask_card_number(card_numb: str | int) -> str | None:
    """Функция маскировки номера банковской карты"""

    card_number_sim = str(card_numb)
    if card_number_sim.isdigit() and len(card_number_sim) == 16:
        return f"{card_number_sim[0:4]} {card_number_sim[4:6]}** **** {card_number_sim[12:]}"
    else:
        return None


def get_mask_account(acc_number: str | int) -> str | None:
    """Функция маскировки номера банковского счета"""

    acc_number_sim = str(acc_number)
    if acc_number_sim.isdigit() and len(acc_number_sim) == 20:
        return f"**{acc_number_sim[16:]}"
    else:
        return None


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))
