import pathlib
import unittest
from html.parser import HTMLParser


ROOT = pathlib.Path(__file__).resolve().parents[1]


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.forms = []
        self.scripts = []
        self.inputs = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "form":
            self.forms.append(a)
        if tag == "script":
            self.scripts.append(a)
        if tag == "input":
            self.inputs.append(a)


class SiteTests(unittest.TestCase):
    def test_pages(self):
        for name in ("index.html", "course38.html"):
            with self.subTest(name=name):
                html = (ROOT / name).read_text(encoding="utf-8")
                page = SiteParser()
                page.feed(html)
                self.assertIn("Demo Only", html)
                self.assertNotIn("120253338", html)
                self.assertIn("No data was sent", (ROOT / "script.js").read_text())
                self.assertEqual(len(page.forms), 1)
                self.assertEqual(page.forms[0]["id"], "demo-registration-form")
                self.assertTrue(any(s.get("src") == "script.js" for s in page.scripts))
                self.assertEqual(len(page.inputs), 3)
                self.assertTrue(all("required" in field for field in page.inputs))


if __name__ == "__main__":
    unittest.main()
