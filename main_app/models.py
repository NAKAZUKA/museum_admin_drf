from django.db import models


class Question(models.Model):
    """Model definition for Question."""

    question_text = models.CharField(max_length=200, verbose_name='Вопрос')
    answer = models.ForeignKey('Answer', on_delete=models.CASCADE, verbose_name='Ответ(ы)')

    class Meta:
        """Meta definition for Question."""

        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        """Unicode representation of Question."""
        return self.question_text


class Answer(models.Model):
    """Model definition for Answer."""

    answer_text = models.CharField(max_length=200, verbose_name='Ответ')

    class Meta:
        """Meta definition for Answer."""

        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        """Unicode representation of Answer."""
        return self.answer_text


class Post(models.Model):
    """Model definition for Post."""

    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    img = models.CharField(max_length=200, verbose_name='Картинка', blank=True, null=True)

    class Meta:
        """Meta definition for Post."""

        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        """Unicode representation of Post."""
        return self.title


class Exhibit(models.Model):
    """Model definition for Exhibit."""

    title = models.CharField(max_length=200, verbose_name='Экспонат')
    text = models.TextField(verbose_name='Описание')
    added = models.DateTimeField(verbose_name='Добавлен')
    img = models.CharField(max_length=200, verbose_name='Картинка', blank=True, null=True)

    class Meta:
        """Meta definition for Exhibit."""

        verbose_name = 'Экспонат'
        verbose_name_plural = 'Экспонаты'

    def __str__(self):
        """Unicode representation of Exhibit."""
        return self.title
    