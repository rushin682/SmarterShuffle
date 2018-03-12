from django import forms

class SearchBar(forms.Form):
    class Media:
        css = {
                'all' : ('/css/style.css'),
            }
        js = ('/js/jquery-2.1.4.js',)
    search_ID = forms.CharField(label = 'Search', max_length = 100)
