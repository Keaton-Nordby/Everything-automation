from playwright.sync_api import Page, expect


def test_homepage_loads(app: Page):
    """Verify the TechMart homepage loads successfully."""
    expect(app).to_have_title("TechMart - Your Tech Essentials Store")


def test_homepage_hero(app: Page):
    """Verify the homepage hero section displays the expected content."""
    expect(app.get_by_role("heading", name="Welcome to TechMart")).to_be_visible()
    expect(
        app.get_by_text("Find the best tech accessories for your setup")
    ).to_be_visible()


def test_homepage_search(app: Page):
    """Verify users can search for products from the homepage."""
    search = app.get_by_role("textbox", name="Search products")
    search.fill("Keyboard")

    app.get_by_role("button", name="Search").click()
    expect(app.get_by_text("Mechanical Keyboard")).to_be_visible()


def test_homepage_category_filter(app: Page):
    """Verify users can filter products by category."""
    category_filter = app.get_by_role("combobox", name="Category: ")
    category_filter.select_option("Accessories")

    products = app.locator(".product-card")
    expect(products).to_have_count(2)

    expect(app.get_by_text("Monitor Stand")).to_be_visible()


def test_homepage_sort_price_high_to_low(app: Page):
    """Verify users can sort products from highest to lowest price"""
    sort_by_filter = app.get_by_role("combobox", name="Sort by: ")
    sort_by_filter.select_option("price-high")

    products = app.locator(".product-card")
    expect(products).to_have_count(6)
    expect(products.first.locator("h3")).to_have_text("Mechanical Keyboard")
    expect(products.last.locator("h3")).to_have_text("Mouse Pad XL")


def test_homepage_sort_price_low_to_high(app: Page):
    """Verify users can sort products from lowest to highest price"""
    sort_by_filter = app.get_by_role("combobox", name="Sort by: ")
    sort_by_filter.select_option("price-low")

    products = app.locator(".product-card")
    expect(products).to_have_count(6)
    expect(products.first.locator("h3")).to_have_text("Mouse Pad XL")
    expect(products.last.locator("h3")).to_have_text("Mechanical Keyboard")


def test_homepage_filter_price_drag(app: Page):
    """Verify users can filter products by price selection"""
    price_filter = app.get_by_role("slider", name="Max Price: $200")
    price_filter.fill("50")

    products = app.locator(".product-card")
    expect(products).to_have_count(2)


def test_homepage_products(app: Page):
    """Verify products are displayed correctly on the homepage."""
    products = app.locator(".product-card")
    expect(products).to_have_count(6)
