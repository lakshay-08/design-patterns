from abc import ABC, abstractmethod

# Implementor
class DrawingAPI(ABC):
    @abstractmethod
    def draw_circle(self, x, y, radius):
        pass

# ConcreteImplementors
class OpenGLAPI(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"OpenGL: Drawing circle at ({x}, {y}) with radius {radius}")

class DirectXAPI(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"DirectX: Drawing circle at ({x}, {y}) with radius {radius}")

# Abstraction
class Shape(ABC):
    def __init__(self, drawing_api: DrawingAPI):
        self.drawing_api = drawing_api

    @abstractmethod
    def draw(self):
        pass

# Refined Abstraction
class Circle(Shape):
    def __init__(self, x, y, radius, drawing_api: DrawingAPI):
        super().__init__(drawing_api)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        self.drawing_api.draw_circle(self.x, self.y, self.radius)

# Client code
if __name__ == "__main__":
    circle1 = Circle(1, 2, 3, OpenGLAPI())
    circle2 = Circle(5, 7, 10, DirectXAPI())

    circle1.draw()
    circle2.draw()
