# -*- coding: utf-8 -*-

import os
import webapp2
import jinja2
from artist_service import artist_info
from album_service import album_info

jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = jinja_current_directory.get_template(
            "templates/welcome.html")
        self.response.write(welcome_template.render())

class ArtistsHandler(webapp2.RequestHandler):
    def get(self):
        artists_template = jinja_current_directory.get_template(
            "templates/artists.html")
        self.response.write(artists_template.render())

class AlbumsHandler(webapp2.RequestHandler):
    def get(self):
        albums_template = jinja_current_directory.get_template(
            "templates/albums.html")
        self.response.write(albums_template.render())

class ArtistHandler(webapp2.RequestHandler):
    def get(self):
        name = self.request.get("name")
        artist_template = jinja_current_directory.get_template("templates/artist.html")
        self.response.write(artist_template.render({
            "name": name,
            "image": artist_info[name]['image'],
            "spotify_link": artist_info[name]['spotify_link']}))
class AlbumHandler(webapp2.RequestHandler):
    def get(self):
        title = self.request.get("title")
        album_template = jinja_current_directory.get_template("templates/album.html")
        self.response.write(album_template.render({
            "title": title,
            "image": album_info[title]['image'],
            "spotify_link_a": album_info[title]['spotify_link_a']}))
app = webapp2.WSGIApplication([
    ('/', WelcomeHandler),
    ('/albums', AlbumsHandler),
    ('/album', AlbumHandler),
    ('/artists', ArtistsHandler),
    ('/artist', ArtistHandler),
], debug=True)
