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

    # GitHub protects the signup flow with DataDome, so page content (form or
    # challenge) is not deterministic. This test covers the entry point only:
    # the CTA routes to /signup.
    def test_sign_up_page(self, page: Page):
        page.goto("/")
        page.get_by_role("link", name=re.compile("Sign up", re.IGNORECASE)).first.click()
        # Wait for the URL to commit, not for the page to fully load: an
        # anti-bot challenge page can take a long time to finish loading,
        # but the navigation itself starts right away.
        page.wait_for_url(re.compile(r"/signup"), wait_until="commit")
        assert "/signup" in page.url
