from django.db import models
from django.utils.translation import ugettext_lazy as _
import jsonfield

class SampleCount(models.Model):
  num = models.IntegerField(default = 0)

class TaskHistory(models.Model):
    # Relations
    # Attributes - mandatory
    name = models.CharField(
        max_length=100,
        verbose_name=_("Task name"),
        help_text=_("Select a task to record"),
        )
    # Attributes - optional
    history = jsonfield.JSONField(
        default={},
        verbose_name=_("history"),
        help_text=_("JSON containing the tasks history")
        )
    # Manager
    # Functions

    # Meta & unicode
    class Meta:
        verbose_name = _('Task History')
        verbose_name_plural = _('Task Histories')

    def __unicode__(self):
        return _("Task History of Task: %s") % self.name