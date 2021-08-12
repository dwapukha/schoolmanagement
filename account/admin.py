from django.contrib import admin
from account.models import Account, transaction, ledger_entry

# Register your models here.
@admin.register(Account)
class AdminAccount(admin.ModelAdmin):
    pass

@admin.register(transaction)
class Admintransaction(admin.ModelAdmin):
    pass

@admin.register(ledger_entry)
class Adminledger_entry(admin.ModelAdmin):
    pass