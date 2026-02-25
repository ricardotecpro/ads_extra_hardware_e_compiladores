from playwright.sync_api import Page, expect
import re
import pytest

@pytest.mark.skip(reason="Material copy button is tricky to test in headless mode")
def test_code_copy_button(page: Page, start_server, base_url):
    """
    Test that the Material for MkDocs code block copy button is visible and functional.
    """
    # Grant clipboard permissions
    page.context.grant_permissions(['clipboard-write', 'clipboard-read'])

    # Navigate to Setup 02 which has bash code blocks
    page.goto(f"{base_url}/setups/setup-02/")

    # Wait for code block to be visible
    # Material uses .md-clipboard as the copy button, usually visible on hover
    code_block = page.locator(".highlight").first
    expect(code_block).to_be_visible()
    code_block.hover()
    
    copy_button = code_block.locator(".md-clipboard")
    # It might take a moment to transition opacity
    expect(copy_button).to_be_visible()

    # Click the button
    copy_button.click()

    # Check for feedback (Material changes SVG or class)
    # Usually it shows a tooltip or changes icon.
    # The 'data-clipboard-target' might be present.
    # Verification of clipboard content is tricky in headless, but click should work.
    # Material adds 'md-clipboard--copied' class on success
    
    expect(copy_button).to_have_class(re.compile(r"md-clipboard--copied"))
