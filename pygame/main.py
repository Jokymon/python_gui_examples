import pygame
import pygame_gui


WINDOW_SIZE = (400, 180)
ROW_HEIGHT = 40


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("PyGame-GUI Beispiel GUI")

    screen = pygame.display.set_mode(WINDOW_SIZE)

    manager = pygame_gui.UIManager(WINDOW_SIZE, 'theme.json')

    label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect(10, 10, -1, ROW_HEIGHT),
        text="Lass dich begrüssen",
        manager=manager)
    label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect(10, 10+ROW_HEIGHT, -1, ROW_HEIGHT),
        text="Wie ist dein Name?",
        manager=manager)
    name_entry = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect(190, 10+ROW_HEIGHT, 190, ROW_HEIGHT),
        manager=manager)
    greet_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(140, 10+2*ROW_HEIGHT, -1, ROW_HEIGHT),
        text="Begrüsse",
        manager=manager)
    output_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect(10, 10+3*ROW_HEIGHT, 200, ROW_HEIGHT),
        text='',
        manager=manager)

    clock = pygame.time.Clock()
    running = True
    while running:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == greet_button:
                    name = name_entry.get_text()
                    output_label.set_text(f"Hallo {name}")

            manager.process_events(event)

        manager.update(time_delta)

        screen.fill(pygame.Color('#000000'))
        manager.draw_ui(screen)

        pygame.display.flip()

    pygame.quit()
