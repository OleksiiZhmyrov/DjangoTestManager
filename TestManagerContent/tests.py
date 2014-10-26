from django.contrib.auth.models import User
from django import test
from TestManagerContent.models import TestStepStatus, TestCaseStatus, TestStep, TestCase, TestSuite


class TestStepStatusTests(test.TestCase):
    """TestStepStatus model tests."""

    def test_str(self):

        test_step_status = TestStepStatus(
            name='Verified',
            description='Test step has been verified')

        self.assertEquals(
            'Verified',
            str(test_step_status),
        )


class TestCaseStatusTests(test.TestCase):
    """TestCaseStatus model tests."""

    def test_str(self):

        test_case_status = TestCaseStatus(
            name='Approved',
            description='Test case has been approved')

        self.assertEquals(
            'Approved',
            str(test_case_status),
        )


class TestStepTests(test.TestCase):
    """TestStep model tests."""

    def test_str(self):

        test_step = TestStep(
            author=User(username='adele'),
            name='Navigate to homepage',
            expected_result='User is navigated to homepage',
            status=TestStepStatus(name='Failed'),
        )

        self.assertEquals(
            'Navigate to homepage',
            str(test_step),
        )


class TestCaseTests(test.TestCase):
    """TestCase model tests."""

    def test_str(self):

        test_case = TestCase(
            author=User(
                username='adele',
            ),
            name='Verify basic login functionality',
            status=TestCaseStatus(
                name='Valid',
            ),
        )

        self.assertEquals(
            'Verify basic login functionality',
            str(test_case),
        )


class TestSuiteTests(test.TestCase):
    """TestSuite model tests."""

    def test_str(self):

        test_suite = TestSuite(
            author=User(
                username='adele',
            ),
            name='Login and Registration',
        )

        self.assertEquals(
            'Login and Registration',
            str(test_suite),
        )
