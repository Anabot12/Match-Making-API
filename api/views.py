from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from maincode import gale_shapley

def calculate_compatibility(tags1, tags2):
    max_compatibility_score = 20  # Define the maximum compatibility score

    # Calculate compatibility based on tags
    tag_intersection = len(set(tags1).intersection(tags2))
    tag_score = (tag_intersection / max(len(tags1), len(tags2))) * 10

    # Calculate overall compatibility score
    compatibility_score = tag_score
    compatibility_percentage = (compatibility_score / max_compatibility_score) * 100

    return compatibility_percentage


class ListAPI(generics.GenericAPIView):
    def post(self, request):
        person1 = request.data.get('person1')
        person2 = request.data.get('person2')

        if not person1 or not person2:
            return Response({"status": "error", "message": "Invalid input"}, status=status.HTTP_400_BAD_REQUEST)

        # Extract details for person1
        person1_age = person1.get('age') if 'age' in person1 else None
        person1_gender = person1.get('gender') if 'gender' in person1 else None
        person1_tags_string = person1['tags']  # Assuming tags input is a string separated by a delimiter
        person1_tags = person1_tags_string.split(',')  # Split the string using a delimiter

        # Extract details for person2
        person2_age = person2.get('age') if 'age' in person2 else None
        person2_gender = person2.get('gender') if 'gender' in person2 else None
        person2_tags_string = person2['tags']  # Assuming tags input is a string separated by a delimiter
        person2_tags = person2_tags_string.split(',')  # Split the string using a delimiter

        if person1_age is not None and person2_age is not None and (person1_age < 18 or person2_age < 18):
            return Response({"status": "error", "message": "Age must be 18 or above"}, status=status.HTTP_400_BAD_REQUEST)

        # Calculate compatibility based on tags and age
        compatibility = calculate_compatibility(person1_tags, person2_tags)

        if compatibility < 4:
            return Response({"status": "error", "message": "Incompatible"}, status=status.HTTP_400_BAD_REQUEST)

        # Perform match-making algorithm
        match = gale_shapley(person1_tags, person2_tags, compatibility)

        # Construct response data
        data = {
            'compatibility_score': round(compatibility, 2)
            #'match': match
        }

        return Response({"status": "success", "data": data}, status=status.HTTP_200_OK)
