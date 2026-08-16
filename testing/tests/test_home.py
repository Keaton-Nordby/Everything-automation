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
    
    


def test_homepage_filters(app: Page):
    """Verify users can filter and sort products from the homepage."""
    pass


def test_homepage_products(app: Page):
    """Verify products are displayed correctly on the homepage."""
    pass


def test_homepage_add_to_cart(app: Page):
    """Verify users can add a product to their shopping cart."""
    pass
