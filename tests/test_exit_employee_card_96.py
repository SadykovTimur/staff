from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.steps import (
    exit_employee_card,
    logout,
    open_employee,
    open_employee_card,
    open_main_page,
    open_start_page,
    search_employee,
    sign_in,
)


@allure.label('owner', 't.sadykov')
@allure.label('component', 'DIT')
@allure.epic('STAFF')
@allure.story('Карточка физ.лица')
@allure.title('Закрываем карточку сотрудника (Изменение даты рожжения 96)')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_exit_employee_card_96(
    request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str
) -> None:

    app = make_app(browser, device_type)

    open_start_page(app)

    sign_in(app, request.config.option.username, request.config.option.password)
    open_main_page(app)

    open_employee(app)
    search_employee(app)
    open_employee_card(app)
    exit_employee_card(app)

    logout(app)
