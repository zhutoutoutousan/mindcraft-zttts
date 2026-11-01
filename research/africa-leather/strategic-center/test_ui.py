#!/usr/bin/env python3
"""
UI test script using Playwright to verify language switching functionality
"""
import asyncio
from playwright.async_api import async_playwright
import json

async def test_language_switching():
    """Test language switching on both desktop and mobile viewports"""
    
    async with async_playwright() as p:
        # Launch browser in headless mode
        browser = await p.chromium.launch(headless=True)
        
        results = {
            "desktop": {},
            "mobile": {}
        }
        
        # Test 1: Desktop viewport
        print("\n=== Testing Desktop Viewport ===")
        context_desktop = await browser.new_context(viewport={"width": 1920, "height": 1080})
        page_desktop = await context_desktop.new_page()
        
        # Enable console logging
        page_desktop.on("console", lambda msg: print(f"[CONSOLE-DESKTOP] {msg.type}: {msg.text}"))
        page_desktop.on("pageerror", lambda exc: print(f"[ERROR-DESKTOP] {exc}"))
        
        # Navigate to the page
        await page_desktop.goto("http://localhost:8080")
        await page_desktop.wait_for_load_state("networkidle")
        
        # Check initial language
        hero_title_desktop = await page_desktop.locator('.hero h2').text_content()
        print(f"Initial hero title (Desktop): {hero_title_desktop}")
        results["desktop"]["initial_hero_title"] = hero_title_desktop
        
        # Click language toggle to open menu
        await page_desktop.click('.lang-toggle')
        await page_desktop.wait_for_timeout(500)
        
        # Check if menu is expanded
        is_expanded_desktop = await page_desktop.evaluate("""
            document.getElementById('langSwitcher').classList.contains('expanded')
        """)
        print(f"Menu expanded (Desktop): {is_expanded_desktop}")
        results["desktop"]["menu_expanded"] = is_expanded_desktop
        
        # Click Chinese language button
        print("Clicking Chinese language button...")
        await page_desktop.click('[data-lang="zh"]')
        await page_desktop.wait_for_timeout(1000)
        
        # Check updated hero title
        hero_title_zh_desktop = await page_desktop.locator('.hero h2').text_content()
        print(f"Hero title after clicking Chinese (Desktop): {hero_title_zh_desktop}")
        results["desktop"]["hero_title_zh"] = hero_title_zh_desktop
        
        # Click language toggle again
        await page_desktop.click('.lang-toggle')
        await page_desktop.wait_for_timeout(500)
        
        # Click German language button
        print("Clicking German language button...")
        await page_desktop.click('[data-lang="de"]')
        await page_desktop.wait_for_timeout(1000)
        
        # Check updated hero title
        hero_title_de_desktop = await page_desktop.locator('.hero h2').text_content()
        print(f"Hero title after clicking German (Desktop): {hero_title_de_desktop}")
        results["desktop"]["hero_title_de"] = hero_title_de_desktop
        
        await context_desktop.close()
        
        # Test 2: Mobile viewport
        print("\n=== Testing Mobile Viewport ===")
        context_mobile = await browser.new_context(
            viewport={"width": 375, "height": 667},
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15"
        )
        page_mobile = await context_mobile.new_page()
        
        # Enable console logging
        page_mobile.on("console", lambda msg: print(f"[CONSOLE-MOBILE] {msg.type}: {msg.text}"))
        page_mobile.on("pageerror", lambda exc: print(f"[ERROR-MOBILE] {exc}"))
        
        # Navigate to the page
        await page_mobile.goto("http://localhost:8080")
        await page_mobile.wait_for_load_state("networkidle")
        
        # Check initial language
        hero_title_mobile = await page_mobile.locator('.hero h2').text_content()
        print(f"Initial hero title (Mobile): {hero_title_mobile}")
        results["mobile"]["initial_hero_title"] = hero_title_mobile
        
        # Click language toggle to open menu
        await page_mobile.click('.lang-toggle')
        await page_mobile.wait_for_timeout(500)
        
        # Check if menu is expanded
        is_expanded_mobile = await page_mobile.evaluate("""
            document.getElementById('langSwitcher').classList.contains('expanded')
        """)
        print(f"Menu expanded (Mobile): {is_expanded_mobile}")
        results["mobile"]["menu_expanded"] = is_expanded_mobile
        
        # Click Chinese language button
        print("Clicking Chinese language button...")
        await page_mobile.click('[data-lang="zh"]')
        await page_mobile.wait_for_timeout(1000)
        
        # Check updated hero title
        hero_title_zh_mobile = await page_mobile.locator('.hero h2').text_content()
        print(f"Hero title after clicking Chinese (Mobile): {hero_title_zh_mobile}")
        results["mobile"]["hero_title_zh"] = hero_title_zh_mobile
        
        # Click language toggle again
        await page_mobile.click('.lang-toggle')
        await page_mobile.wait_for_timeout(500)
        
        # Click Russian language button
        print("Clicking Russian language button...")
        await page_mobile.click('[data-lang="ru"]')
        await page_mobile.wait_for_timeout(1000)
        
        # Check updated hero title
        hero_title_ru_mobile = await page_mobile.locator('.hero h2').text_content()
        print(f"Hero title after clicking Russian (Mobile): {hero_title_ru_mobile}")
        results["mobile"]["hero_title_ru"] = hero_title_ru_mobile
        
        # Verify localStorage (check after Russian selection)
        stored_lang = await page_mobile.evaluate("localStorage.getItem('preferredLanguage')")
        print(f"Stored language in localStorage: {stored_lang}")
        results["mobile"]["stored_language"] = stored_lang
        
        await context_mobile.close()
        await browser.close()
        
        # Print summary
        print("\n=== Test Results Summary ===")
        print(json.dumps(results, indent=2, ensure_ascii=False))
        
        # Verify expectations
        print("\n=== Verification ===")
        passed = True
        
        # Desktop checks
        if "China → Africa" not in results["desktop"]["initial_hero_title"]:
            print("❌ Desktop: Initial title should be in English")
            passed = False
        else:
            print("✅ Desktop: Initial title is in English")
        
        if "中国" in results["desktop"]["hero_title_zh"]:
            print("✅ Desktop: Chinese language switch works")
        else:
            print("❌ Desktop: Chinese language switch failed")
            passed = False
        
        if "China →" in results["desktop"]["hero_title_de"] or "Leder" in results["desktop"]["hero_title_de"]:
            print("✅ Desktop: German language switch works")
        else:
            print("❌ Desktop: German language switch failed")
            passed = False
        
        # Mobile checks
        if "China → Africa" not in results["mobile"]["initial_hero_title"]:
            print("❌ Mobile: Initial title should be in English")
            passed = False
        else:
            print("✅ Mobile: Initial title is in English")
        
        if "中国" in results["mobile"]["hero_title_zh"]:
            print("✅ Mobile: Chinese language switch works")
        else:
            print("❌ Mobile: Chinese language switch failed")
            passed = False
        
        if "Китай" in results["mobile"]["hero_title_ru"] or "Африка" in results["mobile"]["hero_title_ru"]:
            print("✅ Mobile: Russian language switch works")
        else:
            print("❌ Mobile: Russian language switch failed")
            passed = False
        
        if results["mobile"]["stored_language"] == "ru":
            print("✅ Mobile: Language preference stored in localStorage")
        else:
            print("❌ Mobile: Language preference not stored correctly")
            passed = False
        
        if passed:
            print("\n🎉 All tests PASSED!")
            return 0
        else:
            print("\n❌ Some tests FAILED!")
            return 1

if __name__ == "__main__":
    exit_code = asyncio.run(test_language_switching())
    exit(exit_code)
