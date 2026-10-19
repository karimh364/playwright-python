from playwright.sync_api import Page, expect


def test_ejercicio_01_navegar(page: Page):
    page.goto("https://the-internet.herokuapp.com/")

    expect(page).to_have_url("https://the-internet.herokuapp.com/")