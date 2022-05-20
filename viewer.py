import math
import sys

WHITE = 0xFFFFFF
RED = 0xFF0000
GREEN = 0x00FF00
BLUE = 0x8888FF
YELLOW = 0xFFFF00


def view(width, height, title, helix, output):
	half = width // 2

	import pygame

	pygame.init()
	surface = pygame.display.set_mode((width, height))
	pygame.display.set_caption(title)

	cells = [helix.start, helix.size, helix.checksum]

	for cell in helix.data:
		cells.append(cell)
	cells.append(helix.end)

	for cell in cells:
		print(cell)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		surface.fill((255, 255, 255))

		start_y = 0

		for cell in cells:
			lines = list(zip(cell.get_left()[0], cell.get_right()[0]))

			degrees = [30, 75, 115, 150]
			colors = {
				'A': RED,
				'T': GREEN,
				'C': YELLOW,
				'G': BLUE
			}

			step = 180 // (len(lines) + 1)

			mapped_bars = {
				step * (index + 1): [colors[letter] for letter in line]
				for index, line in enumerate(lines)
			}

			for degrees in range(0, 180):
				x = int(math.sin(math.radians(degrees)) * 50)
				y = start_y + degrees

				left = half + x
				right = half - x

				if degrees in mapped_bars:
					bars = mapped_bars[degrees]

					distance = right - left
					bar_length = distance / len(bars)

					for index, bar in enumerate(bars):
						start = (left + (bar_length * index), y)
						end = (left + (bar_length * (index + 1)), y)
						pygame.draw.line(surface, bar, start, end, 2)

				surface.set_at((left, y), 0x000000)
				surface.set_at((right, y), 0x000000)

				"""if degrees == 0:
					pygame.draw.line(surface, YELLOW, (0, y), (width, y), 1)"""

			start_y += 180
		pygame.image.save(surface, output)
		pygame.display.update()
