import allure
from coms.qa.fixtures.application import Application
from coms.qa.frontend.helpers.attach_helper import screenshot_attach
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

from dit.qa.pages.logout_page import LogoutPage
from dit.qa.pages.main_page import MainPage
from dit.qa.pages.start_page import StartPage

__all__ = [
    'open_start_page',
    'sign_in',
    'open_main_page',
    'open_employee',
    'search_employee',
    'open_employee_card',
    'open_physical_card',
    'changed_date_birth_95',
    'changed_date_birth_96',
    'save_changed_date_birth_95',
    'save_changed_date_birth_96',
    'exit_employee_card',
    'open_documents',
    'open_journal_documents',
    'change_data_documents_2',
    'change_data_documents_3',
    'save_data_documents',
    'logout',
]


def open_start_page(app: Application) -> None:
    with allure.step('Opening Start page'):
        try:
            page = StartPage(app)
            page.open()

            page.wait_for_loading()

            screenshot_attach(app, 'start_page')
        except Exception as e:
            screenshot_attach(app, 'start_page_error')

            raise e


def sign_in(app: Application, login: str, password: str) -> None:
    with allure.step(f'{login} signing in'):
        try:
            auth_form = StartPage(app)

            auth_form.login.send_keys(login)
            auth_form.password.send_keys(password)

            screenshot_attach(app, 'auth_data')
        except Exception as e:
            screenshot_attach(app, 'auth_data_error')

            raise NoSuchElementException('Ошибка ввода данных') from e

        auth_form.submit.click()


def open_main_page(app: Application) -> None:
    with allure.step('Opening Main page'):
        try:
            MainPage(app).wait_for_loading()

            screenshot_attach(app, 'main_page')
        except Exception as e:
            screenshot_attach(app, 'main_page_error')

            raise e


def open_employee(app: Application) -> None:
    with allure.step('Opening Employee'):
        try:
            page = MainPage(app)
            page.menu.staff.click()
            page.main.item_employee[0].webelement.click()

            page.wait_for_loading_employee()

            screenshot_attach(app, 'directory_employee')
        except Exception as e:
            screenshot_attach(app, 'directory_employee_error')

            raise e


def search_employee(app: Application) -> None:
    with allure.step('Searching Employee'):
        try:
            page = MainPage(app)
            page.main.field_search.send_keys("Тест для Мониторинга")

            page.wait_for_loading_search_employee()

            screenshot_attach(app, 'search_employee')
        except Exception as e:
            screenshot_attach(app, 'search_employee_error')

            raise e


def open_employee_card(app: Application) -> None:
    with allure.step('Opening Employee card'):
        try:
            page = MainPage(app)
            ActionChains(app.driver).double_click(page.main.card_employee.webelement).perform()  # type: ignore[no-untyped-call]

            page.wait_for_loading_employee_card()

            screenshot_attach(app, 'employee_card')
        except Exception as e:
            screenshot_attach(app, 'employee_card_error')

            raise e


def open_physical_card(app: Application) -> None:
    with allure.step('Opening Physical card'):
        try:
            page = MainPage(app)
            page.main.physical_card.click()

            page.wait_for_loading_physical_card()

            screenshot_attach(app, 'physical_card')
        except Exception as e:
            screenshot_attach(app, 'physical_card_error')

            raise e


def changed_date_birth_95(app: Application, data: str) -> None:
    with allure.step('Changing date birth 95'):
        try:
            page = MainPage(app)
            page.main.input_birthday.send_keys("02.10.1995")

            page.wait_for_loading_changing_date_birth_95(data)

            screenshot_attach(app, 'changing_date_birth_95')
        except Exception as e:
            screenshot_attach(app, 'changing_date_birth_error_95')

            raise e


def changed_date_birth_96(app: Application, data: str) -> None:
    with allure.step('Changing date birth 96'):
        try:
            page = MainPage(app)
            page.main.input_birthday.send_keys("02.10.1996")

            page.wait_for_loading_changing_date_birth_96(data)

            screenshot_attach(app, 'changing_date_birth_96')
        except Exception as e:
            screenshot_attach(app, 'changing_date_birth_error_96')

            raise e


def save_changed_date_birth_95(app: Application) -> None:
    with allure.step('Save changed date birth 95'):
        try:
            page = MainPage(app)
            page.main.save.click()

            page.wait_for_loading_employee_card()

            screenshot_attach(app, 'save_changed_date_birth_95')
        except Exception as e:
            screenshot_attach(app, 'save_changed_date_birth_error_95')

            raise e


def save_changed_date_birth_96(app: Application) -> None:
    with allure.step('Save changed date birth 96'):
        try:
            page = MainPage(app)
            page.main.save.click()

            page.wait_for_loading_employee_card()

            screenshot_attach(app, 'save_changed_date_birth_96')
        except Exception as e:
            screenshot_attach(app, 'save_changed_date_birth_error_96')

            raise e


def exit_employee_card(app: Application) -> None:
    with allure.step('Exit Employee card'):
        try:
            page = MainPage(app)
            page.main.exit.click()

            page.wait_for_loading_employee()

            screenshot_attach(app, 'exit_employee_card')
        except Exception as e:
            screenshot_attach(app, 'exit_employee_card_error')

            raise e


def open_journal_documents(app: Application) -> None:
    with allure.step('Opening Journal documents'):
        try:
            page = MainPage(app)
            page.menu.staff.click()
            page.main.item_journal[0].webelement.click()

            page.wait_for_loading_journal_documents()

            screenshot_attach(app, 'journal_documents')
        except Exception as e:
            screenshot_attach(app, 'journal_documents_error')

            raise e


def open_documents(app: Application) -> None:
    with allure.step('Opening Documents'):
        try:
            page = MainPage(app)
            page.main.field_physical.send_keys("Тест для Мониторинга")
            page.dropdown.click()
            ActionChains(app.driver).double_click(page.main.document_monitoring.webelement).perform()  # type: ignore[no-untyped-call]

            page.wait_for_loading_document()

            screenshot_attach(app, 'documents')
        except Exception as e:
            screenshot_attach(app, 'documents_error')

            raise e


def change_data_documents_2(app: Application, data: str) -> None:
    with allure.step('Changing Data documents'):
        try:
            page = MainPage(app)
            page.main.field_data.webelement.click()
            page.main.field_data.send_keys('2')

            page.wait_for_loading_data_document(data)

            screenshot_attach(app, 'change_documents')
        except Exception as e:
            screenshot_attach(app, 'change_documents_error')

            raise e


def change_data_documents_3(app: Application, data: str) -> None:
    with allure.step('Changing Data documents'):
        try:
            page = MainPage(app)
            page.main.field_data.webelement.click()
            page.main.field_data.send_keys('3')

            page.wait_for_loading_data_document(data)

            screenshot_attach(app, 'change_documents')
        except Exception as e:
            screenshot_attach(app, 'change_documents_error')

            raise e


def save_data_documents(app: Application) -> None:
    with allure.step('Saving Data documents'):
        try:
            page = MainPage(app)
            page.main.save_data.click()

            page.wait_for_loading_journal_documents()

            screenshot_attach(app, 'save_documents')
        except Exception as e:
            screenshot_attach(app, 'save_documents_error')

            raise e


def logout(app: Application) -> None:
    with allure.step('Logout'):
        try:
            page = MainPage(app)
            page.header.logout.click()
            page.exit.click()
            page.alert_logout()

            LogoutPage(app).wait_for_loading()

            screenshot_attach(app, 'logout')
        except Exception as e:
            screenshot_attach(app, 'logout_error')

            raise e
