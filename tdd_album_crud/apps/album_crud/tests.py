from operator import methodcaller
from django.test import TestCase, Client
#clinet: allows for simultatig requests
#TestCase gives all basic unittest asserts and more

from .models import * #import all form models

class AlbumTest(TestCase):
    #######testing urls###########
    def test_index(self):
        c = Client()
        response = c.get('/')
        bad = c.get('/bugs')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(bad.status_code, 404)#page doesnt exist

    def test_create_album(self):
        c = Client()
        response = c.get('/album/create')
        self.assertEqual(response.status_code, 302)

        # look to combine test in a single method
    def test_urls(self):
        c = Client()
        idx_response = c.get('/')
        self.assertEqual(idx_response.status_code, 200)
        create_response = c.get('/album/create')
        self.assertEqual(create_response.status_code, 302)

    ######Testing models######## import .models above
    @classmethod
    def setUpTestData(cls):
        Album.objects.create(title = "A Test Album", artist = "The Pythons", year = 2200)
        #^^^this is dummy data.  all tests can access this for testing
        ##you do want to test create method first to ensure it works

    def test_model_creation(self): 
        a = Album.objects.create(title = "Testing Time", artist = "The Pythons", year = 2018)
        self.assertEqual(a.title, "Testing Time")
        self.assertEqual(a.artist, "The Pythons")
        self.assertEqual(a.year, 2018)

    def test_model_get(self):
        a = Album.objects.get(id = 1)
        self.assertEqual(a.id, 1)
        self.assertIsInstance(a, Album)

    def test_model_edit(self):
        a = Album.objects.first()
        a.title = "EditedTitle"
        a.artist = "Django Doug"
        a.year = 1999
        a.save()
        edited_a = Album.objects.first()
        self.assertEqual(edited_a.title, "EditedTitle")
        self.assertEqual(edited_a.artist, "Django Doug")
        self.assertEqual(edited_a.year, 1999)

    def test_model_delete(self):
        # Delete will return a tuple that holds the number of entities deleted in the 0 index
        num_deleted = Album.objects.get(id = 1).delete()[0]
        self.assertEqual(num_deleted, 1)

    ########testing views (post forms)######### generally you want to test views after urls, and models

    # Adding to our test class
    def test_view_create(self):
        # First, we make a POST request to the server. We can send a dictionary of POST data
        c = Client()
        post_data = {
            "title": "Testing Views",
            "artist" : "Danger Django",
            "year": 2017
        }
        response = c.post('/album/create', post_data)
        # We also want to test to make sure that the view function did actually redirect as we wanted
        self.assertEqual(response.status_code, 302)
        # If the Album was made successfully, we should be able to grab the last Album and check its values against the post_data we submitted
        newly_created_album = Album.objects.last()
        self.assertEqual(newly_created_album.title, post_data['title'])
        self.assertEqual(newly_created_album.artist, post_data['artist'])
        self.assertEqual(newly_created_album.year, post_data['year'])
    
    def test_context(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.context['answer'], 42)

    def test_view_edit(self):
        ## For this one, we have given you a good jumping off point, but it's still
        ## up to you to create the url and the view function to make this test pass
        c = Client()
        post_data = {
            "title": "A Test Edit",
            "artist" : "Test Artist Edit",
            "year": 3099
        }
        # This should edit the single album that is created by our setUp method
        response = c.post('/album/1/edit', post_data)
        # Let's make sure the view function eventually redirects
        self.assertEqual(response.status_code, 302)
        # Let's test to make sure the edit worked
        edited = Album.objects.get(id = 1)
        self.assertEqual(edited.title, post_data['title'])
        self.assertEqual(edited.artist, post_data['artist'])
        self.assertEqual(edited.year, post_data['year'])
    def test_view_delete(self):
        # Test to make sure a view function can retrieve an album based on an id being sent in the url
        # Test to make sure that this specific album gets deleted
        pass
    def test_view_read(self):
        # Test to make sure a view function can retrieve an album based on an id being sent in the url
        # Make sure this single record is getting passed via context
        pass
