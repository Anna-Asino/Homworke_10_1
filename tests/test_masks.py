import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    'card_numb, expected', [
        ('7000792289606361', '7000 79** **** 6361'),
        ('8000792289606361', '8000 79** **** 6361'),
        ('700079228960630', None),
    ]
)
def test_get_mask_card_number(card_numb, expected):
    assert get_mask_card_number(card_numb) == expected


@pytest.mark.parametrize(
    'acc_number, expected', [
        ('73654108430135874305', '**4305'),
        ('736541084301358743', None),
        ('73654108430135874300', '**4300')])
def test_get_mask_account(acc_number, expected):
    assert get_mask_account(acc_number) == expected
