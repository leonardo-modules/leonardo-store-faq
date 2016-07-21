from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = _("question")
        verbose_name_plural = _("questions")


class ProductQuestion(models.Model):
    question = models.ForeignKey(Question, related_name="product_questions")
    product = models.ForeignKey("catalogue.Product", related_name="questions")
    order = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = _("Product question")
        verbose_name_plural = _("Product questions")
