from django.contrib import admin
from .models import Election, Candidate , VoteBlocks

class VoteBlocksAdmin(admin.ModelAdmin):
    readonly_fields = [field.name for field in VoteBlocks._meta.fields]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields
        return []

admin.site.register(VoteBlocks, VoteBlocksAdmin)
admin.site.register(Election)
admin.site.register(Candidate)