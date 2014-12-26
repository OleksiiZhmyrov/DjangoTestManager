from TestManagerContent.models import TestCase, OrderTestStep
from TestManagerCore.logger import LOGGER
import ezodf


class OpenDocumentSpreadsheet:
    _doctype = "ods"

    def __init__(self):
        self.document = None

    def create(self, test_case_pk):
        test_case = None
        test_steps = None
        try:
            test_case = TestCase.objects.get(
                pk=test_case_pk,
            )
            test_steps = OrderTestStep.objects.filter(
                test_case=test_case,
            ).order_by('number')
        except TestCase.DoesNotExist:
            LOGGER.error(
                'TestCase with pk={pk} does not exist. Setting None value.'.format(
                    pk=test_case_pk,
                )
            )
        except OrderTestStep.DoesNotExist:
            LOGGER.error(
                'OrderTestStep for TestCase with pk={pk} does not exist. Setting None value.'.format(
                    pk=test_case_pk,
                    )
            )
        self.document = ezodf.newdoc(doctype=self._doctype)
        sheets = self.document.sheets
        sheets += ezodf.Table(test_case.name)
        sheet = sheets[test_case.name]

        sheet[0, 0].set_value(test_case.name)

        if test_steps:
            for test_step in test_steps:
                sheet.append_rows(1)
                sheet[test_step.number, 0].set_value(test_step.number)
                sheet[test_step.number, 1].set_value(test_step.test_step.name)
                sheet[test_step.number, 2].set_value(test_step.test_step.description)
                sheet[test_step.number, 3].set_value(test_step.test_step.expected_result)
