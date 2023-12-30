from src.context.scene_context import SceneContext


class IftachComputerContext(SceneContext):

    def __init__(self, **kwargs):
        super(IftachComputerContext, self).__init__(**kwargs)


    def is_omer_adam_playing(self):
        return self.game_context.current_team_song == "omer adam"

    def is_room_done(self) -> bool:
        return self.game_context.current_team_song == "omer adam"


