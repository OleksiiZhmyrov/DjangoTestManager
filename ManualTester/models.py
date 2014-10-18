from django.db import models


class TestStepStatus(models.Model):

    name = models.CharField(
        "Name",
        max_length=64,
    )

    description = models.CharField(
        "Description",
        max_length=256,
    )

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = "Test Step Status"
        verbose_name_plural = "Test Step Statuses"


class TestCaseStatus(models.Model):

    name = models.CharField(
        "Name",
        max_length=64,
    )

    description = models.CharField(
        "Description",
        max_length=256,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = "Test Case Status"
        verbose_name_plural = "Test Case Statuses"


class ExecutionResult(models.Model):

    name = models.CharField(
        "Name",
        max_length=64,
    )

    description = models.CharField(
        "Description",
        max_length=256,
    )

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = "Execution Result"
        verbose_name_plural = "Execution Results"


class TestStep(models.Model):

    author = models.ForeignKey("auth.User")

    creation_date = models.DateTimeField(
        "Creation date",
        auto_now_add=True,
    )

    name = models.CharField(
        "Name",
        max_length=256,
    )

    description = models.CharField(
        "Description",
        null=True,
        blank=True,
        max_length=1024,
    )

    expected_result = models.CharField(
        "Expected outcome",
        max_length=2048,
    )

    screenshot = models.FileField(
        "Screenshot",
        blank=True,
        null=True,
    )

    tags = models.ManyToManyField(
        "TestManagerCore.Tag",
        verbose_name="Related tags",
        blank=True,
        null=True,
    )

    status = models.ForeignKey(TestStepStatus)

    def __str__(self):
        return self.name

    class Meta:

        ordering = ('name',)
        verbose_name = "Test Step"
        verbose_name_plural = "Test Steps"


class TestCase(models.Model):

    author = models.ForeignKey("auth.User")

    creation_date = models.DateTimeField(
        "Creation date",
        auto_now_add=True,
    )

    name = models.CharField(
        "Name",
        max_length=256,
    )

    description = models.CharField(
        "Description",
        null=True,
        blank=True,
        max_length=1024,
    )

    status = models.ForeignKey(TestCaseStatus)

    linked_issues = models.ManyToManyField(
        "TestManagerCore.JiraIssue",
        verbose_name="Related Jira Issues",
        blank=True,
        null=True,
    )

    tags = models.ManyToManyField(
        "TestManagerCore.Tag",
        verbose_name="Related tags",
        blank=True,
        null=True,
    )

    test_steps = models.ManyToManyField(
        "ManualTester.TestStep",
        verbose_name="Related Test Steps",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = "Test Case"
        verbose_name_plural = "Test Cases"


class TestSuite(models.Model):

    author = models.ForeignKey("auth.User")

    creation_date = models.DateTimeField(
        "Creation date",
        auto_now_add=True,
    )

    name = models.CharField(
        "Name",
        max_length=256,
    )

    description = models.CharField(
        "Description",
        null=True,
        blank=True,
        max_length=1024,
    )

    tags = models.ManyToManyField(
        "TestManagerCore.Tag",
        verbose_name="Related tags",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Test Suite"
        verbose_name_plural = "Test Suites"


class TestStepResult(models.Model):

    exec_result = models.ForeignKey(
        ExecutionResult,
        blank=True,
        null=True,
    )

    tester = models.ForeignKey("auth.User")

    creation_date = models.DateTimeField(
        "Creation date",
        auto_now_add=True,
    )

    step = models.ForeignKey(TestStep)

    linked_issues = models.ManyToManyField(
        "TestManagerCore.JiraIssue",
        verbose_name="Related Jira Issues",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Test Step Result"
        verbose_name_plural = "Test Step Results"


class TestCaseResult(models.Model):

    exec_result = models.ForeignKey(
        ExecutionResult,
        blank=True,
        null=True,
    )

    tester = models.ForeignKey("auth.User")

    creation_date = models.DateTimeField(
        "Creation date",
        auto_now_add=True,
    )

    test_case = models.ForeignKey(TestCase)

    steps_results = models.ManyToManyField(
        TestStepResult,
        verbose_name="Results of related test steps",
    )

    environment = models.CharField(
        "Environment",
        blank=True,
        null=True,
        max_length=512,
    )

    sprint = models.ForeignKey(
        "TestManagerCore.Sprint",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Test Case Result"
        verbose_name_plural = "Test Case Results"


class OrderTestStep(models.Model):
    number = models.PositiveIntegerField()
    test_case = models.ForeignKey(TestCase)
    test_step = models.ForeignKey(TestStep)

    class Meta:
        unique_together = (("number", "test_case"),)


class OrderTestCase(models.Model):
    number = models.PositiveIntegerField()
    test_suite = models.ForeignKey(TestSuite)
    test_case = models.ForeignKey(TestCase)

    class Meta:
        unique_together = (("number", "test_suite"),)
