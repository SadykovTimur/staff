from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

__all__ = ['LogoutPage']


class LogoutPage(Page):
    title = Text(class_name="exitBy")
    logo = Component(class_name="exitImg")
    submit = Button(id="repeatEnter")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert 'До новых встреч!' == self.title
                assert self.logo.visible

                return self.submit.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=40, msg='Страница выхода из информационной базы ЕАИС Кадры 2.0 не загружена')
        self.app.restore_implicitly_wait()
