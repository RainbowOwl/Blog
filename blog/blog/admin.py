from django.contrib import admin
from django.utils.html import format_html


class PorfolioModelAdmin(admin.ModelAdmin):

    def edit_link(self, obj):
        return format_html('<span>Edit</span>')

    edit_link.short_description = ''


class PortfolioAdminSite(admin.AdminSite):
    site_header = 'Portfolio'


portfolio_admin_site = PortfolioAdminSite()