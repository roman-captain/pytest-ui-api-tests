import re

import pytest
from playwright.sync_api import Page


@pytest.mark.ui
class TestGitHubNav:

    def test_sign_in_page(self, page: Page):
        page.goto("/")
        page.get_by_role("link", name="Sign in").first.click()
        assert page.get_by_role("heading", name="Sign in to GitHub").is_visible()

    def test_pricing_page(self, page: Page):
        page.goto("/")
        page.get_by_role("link", name="Pricing").first.click()
        assert "Pricing" in page.title()

    def test_sign_up_page(self, page: Page):
        page.goto("/")
        page.get_by_role("link", name=re.compile("Sign up", re.IGNORECASE)).first.click()
        assert page.get_by_text("Create your free account").is_visible()
