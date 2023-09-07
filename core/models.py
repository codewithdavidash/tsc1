from django.db import models


class HTML_CSS(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255, null=True, blank=True)
    video = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'HTML_CSS'
        verbose_name = 'HTML_CSS'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title


class JavaScript(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255, null=True, blank=True)
    video = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'JavaScript'
        verbose_name = 'JavaScript'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title


class Python(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255, null=True, blank=True)
    video = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Python'
        verbose_name = 'Python'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

