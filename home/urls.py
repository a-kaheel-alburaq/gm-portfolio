from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('about/heritage/', views.heritage, name='heritage'),
    path('about/team/', views.team, name='team'),
    path('about/corporate-governance/', views.corporate_governance, name='corporate-governance'),
    path('about/vision-mission-values/', views.vision_mission_values, name='vision-mission-values'),

    # Media Pages
    path('media/photos-videos/', views.photos_videos, name='photos-videos'),
    path('media/news-insights/', views.news_insights, name='news-insights'),

    # Commitments Pages
    path('commitments/sustainability/', views.sustainability, name='sustainability'),
    path('commitments/saudi-vision/', views.saudi_vision, name='saudi-vision'),

    # Products Pages
    path('meats/', views.meats, name='meats'),
    path('dairy/', views.dairy, name='dairy'),
    path('vegitable-fruits/', views.vegitablefruits, name='vegitable-fruits'),
    path('oils/', views.oils, name='oils'),
    path('others/', views.others, name='others'),

    # path('portfolio/', views.portfolio, name='portfolio'),
    # path('get_portfolio_items/<slug:category_slug>/', views.get_portfolio_items, name='get_portfolio_items'),
    # path('get_subcategories/<int:category_id>/', views.get_subcategories, name='get_subcategories'),
    # path('products_/', views.products, name='products_all'),
    
    # Contact Us Dropdown Pages
    path('contact-us/sales/', views.sales, name='sales'),
    path('contact-us/info/', views.contact_info, name='contact-info'),
    path('products/filter/', views.products_filter, name='products_filter'),

    # Careers
    path('careers/', views.careers, name='careers'),
    path('jobs/', views.job_list, name='job_list'),
    path('job-details/', views.job_details, name='job_details'),
    
    # Branches
    path('branches/', views.branches, name='branches'),
]
