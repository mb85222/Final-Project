import pytest

from buscaminas import Minesweeper

@pytest.fixture
def game():
    return test_reveal_empty_cell (rows=5, cols=5, mines=0)  

def test_reveal_empty_cell(game):
    game.board[2][2] = 0  
    game.reveal_cell(2, 2)
    assert game.revealed[2][2] == True  

def test_reveal_numbered_cell(game):
    game.board[1][1] = 2  
    game.reveal_cell(1, 1)
    assert game.revealed[1][1] == True  
def test_reveal_mine(game, capsys):
    game.board[3][3] = -1  
    game.reveal_cell(3, 3)
    captured = capsys.readouterr()
    assert "Boom! You hit a mine! Game Over."