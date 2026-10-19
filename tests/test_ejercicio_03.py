from playwright.sync_api import Page, expect


def test_ejercicio_03_hacer_clic_en_link(page: Page):
    page.goto("https://the-internet.herokuapp.com/")

    link_login = page.get_by_role(
        "link",
        name="Form Authentication",
        exact=True
    )

    link_login.click()

    expect(page).to_have_url("https://the-internet.herokuapp.com/login")