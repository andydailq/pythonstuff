from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.graphics.gtypes import GPoint
from campy.gui.events.mouse import onmouseclicked, onmousemoved


class RubberBandGraphics:
	def __init__(self, width=500, height=300):
		self.window = GWindow(width, height)
		self.line = None
		onmouseclicked(self.click_handler)
		onmousemoved(self.move_handler)
		self.inline = False

	def click_handler(self, event):
		x = event.x
		y = event.y
		self.draw_line(x, y, x, y)

	def begin(self, x, y):
		point = GPoint(x, y)
		return point

	def move_handler(self, event):
		x = event.x
		y = event.y
		if self.line is not None:
			self.line.end = self.end(x, y)

	def end(self, x, y):
		point = GPoint(x, y)
		return point

	def draw_line(self, x0, y0, x1, y1):
		line = GLine(x0, y0, x1, y1)
		self.line = line
		self.window.add(self.line)
		return self.line

def main():
	# This line is all that is needed in main!
	# Once the graphical window is created, the mouse
	# listener handlers take care of the rest.
	rubber_band_program = RubberBandGraphics()


if __name__ == '__main__':
	main()