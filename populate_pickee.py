import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pickee_project.settings')
import django
django.setup()
import datetime
from django.contrib.auth.models import User
from pickee_api.models import (UserProfile,FavoriteActor,Actor,
                                FavoriteMovie,Movie,MovieCast,
                                FavoriteGenre,Genre,Recommendation,
                                Session)

users = [
    {'username':'rhys','password':'rhyspassword','email':'rhys@email.com','first_name':'Rhys',
        'last_name':'Stephens','picture':None,'avatar':None,'gender':'MALE','age':23,'associated_users':None},
    {'username':'pedro','password':'pedropassword','email':'pedro@email.com','first_name':'Pedro',
        'last_name':'Belfort','picture':None,'avatar':None,'gender':'MALE','age':42,'associated_users':None},
    {'username':'nathan','password':'nathanpassword','email':'nathan@email.com','first_name':'Nathan',
        'last_name':'Schneddy','picture':None,'avatar':None,'gender':'MALE','age':23,'associated_users':None},
    {'username':'anton','password':'antonpassword','email':'anton@email.com','first_name':'Anton',
        'last_name':'Samoilov','picture':None,'avatar':None,'gender':'MALE','age':19,'associated_users':None},
]

favorite_actors = [
    {'username':'rhys','actor_id':74568},
    {'username':'rhys','actor_id':84223},
    {'username':'pedro','actor_id':31},
    {'username':'nathan','actor_id':4491},
    {'username':'nathan','actor_id':11701},
    {'username':'nathan','actor_id':6193},
    {'username':'anton','actor_id':192},
]

actors = [
    {'person_id':31,'name':'Tom Hanks','picture':None},
    {'person_id':6193,'name':'Leonardo DiCaprio','picture':None},
    {'person_id':74568,'name':'Chris Hemsworth','picture':None},
    {'person_id':4491,'name':'Jennifer Aniston','picture':None},
    {'person_id':11701,'name':'Angelina Jolie','picture':None},
    {'person_id':84223,'name':'Anna Kendrick','picture':None},
    {'person_id':192,'name':'Morgan Freeman','picture':None}
]

favorite_movies = [
    {'username':'rhys','movie_id':301528},
    {'username':'pedro','movie_id':10184},
    {'username':'pedro','movie_id':102651},
    {'username':'nathan','movie_id':10184},
    {'username':'anton','movie_id':26205},
    {'username':'anton','movie_id':278},
    {'username':'anton','movie_id':284053},
]

movies = [
    {'movie_id':301528,'name':'Toy Story 4','picture':None,'rating':75,'release_date':datetime.date(2019,6,19),
    'decription':'''Woody has always been confident about his place in the world and that his priority is taking 
        care of his kid, whether that's Andy or Bonnie. But when Bonnie adds a reluctant new toy called \"Forky\" 
        to her room, a road trip adventure alongside old and new friends will show Woody how big the world can be 
        for a toy.'''},
    {'movie_id':27205,'name':'Inception','picture':None,'rating':83,'release_date':datetime.date(2010,7,15),
    'decription':'''Cobb, a skilled thief who commits corporate espionage by infiltrating the subconscious of his 
        targets is offered a chance to regain his old life as payment for a task considered to be impossible: 
        \"inception\", the implantation of another person's idea into a target's subconscious.'''},
    {'movie_id':284053,'name':'Thor:Ragnarok','picture':None,'rating':75,'release_date':datetime.date(2017,10,25),
    'decription':'''Thor is imprisoned on the other side of the universe and finds himself in a race against time to 
        get back to Asgard to stop Ragnarok, the destruction of his home-world and the end of Asgardian civilization, 
        at the hands of an all-powerful new threat, the ruthless Hela.'''},
    {'movie_id':10184,'name':'He\'s Just Not That Into You','picture':None,'rating':64,'release_date':datetime.date(2009,2,6),
    'decription':'''Remember that really cute girl/guy who said they'd call – and didn't? Maybe they lost your number. Maybe 
        they're in the hospital. Maybe they're awed by your looks, brains or success. Or maybe... They're just not that into you.'''},
    {'movie_id':102651,'name':'Maleficent','picture':None,'rating':71,'release_date':datetime.date(2014,5,28),
    'decription':'''A beautiful, pure-hearted young woman, Maleficent has an idyllic life growing up in a peaceable 
        forest kingdom, until one day when an invading army threatens the harmony of the land.  Maleficent rises to be 
        the land's fiercest protector, but she ultimately suffers a ruthless betrayal – an act that begins to turn her 
        heart into stone. Bent on revenge, Maleficent faces an epic battle with the invading King's successor and, as a 
        result, places a curse upon his newborn infant Aurora. As the child grows, Maleficent realizes that Aurora holds 
        the key to peace in the kingdom – and to Maleficent's true happiness as well.'''},
    {'movie_id':114150,'name':'Pitch Perfect','picture':None,'rating':73,'release_date':datetime.date(2012,9,28),
    'decription':'''College student Beca knows she does not want to be part of a clique, but that's exactly where 
        she finds herself after arriving at her new school. Thrust in among mean gals, nice gals and just plain 
        weird gals, Beca finds that the only thing they have in common is how well they sing together. She takes 
        the women of the group out of their comfort zone of traditional arrangements and into a world of amazing 
        harmonic combinations in a fight to the top of college music competitions.'''},
    {'movie_id':278,'name':'The Shawshank Redemption','picture':None,'rating':87,'release_date':datetime.date(1994,9,23),
    'decription':'''Framed in the 1940s for the double murder of his wife and her lover, upstanding banker Andy Dufresne 
        begins a new life at the Shawshank prison, where he puts his accounting skills to work for an amoral warden. During 
        his long stretch in prison, Dufresne comes to be admired by the other inmates -- including an older prisoner named 
        Red -- for his integrity and unquenchable sense of hope.'''}
]

