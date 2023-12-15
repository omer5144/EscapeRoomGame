import pygame
from pygame import Surface, Rect
from pygame.event import Event

from consts import colors, sizes, items
from window import Window


class Footer(Window):
    image: Surface

    slots: list

    def __init__(self, screen: Surface, width: int, height: int, x: int, y, slots_count: int):
        super(Footer, self).__init__(screen, width, height, x, y)

        self.image = pygame.Surface((self.width, self.height))

        self.slots = [items.EMPTY_SLOT] * slots_count

    def render(self) -> None:
        super(Footer, self).render()

        self.image.fill(colors.BLUE)
        self.screen.blit(self.image, (self.x, self.y))

        for i in range(len(self.slots)):
            pygame.draw.rect(self.screen, colors.BLACK, self.get_slot_frame_rect(i))
            pygame.draw.rect(self.screen, colors.GRAY, self.get_slot_content_rect(i))

    def resize(self, width: int, height: int, x: int, y: int) -> None:
        super(Footer, self).resize(width, height, x, y)

        self.image = pygame.Surface((self.width, self.height))

    def handle_events(self, events: list[Event]) -> None:
        super(Footer, self).handle_events(events)

    @property
    def min_width(self) -> int:
        return len(self.slots) * self._slot_size + (len(self.slots) + 1) * sizes.SLOTS_X_MARGIN

    @property
    def min_height(self) -> int:
        return self.height

    @property
    def _slot_size(self):
        return self.height - sizes.SLOTS_Y_PADDING * 2

    @property
    def _slot_x_padding(self):
        return (self.width - self._slot_size * len(self.slots) - sizes.SLOTS_X_MARGIN * (len(self.slots) + 1)) // 2

    def get_slot_frame_rect(self, index: int) -> Rect:
        return pygame.Rect(
            self.x + self._slot_x_padding + sizes.SLOTS_X_MARGIN + (sizes.SLOTS_X_MARGIN + self._slot_size) * index,
            self.y + sizes.SLOTS_Y_PADDING,
            self._slot_size,
            self._slot_size
        )

    def get_slot_content_rect(self, index: int) -> Rect:
        return pygame.Rect(
            self.x + self._slot_x_padding + sizes.SLOTS_X_MARGIN + sizes.SLOT_FRAME + (
                        sizes.SLOTS_X_MARGIN + self._slot_size) * index,
            self.y + sizes.SLOTS_Y_PADDING + sizes.SLOT_FRAME,
            self._slot_size - 2 * sizes.SLOT_FRAME,
            self._slot_size - 2 * sizes.SLOT_FRAME
        )
