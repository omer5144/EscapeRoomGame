from src.context.game_context import GameContext


class SceneContext:

    game_context: GameContext

    def __init__(self, game_context):
        self.game_context = game_context

    def is_room_done(self) -> bool:
        pass


