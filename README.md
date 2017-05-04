## A Dango-powered blog with RSS feed support ##
Built following the tutorial by [Arun Ravindran](http://arunrocks.com/recreating-the-building-a-blog-in-django-screencast/), based on his screencast [Building a Blog in 16 mins](https://www.youtube.com/watch?v=7rgph8en0Jc&utm_source=ActiveCampaign&utm_medium=email&utm_content=Advanced+Beginner+Challenge%3A+Python+Day+21&utm_campaign=Python+Day+21).

The original tutorial is written for Django 1.7. Many things have changed since then, and the Django 1.11 version requires a bit of adjustment.

**1. Django Markdown is now installed with the "pip install django-markdown-app" command. Using "django-markdown" will install an old version.**

**2. Use of the Context class must be removed from the Django Markdown's utils.py, replaced by a simple dictionary representation. (Easiest with a "find --> 'Context'" command. There should be two instances.)**

**3. Using the markdown app requires the following line in the EntryAdmin class in admin.py:   formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}**

**4. The settings.py file now has a designated section for template directories, labelled 'DIRS' in the templates dictionary declaration. The path should be written as an item in a list.**

The rest of the code works without adjustment.

Cheers,

Wolf