movie_casts = [
    {}
]

favorite_genres = [
    {}
]

genres = [
    {'genre_id':28,'name':'Action'},
    {'genre_id':12,'name':'Adventure'},
    {'genre_id':16,'name':'Animation'},
    {'genre_id':35,'name':'Comedy'},
    {'genre_id':80,'name':'Crime'},
    {'genre_id':99,'name':'Documentary'},
    {'genre_id':18,'name':'Drama'},
    {'genre_id':10751,'name':'Family'},
    {'genre_id':14,'name':'Fantasy'},
    {'genre_id':36,'name':'History'},
    {'genre_id':27,'name':'Horror'},
    {'genre_id':10402,'name':'Music'},
    {'genre_id':9648,'name':'Mystery'},
    {'genre_id':10749,'name':'Romance'},
    {'genre_id':878,'name':'Science Fiction'},
    {'genre_id':10770,'name':'TV Movie'},
    {'genre_id':53,'name':'Thriller'},
    {'genre_id':10752,'name':'War'},
    {'genre_id':37,'name':'Western'}
]

recommendations = [
    {}
]

sessions = [
    {}
]

def add_user(username,password,email,first_name,last_name,picture,avatar,gender,age,associated_users):
    user = UserProfile.objects.get_or_create(user=User.objects.create_user(username,None,password),
                                            email=email,
                                            first_name=first_name,
                                            last_name=last_name,
                                            picture=picture,
                                            avatar=avatar,
                                            gender=gender,
                                            age=age,
                                            associated_users=associated_users)

def add_actor(person_id, name, picture):
    actor = Actor.objects.get_or_create(person_id=person_id,
                                        name=name,
                                        picture=picture)

def add_movie(movie_id,name,picture,rating,release_date,description):
    movie = Movie.objects.get_or_create(movie_id=movie_id,
                                        name=name,
                                        picture=picture,
                                        rating=rating,
                                        release_date=release_date,
                                        description=description)

def add_genre(genre_id,name):
    genre = Genre.objects.get_or_create(genre_id=genre_id,
                                        name=name)

def add_favorite_actor(username,actor_id):
    favorite_actor = FavoriteActor.objects.get_or_create(user=User.objects.get(username=username),
                                                        actor=Actor.objects.get(person_id=actor_id))

def add_favorite_movie(username,movie_id):
    favorite_movie = FavoriteMovie.objects.get_or_create(user=User.objects.get(username=username),
                                                        movie=Movie.objects.get(movie_id=movie_id))