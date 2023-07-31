from django.shortcuts import render
from django.http import JsonResponse

from django.shortcuts import render, redirect
from .models import Profile, Swipe
from .forms import ProfileForm
from maincode import gale_shapley

def swipe(request):
    current_user = request.user
    form = ProfileForm(request.POST or None)
    profiles = Profile.objects.exclude(user=current_user)

    if request.method == 'POST':
        if form.is_valid():
            liked_profile_id = form.cleaned_data['liked_profile']
            liked_profile = Profile.objects.get(id=liked_profile_id)
            Swipe.objects.create(swiper=current_user, liked_profile=liked_profile)
            return redirect('swipe')

    context = {'profiles': profiles, 'form': form}
    return JsonResponse(context)


def matches(request):
    current_user = request.user
    liked_profiles = Profile.objects.filter(id__in=liked_profiles)
    matched_profiles = Profile.objects.filter(id__in=matched_profiles)
    matches = Profile.objects.filter(user__in=matched_profiles)

    # Convert the queryset to a dictionary with the Profile names as keys
    profile_dict = {profile.name: profile for profile in Profile.objects.all()}

    # Create a dictionary of the two groups of people for the gale_shapley function
    profile_groups = {'men': {}, 'women': {}}
    for match in matches:
        profile_groups['men'][match.name] = [profile_dict[liked_profile].name for liked_profile in liked_profiles if liked_profile == match.id]
        profile_groups['women'][match.name] = [profile_dict[swiper].name for swiper in matched_profiles if swiper == match.id]


    engagements = gale_shapley(profile_groups)

    # Get the matched profiles from the engagements dictionary
    matched_profiles = {profile_dict[woman]: profile_dict[man] for woman, man in engagements.items()}

    context = {'matches': matched_profiles}
    return JsonResponse(context)