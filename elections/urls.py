from django.urls import path

from . import views

urlpatterns=[
    path("", views.home, name="home"),
    path("addcandidate", views.addcandidate, name="addcandidate"),
    path("candidates" , views.all_candidates  , name = "candidates"),
    path("vote1/<int:candidate_id>" , views.vote1 , name = "vote1"),
    path("vote2/<int:candidate_id>" , views.vote2 , name = "vote2"),
    path("vote3/<int:candidate_id>" , views.vote3 , name = "vote3"),
    path("candidate/<int:candidate_id>", views.show_candidate, name="show_candidate"),
    path("update/<int:candidate_id>", views.update, name="update"),
    path("result" , views.result , name="result"),

]