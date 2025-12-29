from django.contrib import admin
from .models import Group, GroupMember, GroupSettings

class GroupMemberInline(admin.TabularInline):
    model = GroupMember
    extra = 1

class GroupSettingsInline(admin.StackedInline):
    model = GroupSettings

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at')
    inlines = [GroupSettingsInline, GroupMemberInline]

@admin.register(GroupMember)
class GroupMemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'group', 'role', 'status', 'join_date')
    list_filter = ('group', 'role', 'status')
