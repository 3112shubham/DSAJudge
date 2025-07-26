from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_user, name='logout'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('add_question/', views.add_question, name='add_question'),
    path('questions/', views.view_questions, name='view_questions'),
    path('delete_question/<int:id>/', views.delete_question, name='delete_question'),
    path('add_contest/', views.add_contest, name='add_contest'),
    path('view_contests/', views.view_contests, name='view_contests'),
    path('student/contests/', views.student_view_contests, name='student_contests'),
    path('student/contest/<int:contest_id>/', views.student_view_contest_detail, name='contest_detail'),
    path('dashboard/contest/<int:contest_id>/remove-question/<int:cq_id>/', views.remove_question_from_contest, name='remove_question_from_contest'),
    path('dashboard/contest/<int:contest_id>/add-questions/', views.add_questions_to_contest, name='add_questions_to_contest'),
    path('dashboard/contest/<int:contest_id>/delete/', views.delete_contest, name='delete_contest'),
    path('dashboard/contest/<int:contest_id>/', views.admin_contest_detail, name='admin_contest_detail'),
    path('update_participation/', views.update_participation, name='update_participation'),
    path('profile/<str:username>/', views.student_profile, name='student_profile'),
    path('update_leetcode_score/', views.update_leetcode_score, name='update_leetcode_score'),
    path('update-social-links/', views.update_social_links, name='update_social_links'),
    path('admin_leaderboard/', views.admin_leaderboard, name='admin_leaderboard'),
    path('student_leaderboard/', views.student_leaderboard, name='student_leaderboard'),
    path('admin_leaderboard/download_excel/', views.download_leaderboard_excel, name='download_leaderboard_excel'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)