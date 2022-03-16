from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    
class Casting(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
#    book_id = models.CharField(max_length=255) ## link to google-books-api
    book_name = models.CharField(max_length=255)
    book_image_url = models.CharField(max_length=255)
    description = models.TextField()

class Character(models.Model):
    casting = models.ForeignKey(Casting, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    actor = models.CharField(max_length=255)
    description = models.TextField()
    photo_url = models.CharField(max_length=255, null=True)
    
class Casting_Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    casting = models.ForeignKey(Casting, on_delete=models.CASCADE)
    like = models.NullBooleanField(null=True)
    comment = models.TextField(null=True)

class Character_Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    like = models.BooleanField(null=True)
    comment = models.TextField(null=True)
    
    # sample of data with full joins, GraphQL-style
    
    # user {
    #     username
    #     email
    #     bookCasts {
    #         user_id
    #         book_id
    #         likes {
    #             user_id
    #             cast_id
    #             like
    #             comment
    #         }
    #         book_name
    #         book_image_url
    #         description
    #         characters {
    #             cast_id
    #             character_id
    #             name
    #             actor
    #             description
    #             photo_url
    #             likes {
    #                 user_id
    #                 character_id
    #                 like
    #                 comment
    #             }
    #         }
            
    #     }
    # }