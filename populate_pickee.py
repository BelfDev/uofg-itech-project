import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pickee_project.settings')
import django
django.setup()
import datetime
from django.contrib.auth.models import User
from pickee_api.models import (PickeeUser,FavoriteActor,Actor,
                                FavoriteMovie,Movie,MovieCast,
                                FavoriteGenre,Genre,Recommendation,
                                Session)
from pickee_api.managers import PickeeUserManager

users = [
    {'email':'rhys@email.com','password':'rhyspassword','first_name':'Rhys','last_name':'Stephens',
        'gender':'MALE','age':23},
    {'email':'pedro@email.com','password':'pedropassword','first_name':'Pedro','last_name':'Belfort',
        'gender':'MALE','age':42},
    {'email':'nathan@email.com','password':'nathanpassword','first_name':'Nathan','last_name':'Schneddy',
        'gender':'MALE','age':23},
    {'email':'anton@email.com','password':'antonpassword','first_name':'Anton','last_name':'Samoilov',
        'gender':'MALE','age':19},
]

favorite_actors = [
    {'email':'rhys@email.com','actor_id':74568},
    {'email':'rhys@email.com','actor_id':84223},
    {'email':'pedro@email.com','actor_id':31},
    {'email':'nathan@email.com','actor_id':4491},
    {'email':'nathan@email.com','actor_id':11701},
    {'email':'nathan@email.com','actor_id':6193},
    {'email':'anton@email.com','actor_id':192},
]

actors = [
    {'id':31,'name':'Tom Hanks','image_url':'/2gY92j2lkNHL2cThBhPmgXLd5PL.jpg'},
    {'id':6193,'name':'Leonardo DiCaprio','image_url':'/wo2hJpn04vbtmh0B9utCFdsQhxM.jpg'},
    {'id':74568,'name':'Chris Hemsworth','image_url':'/tlkDiLn2G75Xr7m1ybK8QFzZBso.jpg'},
    {'id':4491,'name':'Jennifer Aniston','image_url':'/uH9FwXtRpiboKeqHUk0RuJRAm6I.jpg'},
    {'id':11701,'name':'Angelina Jolie','image_url':'/gD8jlGkQC8GBajulNlIzBK1YEO1.jpg'},
    {'id':84223,'name':'Anna Kendrick','image_url':'/5ZYBQefB30uWObRzin8R0PYqenh.jpg'},
    {'id':192,'name':'Morgan Freeman','image_url':'/oIciQWr8VwKoR8TmAw1owaiZFyb.jpg'}
]

favorite_movies = [
    {'email':'rhys@email.com','movie_id':301528},
    {'email':'pedro@email.com','movie_id':10184},
    {'email':'pedro@email.com','movie_id':102651},
    {'email':'nathan@email.com','movie_id':10184},
    {'email':'anton@email.com','movie_id':27205},
    {'email':'anton@email.com','movie_id':278},
    {'email':'anton@email.com','movie_id':284053},
]

