from django.contrib import admin
from django.urls import path

from fisher_man.views.user_view import SigninView, SignupView, ChangePasswordView, EditProfileView
from fisher_man.views.border_view import CreateEditBorderView, BorderActiveUpdateView, BorderListView
from fisher_man.views.border_crossed_logs_view import CreateBorderCrossedLogView, BorderCrossedLogsListView
from fisher_man.views.fish_potentials_view import FishPotentialCreateUpdateView, FishPotentialsListView, DeleteFishPotentials
from fisher_man.views.emergency_requests_view import EmergencyRequestCreateView, EmergencyRequestListView
from fisher_man.views.dashboard_counts_view import DashboardCountView, UserDashboardCountView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/signup/', SignupView.as_view(), name='signup'),
    path('api/signin/', SigninView.as_view(), name='signin'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/edit-profile/<int:user_id>/', EditProfileView.as_view(), name='edit-profile'),
    path('api/border-create/', CreateEditBorderView.as_view(), name='border-create'),
    path('api/update-active/<int:border_id>/', BorderActiveUpdateView.as_view(), name='update-active'),
    path('api/get-borders/', BorderListView.as_view(), name='get-borders'),
    path('api/create-border-crossed-logs/', CreateBorderCrossedLogView.as_view(), name='create-border-crossed-logs'),
    path('api/get-border-crossed-logs/', BorderCrossedLogsListView.as_view(), name='get-border-crossed-logs'), #for get by user_id http://127.0.0.1:8000/api/get-border-crossed-logs?user_id=1
    path('api/create-fish-potentials/', FishPotentialCreateUpdateView.as_view(), name='create-fish-potentials'),
    path('api/get-fish-potentials/', FishPotentialsListView.as_view(), name='get-fish-potentials'),
    path('api/delete-fish-potential/', DeleteFishPotentials.as_view(), name='delete_fish_potential'),
    path('api/create-emergency-request/', EmergencyRequestCreateView.as_view(), name='create-emergency-request'),
    path('api/get-emergency-request/', EmergencyRequestListView.as_view(), name='get-emergency-request'),
    path('api/dashboard-count/', DashboardCountView.as_view(), name='dashboard-count'),
    path('api/user-dashboard-count/', UserDashboardCountView.as_view(), name='user-dashboard-count'),
]
