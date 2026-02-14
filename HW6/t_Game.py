from Game import Game

game = Game(2, 2, 2, ["Shir"])
game.play_turn()
print(game.run_game())
path = game.solve()
print(path, f"\nTest result for shortest path {path == [1, 2, 3, 4, 5, 6, 24, 25]}")
add_game = Game(6, 6, snakes_ladders={"L": {5: 18, 10: 33, 14: 25}, "S": {34: 9, 32: 16, 22: 12, 19: 17}},
                game_players=["Tal", "Yuval"])
add_game.play_turn()
print(add_game.run_game())
path = add_game.solve()
print(path, f"\nTest result for shortest path {path == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 33, 34, 35, 36]}")

