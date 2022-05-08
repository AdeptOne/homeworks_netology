from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, TagSection, Tag


class TagSectionInlineFormset(BaseInlineFormSet):
    def clean(self):
        count_main_tag = [form.cleaned_data['is_main'] for form in self.forms].count(True)

        if count_main_tag == 1:
            return super().clean()
        elif count_main_tag > 1:
            raise ValidationError('Основным может быть только один раздел')
        else:
            raise ValidationError('Укажите основной раздел')


class TagSectionInline(admin.TabularInline):
    model = TagSection
    formset = TagSectionInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagSectionInline, ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