movies = [
    {'id':301528,'name':'Toy Story 4','image_url':'/w9kR8qbmQ01HwnvK4alvnQ2ca0L.jpg','rating':7.5,'release_date':datetime.date(2019,6,19),
        'description':'''Woody has always been confident about his place in the world and that his priority is taking 
        care of his kid, whether that's Andy or Bonnie. But when Bonnie adds a reluctant new toy called \"Forky\" 
        to her room, a road trip adventure alongside old and new friends will show Woody how big the world can be 
        for a toy.'''},
    {'id':27205,'name':'Inception','image_url':'/qmDpIHrmpJINaRKAfWQfftjCdyi.jpg','rating':8.3,'release_date':datetime.date(2010,7,15),
        'description':'''Cobb, a skilled thief who commits corporate espionage by infiltrating the subconscious of 
        his targets is offered a chance to regain his old life as payment for a task considered to be impossible: 
        \"inception\", the implantation of another person's idea into a target's subconscious.'''},
    {'id':284053,'name':'Thor:Ragnarok','image_url':'/rzRwTcFvttcN1ZpX2xv4j3tSdJu.jpg','rating':7.5,'release_date':datetime.date(2017,10,25),
        'description':'''Thor is imprisoned on the other side of the universe and finds himself in a race against 
        time to get back to Asgard to stop Ragnarok, the destruction of his home-world and the end of Asgardian 
        civilization, at the hands of an all-powerful new threat, the ruthless Hela.'''},
    {'id':10184,'name':'He\'s Just Not That Into You','rating':6.4,'image_url':'/ruc33YnCrmCL8PHdPQVzfa4shWX.jpg','release_date':datetime.date(2009,2,6),
        'description':'''Remember that really cute girl/guy who said they'd call – and didn't? Maybe they lost your 
        number. Maybe they're in the hospital. Maybe they're awed by your looks, brains or success. Or maybe... 
        They're just not that into you.'''},
    {'id':102651,'name':'Maleficent','image_url':'/zsGiTcMZ9yp2as3FmPMgZyil5mc.jpg','rating':7.1,'release_date':datetime.date(2014,5,28),
        'description':'''A beautiful, pure-hearted young woman, Maleficent has an idyllic life growing up in a 
        peaceable forest kingdom, until one day when an invading army threatens the harmony of the land.  Maleficent 
        rises to be the land's fiercest protector, but she ultimately suffers a ruthless betrayal – an act that 
        begins to turn her heart into stone. Bent on revenge, Maleficent faces an epic battle with the invading 
        King's successor and, as a result, places a curse upon his newborn infant Aurora. As the child grows, 
        Maleficent realizes that Aurora holds the key to peace in the kingdom – and to Maleficent's true happiness 
        as well.'''},
    {'id':114150,'name':'Pitch Perfect','image_url':'/qSjruLiFB4uqRtz2xheQPxG8uaB.jpg','rating':7.3,'release_date':datetime.date(2012,9,28),
        'description':'''College student Beca knows she does not want to be part of a clique, but that's exactly 
        where she finds herself after arriving at her new school. Thrust in among mean gals, nice gals and just 
        plain weird gals, Beca finds that the only thing they have in common is how well they sing together. She 
        takes the women of the group out of their comfort zone of traditional arrangements and into a world of 
        amazing harmonic combinations in a fight to the top of college music competitions.'''},
    {'id':278,'name':'The Shawshank Redemption','image_url':'/9O7gLzmreU0nGkIB6K3BsJbzvNv.jpg','rating':8.7,'release_date':datetime.date(1994,9,23),
        'description':'''Framed in the 1940s for the double murder of his wife and her lover, upstanding banker Andy 
        Dufresne begins a new life at the Shawshank prison, where he puts his accounting skills to work for an 
        amoral warden. During his long stretch in prison, Dufresne comes to be admired by the other inmates -- 
        including an older prisoner named Red -- for his integrity and unquenchable sense of hope.'''},
    {'id':5255,'name':'The Polar Express','image_url':'/2NETsNUxcfBdKtq3W5YbT9O03Ak.jpg','rating':6.6,'release_date':datetime.date(2004,11,10),
        'description':'''When a doubting young boy takes an extraordinary train ride to the North Pole, he embarks on 
        a journey of self-discovery that shows him that the wonder of life never fades for those who believe.'''},
    {'id':32407,'name':'Malice In Wonderland','image_url':None,'rating':5.7,'release_date':datetime.date(2009,1,1),
        'description':'''A modern take on the classic fairytale, Alice in Wonderland, set in South East England.An 
        American law student in London. Knocked down by a black cab, she wakes with amnesia in a world that's a 
        million miles from home - Wonderland. We follow her adventures as she's dragged through an underworld filled 
        with twisted individuals and the lowest low-lifers, by the enigmatic cab driver, Whitey. She needs to find 
        out who she is, where she's from and use what wits she has left to get back home in one piece. As her journey 
        progresses she discovers nothing is what it seems, realizes that fate and life are terminally entwined, and 
        finds true love lurking in the unlikeliest place.'''},
    {'id':8999,'name':'Derailed','rating':6.2,'image_url':'/inBGQGHUUFAmt9nINRAdTUBkmQN.jpg','release_date':datetime.date(2005,11,11),
        'description':'''When two married business executives having an affair are blackmailed by a violent criminal, 
        they are forced to turn the tables on him to save their families.'''},
    {'id':393624,'name':'Official Secrets','image_url':'/lyCGqSkT3PqLYQXiWs4FCVJBAYW.jpg','rating':7.3,'release_date':datetime.date(2019,8,30),
        'description':'''The true story of British intelligence whistleblower Katharine Gun who—prior to the 2003 
        Iraq invasion—leaked a top-secret NSA memo exposing a joint US-UK illegal spying operation against members 
        of the UN Security Council. The memo proposed blackmailing member states into voting for war.'''}
]

movie_casts = [
    {'movie_id':301528,'actor_id':31},
    {'movie_id':27205,'actor_id':6193},
    {'movie_id':284053,'actor_id':74568},
    {'movie_id':10184,'actor_id':4491},
    {'movie_id':102651,'actor_id':11701},
    {'movie_id':114150,'actor_id':84223},
    {'movie_id':278,'actor_id':192},
]

favorite_genres = [
    {'email':'rhys@email.com','genre_id':16},
    {'email':'rhys@email.com','genre_id':14},
    {'email':'pedro@email.com','genre_id':28},
    {'email':'pedro@email.com','genre_id':10402},
    {'email':'nathan@email.com','genre_id':18},
    {'email':'nathan@email.com','genre_id':53},
    {'email':'anton@email.com','genre_id':10749},
    {'email':'anton@email.com','genre_id':80},
]

