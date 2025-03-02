from django.shortcuts import render
from .models import Category, PortfolioItem
from django.http import JsonResponse


def get_subcategories(request, category_id):
    try:
        main_category = Category.objects.get(id=category_id)
        # Assuming `subcategories` is the related name for subcategories in your model
        subcategories = main_category.subcategories.all()
        data = [{'id': sub.id, 'name': sub.name} for sub in subcategories]
        return JsonResponse({'subcategories': data})
    except Category.DoesNotExist:
        return JsonResponse({'subcategories': []})

def portfolio(request):
    # Fetch all categories and portfolio items
    categories = Category.objects.all()
    portfolio_items = PortfolioItem.objects.all()

    context = {
        'categories': categories,
        'portfolio_items': portfolio_items,
    }
    return render(request, 'portfolio.html', context)

def get_portfolio_items(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    portfolio_items = PortfolioItem.objects.filter(category=category)
    
    items_data = [
        {
            'title': item.title,
            'description': item.description,
            'image': item.image.url,
            'link': item.link,
        }
        for item in portfolio_items
    ]
    return JsonResponse({'items': items_data})

def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/whoweare.html') 

def heritage(request):
    return render(request, 'home/heritage.html')

def team(request):
    return render(request, 'home/team.html')

def corporate_governance(request):
    return render(request, 'home/corporate_governance.html')

def vision_mission_values(request):
    return render(request, 'home/vision_mission_values.html')

# Media Pages
def photos_videos(request):
    return render(request, 'home/photos_videos.html')

def news_insights(request):
    return render(request, 'home/news_insights.html')

# Commitments Pages
def sustainability(request):
    return render(request, 'home/sustainability.html')

def saudi_vision(request):
    return render(request, 'home/saudi_vision.html')

# Products Pages
def meats(request):
    return render(request, 'home/meats.html', )

def dairy(request):
    return render(request, 'home/dairy.html', )

def vegitablefruits(request):
    return render(request, 'home/vegitable-fruits.html', )

def oils(request):
    return render(request, 'home/oils.html', )

def others(request):
    return render(request, 'home/others.html', )

# Contact Us Pages
def sales(request):
    return render(request, 'home/sales.html')

def contact_info(request):
    return render(request, 'home/contact_info.html')

def products_filter(request):
    return render(request, 'home/products_filter.html')

def careers(request):
    return render(request, 'home/careers.html')


def job_list(request):
    # jobs = Job.objects.all()  # Fetch all jobs, apply filters if necessary
    return render(request, 'home/jobs.html')

def job_details(request):
    return render(request, 'home/job_details.html')

# Branches
def branches(request):
    return render(request, 'home/branches.html')