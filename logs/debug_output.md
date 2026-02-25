============================= test session starts =============================
platform win32 -- Python 3.13.0, pytest-8.4.2, pluggy-1.6.0 -- C:\Users\rlp\AppData\Local\pypoetry\Cache\virtualenvs\ads-spec-backend-com-python-UQs95u0N-py3.13\Scripts\python.exe
cachedir: .pytest_cache
baseurl: http://127.0.0.1:8766
rootdir: D:\SourceCode\REPOS\github.io\ads_mod_01_fundamentos_da_computacao
configfile: pyproject.toml
plugins: base-url-2.1.0, playwright-0.5.2
collecting ... collected 1 item

tests/debug_quiz.py::test_debug_quiz_elements[chromium] Navigating to http://127.0.0.1:8766/quizzes/quiz-01/
CONSOLE: Failed to load resource: the server responded with a status of 404 (File not found)
CONSOLE: Failed to load resource: the server responded with a status of 403 ()
CONSOLE: Failed to load resource: the server responded with a status of 403 ()
CONSOLE: Termynal loaded
CONSOLE: Quiz JS loaded
CONSOLE: Found termynals: 0
CONSOLE: Quiz JS loaded
CONSOLE: Failed to load resource: the server responded with a status of 404 (File not found)
Found 1 .quiz-question elements.
Question 1: 1. Qual o principal conceito de Aula 01 – Introdução à Computação e Bases Numéricas?

Clicking option...
Feedback visible: True
Feedback display style: block
Feedback inner HTML: <strong>Correto!</strong> Correto!
FAILED

================================== FAILURES ===================================
_____________________ test_debug_quiz_elements[chromium] ______________________

page_with_base_url = <Page url='http://127.0.0.1:8766/quizzes/quiz-01/'>
base_url = 'http://127.0.0.1:8766'

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
>       assert False, "Debug run complete"
E       AssertionError: Debug run complete
E       assert False

tests\debug_quiz.py:46: AssertionError
=========================== short test summary info ===========================
FAILED tests/debug_quiz.py::test_debug_quiz_elements[chromium] - AssertionError: Debug run complete
assert False
============================== 1 failed in 4.71s ==============================
