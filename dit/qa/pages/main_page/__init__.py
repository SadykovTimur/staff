from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException

from dit.qa.pages.main_page.component.header import Header
from dit.qa.pages.main_page.component.main import Main
from dit.qa.pages.main_page.component.menu import Menu

__all__ = ['MainPage']


class MainPage(Page):
    close = Button(css='[id*="cmd_CloseButton"]')
    header = Header(id="captionbar")
    menu = Menu(id="themesCell")
    main = Main(id="pagesArea")
    exit = Button(id="LogoutCloseButton")
    dropdown = Button(css='[class*="eddText"] b span')

    def alert_logout(self) -> None:
        try:
            self.driver.switch_to.alert.accept()

        except UnexpectedAlertPresentException:
            pass

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.is_visible

                assert (
                    'Главное\nКадровый учет\nОбучение\nОтчеты КС\nОтчетность, справки\nНаграды\nЭКДО'
                    == self.menu.themes
                )

                return self.main.is_visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=40, msg='Главная страница не загружена')
        self.app.restore_implicitly_wait()

    def wait_for_loading_employee(self) -> None:
        def condition() -> bool:
            try:
                assert self.main.title_employee.visible

                return self.main.table_field[0].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=40, msg='Справочник "Сотрудники" не загружен')
        self.app.restore_implicitly_wait()

    def wait_for_loading_search_employee(self) -> None:
        def condition() -> bool:
            try:
                return 'Тест для Мониторинга' == self.main.search_employee

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=50, msg='Поиск в справочнике "Сотрудники" не загружен')
        self.app.restore_implicitly_wait()

    def wait_for_loading_employee_card(self) -> None:
        def condition() -> bool:
            try:
                return self.main.title_card.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=60, msg='Карточка сотрудника не загружена')
        self.app.restore_implicitly_wait()

    def wait_for_loading_physical_card(self) -> None:
        def condition() -> bool:
            try:
                return self.main.physical_title.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=40, msg='Карточка физлица не загружена')
        self.app.restore_implicitly_wait()

    def wait_for_loading_changing_date_birth_95(self, data: str) -> None:
        def condition() -> bool:
            try:
                return self.main.input_birthday.value == data

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=40, msg='Изменение реквизита 02.10.1995 в дате рождения не загружена')
        self.app.restore_implicitly_wait()

    def wait_for_loading_changing_date_birth_96(self, data: str) -> None:
        def condition() -> bool:
            try:
                return self.main.input_birthday.value == data

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=50, msg='Изменение реквизита 02.10.1996 в дате рождения не загружена')
        self.app.restore_implicitly_wait()

    def wait_for_loading_save_changing_date_birth_95(self) -> None:
        def condition() -> bool:
            try:
                return self.main.birth_95.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Сохранение реквизита 02.10.1995 в дате рождения не загружена')
        self.app.restore_implicitly_wait()

    def wait_for_loading_save_changing_date_birth_96(self) -> None:
        def condition() -> bool:
            try:
                return self.main.birth_96.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Сохранение реквизита 02.10.1996 в дате рождения не загружена')
        self.app.restore_implicitly_wait()

    def wait_for_loading_journal_documents(self) -> None:
        def condition() -> bool:
            try:
                assert self.main.title_journal.visible

                return self.main.table_field[0].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Журнал документов "Приемы на работу" не загружен')
        self.app.restore_implicitly_wait()

    def wait_for_loading_document(self) -> None:
        def condition() -> bool:
            try:
                return self.main.title_document.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=40, msg='Документ "Прием на работу" не загружен')
        self.app.restore_implicitly_wait()

    def wait_for_loading_data_document(self, data: str) -> None:
        def condition() -> bool:
            try:
                return self.main.field_data.value == data

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=50, msg='Изменение реквизита не загружена')
        self.app.restore_implicitly_wait()
