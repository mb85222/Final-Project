import pytest
from unittest.mock import patch
from buscaminas import Minesweeper

@pytest.fixture
def minesweeper():
    game = Minesweeper(5, 5)
    return game

def test_restart_game_yes(minesweeper):
    with patch("builtins.input", return_value="y"), patch.object(minesweeper, "initialize_game") as mock_init, patch.object(minesweeper, "play") as mock_play:
        minesweeper.restart_game()
        mock_init.assert_called_once()
        mock_play.assert_called_once()

def test_restart_game_no(minesweeper, capsys):
    with patch("builtins.input", return_value="n"), patch("builtins.exit") as mock_exit:
        minesweeper.restart_game()
        mock_exit.assert_called_once()
        captured = capsys.readouterr()
        assert "Thanks for playing!"
