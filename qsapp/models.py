from django.db import models
import uuid


# answeres table
class Answers(models.Model):

    # Primary key, auto generated
    recID = models.AutoField(primary_key=True)
    
    # varchar Field max lenth 255
    # blank is allowed
    answer = models.CharField(max_length=255, blank=True)
    
    # atag Unique key with UUID as unique field
    # UUID field is used here
    # unique constraint is True
    # not a editable field
    atag = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    
    # normal TEXT field with blank allowed
    comment = models.TextField(blank=True)

    # auto generated publishing date field
    # generated according to UTC
    pub_date = models.DateTimeField(auto_now_add=True)
    
    # return Answer String 
    # when referenced by default
    def __str__(self):
        return self.answer

#questions table
class Questions(models.Model):

    # Primary key, auto generated
    recID = models.AutoField(primary_key=True)
    
    # varchar Field max lenth 255
    # blank is allowed
    question = models.CharField(max_length=255, blank=True)

    # using the UUIDFIELD from the Answers table 
    # as foreignkey , when a row is deleted
    # cascade (delete corresponding rows in 
    # Answers table too, if all 
    # reference to that answer is deleted)
    atag = models.ForeignKey(Answers, to_field="atag", db_column="atag", on_delete=models.CASCADE)
    
    # auto generated publishing date field
    # generated according to UTC
    pub_date = models.DateTimeField(auto_now_add=True)

    # return Question String 
    # when referenced by default
    def __str__(self):
        return self.question