genres = [
    {'id':28,'name':'Action'},
    {'id':12,'name':'Adventure'},
    {'id':16,'name':'Animation'},
    {'id':35,'name':'Comedy'},
    {'id':80,'name':'Crime'},
    {'id':99,'name':'Documentary'},
    {'id':18,'name':'Drama'},
    {'id':10751,'name':'Family'},
    {'id':14,'name':'Fantasy'},
    {'id':36,'name':'History'},
    {'id':27,'name':'Horror'},
    {'id':10402,'name':'Music'},
    {'id':9648,'name':'Mystery'},
    {'id':10749,'name':'Romance'},
    {'id':878,'name':'Science Fiction'},
    {'id':10770,'name':'TV Movie'},
    {'id':53,'name':'Thriller'},
    {'id':10752,'name':'War'},
    {'id':37,'name':'Western'}
]

recommendations = [
    {'movie_id':5255,'session_id':1,'user_choice':'ACCEPTED'},
    {'movie_id':32407,'session_id':2,'user_choice':'ACCEPTED'},
    {'movie_id':8999,'session_id':3,'user_choice':'REJECTED'},
    {'movie_id':393624,'session_id':4,'user_choice':'BOOKMARKED'}
]

sessions = [
    {'users':{'rhys@email.com','pedro@email.com'}},
    {'users':{'rhys@email.com','pedro@email.com','nathan@email.com','anton@email.com'}},
    {'users':{'nathan@email.com'}},
    {'users':{'nathan@email.com','anton@email.com'}}
]

def populate():
    for user in users:
        add_user(user['email'],user['password'],user['first_name'],user['last_name'],user['gender'],user['age'])
    
    for actor in actors:
        add_actor(actor['id'],actor['name'],actor['image_url'])
    
    for movie in movies:
        add_movie(movie['id'],movie['name'],movie['image_url'],movie['rating'],movie['release_date'],movie['description'])
    
    for genre in genres:
        add_genre(genre['id'],genre['name'])
    
    for actor in favorite_actors:
        add_favorite_actor(actor['email'],actor['actor_id'])
    
    for movie in favorite_movies:
        add_favorite_movie(movie['email'],movie['movie_id'])
    
    for actor in movie_casts:
        add_movie_cast(actor['movie_id'],actor['actor_id'])
    
    for genre in favorite_genres:
        add_favorite_genre(genre['email'],genre['genre_id'])
    
    for session in sessions:
        add_session(session['users'])
    
    for recommendation in recommendations:
        add_recommendation(recommendation['movie_id'],recommendation['session_id'],recommendation['user_choice'])

def add_user(email,password,first_name,last_name,gender,age):
    user = PickeeUser.objects.create_user(email=email,
                                            password=password,
                                            first_name=first_name,
                                            last_name=last_name,
                                            gender=gender,
                                            age=age)

def add_actor(id, name, image_url):
    actor = Actor.objects.get_or_create(id=id, name=name, image_url=image_url)

def add_movie(id,name,image_url,rating,release_date,description):
    movie = Movie.objects.get_or_create(id=id,
                                        name=name,
                                        image_url=image_url,
                                        rating=rating,
                                        release_date=release_date,
                                        description=description)

def add_genre(id,name):
    genre = Genre.objects.get_or_create(id=id, name=name)

def add_favorite_actor(email,actor_id):
    favorite_actor = FavoriteActor.objects.get_or_create(user=PickeeUser.objects.get(email=email),
                                                        actor=Actor.objects.get(id=actor_id))

def add_favorite_movie(email,movie_id):
    favorite_movie = FavoriteMovie.objects.get_or_create(user=PickeeUser.objects.get(email=email),
                                                        movie=Movie.objects.get(id=movie_id))

def add_movie_cast(movie_id,actor_id):
    movie_cast = MovieCast.objects.get_or_create(movie=Movie.objects.get(id=movie_id),
                                                actor=Actor.objects.get(id=actor_id))

def add_favorite_genre(email,genre_id):
    favorite_genre = FavoriteGenre.objects.get_or_create(user=PickeeUser.objects.get(email=email),
                                                        genre=Genre.objects.get(id=genre_id))

def add_session(users):
    session = Session.objects.create()
    for user_email in users:
        session.users.add(PickeeUser.objects.get(email=user_email))

def add_recommendation(movie_id,session_id,user_choice):
    recommendation = Recommendation.objects.get_or_create(movie=Movie.objects.get(id=movie_id),
                                                        session=Session.objects.get(id=session_id),
                                                        user_choice=user_choice)

if __name__=='__main__':
    print('Starting Pickee population script...')
    populate()