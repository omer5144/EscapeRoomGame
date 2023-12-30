from pygame import Surface
from pygame.event import Event

from src.base import Window, Header, Footer
from src.scenes import Scene
from src.context.game_context import GameContext


class Body(Window):
    scenes: dict[type, Scene]
    current_scene: type

    def __init__(self, game_context: GameContext, screen: Surface, width: int, height: int, x: int, y,
                 scene_types: set[type], first_scene_type: type, header: Header, footer: Footer):
        super(Body, self).__init__(screen, width, height, x, y)

        self.scenes = {scene_type: scene_type(game_context=game_context, screen=self.screen, width=self.width,
                                              height=self.height, x=self.x, y=self.y, header=header, footer=footer) for
                       scene_type in
                       scene_types}
        self.set_current_scene(first_scene_type)

    def render(self) -> None:
        super(Body, self).render()

        self.scenes[self.current_scene].render()

    def handle_events(self, events: list[Event]) -> None:
        super(Body, self).handle_events(events)

        next_scene = self.scenes[self.current_scene].handle_events(events)
        if next_scene:
            self.set_current_scene(next_scene)

    def set_current_scene(self, scene_type: type) -> None:
        self.current_scene = scene_type
        self.scenes[self.current_scene].on_start_scene()
