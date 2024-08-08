from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from coms.qa.frontend.pages.component.text_field import TextField

__all__ = ['Main']


class MainWrapper(ComponentWrapper):
    title = Component(css='[class*="toplineCenter"]')
    list = Component(xpath='//div[text()="Списочный состав"]')
    work = Component(xpath='//div[text()="Мои задачи"]')
    my_work = Component(xpath='//div[text()="Задачи"]')
    item_employee = Components(xpath='//div[text()="Сотрудники"]')
    item_journal = Components(xpath='//div[text()="Приемы на работу"]')
    title_employee = Component(css='[data-title="Сотрудники"]')
    title_journal = Component(css='[data-title="Приемы на работу"]')
    title_document = Component(css='[data-title="Прием на работу 0000-000702 от 05.04.2021"]')
    table_field = Components(css='[class="gridBox"]')
    save_data = Button(css='[title*="Провести и закрыть"]')
    field_search = TextField(css='[class="inputsBox dots"] [id*="СписокСтрокаПоиска"]')
    field_physical = TextField(css='[class="inputsBox dots"] [id*="ФизическоеЛицо"]')
    dropdown = Button(css='[class*="eddText"] b span')
    field_data = TextField( css='[class="inputs"] [id*="ДлительностьИспытательногоСрока"] ')
    search_employee = Text(css='[class="gridBox select"]')
    card_employee = Button(css='[class="gridBoxText"] b')
    title_card = Component(css='[data-title="Тест для Мониторинга (Сотрудник)"]')
    physical_card = Button(xpath='//span[text()="Перейти на карточку физлица"]')
    physical_title = Component(css='[data-title="Тест для Мониторинга (Физическое лицо)"]')
    input_birthday = TextField(xpath='(//label[@title="Дата рождения физического лица"]//input)[2]')  # обратить внимание
    save = Button(xpath='(//span[@title="Записать и закрыть (Ctrl+Enter)"])[2] ')  # обратить внимание
    exit = Button(css='[id*="2headerTopLine_cmd_CloseButton"]') #обратить внимание
    document_monitoring = Button(xpath='//div[text()="Тест для Мониторинга"]')

    @property
    def is_visible(self) -> bool:
        assert self.title.visible
        assert self.list.visible
        assert self.work.visible

        return self.my_work.visible


class Main(Component):
    def __get__(self, instance, owner) -> MainWrapper:
        return MainWrapper(instance.app, self.find(instance), self._locator)
