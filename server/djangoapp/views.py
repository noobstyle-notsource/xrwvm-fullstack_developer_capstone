import logging
import json
import requests
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import CarMake, CarModel

logger = logging.getLogger(__name__)

# URL for backend Express microservices & sentiment analyzer
BACKEND_URL = "http://localhost:3030"
SENTIMENT_URL = "http://localhost:5050"

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('userName')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        res_data = {"userName": username}
        if user is not None:
            login(request, user)
            res_data = {"userName": username, "status": "Authenticated"}
        else:
            res_data = {"userName": username, "status": "Failed", "error": "Invalid credentials"}
        return JsonResponse(res_data)
    return JsonResponse({"error": "Invalid request method"}, status=400)

@csrf_exempt
def logout_user(request):
    logout(request)
    return JsonResponse({"userName": "", "status": "Logged out"})

@csrf_exempt
def registration(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('userName')
        password = data.get('password')
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        email = data.get('email')
        
        try:
            if User.objects.filter(username=username).exists():
                return JsonResponse({"userName": username, "error": "Already Registered"})
            user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
            login(request, user)
            return JsonResponse({"userName": username, "status": True})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request method"}, status=400)

def get_cars(request):
    count = CarMake.objects.filter().count()
    if count == 0:
        # Populate initial test data if empty
        make1 = CarMake.objects.create(name="Toyota", description="Japanese car manufacturer")
        make2 = CarMake.objects.create(name="Ford", description="American car manufacturer")
        make3 = CarMake.objects.create(name="Honda", description="Japanese car manufacturer")
        make4 = CarMake.objects.create(name="BMW", description="German car manufacturer")
        CarModel.objects.create(name="Camry", car_make=make1, type="SEDAN", year=2021)
        CarModel.objects.create(name="RAV4", car_make=make1, type="SUV", year=2022)
        CarModel.objects.create(name="Corolla", car_make=make1, type="SEDAN", year=2020)
        CarModel.objects.create(name="Mustang", car_make=make2, type="SEDAN", year=2020)
        CarModel.objects.create(name="Explorer", car_make=make2, type="SUV", year=2023)
        CarModel.objects.create(name="Civic", car_make=make3, type="SEDAN", year=2022)
        CarModel.objects.create(name="CR-V", car_make=make3, type="SUV", year=2021)
        CarModel.objects.create(name="X5", car_make=make4, type="SUV", year=2023)
        
    car_models = CarModel.objects.select_related('car_make').all()
    cars = [{"CarModel": cm.name, "CarMake": cm.car_make.name, "Type": cm.type, "Year": cm.year} for cm in car_models]
    return JsonResponse({"CarModels": cars})

def get_dealerships(request, state="All"):
    if state == "All":
        endpoint = f"{BACKEND_URL}/fetchDealers"
    else:
        endpoint = f"{BACKEND_URL}/fetchDealers/{state}"
    try:
        response = requests.get(endpoint)
        return JsonResponse({"status": 200, "dealers": response.json()})
    except Exception as e:
        return JsonResponse({"status": 500, "error": str(e)})

def get_dealer_details(request, dealer_id):
    endpoint = f"{BACKEND_URL}/fetchDealer/{dealer_id}"
    try:
        response = requests.get(endpoint)
        return JsonResponse({"status": 200, "dealer": response.json()})
    except Exception as e:
        return JsonResponse({"status": 500, "error": str(e)})

def get_dealer_reviews(request, dealer_id):
    endpoint = f"{BACKEND_URL}/fetchReviews/dealer/{dealer_id}"
    try:
        response = requests.get(endpoint)
        reviews = response.json()
        # Add sentiment for each review
        for review in reviews:
            try:
                sentiment_response = requests.get(f"{SENTIMENT_URL}/analyze/{review.get('review', '')}")
                review['sentiment'] = sentiment_response.json().get('sentiment', 'neutral')
            except Exception:
                review['sentiment'] = 'neutral'
        return JsonResponse({"status": 200, "reviews": reviews})
    except Exception as e:
        return JsonResponse({"status": 500, "error": str(e)})

def analyze_review(request, review_text):
    endpoint = f"{SENTIMENT_URL}/analyze/{review_text}"
    try:
        response = requests.get(endpoint)
        return JsonResponse(response.json(), safe=False)
    except Exception as e:
        # Fallback sentiment analysis
        text_lower = review_text.lower()
        positive_words = ["fantastic", "great", "excellent", "amazing", "wonderful", "good", "love", "best", "recommend", "awesome"]
        negative_words = ["terrible", "horrible", "awful", "bad", "worst", "hate", "poor", "disappointing"]
        pos_count = sum(1 for w in positive_words if w in text_lower)
        neg_count = sum(1 for w in negative_words if w in text_lower)
        sentiment = "positive" if pos_count > neg_count else "negative" if neg_count > pos_count else "neutral"
        return JsonResponse({"sentiment": sentiment})

@csrf_exempt
def add_review(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return JsonResponse({"status": 403, "message": "Unauthorized"})
        data = json.loads(request.body)
        try:
            endpoint = f"{BACKEND_URL}/insert_review"
            response = requests.post(endpoint, json=data)
            return JsonResponse({"status": 200})
        except Exception as e:
            return JsonResponse({"status": 500, "error": str(e)})
    return JsonResponse({"status": 400, "error": "Invalid request method"})
