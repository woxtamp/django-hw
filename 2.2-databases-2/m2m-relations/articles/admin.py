from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        sign_main = 0
        for form in self.forms:
            if len(form.cleaned_data) == 0:
                continue

            if form.cleaned_data.get('is_main'):
                sign_main += 1

        if sign_main == 0:
            raise ValidationError('Укажите основной раздел')
        if sign_main > 1:
            raise ValidationError('Основным может быть только один раздел')

        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass