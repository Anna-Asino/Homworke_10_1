import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    'my_card, expected', [
        ('Maestro 1596837868705199', 'Maestro 1596 83** ****5199'),
        ('Maestro 2096837868705200', 'Maestro 2096 83** ****5200'),
        ('Счет 646864736788947795891', 'Счет **5891'),
        ('MasterCard 715830073472675', None),
        ('Master 7158300734726758', None),
        ('Счет 64686473678894779', None),
        ('Maestro 96837868705199', None)
    ]
)
def test_mask_account_card(my_card, expected):
    mask_account_card(my_card) == expected


@pytest.mark.parametrize(
    'old_date, expected', [
        ('2024-03-11T02:26:18.671407', '11.03.2024'),
        ('2023-05-01T02:26:18.6714071', '01.05.2023'),
        ('2024-3-11T02:26:18.671407', ''),
        ('', '')
]
)
def test_get_date(old_date, expected):
    get_date(old_date) == expected
