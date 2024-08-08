from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text

__all__ = ['Header']


class HeaderWrapper(ComponentWrapper):
    title = Text(id="captionbarTitle")
    title_1c = Text(id="captionbar1C")
    logo = Component(id="captionbarLogo")
    menu = Component(id="captionbarFunction")
    field = Component(id="captionbarField")
    logout = Button(id="LogoutButton")

    @property
    def is_visible(self) -> bool:
        assert 'Кадры 2 / Зарплата и кадры государственного учреждения КОРП, редакция 3.1' == self.title
        assert '(1С:Предприятие)' == self.title_1c
        assert self.logo.visible
        assert self.menu.visible
        assert self.field.visible

        return self.logout.visible


class Header(Component):
    def __get__(self, instance, owner) -> HeaderWrapper:
        return HeaderWrapper(instance.app, self.find(instance), self._locator)
