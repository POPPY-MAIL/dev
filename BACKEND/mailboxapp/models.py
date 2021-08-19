from django.db import models
from dev.BACKEND.accountapp.models import AppUser


class MailBox(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column="mailbox_id")
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name="mailboxes")
    nickname = models.CharField(max_length=20)
    link_title = models.CharField(max_length=40)
    mailbox_link = models.URLField()  # default max_length = 200
    open_date = models.DateTimeField()

    ThemeType = models.TextChoices('ThemeType', 'RED YELLOW ORANGE')  # 수정 - value 값 변경해야 함
    theme = models.CharField(max_length=20, choices=ThemeType.choices)

    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
