from django.contrib import admin
from .models import Issue, IssueEntry
from markdownx.admin import MarkdownxModelAdmin


class InlineEntries(admin.TabularInline):
    model = IssueEntry
    extra = 0
    can_delete = False
    readonly_fields = ["created_at", "title", "description"]
    show_change_link = True


class IssueFilter(MarkdownxModelAdmin):
    model = Issue
    inlines = [InlineEntries]
    list_display = ["created_at", "customer", "machine", "status"]
    list_editable = ["status"]
    list_filter = ["status", "customer", "machine"]
    search_fields = ["title", "description", "contact"]


class IssueEntryFilter(MarkdownxModelAdmin):
    model = IssueEntry
    list_display = ["created_at", "title", "issue"]
    list_display_links = ["created_at", "title"]
    list_filter = ["issue"]
    search_fields = ["title", "description"]


admin.site.register(Issue, IssueFilter)
admin.site.register(IssueEntry, IssueEntryFilter)
