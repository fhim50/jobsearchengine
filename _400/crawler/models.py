from django.db import models

class Searchword(models.Model):
    word = models.CharField(max_length = 100)
    urls = models.TextFields(max_length = None)

    class Meta:
        db_table = searchword


    def __unicode__ (self):
        return self.keyword

    def get_url(self):
	return "some/keywords/url"


class Page(models.Model):
    serchword = models.ForiegnKey(Searchword)
    url = models.CharField(max_length = 100)
    title = models.CharField(max_length = )
    def page_preview():
         return " content  preview"
         pass
    page_preview = models.TextField(max_length = "some number" , default = page_preview() ) 
    rank = models.FloatField(max_degit = 19 , decimal_places = "some_number" , editable = False)

    def number_clicks():
        pass
    clicks = models.IntegerField(max_length = 4 , default = number_clicks())

    class Meta:
        db_table = page

    def __unicode__ (self):
        return self.url


