class MenuItem:
    def __init__(self, label, callback):
        if len(label) < 1:
            raise Exception("MenuItem: Label must not be an empty string")
        self.label = label
        self.callback = callback


class Menu:
    def __init__(self, items, title, framebuffer):
        if len(items) < 1:
            raise Exception("Menu: Menu must contain at least one item")
        self.items = items
        self.title = title
        self.framebuffer = framebuffer
        self.focused_item = 0

    def focus_id(self, focus_id):
        if 0 > focus_id >= len(self.items):
            raise Exception("Menu: Got invalid id in 'focus' method")
        self.focused_item = focus_id
        print(f"Focused item: ID={self.focused_item}, LABEL: {self.items[self.focused_item].label}")

    def focus_next(self):
        self.focused_item += 1
        if self.focused_item >= len(self.items):
            self.focused_item = 0
        print(f"Focused item: ID={self.focused_item}, LABEL: {self.items[self.focused_item].label}")

    def focus_previous(self):
        self.focused_item -= 1
        if self.focused_item < 0:
            self.focused_item = len(self.items) - 1
        print(f"Focused item: ID={self.focused_item}, LABEL: {self.items[self.focused_item].label}")

    def click_focused_item(self):
        self.items[self.focused_item].callback()

    def draw_menu(self):
        pass


def test():
    menu_items = []

    def cb(item_id):
        return lambda: print(f"Callback {item_id}")

    for i in range(4):
        menu_items.append(MenuItem(f"Label_{i}", cb(i)))

    menu = Menu(menu_items, "Menu Title")
    menu.focus_next()
    menu.focus_next()
    menu.focus_next()
    menu.focus_previous()
    menu.focus_id(1)
    menu.click_focused_item()
