from dataclasses import dataclass
from typing import Optional
import pygame
from pygame import Surface, Rect
from pygame.event import Event
from src.context.game_context import GameContext
from src.context.scene_context import SceneContext

from src.consts import strings, colors, backgrounds
from src.base import Window, Header, Footer

from src.consts.config import Config


@dataclass
class Object:
    name: str
    image: Surface
    rect: Rect


class Scene(Window):
    scene_context: SceneContext
    game_context: GameContext

    background: Surface

    header: Header
    footer: Footer

    scene_name: str

    objects: list[Object]

    def __init__(self, game_context: GameContext, screen: Surface, width: int, height: int,
                 x: int, y: int, header: Header, footer: Footer, scene_name: str = strings.DEFAULT_SCENE_NAME,
                 background_name: str = backgrounds.DEFAULT_BACKGROUND, scene_context_type: type = SceneContext):
        super(Scene, self).__init__(screen, width, height, x, y)

        self.scene_context = scene_context_type(game_context=game_context)

        self.header = header
        self.footer = footer

        self.scene_name = scene_name
        self.objects = []

        if background_name == backgrounds.DEFAULT_BACKGROUND:
            self.background = pygame.Surface((self.width, self.height))
            self.background.fill(colors.WHITE)
        else:
            self.set_background(background_name)

    def render(self) -> None:
        super(Scene, self).render()

        self.screen.blit(self.background, (self.x, self.y))

        for obj in self.objects:
            self.screen.blit(obj.image, obj.rect)

    def on_mouse_left_button_down(self, event: Event) -> type | None:
        super(Scene, self).on_mouse_left_button_down(event)
        for obj in self.objects[::-1]:
            if obj.rect.collidepoint(event.pos):
                x, y = event.pos
                if obj.image.get_at((x - obj.rect.x, y - obj.rect.y)).a > 0:
                    if self.footer.selected_item:
                        return self.on_item_used_on_object(self.footer.selected_item, obj.name)
                    else:
                        return self.on_pressed_on_object(obj.name)

    def on_item_used_on_object(self, item_name: str, object_name: str) -> None:
        pass

    def on_pressed_on_object(self, object_name: str) -> None:
        pass

    def set_background(self, background_name: str) -> None:
        try:
            self.background = pygame.transform.scale(
                pygame.image.load(f'resources/images/{background_name}.png'), (self.width, self.height))
            return
        except:
            if not Config.DEBUG:
                raise Exception("image does not exist in release mode")

        try:
            self.background = pygame.transform.scale(
                pygame.image.load(f'debug_resources/images/{background_name}.png'), (self.width, self.height))
        except:
            raise Exception("image does not exist in debug mode")

    def on_start_scene(self) -> None:
        self.set_title(strings.SCENE_TITLE_FORMAT.format(scene_name=self.scene_name))

    def add_object(self, object_name: str, object_filename: str, x: int, y: int, width: int, height: int,
                   angle: int = 0) -> None:
        try:
            object = pygame.image.load(f'resources/images/{object_filename}.png')
        except:
            if not Config.DEBUG:
                raise Exception("object does not exist in release mode")

            try:
                object = pygame.image.load(f'debug_resources/images/{object_filename}.png')
            except:
                raise Exception("object does not exist in debug mode")

        object = pygame.transform.scale(object, (width, height))
        object = pygame.transform.rotate(object, angle)

        self.objects.append(Object(object_name, object, pygame.Rect(self.x + x, self.y + y, width, height)))

    def remove_object(self, object_name) -> None:
        for obj in self.objects.copy():
            if obj.name == object_name:
                self.objects.remove(obj)

    def set_title(self, title: str) -> None:
        self.header.set_title(title)

    def add_item(self, item_name: str) -> None:
        self.footer.add_item(item_name)

    def use_selected_item(self) -> None:
        self.footer.use_selected_item()
