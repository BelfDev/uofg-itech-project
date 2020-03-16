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
    {'email':'rhys@email.com','first_name':'Rhys','last_name':'Stephens','gender':'MALE','age':23,
        'password':'rhyspassword'},
    {'email':'pedro@email.com','first_name':'Pedro','last_name':'Belfort','gender':'MALE','age':42,
        'password':'pedropassword'},
    {'email':'nathan@email.com','first_name':'Nathan','last_name':'Schneddy','gender':'MALE','age':23,
        'password':'nathanpassword'},
    {'email':'anton@email.com','first_name':'Anton','last_name':'Samoilov','gender':'MALE','age':19,
        'password':'antonpassword'},
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
        Red -- for his integrity and unquenchable sense of hope.'''},
    {'movie_id':5255,'name':'The Polar Express','picture':None,'rating':66,'release_date':datetime.date(2004,11,10),
    'decription':'''When a doubting young boy takes an extraordinary train ride to the North Pole, he embarks on a 
        journey of self-discovery that shows him that the wonder of life never fades for those who believe.'''},
    {'movie_id':32407,'name':'Malice In Wonderland','picture':None,'rating':57,'release_date':datetime.date(2009,1,1),
    'decription':'''A modern take on the classic fairytale, Alice in Wonderland, set in South East England.An American 
        law student in London. Knocked down by a black cab, she wakes with amnesia in a world that's a million miles 
        from home - Wonderland. We follow her adventures as she's dragged through an underworld filled with twisted 
        individuals and the lowest low-lifers, by the enigmatic cab driver, Whitey. She needs to find out who she is, 
        where she's from and use what wits she has left to get back home in one piece. As her journey progresses she 
        discovers nothing is what it seems, realizes that fate and life are terminally entwined, and finds true love 
        lurking in the unlikeliest place.'''},
    {'movie_id':8999,'name':'Derailed','picture':None,'rating':62,'release_date':datetime.date(2005,11,11),
    'decription':'''When two married business executives having an affair are blackmailed by a violent 
        criminal, they are forced to turn the tables on him to save their families.'''},
    {'movie_id':393624,'name':'Official Secrets','picture':None,'rating':73,'release_date':datetime.date(2019,8,30),
    'decription':'''The true story of British intelligence whistleblower Katharine Gun who—prior to the 2003 Iraq 
        invasion—leaked a top-secret NSA memo exposing a joint US-UK illegal spying operation against members of 
        the UN Security Council. The memo proposed blackmailing member states into voting for war.'''}
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
    {'username':'rhys','genre_id':16},
    {'username':'rhys','genre_id':14},
    {'username':'pedro','genre_id':28},
    {'username':'pedro','genre_id':10402},
    {'username':'nathan','genre_id':18},
    {'username':'nathan','genre_id':53},
    {'username':'anton','genre_id':10749},
    {'username':'anton','genre_id':80},
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
    {'movie_id':5255,'session_id':1,'user_choice':'ACCEPTED'},
    {'movie_id':32407,'session_id':2,'user_choice':'ACCEPTED'},
    {'movie_id':8999,'session_id':3,'user_choice':'REJECTED'},
    {'movie_id':393624,'session_id':4,'user_choice':'BOOKMARKED'}
]

sessions = [
    {'users':{'rhys','pedro'}},
    {'users':{'rhys','pedro','nathan','anton'}},
    {'users':{'nathan'}},
    {'users':{'nathan','anton'}}
]

def populate():
    for user in users:
        add_user(user['username'],user['password'],user['email'],user['first_name'],user['last_name'],
                    user['picture'],user['avatar'],user['gender'],user['age'],user['associated_users'])
    
    for actor in actors:
        add_actor(actor['person_id'],actor['name'],actor['picture'])
    
    for movie in movies:
        add_movie(movie['movie_id'],movie['name'],movie['picture'],movie['rating'],movie['release_date'],
                    movie['description'])
    
    for genre in genres:
        add_genre(genre['genre_id'],genre['name'])
    
    for actor in favorite_actors:
        add_favorite_actor(actor['username']),actor['actor_id']
    
    for movie in favorite_movies:
        add_favorite_movie(movie['username'],movie['movie_id'])
    
    for actor in movie_casts:
        add_movie_cast(actor['movie_id'],actor['actor_id'])
    
    for genre in favorite_genres:
        add_favorite_genre(genre['username'],genre['genre_id'])
    
    for session in sessions:
        add_session(session['users'])
    
    for recommendation in recommendations:
        add_recommendation(recommendation['movie_id'],recommendation['session_id'],recommendation['user_choice'])
    
    for user in UserProfile.objects.all():
        for actor in Actor.objects.filter(user=user):
            print(f'- {user}: {actor}')
        for movie in Movie.objects.filter(user=user):
            print(f'- {user}: {movie}')

def add_user(username,password,email,first_name,last_name,picture,avatar,gender,age,associated_users):
    user = UserProfile.objects.get_or_create(user=User.objects.create_user(username,None,password),
                                            email=email,
                                            first_name=first_name,
                                            last_name=last_name,
                                            picture=picture,
                                            avatar=avatar,
                                            gender=gender,
                                            age=age)

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

def add_movie_cast(movie_id,actor_id):
    movie_cast = MovieCast.objects.get_or_create(movie=Movie.objects.get(movie_id=movie_id),
                                                actor=Actor.objects.get(person_id=actor_id))

def add_favorite_genre(username,genre_id):
    favorite_genre = FavoriteGenre.objects.get_or_create(user=User.objects.get(username=username),
                                                        genre=Genre.objects.get(genre_id=genre_id))

def add_session(users):
    session = Session.objects.create()
    for user in users:
        session.users.add(user=User.objects.get(username=user))

def add_recommendation(movie_id,session_id,user_choice):
    recommendation = Recommendation.objects.get_or_create(movie=Movie.objects.get(movie_id=movie_id),
                                                        session=Session.objects.get(id=session_id),
                                                        user_choice=user_choice)

if __name__=='__main__':
    print('Starting Pickee population script...')
    populate()