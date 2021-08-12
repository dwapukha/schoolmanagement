from django.db import models

# Create your models here.
class Account(models.Model):
    account_name = models.CharField(max_length=100)
    ACCOUNT_TYPES =(
        ('Ex', 'Expenses'),
        ('St', 'Students'),
        ('Inc', 'Income'),
    )
    account_type = models.CharField(max_length=100,  choices= ACCOUNT_TYPES, default='Ex')
    Account_Number = models.IntegerField()
    Bank_Name = models.CharField(max_length=100)
    Branch = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.account_name},{self.Account_Number}, {self.Bank_Name}'

class transaction(models.Model):
    transactiontype = models.CharField(max_length=100)
    trans_Date = models.DateField()
    desc = models.TextField(max_length=270)

class ledger_entry(models.Model):
    transaction_id = models.IntegerField()
    accounts = models.ForeignKey(Account,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Legder Entries'