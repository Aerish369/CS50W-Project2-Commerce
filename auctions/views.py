from django.http import HttpResponse, HttpResponseRedirect
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import ListingsForm, CommentsForm

from django.contrib import messages

from .models import User, Listings, Bid, Comments
from django.db.models import Max


def index(request):
    listings = Listings.objects.all()
    context = {
        'listings': listings,
    }
    return render(request, "auctions/index.html", context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required(login_url='login')
def createListing(request):
    form = ListingsForm()

    if request.method == 'POST':
        form = ListingsForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.owner = request.user
            listing.save()

            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'auctions/add-listing.html', context)


def bidListing(request, pk):
    listingObj = Listings.objects.get(id=pk)
    comment_form = CommentsForm()
    all_comments = Comments.objects.filter(listing=listingObj)

    if request.method == 'POST':
        bid_amount = request.POST.get('bid_amount')
        if bid_amount:
            if int(bid_amount)>listingObj.bid_price:    
                new_bid = Bid.objects.create(bid_amount=int(bid_amount), bid_owner=request.user, bid_listing=listingObj)
                listingObj.bid_price = int(bid_amount)
                listingObj.save()
                messages.success(request, "Bid placed! You are the highest bidder now. ")
            else:
                messages.error(request, "Bidding should be higher than previous bid.")

    
    context ={
        'listing': listingObj,
        'bid_amount' : request.POST.get('bid_amount'),
        'form': comment_form,
        'comments': all_comments,     
    }
    return render(request, 'auctions/listing.html', context)


def closeListing(request, pk):

    listingObj = Listings.objects.get(id = pk)
    
    if request.method == 'POST':
        listingObj.is_active = False
        listingObj.save()
        messages.success(request, "Bidding Closed !!! ")
    else:
        return render(request, 'auctions/listing.html', {"listing": listingObj})

    context ={
        "listing": listingObj,
    }
    return render(request, 'auctions/listing.html', context) 


def addRemoveWatchlist(request, pk):
    listingObj = Listings.objects.get(id=pk)
    if request.method == 'POST':
        listing_id = listingObj.id
        listing = Listings.objects.get(id=listing_id)
        if request.user in listing.in_watchlist.all():
            listing.in_watchlist.remove(request.user)
            listing.save()
        else:
            listing.in_watchlist.add(request.user)
            listing.save()

    context = {
        'listing': listingObj,
    }

    return render(request, 'auctions/listing.html', context)  


def viewWatchlist(request):
    allWatchlist = Listings.objects.filter(in_watchlist=request.user)

    context = {
        'watchlist': allWatchlist,
    }
    return render(request, 'auctions/watchlist.html', context)


def addComment(request, pk):
    listingObj = Listings.objects.get(id=pk)
    all_comments = Comments.objects.filter(listing=listingObj)
    comment_form = CommentsForm()

    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['body'] != '':
                comment = form.save(commit=False)
                comment.owner = request.user
                comment.listing = listingObj
                comment.save()

                messages.success(request, "Comment added successfully.")
                return HttpResponseRedirect(reverse('listing', args=(pk,)))
            else:
                messages.error(request, "Comment cannot be empty.")
                return HttpResponseRedirect(reverse('listing', args=(pk,)))
    
    return render(request, 'auctions/listing.html', {
        'listing': listingObj,
        'form': comment_form,
        'comments': all_comments,     })