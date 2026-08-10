"""
Shared pytest fixtures and configuration for Playwright tests.
"""

import pytest
from playwright import Page, expect


@pytest.fixture
def app(page: Page) -> Page:
    """Navigate to the application before each test"""
    page.goto("http://localhost:3000/")
    return page