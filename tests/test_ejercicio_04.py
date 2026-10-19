from playwright.sync_api import Page, expect


def test_ejercicio_04_escribir_en_campo(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")

    campo_usuario = page.get_by_label("Username")

    campo_usuario.fill("tomsmith")

    expect(campo_usuario).to_have_value("tomsmith")