from django.urls import path, include
from job_seeker import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.JobListView.as_view(), name='jobs'),
    path('profile/', views.profile, name='emp_view_profile'),

    path('profile/exams/', views.ViewExams.as_view(), name='viewExam'),
    path('profile/exams/<int:pk>/', views.ExamAttendView.as_view(), name='attendExam'),
    path('profile/exams/<int:pk>/sendresult/', views.SendExamResult.as_view(), name='sendResult'),

    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('edit/profile/', views.edit_profile, name='edit_profile'),
    path('edit/profile/update/', views.edit_employee, name='edit_emp_data'),
    path('search/',views.SearchResultsView, name='search_results'),
]