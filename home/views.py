from django.shortcuts import render
from .models import Category, PortfolioItem, ProductCategory, Product
from django.http import JsonResponse


def get_subcategories(request, category_id):
    try:
        print(f"Fetching subcategories for category ID: {category_id}")  # Debug print
        category = ProductCategory.objects.get(id=category_id)
        subcategories = category.subcategories.filter(is_active=True).order_by('order')
        print(f"Found {subcategories.count()} subcategories")  # Debug print
        
        data = [{
            'id': sub.id,
            'name': sub.name,
            'filter_class': sub.filter_class,
            'has_children': sub.subcategories.exists()
        } for sub in subcategories]
        print(f"Returning data: {data}")  # Debug print
        return JsonResponse({'subcategories': data})
    except ProductCategory.DoesNotExist:
        print(f"Category {category_id} not found")  # Debug print
        return JsonResponse({'error': f'Category {category_id} not found'}, status=404)
    except Exception as e:
        print(f"Error: {str(e)}")  # Debug print
        return JsonResponse({'error': str(e)}, status=500)

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
    # Get main categories (level 0)
    main_categories = ProductCategory.objects.filter(
        level=0,
        is_active=True
    ).order_by('order')
    
    print(f"Found {main_categories.count()} main categories")  # Debug print
    for cat in main_categories:
        print(f"Category: {cat.name} (ID: {cat.id})")  # Debug print

    # Get all active products
    products = Product.objects.filter(
        category__is_active=True
    ).select_related('category').order_by('category__order', 'order')
    
    context = {
        'main_categories': main_categories,
        'products': products,
        'debug': True,  # Enable debug output in template
    }
    return render(request, 'home/meats.html', context)

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

def vendor(request):
    return render(request, 'home/vendor.html')

def get_all_subcategories(request):
    # First get all level 1 categories (subcategories)
    subcategories = ProductCategory.objects.filter(
        level=1,  # Only get level 1 categories
        is_active=True
    ).select_related('parent').order_by('order')
    
    # Group subcategories by their parent (main category)
    grouped_data = {}
    
    for subcategory in subcategories:
        main_category = subcategory.parent
        
        if main_category and main_category.is_active:
            if main_category.id not in grouped_data:
                grouped_data[main_category.id] = {
                    'id': main_category.id,
                    'name': main_category.name,
                    'filter_class': main_category.filter_class,
                    'subcategories': []
                }
            
            # Check for level 2 subcategories
            has_children = ProductCategory.objects.filter(
                parent=subcategory,
                level=2,
                is_active=True
            ).exists()
            
            subcat_data = {
                'id': subcategory.id,
                'name': subcategory.name,
                'filter_class': subcategory.filter_class,
                'has_children': has_children
            }
            grouped_data[main_category.id]['subcategories'].append(subcat_data)
    
    # Convert the grouped data to a list
    categories_data = list(grouped_data.values())
    
    print("Returning categories data:", categories_data)  # Debug print
    return JsonResponse({'categories': categories_data})