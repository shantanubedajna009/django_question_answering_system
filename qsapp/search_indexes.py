import datetime
from haystack import indexes
from qsapp.models import Questions


# search index for the whoosh search engine
class QuestionsIndex(indexes.SearchIndex, indexes.Indexable):

    # text field for the Indexing
    # Indexing is needed for the whoosh SearchEngine
    text = indexes.CharField(document=True, use_template=True)

    # Adding Publication date from the model 
    # model_attr='pub_date' means 
    # referencing the model/tablefield
    pub_date = indexes.DateTimeField(model_attr='pub_date')    

    # the field i am searchsing against 
    # model_attr='question'  EdgeNgramField
    # means that TokeNize each Word
    # for matching against database
    content_auto = indexes.EdgeNgramField(model_attr="question")
    
    def get_model(self):

        # telling Which model/table 
        # we are referencing 
        # for the searching indexing
        return Questions    

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()