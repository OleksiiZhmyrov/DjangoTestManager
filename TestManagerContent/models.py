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


class TestStep(models.Model):

    author = models.ForeignKey("auth.User")

    creation_date = models.DateTimeField(
        "Creation date",
        auto_now_add=True,
    )

    modification_date = models.DateTimeField(
        "Modification date",
        auto_now=True,
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
        "Expected result",
        max_length=2048,
    )

    screenshot = models.ForeignKey(
        "TestManagerCore.Screenshot",
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

    modification_date = models.DateTimeField(
        "Modification date",
        auto_now=True,
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

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = "Test Case"
        verbose_name_plural = "Test Cases"


class TestSuite(models.Model):

    author = models.ForeignKey("auth.User")

    disabled = models.BooleanField(
        "Disabled",
        default=False,
    )

    creation_date = models.DateTimeField(
        "Creation date",
        auto_now_add=True,
    )

    modification_date = models.DateTimeField(
        "Modification date",
        auto_now=True,
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


class OrderTestStep(models.Model):
    number = models.PositiveIntegerField()
    test_case = models.ForeignKey(TestCase)
    test_step = models.ForeignKey(TestStep)

    class Meta:
        unique_together = (("number", "test_case"), ("test_case", "test_step"))


class OrderTestCase(models.Model):
    number = models.PositiveIntegerField()
    test_suite = models.ForeignKey(TestSuite)
    test_case = models.ForeignKey(TestCase)

    class Meta:
        unique_together = (("number", "test_suite"), ("test_suite", "test_case"))
