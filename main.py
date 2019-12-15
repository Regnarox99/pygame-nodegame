import os, sys
import math
import pygame

from benUI import Button

pygame.font.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "100, 100"

WIN_HEIGHT = 800
WIN_WIDTH = 1400

NODE_IMAGE = pygame.image.load(os.path.join("images", "node.png"))

CONNECTION_COLOURS = [(200, 120, 0)]

NODE_SIZE = 100
NODE_RADIUS = 50

STAT_FONT = pygame.font.SysFont("comicsans", 50)

BUTTON_BG_COLOUR = (200, 200, 200)
BUTTON_FONT = STAT_FONT = pygame.font.SysFont("comicsans", 30)


class Node:
    image = NODE_IMAGE
    size = NODE_SIZE
    radius = NODE_RADIUS

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))


class Connection:
    colour = CONNECTION_COLOURS[0]

    def __init__(self, start_node, end_node):
        self.start_node = start_node
        self.end_node = end_node

    def draw(self, win):
        angle = math.atan((self.end_node.y - self.start_node.y) / (self.end_node.x - self.start_node.x))
        pygame.draw.line(win, self.colour,
                         (self.start_node.x + self.start_node.size / 2 + math.cos(angle) * self.start_node.radius,
                          self.start_node.y + self.start_node.size / 2 + math.sin(angle) * self.start_node.radius),
                         (self.end_node.x + self.end_node.size / 2 - math.cos(angle) * self.start_node.radius,
                          self.end_node.y + self.end_node.size / 2 - math.sin(angle) * self.start_node.radius))


def draw_window(win, mode, nodes, connections, buttons):
    win.fill((153, 255, 204))

    for node in nodes:
        node.draw(win)

    for connection in connections:
        connection.draw(win)

    for button in buttons:
        button.draw(win)

    conn_text = STAT_FONT.render("Conns: " + str(len(connections)), 1, (50, 50, 50))
    win.blit(conn_text, (10, WIN_HEIGHT - conn_text.get_height()))

    node_text = STAT_FONT.render("Nodes: " + str(len(nodes)), 1, (50, 50, 50))
    win.blit(node_text, (10, WIN_HEIGHT - node_text.get_height() - conn_text.get_height()))

    pygame.display.update()


def main():
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    running = True

    nodes = [Node(100, 200), Node(300, 100), Node(400, 300), Node(500, 150)]
    connections = [Connection(nodes[0], nodes[1]),
                   Connection(nodes[1], nodes[2]),
                   Connection(nodes[2], nodes[3])]

    buttons = [Button("Add New Node", BUTTON_FONT, BUTTON_BG_COLOUR, (0, 0))]
    buttons.append(Button("Add New Connection", BUTTON_FONT, BUTTON_BG_COLOUR, (buttons[0].bg_rect.width, 0)))

    mode = "regular"

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if mode == "regular":

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos

                    if event.button == 1:
                        for button in buttons:
                            if button.clicked(mouse_x, mouse_y):
                                print("button clicked")
                                mode == "placing node"

            elif mode == "placing node":

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos

                    if event.button == 1:
                        for button in buttons:
                            if button.clicked(mouse_x, mouse_y):
                                print("button clicked")
                                mode == "placing node"

        draw_window(win, mode, nodes, connections, buttons)


if __name__ == '__main__':
    main()
    pygame.quit()
    sys.exit()
