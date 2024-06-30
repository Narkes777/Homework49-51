from django.urls import path
from . import views


urlpatterns = [
    path('anns/by_category/<int:sub_pk>/', views.Ann.as_view(), name = 'ann_list'),
    path('ann/<int:pk>/', views.AnnDetail.as_view(), name='ann_detail'),
    path('ann/create/', views.AnnCreate.as_view(), name='ann_create'),
    path('ann/<int:pk>/update/', views.AnnUpdate.as_view(), name='ann_update'),
    path('ann/<int:pk>/delete/', views.AnnDelete.as_view(), name='ann_delete'),


    path('subcats/by_category/<int:cat_pk>/', views.SubCategoryList.as_view(), name ='subcat_list'),
    path('subcat/<int:pk>/', views.SubCategoryDetail.as_view(), name='subcat_detail'),
    path('subcat/create/', views.SubCategoryCreate.as_view(), name='subcat_create'),
    path('subcat/<int:pk>/update/', views.SubCategoryUpdate.as_view(), name='subcat_update'),
    path('subcat/<int:pk>/delete/', views.SubCategoryDelete.as_view(), name='subcat_delete'),


    path('cats/', views.CategoryList.as_view(), name='cat_list'),
    path('cat/<int:pk>/', views.CategoryDetail.as_view(), name='cat_detail'),
    path('cat/create/', views.CategoryCreate.as_view(), name='cat_create'),
    path('cat/<int:pk>/update/', views.CategoryUpdate.as_view(), name='cat_update'),
    path('cat/<int:pk/delete/', views.CategoryDelete.as_view(), name='cat_delete'),


    path('main/', views.Main.as_view(), name='main_page')
]