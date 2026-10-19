from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_ejercicio_07_tomar_screenshot(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("tomsmith", "SuperSecretPassword!")

    mensaje_exito = page.get_by_text("You logged into a secure area!")
    expect(mensaje_exito).to_be_visible()

    page.screenshot(
        path="screenshots/ejercicio07-login-exitoso.png",
        full_page=True
    )