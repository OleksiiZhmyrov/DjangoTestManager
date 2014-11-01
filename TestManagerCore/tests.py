from django.test import TestCase, Client
from TestManagerCore.models import Tag, Sprint, Browser, Environment, JiraIssue


class JiraIssueTests(TestCase):
    """JiraIssue model tests."""

    def test_str(self):

        issue = JiraIssue(
            key='JIRA-0001',
            summary='Jira Issue',
        )

        self.assertEquals(
            'JIRA-0001 Jira Issue',
            str(issue),
        )


class TagTests(TestCase):
    """Tag model tests."""

    def test_str(self):

        tag = Tag(name='smoke')

        self.assertEquals(
            'smoke',
            str(tag),
        )


class SprintTests(TestCase):
    """Sprint model tests."""

    def test_str(self):

        sprint = Sprint(name='Sprint Theta')

        self.assertEquals(
            'Sprint Theta',
            str(sprint),
        )


class BrowserTests(TestCase):
    """Browser model tests."""

    def test_str(self):

        browser = Browser(
            name='Google Chrome',
            version='23.0.1',
        )

        self.assertEquals(
            'Google Chrome 23.0.1',
            str(browser)
        )


class EnvironmentTests(TestCase):
    """Environment model tests."""

    def test_str(self):

        env = Environment(
            name='CI',
            url='http://ci.example.com:8000/',
        )

        self.assertEquals(
            'CI http://ci.example.com:8000/',
            str(env),
        )


class HomePageViewTests(TestCase):
    """HomePageView view tests."""

    def setUp(self):
        self.client = Client()

    def test_login_required_redirect(self):
        """Verify login required requirement."""

        response = self.client.get('/', follow=True)

        self.assertEquals(
            [('http://testserver/content/testcases/', 301),
             ('http://testserver/accounts/login/?next=/content/testcases/', 302)],
            response.redirect_chain
        )
