from django.db import models
from django.contrib.auth.models import User, Group


# Model Messages to User
class Message(models.Model):
    name = models.CharField(max_length=50)
    message = models.TextField()

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return self.name


# Model Main Process
class Process(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    owner_group = models.ForeignKey(
                                    Group, related_name="owner_group",
                                    on_delete=None
                                    )

    class Meta:
        verbose_name = 'Process'
        verbose_name = 'Processes'

    def __str__(self):
        return "Process Name %s" % (self.name)


# Model Action
class Action(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    approver = models.ForeignKey(
                                User,
                                related_name="action_approver",
                                on_delete=None
                                )
    responsible = models.ForeignKey(
                                User,
                                related_name="action_responsible",
                                on_delete=None
                                )

    class Meta:
        verbose_name = 'Action'
        verbose_name_plural = 'Actions'

    def __str__(self):
        return "Action name %s, ID: %s" % (self.name, self.id)


# Process Pipe
class ProcessWay(models.Model):
    process = models.ForeignKey(
                                Process,
                                related_name="pw_process",
                                on_delete=None
                                )
    action = models.ForeignKey(
                                Action,
                                related_name="pw_action",
                                on_delete=None
                                )
    sequential = models.IntegerField(default=0)

    class Meta:
        ordering = ["sequential"]
        verbose_name = 'ProcessWay'
        verbose_name_plural = 'ProcessWays'

    def __str__(self):
        return self.id


# Tickets opened by users
class Ticket(models.Model):
    process = models.ForeignKey(
                                Process,
                                related_name="tickets",
                                on_delete=None
                                )
    owner = models.ForeignKey(
                                User,
                                related_name="ticket_owner",
                                on_delete=None)
    process_way = models.ForeignKey(
                                    ProcessWay,
                                    related_name="ticket_pw",
                                    on_delete=None
                                    )
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'

    def __str__(self):
        return self.id


# Model Abstract to Log
class LogAbstract(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, related_name="%(class)s", on_delete=None)

    class Meta:
        verbose_name = 'Log Abstract'
        verbose_name_plural = 'Logs Abstracts'
        abstract = True

    def __str__(self):
        return self.id
