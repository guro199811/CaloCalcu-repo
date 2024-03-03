import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  # For demonstration (remove in production)
from django.contrib.auth.decorators import login_required
from django.db import transaction  # For database transactions, any changes on error are being rolled back
import logging
from .models import *
from django.db.models import Q  # For advanced filtering
from collections import Counter
from django.http import JsonResponse, HttpResponseNotFound
from django.core.mail import send_mail
from django.conf import settings





@csrf_exempt  #Should Remove in production
@login_required  # Ensuring authenticated users
def add_food_history(request):
    if request.method == 'POST':
        content_type = request.content_type

        if content_type != 'application/json':
            return JsonResponse({'error': 'Invalid content type: {}'.format(content_type)}, status=400)

        try:
            selected_foods = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        user = request.user

        # Validate data (e.g., check for empty list)
        if not selected_foods:
            return JsonResponse({'error': 'No selected foods'}, status=400)

        # Process and save food items and history entries
        food_list = []
        with transaction.atomic():  # Ensure atomicity
            for food_data in selected_foods.get('selectedFoods'):
                # Extract relevant information
                fdcId = food_data.get('fdcId')
                description = food_data.get('description')
                nutrients = food_data.get('foodNutrients')

                # Check if food already exists (optional)
                try:
                    existing_food = Food.objects.filter(api_id = int(fdcId)).first()
                    if not existing_food:
                        existing_food = Food.objects.create(name=description, nutritional_data=nutrients, api_id = int(fdcId))
                    food_list.append(existing_food.id)
                except Exception as e:
                    logging.warning(f'{e}')
            # Create/update FoodHistory entry
            FoodHistory.objects.create(user=user, food_list=food_list, quantity=1)  # Update quantity if needed
        return JsonResponse({'success': 'Food history updated successfully'})
    

@csrf_exempt  #Should Remove in production
@login_required  # Ensuring authenticated users
def retrieve_food_history(request):
    if request.method == 'GET':
        try:
            food_history = FoodHistory.objects.filter(user=request.user).all().order_by('-date_added')
            data = []

            for food_entry in food_history:
                # Use Counter to efficiently count food IDs and maintain order
                food_counts = Counter(food_entry.food_list)
                food_data = []

                # Iterate through counts and retrieve food objects
                for food_id, count in food_counts.items():
                    food = Food.objects.get(pk=food_id)  # Optimized for efficiency

                    # Create dictionary with name and count for each food
                    food_data.append({
                        'name': food.name,
                        'count': count,
                    })

                # Create final entry with date, food data (including counts), and **original food IDs**
                data.append({
                    'date_added': food_entry.date_added.strftime('%Y-%m-%d'),
                    'food_data': food_data,
                    'food_list': food_entry.food_list,
                    'food_hist_id': food_entry.id,  # Include original food IDs from the database
                })

            return JsonResponse(data, safe=False)

        except Exception as e:
            logging.warning(f'Error retrieving food history: {e}')
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    

@csrf_exempt  #Should Remove in production
@login_required  # Ensuring authenticated users
def remove_food_entry(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            hist_id = data.get('hist_id')

            if not hist_id:
                return JsonResponse({'error': 'Missing required field "hist_id"'}, status=400)

            # Retrieving and deleting the food entry using hist_id
            food_entry = FoodHistory.objects.filter(pk=hist_id).first()

            if not food_entry:
                return JsonResponse({'error': 'Food entry not found'}, status=404)

            food_entry.delete()

            return JsonResponse({'success': True})

        except Exception as e:
            print(f'Error removing food entry: {e}')
            return JsonResponse({'error': 'An error occurred'}, status=500)

    else:
        return HttpResponseNotFound('Method not allowed')
    


# Contact Logic
    
def contact_us(request):
    if request.method == "POST":
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('textfield')

        print(email, subject, message)


        # NOTE FOR FUTURE ME:
        # Contact Page Wont work with filebased system
        # configure settings.py with smtp mailing system
        # it should work then, but youll figure it out.


        # Send an email
        send_mail(
            subject,
            message,
            email,  # User's email as the sender
            [settings.EMAIL_HOST_USER],  # Host's email as the recipient
            fail_silently=False,
        )

        variables = {'contact_sent': True}
        return render(request, 'tracker/contact.html', variables)