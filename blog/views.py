from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "title": "Mountain hiking",
        "image": "mountains.jpg",
        "author": "Ustym",
        "date": date(2023, 12, 25),
        "excerpt": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "text": "Vestibulum at mauris vel enim euismod pulvinar. Fusce consectetur est enim, in porta quam tristique nec. Aenean mattis tincidunt dui. Nullam eu tortor non sem pellentesque porttitor non eget libero. Vivamus scelerisque risus id erat finibus faucibus. Ut id turpis id magna fermentum congue eget vel lorem."
                "Vestibulum at mauris vel enim euismod pulvinar. Fusce consectetur est enim, in porta quam tristique nec. Aenean mattis tincidunt dui. Nullam eu tortor non sem pellentesque porttitor non eget libero. Vivamus scelerisque risus id erat finibus faucibus. Ut id turpis id magna fermentum congue eget vel lorem."
                "Vestibulum at mauris vel enim euismod pulvinar. Fusce consectetur est enim, in porta quam tristique nec. Aenean mattis tincidunt dui. Nullam eu tortor non sem pellentesque porttitor non eget libero. Vivamus scelerisque risus id erat finibus faucibus. Ut id turpis id magna fermentum congue eget vel lorem."
    },
    {
        "slug": "walk-in-the-forest",
        "title": "Forest on foot trip",
        "image": "woods.jpg",
        "author": "Ustym",
        "date": date(2023, 11, 11),
        "excerpt": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "text": "Vestibulum at mauris vel enim euismod pulvinar. Fusce consectetur est enim, in porta quam tristique nec. Aenean mattis tincidunt dui. Nullam eu tortor non sem pellentesque porttitor non eget libero. Vivamus scelerisque risus id erat finibus faucibus. Ut id turpis id magna fermentum congue eget vel lorem."
                "Vestibulum at mauris vel enim euismod pulvinar. Fusce consectetur est enim, in porta quam tristique nec. Aenean mattis tincidunt dui. Nullam eu tortor non sem pellentesque porttitor non eget libero. Vivamus scelerisque risus id erat finibus faucibus. Ut id turpis id magna fermentum congue eget vel lorem."
                "Vestibulum at mauris vel enim euismod pulvinar. Fusce consectetur est enim, in porta quam tristique nec. Aenean mattis tincidunt dui. Nullam eu tortor non sem pellentesque porttitor non eget libero. Vivamus scelerisque risus id erat finibus faucibus. Ut id turpis id magna fermentum congue eget vel lorem."
    },
    {
        "slug": "i-love-coding",
        "title": "Coding is great",
        "image": "coding.png",
        "author": "Ustym",
        "date": date(2023, 9, 1),
        "excerpt": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "text": "Vestibulum at mauris vel enim euismod pulvinar. Fusce consectetur est enim, in porta quam tristique nec. Aenean mattis tincidunt dui. Nullam eu tortor non sem pellentesque porttitor non eget libero. Vivamus scelerisque risus id erat finibus faucibus. Ut id turpis id magna fermentum congue eget vel lorem."
                "Vestibulum at mauris vel enim euismod pulvinar. Fusce consectetur est enim, in porta quam tristique nec. Aenean mattis tincidunt dui. Nullam eu tortor non sem pellentesque porttitor non eget libero. Vivamus scelerisque risus id erat finibus faucibus. Ut id turpis id magna fermentum congue eget vel lorem."
                "Vestibulum at mauris vel enim euismod pulvinar. Fusce consectetur est enim, in porta quam tristique nec. Aenean mattis tincidunt dui. Nullam eu tortor non sem pellentesque porttitor non eget libero. Vivamus scelerisque risus id erat finibus faucibus. Ut id turpis id magna fermentum congue eget vel lorem."
    }

]


# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=lambda item: item['date'])
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    sorted_posts = sorted(all_posts, key=lambda item: item['date'])
    return render(request, "blog/all-posts.html", {
        "posts": sorted_posts
    })


def post(request, slug):
    current_post = next((item for item in all_posts if item['slug'] == slug), None)
    return render(request, "blog/post-detail.html", {
        "post": current_post
    })
