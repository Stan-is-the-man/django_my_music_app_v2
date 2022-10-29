import profile

from django.shortcuts import render, redirect

from my_music_app_stan_v2.web.forms import CreateProfileForm, GeneralAlbumForm, DeleteAlbumForm, DeleteProfileForm
from my_music_app_stan_v2.web.models import Profile, Album


def get_profile():
    try:
        return Profile.objects.get()
    except:
        return None


def profile_create(request):
    # if we have already a profile!
    if get_profile() is not None:
        return redirect('home with no profile')
    # else
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home with profile')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'profile_exists': True,

    }
    return render(request, 'home-no-profile.html', context)


def home_page(request):
    profile = get_profile()
    if profile is None:
        return redirect('home with no profile')
    albums = Album.objects.all()

    context = {
        'albums': albums,

    }

    return render(request, 'home-with-profile.html', context)


def album_add(request):
    if request.method == 'POST':
        form = GeneralAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home with profile')
    else:
        form = GeneralAlbumForm()

    context = {
        'form': form
    }
    return render(request, 'album-add.html', context)


def album_details(request, pk):
    album = Album.objects.get(pk=pk)
    context = {
        'album': album,
    }
    return render(request, 'album-details.html', context)


def album_edit(request, pk):
    album = Album.objects.get(pk=pk)

    if request.method == 'POST':
        form = GeneralAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home with profile')
    else:
        form = GeneralAlbumForm(instance=album)

    context = {
        'form': form
    }

    return render(request, 'album-edit.html', context)


def album_delete(request, pk):
    album = Album.objects.get(pk=pk)

    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home with profile')
    else:
        form = DeleteAlbumForm(instance=album)

    context = {
        'form': form
    }
    return render(request, 'album-delete.html', context)


def profile_details(request):
    profile = get_profile()
    albums = Album.objects.all()
    albums_count = len(albums)
    context = {
        'profile': profile,
        'albums_count': albums_count
        }
    return render(request, 'profile-details.html', context)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home with profile')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {'form': form}

    return render(request, 'profile-delete.html', context)
