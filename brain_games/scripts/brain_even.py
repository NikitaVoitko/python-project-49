#!/usr/bin/env python3
# import game_engine and choose is_even as the game
from brain_games.engine.engine import run_game
import brain_games.games.is_even_game


def main():

    run_game(brain_games.games.is_even_game.DESCRIPTION,
             brain_games.games.is_even_game.get_is_even_game)


if __name__ == '__main__':
    main()
