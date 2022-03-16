from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    
# class BookCast(models.Model):
#     user_id = models.IntegerField()
# #   cast_id: Int # PK
#     book_id = models.CharField(max_length=255) ## link to google-books-api
#     book_name = models.CharField(max_length=255)
#     book_image_url = models.CharField(max_length=255)
#     description = models.TextField()

# class Character(models.Model):
#     cast_id = models.IntegerField()
#     character_id = models.IntegerField()
#     name = models.CharField(max_length=255)
#     actor = models.CharField(max_length=255)
#     description = models.TextField()
#     photo_url = models.CharField(max_length=255)
    
# class BookCast_Like(models.Model):
#     user_id = models.IntegerField()
#     cast_id = models.IntegerField()
#     like = models.BooleanField()
#     comment = models.TextField()

# class Character_Like(models.Model):
#     user_id = models.IntegerField()
#     character_id = models.IntegerField()
#     like = models.BooleanField()
#     comment = models.TextField()
    
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