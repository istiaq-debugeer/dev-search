from django.urls import path
from users.views import profiles,UserProfile,Login,Logout,registerUser,userAccount,editAccount,createSkill,UpdateSkill,deleteskill
urlpatterns=[
    path('',profiles,name='profile'),
    path('user-profile/<str:pk>/',UserProfile,name='userprofile'),
    path('register/', registerUser, name='register'),
    path('create-skill/',createSkill,name='create-skill'),
    path('delete-skill/<str:pk>/',deleteskill,name='delete-skill'),
    path('edit-skill/<str:pk>/',UpdateSkill , name='edit-skill'),
    path('login/',Login.as_view(),name='login'),
    path('logout/',Logout,name='logout'),
    path('account/',userAccount,name='account'),
    path('edit-account/', editAccount, name='edit-account')
]