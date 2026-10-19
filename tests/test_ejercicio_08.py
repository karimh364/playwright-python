from playwright.sync_api import Page, expect


def test_ejercicio_08_navegar_y_volver_atras(page: Page):
    page.goto("https://the-internet.herokuapp.com/")

    link_login = page.get_by_role(
        "link",
        name="Form Authentication",
        exact=True
    )

    link_login.click()
    expect(page).to_have_url("https://the-internet.herokuapp.com/login")

    page.go_back()
    expect(page).to_have_url("https://the-internet.herokuapp.com/")

    link_checkboxes = page.get_by_role(
        "link",
        name="Checkboxes",
        exact=True
    )

    link_checkboxes.click()
    expect(page).to_have_url("https://the-internet.herokuapp.com/checkboxes")

    page.go_back()
    expect(page).to_have_url("https://the-internet.herokuapp.com/")