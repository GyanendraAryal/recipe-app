from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(_("Phone Number"), blank=True, region="NP")
    profile_image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Recipe(models.Model):
    DIFICULTY_CHOICE = [("EA", "Easy"), ("MD", "Medium"), ("HD", "Hard")]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    ingrediants = models.TextField()
    cooking_duration = models.DurationField()
    dificulty = models.CharField(max_length=2, choices=DIFICULTY_CHOICE, default="EA")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    like_user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["like_user", "recipe"], name = "unique_user_recipe_like",)
        ]


class Comment(models.Model):
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=~models.Q(follower = models.F("following")),
                name = "prevent_self_follow",
            ),
            models.UniqueConstraint(
                fields=["follower","following"],
                name = "unique_follow"
            ),
        ]
