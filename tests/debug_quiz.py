import pytest
from playwright.sync_api import Page, expect

def test_debug_quiz_elements(page_with_base_url: Page, base_url: str):
    page = page_with_base_url
    
    # Capture console logs
    page.on("console", lambda msg: print(f"CONSOLE: {msg.text}"))
    page.on("pageerror", lambda err: print(f"PAGE ERROR: {err}"))
    
    url = f"{base_url}/quizzes/quiz-01/"
    print(f"Navigating to {url}")
    page.goto(url)
    
    # 1. Investigate Question Count
    questions = page.locator(".quiz-question")
    count = questions.count()
    print(f"Found {count} .quiz-question elements.")
    
    for i in range(count):
        print(f"Question {i+1}: {questions.nth(i).inner_text()}")
        
    # 2. Investigate Feedback Visibility
    quiz_container = page.locator(".quiz-container").first
    option = quiz_container.locator(".quiz-option").first
    
    print("\nClicking option...")
    option.click()
    
    feedback = quiz_container.locator(".quiz-feedback")
    
    # Wait a moment
    page.wait_for_timeout(1000)
    
    is_visible = feedback.is_visible()
    print(f"Feedback visible: {is_visible}")
    
    # Check computed style
    display = feedback.evaluate("el => window.getComputedStyle(el).display")
    print(f"Feedback display style: {display}")
    
    inner_html = feedback.inner_html()
    print(f"Feedback inner HTML: {inner_html}")
    
    # Fail intentionally to see output
    assert False, "Debug run complete"
