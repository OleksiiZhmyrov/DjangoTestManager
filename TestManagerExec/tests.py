from django import test
from TestManagerExec.models import ExecutionResult


class ExecutionResultTests(test.TestCase):
    """ExecutionResult model tests."""

    def test_str(self):

        execution_result = ExecutionResult(
            name='Passed',
            description='Passed with no errors')

        self.assertEquals(
            'Passed',
            str(execution_result),
        )