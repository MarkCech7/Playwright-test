
from playwright.sync_api import Page, expect
import pytest

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("username").fill('standard_user')
    page.get_by_placeholder("Password").fill('secret_sauce')
    page.locator("[data-test=\"login-button\"]").click()

def test_run(page: Page) -> None:
    inventory_item_t_shirt = page.locator(".inventory_item_name ", has_text="Sauce Labs Bolt T-Shirt")
    expect(inventory_item_t_shirt).to_be_visible()
    inventory_item_t_shirt.click()
    expect(page.locator("[data-test=\"inventory-item-name\"]")).to_have_text("Sauce Labs Bolt T-Shirt")
    add_button = page.locator("[data-test=\"add-to-cart\"]")
    add_button.click()
    remove_button = expect(page.locator("[data-test=\"remove\"]"))
    remove_button.to_contain_text('Remove')
    page.get_by_role('button', name="Back to products").click()
    inventory_item_fleece_jacket = page.locator(".inventory_item_name ", has_text="Sauce Labs Fleece Jacket")
    expect(inventory_item_fleece_jacket).to_be_visible()
    inventory_item_fleece_jacket.click()
    expect(page.locator("[data-test=\"inventory-item-name\"]")).to_have_text("Sauce Labs Fleece Jacket")
    add_button.click()
    remove_button.to_contain_text('Remove')
    page.locator(".shopping_cart_link").click()
    expect(inventory_item_t_shirt).to_be_visible()
    expect(inventory_item_fleece_jacket).to_be_visible()
    page.get_by_role('button', name="Checkout").click()
    page.get_by_placeholder("First Name").fill('Saucer')
    page.get_by_placeholder("Last Name").fill('MerchBuyer')
    page.get_by_placeholder("Zip/Postal Code").fill("010 10")
    page.locator("[data-test=\"continue\"]").click()
    expect(inventory_item_t_shirt).to_be_visible()
    expect(inventory_item_fleece_jacket).to_be_visible()
    expect(page.locator(".summary_tax_label")).to_contain_text("Tax: $" "5.28")
    expect(page.locator(".summary_total_label")).to_contain_text("Total: $" "71.26")

def test_add_remove(page: Page) -> None:
    inventory_item_bike_light = page.locator(".inventory_item_name ", has_text="Sauce Labs Bike Light")
    expect(inventory_item_bike_light).to_be_visible()
    inventory_item_bike_light.click()
    page.locator("[data-test=\"add-to-cart\"]").click()
    page.locator("[data-test=\"remove\"]").click()
    expect(page.locator(".shopping_cart_link")).to_be_empty()
  
def test_cart(page: Page) -> None:
    inventory_item_onesie = page.locator(".inventory_item_name ", has_text="Sauce Labs Onesie")
    expect(inventory_item_onesie).to_be_visible()
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    page.locator(".shopping_cart_link").click()
    page.get_by_role('button', name="Remove").click()
    expect(page.locator(".shopping_cart_link")).to_be_empty()
    