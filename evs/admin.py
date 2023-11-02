from django.contrib import admin
from .models import Election, Candidate , BlockchainCode

class BlockchainCodeAdmin(admin.ModelAdmin):
    readonly_fields = [field.name for field in BlockchainCode._meta.fields]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields
        return []

admin.site.register(BlockchainCode, BlockchainCodeAdmin)
admin.site.register(Election)
admin.site.register(Candidate)