import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize('card_numb','card_number_sim',[
    ('1234567891234564', '1234 56** **** **64'),
    ('1234567891234789', '1234 56** **** **89'),
    ('1234567891234001', '1234 56** **** **01')

])
def test_get_mask_card_number(card_numb,card_number_sim):
    assert test_get_mask_card_number(card_numb) == card_number_sim
