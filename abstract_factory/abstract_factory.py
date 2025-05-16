# Abstract Products
class Button:
    def click(self):
        pass

class Checkbox:
    def check(self):
        pass    

# Concrete Products for Windows
class WindowsButton(Button):
    def click(self):
        return "Windows Button Clicked"

class WindowsCheckbox(Checkbox):
    def check(self):
        return "Windows Checkbox Checked"

# Concrete Products for Mac
class MacButton(Button):
    def click(self):
        return "Mac Button Clicked"

class MacCheckbox(Checkbox):
    def check(self):
        return "Mac Checkbox Checked"
    
# Abstract Factory
class GUIFactory:
    def create_button(self) -> Button:
        pass

    def create_checkbox(self) -> Checkbox:
        pass

# Concrete Factory for Windows
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

# Concrete Factory for MacOS
class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

# Client
class Application:
    def __init__(self, factory: GUIFactory):
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def render(self):
        print(self.button.click())
        print(self.checkbox.check())

# Usage
def create_ui(os_type: str):
    if os_type == "Windows":
        factory = WindowsFactory()
    elif os_type == "Mac":
        factory = MacFactory()
    else:
        raise ValueError("Unknown OS")
    
    app = Application(factory)
    app.render()

# Run the example
create_ui("Windows")
create_ui("Mac")

            