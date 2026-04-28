from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        mains = [form for form in self.forms 
                if form.cleaned_data and form.cleaned_data.get('is_main')]
        if len(mains) != 1:
            raise ValidationError('Нужно ровно ОДИН основной раздел!')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    fields = ('tag', 'is_main')
    extra = 1


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'main_tag')
    list_editable = ('published_at',)
    inlines = [ScopeInline]
    save_on_top = True

    def main_tag(self, obj):
        try:
            return obj.scopes.filter(is_main=True).first().tag.name
        except:
            return "-"
    main_tag.short_description = 'Основная тема'