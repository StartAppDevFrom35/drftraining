import uuid
from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # auto_now : 何らかのDBへの保存操作時に常に操作時点のタイムスタンプ
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    # auto_now_add : 初回DB登録時に、登録時のタイムスタンプを設定
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)


class MIncomeCategory(BaseModel):
    name = models.CharField(max_length=10, unique=True)


class TIncome(BaseModel):
    amount = models.BigIntegerField()
    m_income_category = models.ForeignKey(MIncomeCategory,
                                          on_delete=models.CASCADE, related_name='t_incomes')
