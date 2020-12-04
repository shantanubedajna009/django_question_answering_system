
from django.shortcuts import render
from qsapp.models import Answers, Questions
from haystack.query import SearchQuerySet, AutoQuery
from django.db.models import Q


"""
#View / Controller of the project

#Index View
Renderes the homepage with GET 
Request with **qsapp/home.html**
"""

def index(request):
    return render(request, "qsapp/home.html", context={})

"""
#Answer View
Take sthe POST request 
from the HomePage/Index

"""
def correct_answer(request):

    if request.method == "POST":

        """
        **co_if = False** signifies 
        if anything found with Haystack
        """

        co_if = False


        """

         Searches from the database With 
         Haystack API Which Connects 
         with Whoosh Engine

         """
        context_data = SearchQuerySet().autocomplete(content_auto=request.POST.get("question", ""))

        """
        **if len(context_data) == 0:** 
        means nothing found 
        in Haystack Search (unknown words)
        """
        
        if len(context_data) == 0:

            """
            Set **co_if = True** means 
            Haystack Search failed
            Do normal icontains /SQL LIKE 
            search with case insensitive
            """
            
            co_if = True
            """
            Split the words and search ad try match each word 
            """
            search = request.POST.get("question", "")
            
            search = search.split()
            """First Word"""
            db_query = Q(question__icontains=search[0])

            """ALl words with **OR** condition"""
            for term in search[1:]:
                db_query = db_query | Q(question__icontains=term)  

            context_data = Questions.objects.filter(db_query)

    else:
        """Empty context if **GET** REquest"""
        context_data = {}


    """
    Render different templates based 
    """
    """
    if **ONE** data found 
    **len(context_data) == 1**
    """
    """
    If **NO** data found 
    **len(context_data) == 0**
    """
    """
    If **Multiple** data found 
    **len(context_data) > 1**
    """
    if len(context_data) == 1:
        return render(request, "qsapp/answer.html", context={"questions": context_data, "is_empty": False, "co_if": co_if})




    elif  len(context_data) == 0:
        return render(request, "qsapp/answer.html", context={"questions": context_data, "is_empty": True, "co_if": co_if})



    elif len(context_data) > 1:
        return render(request, "qsapp/list_view.html", context={"questions": context_data, "co_if": co_if})


