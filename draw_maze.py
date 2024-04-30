from PIL import Image, ImageDraw
import path_to_walls

NUM_COLUMNS = 3
NUM_ROWS = 6
CELL_WIDTH = 100
MAZE_WIDTH = NUM_COLUMNS * CELL_WIDTH
MAZE_HEIGHT = NUM_ROWS * CELL_WIDTH


def create_base(draw):
    # draw white columns
    for i in range(NUM_COLUMNS):
        draw.line(xy=(CELL_WIDTH * (i + 0.5), 0, CELL_WIDTH * (i + 0.5), MAZE_HEIGHT), fill="white", width=5)
    # draw white rows
    for i in range(NUM_ROWS):
        draw.line(xy=(0, CELL_WIDTH * (i + 0.5), MAZE_WIDTH, CELL_WIDTH * (i + 0.5)), fill="white", width=5)


def draw_walls(draw, walls):
    for wall in walls:
        a = wall[0]
        b = wall[1]
        if a[0] == b[0]:
            # aligned on y-axis, draw a horizontal line
            x0 = a[0] - 0.5
            y0 = (a[1] + b[1]) / 2
            x1 = a[0] + 0.5
            y1 = (a[1] + b[1]) / 2
        elif a[1] == b[1]:
            # aligned on x-axis, draw a vertical line
            x0 = (a[0] + b[0]) / 2
            y0 = a[1] - 0.5
            x1 = (a[0] + b[0]) / 2
            y1 = a[1] + 0.5
        else:
            # shouldn't reach this case ever, skip
            continue

        draw.line(xy=((x0 + 0.5) * CELL_WIDTH, MAZE_HEIGHT - (y0 + 0.5) * CELL_WIDTH,
                      (x1 + 0.5) * CELL_WIDTH, MAZE_HEIGHT - (y1 + 0.5) * CELL_WIDTH),
                  fill="brown", width=5)


def draw_maze(walls):
    # create image with a dark grey background
    img = Image.new(mode="RGB", size=(MAZE_WIDTH, MAZE_HEIGHT), color=(50, 50, 50))
    draw = ImageDraw.Draw(img)
    create_base(draw)
    draw_walls(draw, walls)
    img.show()


if __name__ == "__main__":
    w = path_to_walls.read_coordinates("examples/coordinates1.txt").find_walls()
    draw_maze(w)
