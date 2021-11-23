from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

CRY = "Crypto"
ADS = "Adesso nel mondo"
ECO = "Economia"
TEC = "Tecnologia"

ARGS_CHOICES = (
    (CRY,"Crypto"),
    (ADS,"Adesso nel mondo"),
    (ECO, "Economia"),
    (TEC, "Tecnologia"),
)


class PostModel(models.Model):
    autore = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    titolo = models.CharField(max_length=70)
    contenuto = models.TextField()
    data_creazione = models.DateTimeField(auto_now_add=True)
    argomento = models.CharField(max_length=70,choices = ARGS_CHOICES )

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        return reverse("crea_post")


class Comment(models.Model):
    post = models.ForeignKey(PostModel,on_delete=models.CASCADE, related_name="comments")
    user  = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    contenuto_commento = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ("data",)

    def __str__(self):
        return self.post.__str__()