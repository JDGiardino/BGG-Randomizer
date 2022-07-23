from src.models.BoardGame import BoardGame


class OrderBoardGames:
    ORDER_BY_ALPHABET = "alphabet"
    ORDER_BY_RANK = "rank"
    ORDER_BY_RATING = "rating"
    ORDER_BY_COMPLEXITY = "complexity"

    def __init__(self, board_games: list[BoardGame], order_by: str):
        self.board_games = board_games
        self.order_by = order_by

    def order_games(self) -> list[BoardGame]:
        if self.order_by == self.ORDER_BY_ALPHABET:
            ordered_board_games = self.__order_by_alphabet()
            return ordered_board_games
        elif self.order_by == self.ORDER_BY_RANK:
            ordered_board_games = self.__order_by_rank()
            return ordered_board_games
        elif self.order_by == self.ORDER_BY_RATING:
            ordered_board_games = self.__order_by_rating()
            return ordered_board_games
        elif self.order_by == self.ORDER_BY_COMPLEXITY:
            ordered_board_games = self.__order_by_complexity()
            return ordered_board_games
        else:
            ordered_board_games = self.__order_by_alphabet()
            return ordered_board_games

    def __order_by_alphabet(self) -> list[BoardGame]:
        ordered_board_games = self.board_games
        ordered_board_games.sort(key=lambda x: x.name)
        return ordered_board_games

    def __order_by_rank(self) -> list[BoardGame]:
        ordered_board_games = self.board_games
        ordered_board_games.sort(key=lambda x: x.overallrank)
        return ordered_board_games

    def __order_by_rating(self) -> list[BoardGame]:
        ordered_board_games = self.board_games
        ordered_board_games.sort(key=lambda x: x.averagerating, reverse=True)
        return ordered_board_games

    def __order_by_complexity(self) -> list[BoardGame]:
        ordered_board_games = self.board_games
        ordered_board_games.sort(key=lambda x: x.complexity, reverse=True)
        return ordered_board_games
