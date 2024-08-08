from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text

__all__ = ['Menu']


class MenuWrapper(ComponentWrapper):
    themes = Text(id="themesCellLimiter")
    staff = Button(xpath="//span[text()='Кадровый учет']")


class Menu(Component):
    def __get__(self, instance, owner) -> MenuWrapper:
        return MenuWrapper(instance.app, self.find(instance), self._locator)
