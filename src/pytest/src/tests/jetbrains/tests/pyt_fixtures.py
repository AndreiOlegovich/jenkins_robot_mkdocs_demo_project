import pytest

@pytest.fixture
def player_one() -> Player:
    return Player('Tatiana', 'Jones')

def test_construction(player_one):
    assert 'Tatiana' == player_one.first_name
    assert 'Jones' == player_one.last_name
    # assert [] == player_one.guardians