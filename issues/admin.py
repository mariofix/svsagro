from django.contrib import admin
from .models import Issue, IssueEntry


class IssueFilter(admin.ModelAdmin):
    model = Issue
    list_display = ["created_at", "customer", "machine", "status"]


class IssueEntryFilter(admin.ModelAdmin):
    model = IssueEntry
    list_display = ["created_at", "title", "issue"]


admin.site.register(Issue, IssueFilter)
admin.site.register(IssueEntry, IssueEntryFilter)
