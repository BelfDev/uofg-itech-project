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
    {'id':2,'name':'Mark Hamill','image_url':'https://image.tmdb.org/t/p/w500/fk8OfdReNltKZqOk2TZgkofCUFq.jpg'},
    {'id':3,'name':'Harrison Ford','image_url':'https://image.tmdb.org/t/p/w500/5M7oN3sznp99hWYQ9sX0xheswWX.jpg'},
    {'id':4,'name':'Carrie Fisher','image_url':'https://image.tmdb.org/t/p/w500/rfJtncHewKVnHjqpIZvjn24ESeC.jpg'},
    {'id':31,'name':'Tom Hanks','image_url':'https://image.tmdb.org/t/p/w500/2gY92j2lkNHL2cThBhPmgXLd5PL.jpg'},
    {'id':85,'name':'Johnny Depp','image_url':'https://image.tmdb.org/t/p/w500/kbWValANhZI8rbWZXximXuMN4UN.jpg'},
    {'id':204,'name':'Kate Winslet','image_url':'https://image.tmdb.org/t/p/w500/e3tdop3WhseRnn8KwMVLAV25Ybv.jpg'},
    {'id':287,'name':'Brad Pitt','image_url':'https://image.tmdb.org/t/p/w500/kU3B75TyRiCgE270EyZnHjfivoq.jpg'},
    {'id':380,'name':'Robert De Niro','image_url':'https://image.tmdb.org/t/p/w500/lvTSwUcvJRLAJ2FB5qFaukel516.jpg'},
    {'id':500,'name':'Tom Cruise','image_url':'https://image.tmdb.org/t/p/w500/2Dkx4uuGoWFrPSitxdikv9z5azR.jpg'},
    {'id':192,'name':'Morgan Freeman','image_url':'https://image.tmdb.org/t/p/w500/oIciQWr8VwKoR8TmAw1owaiZFyb.jpg'},
    {'id':934,'name':'Russell Crowe','image_url':'https://image.tmdb.org/t/p/w500/tZCbQwF5btUvutbc3AjJKPzrJV7.jpg'},
    {'id':1204,'name':'Julia Roberts','image_url':'https://image.tmdb.org/t/p/w500/h13yvG0tRNMTAwciQXxYmQWdYW8.jpg'},
    {'id':1245,'name':'Scarlett Johansson','image_url':'https://image.tmdb.org/t/p/w500/6NsMbJXRlDZuDzatN2akFdGuTvx.jpg'},
    {'id':1461,'name':'George Clooney','image_url':'https://image.tmdb.org/t/p/w500/kHiVY6r1k6juXrNetAYk2jILqn9.jpg'},
    {'id':1892,'name':'Matt Damon','image_url':'https://image.tmdb.org/t/p/w500/elSlNgV8xVifsbHpFsqrPGxJToZ.jpg'},
    {'id':2157,'name':'Robin Williams','image_url':'https://image.tmdb.org/t/p/w500/3vypmub75rLItlC51uJUurNYkW0.jpg'},
    {'id':2227,'name':'Nicole Kidman','image_url':'https://image.tmdb.org/t/p/w500/t1HaRL7lRJemWySXcXxOT8fAGhj.jpg'},
    {'id':2231,'name':'Samuel L. Jackson','image_url':'https://image.tmdb.org/t/p/w500/qjYcO8jKNlb7lnJ05vh2U7lNt8r.jpg'},
    {'id':2888,'name':'Will Smith','image_url':'https://image.tmdb.org/t/p/w500/eze9FO9VuryXLP0aF2cRqPCcibN.jpg'},
    {'id':3896,'name':'Liam Neeson','image_url':'https://image.tmdb.org/t/p/w500/r1DRqmZhLrzhTTwg9PtuMMQTvuB.jpg'},
    {'id':4491,'name':'Jennifer Aniston','image_url':'https://image.tmdb.org/t/p/w500/uH9FwXtRpiboKeqHUk0RuJRAm6I.jpg'},
    {'id':5064,'name':'Meryl Streep','image_url':'https://image.tmdb.org/t/p/w500/xqL5IJxV0fDeD3OfkS3eWqwJoGV.jpg'},
    {'id':5309,'name':'Judi Dench','image_url':'https://image.tmdb.org/t/p/w500/cpna5VGvAxuKuC31xJPBKy9zbnv.jpg'},
    {'id':6193,'name':'Leonardo DiCaprio','image_url':'https://image.tmdb.org/t/p/w500/wo2hJpn04vbtmh0B9utCFdsQhxM.jpg'},
    {'id':11701,'name':'Angelina Jolie','image_url':'https://image.tmdb.org/t/p/w500/gD8jlGkQC8GBajulNlIzBK1YEO1.jpg'},
    {'id':15735,'name':'Helen Mirren','image_url':'https://image.tmdb.org/t/p/w500/1reKRrsdsHXJaRVHVyOEg4oPTcZ.jpg'},
    {'id':72129,'name':'Jennifer Lawrence','image_url':'https://image.tmdb.org/t/p/w500/q0tf3XEo7wa8XglIznTC7WzZ9W3.jpg'},
    {'id':74568,'name':'Chris Hemsworth','image_url':'https://image.tmdb.org/t/p/w500/tlkDiLn2G75Xr7m1ybK8QFzZBso.jpg'},
    {'id':84223,'name':'Anna Kendrick','image_url':'https://image.tmdb.org/t/p/w500/5ZYBQefB30uWObRzin8R0PYqenh.jpg'}
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
    {'id':301528,'name':'Toy Story 4','image_url':'https://image.tmdb.org/t/p/w500/w9kR8qbmQ01HwnvK4alvnQ2ca0L.jpg','rating':7.5,'release_date':datetime.date(2019,6,19),
        'description':'''Woody has always been confident about his place in the world and that his priority is taking 
        care of his kid, whether that's Andy or Bonnie. But when Bonnie adds a reluctant new toy called \"Forky\" 
        to her room, a road trip adventure alongside old and new friends will show Woody how big the world can be 
        for a toy.'''},
    {'id':27205,'name':'Inception','image_url':'https://image.tmdb.org/t/p/w500/qmDpIHrmpJINaRKAfWQfftjCdyi.jpg','rating':8.3,'release_date':datetime.date(2010,7,15),
        'description':'''Cobb, a skilled thief who commits corporate espionage by infiltrating the subconscious of 
        his targets is offered a chance to regain his old life as payment for a task considered to be impossible: 
        \"inception\", the implantation of another person's idea into a target's subconscious.'''},
    {'id':284053,'name':'Thor:Ragnarok','image_url':'https://image.tmdb.org/t/p/w500/rzRwTcFvttcN1ZpX2xv4j3tSdJu.jpg','rating':7.5,'release_date':datetime.date(2017,10,25),
        'description':'''Thor is imprisoned on the other side of the universe and finds himself in a race against 
        time to get back to Asgard to stop Ragnarok, the destruction of his home-world and the end of Asgardian 
        civilization, at the hands of an all-powerful new threat, the ruthless Hela.'''},
    {'id':10184,'name':'He\'s Just Not That Into You','rating':6.4,'image_url':'https://image.tmdb.org/t/p/w500/ruc33YnCrmCL8PHdPQVzfa4shWX.jpg','release_date':datetime.date(2009,2,6),
        'description':'''Remember that really cute girl/guy who said they'd call – and didn't? Maybe they lost your 
        number. Maybe they're in the hospital. Maybe they're awed by your looks, brains or success. Or maybe... 
        They're just not that into you.'''},
    {'id':102651,'name':'Maleficent','image_url':'https://image.tmdb.org/t/p/w500/1cFVCUYKSBuEUDoVftKvqcfuIgc.jpg','rating':7.1,'release_date':datetime.date(2014,5,28),
        'description':'''A beautiful, pure-hearted young woman, Maleficent has an idyllic life growing up in a 
        peaceable forest kingdom, until one day when an invading army threatens the harmony of the land.  Maleficent 
        rises to be the land's fiercest protector, but she ultimately suffers a ruthless betrayal – an act that 
        begins to turn her heart into stone. Bent on revenge, Maleficent faces an epic battle with the invading 
        King's successor and, as a result, places a curse upon his newborn infant Aurora. As the child grows, 
        Maleficent realizes that Aurora holds the key to peace in the kingdom – and to Maleficent's true happiness 
        as well.'''},
    {'id':114150,'name':'Pitch Perfect','image_url':'https://image.tmdb.org/t/p/w500/qSjruLiFB4uqRtz2xheQPxG8uaB.jpg','rating':7.3,'release_date':datetime.date(2012,9,28),
        'description':'''College student Beca knows she does not want to be part of a clique, but that's exactly 
        where she finds herself after arriving at her new school. Thrust in among mean gals, nice gals and just 
        plain weird gals, Beca finds that the only thing they have in common is how well they sing together. She 
        takes the women of the group out of their comfort zone of traditional arrangements and into a world of 
        amazing harmonic combinations in a fight to the top of college music competitions.'''},
    {'id':278,'name':'The Shawshank Redemption','image_url':'https://image.tmdb.org/t/p/w500/9O7gLzmreU0nGkIB6K3BsJbzvNv.jpg','rating':8.7,'release_date':datetime.date(1994,9,23),
        'description':'''Framed in the 1940s for the double murder of his wife and her lover, upstanding banker Andy 
        Dufresne begins a new life at the Shawshank prison, where he puts his accounting skills to work for an 
        amoral warden. During his long stretch in prison, Dufresne comes to be admired by the other inmates -- 
        including an older prisoner named Red -- for his integrity and unquenchable sense of hope.'''},
    {'id':5255,'name':'The Polar Express','image_url':'https://image.tmdb.org/t/p/w500/2NETsNUxcfBdKtq3W5YbT9O03Ak.jpg','rating':6.6,'release_date':datetime.date(2004,11,10),
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
    {'id':8999,'name':'Derailed','rating':6.2,'image_url':'https://image.tmdb.org/t/p/w500/inBGQGHUUFAmt9nINRAdTUBkmQN.jpg','release_date':datetime.date(2005,11,11),
        'description':'''When two married business executives having an affair are blackmailed by a violent criminal, 
        they are forced to turn the tables on him to save their families.'''},
    {'id':393624,'name':'Official Secrets','image_url':'https://image.tmdb.org/t/p/w500/lyCGqSkT3PqLYQXiWs4FCVJBAYW.jpg','rating':7.3,'release_date':datetime.date(2019,8,30),
        'description':'''The true story of British intelligence whistleblower Katharine Gun who—prior to the 2003 
        Iraq invasion—leaked a top-secret NSA memo exposing a joint US-UK illegal spying operation against members 
        of the UN Security Council. The memo proposed blackmailing member states into voting for war.'''},
    {'id':181812,'name':'Star Wars: The Rise of Skywalker','image_url':'https://image.tmdb.org/t/p/w500/db32LaOibwEliAmSL2jjDF6oDdj.jpg','rating':6.5,'release_date':datetime.date(2019,12,18),
        'description':'''The surviving Resistance faces the First Order once again as the journey of Rey, Finn and 
        Poe Dameron continues. With the power and knowledge of generations behind them, the final battle begins.'''},
    {'id':11,'name':'Star Wars','image_url':'https://image.tmdb.org/t/p/w500/btTdmkgIvOi0FFip1sPuZI2oQG6.jpg','rating':8.2,'release_date':datetime.date(1977,5,25),
        'description':'''Princess Leia is captured and held hostage by the evil Imperial forces in their effort to 
        take over the galactic Empire. Venturesome Luke Skywalker and dashing captain Han Solo team together with the 
        loveable robot duo R2-D2 and C-3PO to rescue the beautiful princess and restore peace and justice in the Empire.'''},
    {'id':475557,'name':'Joker','image_url':'https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg','rating':8.2,'release_date':datetime.date(2019,10,2),
        'description':'''During the 1980s, a failed stand-up comedian is driven insane and turns to a life of crime 
        and chaos in Gotham City while becoming an infamous psychopathic crime figure.'''},
    {'id':22,'name':'Pirates of the Caribbean: The Curse of the Black Pearl','image_url':'https://image.tmdb.org/t/p/w500/tkt9xR1kNX5R9rCebASKck44si2.jpg','rating':7.7,'release_date':datetime.date(2003,7,9),
        'description':'''Jack Sparrow, a freewheeling 18th-century pirate, quarrels with a rival pirate bent on pillaging 
        Port Royal. When the governor's daughter is kidnapped, Sparrow decides to help the girl's love save her.'''},
    {'id':392044,'name':'Murder on the Orient Express','image_url':'https://image.tmdb.org/t/p/w500/iBlfxlw8qwtUS0R8YjIU7JtM6LM.jpg','rating':6.7,'release_date':datetime.date(2017,11,3),
        'description':'''Genius Belgian detective Hercule Poirot investigates the murder of an American tycoon aboard the Orient Express train.'''},
    {'id':398978,'name':'The Irishman','image_url':'https://image.tmdb.org/t/p/w500/mbm8k3GFhXS0ROd9AD1gqYbIFbM.jpg','rating':7.8,'release_date':datetime.date(2019,11,1),
        'description':'''Pennsylvania, 1956. Frank Sheeran, a war veteran of Irish origin who works as a truck driver, 
        accidentally meets mobster Russell Bufalino. Once Frank becomes his trusted man, Bufalino sends him to Chicago 
        with the task of helping Jimmy Hoffa, a powerful union leader related to organized crime, with whom Frank will 
        maintain a close friendship for nearly twenty years.'''},
    {'id':597,'name':'Titanic','image_url':'https://image.tmdb.org/t/p/w500/kHXEpyfl6zqn8a6YuozZUujufXf.jpg','rating':7.8,'release_date':datetime.date(1997,11,18),
        'description':'''101-year-old Rose DeWitt Bukater tells the story of her life aboard the Titanic, 84 years later. 
        A young Rose boards the ship with her mother and fiancé. Meanwhile, Jack Dawson and Fabrizio De Rossi win third-class 
        tickets aboard the ship. Rose tells the whole story from Titanic's departure through to its death—on its first and 
        last voyage—on April 15, 1912.'''},
    {'id':550,'name':'Fight Club','image_url':'https://image.tmdb.org/t/p/w500/4GpwvwDjgwiShr1UBJIn5fk1gwT.jpg','rating':8.4,'release_date':datetime.date(1999,10,15),
        'description':'''A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a 
        shocking new form of therapy. Their concept catches on, with underground \"fight clubs\" forming in every town, 
        until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion.'''},
    {'id':259316,'name':'Fantastic Beasts and Where to Find Them','image_url':'https://image.tmdb.org/t/p/w500/1M91Bt3oGspda75H9eLqYZkJzgO.jpg','rating':7.4,'release_date':datetime.date(2016,11,16),
        'description':'''In 1926, Newt Scamander arrives at the Magical Congress of the United States of America with a 
        magically expanded briefcase, which houses a number of dangerous creatures and their habitats. When the creatures 
        escape from the briefcase, it sends the American wizarding authorities after Newt, and threatens to strain even 
        further the state of magical and non-magical relations.'''},
    {'id':954,'name':'Mission: Impossible','image_url':'https://image.tmdb.org/t/p/w500/1PVKS17pIBFsIhgFws2uagPDNLW.jpg','rating':6.9,'release_date':datetime.date(1996,5,22),
        'description':'''When Ethan Hunt, the leader of a crack espionage team whose perilous operation has gone awry with 
        no explanation, discovers that a mole has penetrated the CIA, he's surprised to learn that he's the No. 1 suspect. 
        To clear his name, Hunt now must ferret out the real double agent and, in the process, even the score.'''},
    {'id':769,'name':'GoodFellas','image_url':'https://image.tmdb.org/t/p/w500/pwpGfTImTGifEGgLb3s6LRPd4I6.jpg','rating':8.4,'release_date':datetime.date(1990,9,12),
        'description':'''The true story of Henry Hill, a half-Irish, half-Sicilian Brooklyn kid who is adopted by neighbourhood 
        gangsters at an early age and climbs the ranks of a Mafia family under the guidance of Jimmy Conway.'''},
    {'id':299536,'name':'Avengers: Infinity War','image_url':'https://image.tmdb.org/t/p/w500/7WsyChQLEftFiDOVTGkv3hFpyyt.jpg','rating':8.3,'release_date':datetime.date(2018,4,25),
        'description':'''As the Avengers and their allies have continued to protect the world from threats too large for any 
        one hero to handle, a new danger has emerged from the cosmic shadows: Thanos. A despot of intergalactic infamy, his 
        goal is to collect all six Infinity Stones, artifacts of unimaginable power, and use them to inflict his twisted will 
        on all of reality. Everything the Avengers have fought for has led up to this moment - the fate of Earth and existence 
        itself has never been more uncertain.'''},
    {'id':299537,'name':'Captain Marvel','image_url':'https://image.tmdb.org/t/p/w500/AtsgWhDnHTq68L0lLsUrCnM7TjG.jpg','rating':7.0,'release_date':datetime.date(2019,3,6),
        'description':'''The story follows Carol Danvers as she becomes one of the universe’s most powerful heroes when Earth 
        is caught in the middle of a galactic war between two alien races. Set in the 1990s, Captain Marvel is an all-new 
        adventure from a previously unseen period in the history of the Marvel Cinematic Universe.'''},
    {'id':157336,'name':'Interstellar','image_url':'https://image.tmdb.org/t/p/w500/nBNZadXqJSdt05SHLqgT0HuC5Gm.jpg','rating':8.3,'release_date':datetime.date(2014,11,5),
        'description':'''Interstellar chronicles the adventures of a group of explorers who make use of a newly discovered 
        wormhole to surpass the limitations on human space travel and conquer the vast distances involved in an interstellar 
        voyage.'''},
    {'id':286217,'name':'The Martian','image_url':'https://image.tmdb.org/t/p/w500/5aGhaIHYuQbqlHWvWYqMCnj40y2.jpg','rating':7.7,'release_date':datetime.date(2015,9,30),
        'description':'''During a manned mission to Mars, Astronaut Mark Watney is presumed dead after a fierce storm and 
        left behind by his crew. But Watney has survived and finds himself stranded and alone on the hostile planet. With 
        only meager supplies, he must draw upon his ingenuity, wit and spirit to subsist and find a way to signal to Earth 
        that he is alive.'''},
    {'id':857,'name':'Saving Private Ryan','image_url':'https://image.tmdb.org/t/p/w500/gc7IN6bWNaWXv4vI6cxSmeB7PeO.jpg','rating':8.1,'release_date':datetime.date(1998,7,24),
        'description':'''As U.S. troops storm the beaches of Normandy, three brothers lie dead on the battlefield, with a 
        fourth trapped behind enemy lines. Ranger captain John Miller and seven men are tasked with penetrating German-held 
        territory and bringing the boy home.'''},
    {'id':158852,'name':'Tomorrowland','image_url':'https://image.tmdb.org/t/p/w500/69Cz9VNQZy39fUE2g0Ggth6SBTM.jpg','rating':6.2,'release_date':datetime.date(2015,5,19),
        'description':'''Bound by a shared destiny, a bright, optimistic teen bursting with scientific curiosity and a former 
        boy-genius inventor jaded by disillusionment embark on a danger-filled mission to unearth the secrets of an enigmatic 
        place somewhere in time and space that exists in their collective memory as "Tomorrowland."'''},
    {'id':98,'name':'Gladiator','image_url':'https://image.tmdb.org/t/p/w500/6WBIzCgmDCYrqh64yDREGeDk9d3.jpg','rating':8.1,'release_date':datetime.date(2000,5,1),
        'description':'''In the year 180, the death of emperor Marcus Aurelius throws the Roman Empire into chaos.  Maximus is 
        one of the Roman army's most capable and trusted generals and a key advisor to the emperor.  As Marcus' devious son 
        Commodus ascends to the throne, Maximus is set to be executed.  He escapes, but is captured by slave traders.  Renamed 
        Spaniard and forced to become a gladiator, Maximus must battle to the death with other men for the amusement of paying 
        audiences.'''},
    {'id':161,'name':'Ocean\'s Eleven','image_url':'https://image.tmdb.org/t/p/w500/o0h76DVXvk5OKjmNez5YY0GODC2.jpg','rating':7.4,'release_date':datetime.date(2001,12,7),
        'description':'''Less than 24 hours into his parole, charismatic thief Danny Ocean is already rolling out his next plan: 
        In one night, Danny's hand-picked crew of specialists will attempt to steal more than $150 million from three Las Vegas 
        casinos. But to score the cash, Danny risks his chances of reconciling with ex-wife, Tess.'''},
    {'id':7451,'name':'xXx','image_url':'https://image.tmdb.org/t/p/w500/86BnliVDBo2TjKmrgQTJIPHxAKd.jpg','rating':5.9,'release_date':datetime.date(2002,8,9),
        'description':'''Xander Cage is your standard adrenaline junkie with no fear and a lousy attitude. When the US Government 
        \"recruits\" him to go on a mission, he's not exactly thrilled. His mission: to gather information on an organization that 
        may just be planning the destruction of the world, led by the nihilistic Yorgi.'''},
    {'id':420817,'name':'Aladdin','image_url':'https://image.tmdb.org/t/p/w500/3iYQTLGoy7QnjcUYRJy4YrAgGvp.jpg','rating':7.0,'release_date':datetime.date(2019,5,22),
        'description':'''A kindhearted street urchin named Aladdin embarks on a magical adventure after finding a lamp that releases 
        a wisecracking genie while a power-hungry Grand Vizier vies for the same lamp that has the power to make their deepest wishes 
        come true.'''},
    {'id':812,'name':'Aladdin','image_url':'https://image.tmdb.org/t/p/w500/mjKozYRuHc9j7SmiXmbVmCiAM0A.jpg','rating':7.6,'release_date':datetime.date(1992,11,25),
        'description':'''Princess Jasmine grows tired of being forced to remain in the palace, so she sneaks out into the marketplace, 
        in disguise, where she meets street-urchin Aladdin.  The couple falls in love, although Jasmine may only marry a prince.  After 
        being thrown in jail, Aladdin becomes embroiled in a plot to find a mysterious lamp, with which the evil Jafar hopes to rule the 
        land.'''},
    {'id':680,'name':'Pulp Fiction','image_url':'https://image.tmdb.org/t/p/w500/d5iIlFn5s0ImszYzBPb8JPIfbXD.jpg','rating':8.5,'release_date':datetime.date(1994,9,10),
        'description':'''A burger-loving hit man, his philosophical partner, a drug-addled gangster's moll and a washed-up boxer converge 
        in this sprawling, comedic crime caper. Their adventures unfurl in three stories that ingeniously trip back and forth in time.'''},
    {'id':68718,'name':'Django Unchained','image_url':'https://image.tmdb.org/t/p/w500/eCt596Z4zkqxW5AHz1HEhGm1eif.jpg','rating':8.1,'release_date':datetime.date(2012,12,25),
        'description':'''With the help of a German bounty hunter, a freed slave sets out to rescue his wife from a brutal Mississippi 
        plantation owner.'''},
    {'id':6479,'name':'I Am Legend','image_url':'https://image.tmdb.org/t/p/w500/9skUuHTFtsJznuFPwmB17ZZvq09.jpg','rating':7.1,'release_date':datetime.date(2007,12,14),
        'description':'''Robert Neville is a scientist who was unable to stop the spread of the terrible virus that was incurable and 
        man-made. Immune, Neville is now the last human survivor in what is left of New York City and perhaps the world. For three years, 
        Neville has faithfully sent out daily radio messages, desperate to find any other survivors who might be out there. But he is not 
        alone.'''},
    {'id':331482,'name':'Little Women','image_url':'https://image.tmdb.org/t/p/w500/mSmiB8XjUnR1GSIljuCPGsk0cwX.jpg','rating':8.0,'release_date':datetime.date(2019,12,25),
        'description':'''Four sisters come of age in America in the aftermath of the Civil War.'''},
    {'id':536869,'name':'Cats','image_url':'https://image.tmdb.org/t/p/w500/aCNch5FmzT2WaUcY44925owIZXY.jpg','rating':4.4,'release_date':datetime.date(2019,12,19),
        'description':'''A tribe of cats called the Jellicles must decide yearly which one will ascend to the Heaviside Layer and come 
        back to a new Jellicle life.'''},
    {'id':272,'name':'Batman Begins','image_url':'https://image.tmdb.org/t/p/w500/dr6x4GyyegBWtinPBzipY02J2lV.jpg','rating':7.6,'release_date':datetime.date(2005,6,10),
        'description':'''Driven by tragedy, billionaire Bruce Wayne dedicates his life to uncovering and defeating the corruption that 
        plagues his home, Gotham City.  Unable to work within the system, he instead creates a new identity, a symbol of fear for the 
        criminal underworld - The Batman.'''},
    {'id':36557,'name':'Casino Royale','image_url':'https://image.tmdb.org/t/p/w500/zlWBxz2pTA9p45kUTrI8AQiKrHm.jpg','rating':7.4,'release_date':datetime.date(2006,11,14),
        'description':'''Le Chiffre, a banker to the world's terrorists, is scheduled to participate in a high-stakes poker game in 
        Montenegro, where he intends to use his winnings to establish his financial grip on the terrorist market. M sends Bond—on his 
        maiden mission as a 00 Agent—to attend this game and prevent Le Chiffre from winning. With the help of Vesper Lynd and Felix 
        Leiter, Bond enters the most important poker game in his already dangerous career.'''},
    {'id':479455,'name':'Men in Black: International','image_url':'https://image.tmdb.org/t/p/w500/dPrUPFcgLfNbmDL8V69vcrTyEfb.jpg','rating':5.9,'release_date':datetime.date(2019,6,12),
        'description':'''The Men in Black have always protected the Earth from the scum of the universe. In this new adventure, they 
        tackle their biggest, most global threat to date: a mole in the Men in Black organization.'''},
    {'id':424,'name':'Schindler\'s List','image_url':'https://image.tmdb.org/t/p/w500/yPisjyLweCl1tbgwgtzBCNCBle.jpg','rating':8.6,'release_date':datetime.date(1993,11,30),
        'description':'''The true story of how businessman Oskar Schindler saved over a thousand Jewish lives from the Nazis while 
        they worked as slaves in his factory during World War II.'''},
    {'id':37724,'name':'Skyfall','image_url':'https://image.tmdb.org/t/p/w500/lQCkPLDxFONmgzrWLvq085v1g2d.jpg','rating':7.1,'release_date':datetime.date(2012,10,25),
        'description':'''When Bond's latest assignment goes gravely wrong and agents around the world are exposed, MI6 is attacked 
        forcing M to relocate the agency. These events cause her authority and position to be challenged by Gareth Mallory, the new 
        Chairman of the Intelligence and Security Committee. With MI6 now compromised from both inside and out, M is left with one 
        ally she can trust: Bond. 007 takes to the shadows - aided only by field agent, Eve - following a trail to the mysterious 
        Silva, whose lethal and hidden motives have yet to reveal themselves.'''},
    {'id':283366,'name':'Miss Peregrine\'s Home for Peculiar Children','image_url':'https://image.tmdb.org/t/p/w500/AvekzUdI8HZnImdQulmTTmAZXrC.jpg','rating':6.7,'release_date':datetime.date(2016,9,28),
        'description':'''A teenager finds himself transported to an island where he must help protect a group of orphans with special 
        powers from creatures intent on destroying them.'''},
    {'id':281957,'name':'The Revenant','image_url':'https://image.tmdb.org/t/p/w500/oXUWEc5i3wYyFnL1Ycu8ppxxPvs.jpg','rating':7.5,'release_date':datetime.date(2015,12,25),
        'description':'''In the 1820s, a frontiersman, Hugh Glass, sets out on a path of vengeance against those who left him for 
        dead after a bear mauling.'''},
    {'id':8966,'name':'Twilight','image_url':'https://image.tmdb.org/t/p/w500/lcMp3AONdNhjYE9MmTtMMTOiRDP.jpg','rating':6.0,'release_date':datetime.date(2008,11,20),
        'description':'''When Bella Swan moves to a small town in the Pacific Northwest to live with her father, she meets the 
        reclusive Edward Cullen, a mysterious classmate who reveals himself to be a 108-year-old vampire. Despite Edward's repeated 
        cautions, Bella can't help but fall in love with him, a fatal move that endangers her own life when a coven of bloodsuckers 
        try to challenge the Cullen clan.'''},
    {'id':70160,'name':'The Hunger Games','image_url':'https://image.tmdb.org/t/p/w500/iLJdwmzrHFjFwI5lvYAT1gcpRuA.jpg','rating':7.1,'release_date':datetime.date(2012,3,12),
        'description':'''Every year in the ruins of what was once North America, the nation of Panem forces each of its twelve districts 
        to send a teenage boy and girl to compete in the Hunger Games.  Part twisted entertainment, part government intimidation tactic, 
        the Hunger Games are a nationally televised event in which “Tributes” must fight with one another until one survivor remains.  
        Pitted against highly-trained Tributes who have prepared for these Games their entire lives, Katniss is forced to rely upon her 
        sharp instincts as well as the mentorship of drunken former victor Haymitch Abernathy.  If she’s ever to return home to District 
        12, Katniss must make impossible choices in the arena that weigh survival against humanity and life against love. The world will 
        be watching.'''},
    {'id':127585,'name':'X-Men: Days of Future Past','image_url':'https://image.tmdb.org/t/p/w500/pb1IURTkK5rImP9ZV83lxJO2us7.jpg','rating':7.5,'release_date':datetime.date(2014,5,15),
        'description':'''The ultimate X-Men ensemble fights a war for the survival of the species across two time periods as they join 
        forces with their younger selves in an epic battle that must change the past – to save our future.'''},
    {'id':62211,'name':'Monsters University','image_url':'https://image.tmdb.org/t/p/w500/a05xQU9huY3P5uurLcGGHmsf2Vh.jpg','rating':7.0,'release_date':datetime.date(2013,6,20),
        'description':'''A look at the relationship between Mike and Sulley during their days at Monsters University — when they weren't 
        necessarily the best of friends.'''},
    {'id':9502,'name':'Kung Fu Panda','image_url':'https://image.tmdb.org/t/p/w500/mk3UyyaLyXhgIhmLji25OUPXvGR.jpg','rating':7.1,'release_date':datetime.date(2008,6,4),
        'description':'''When the Valley of Peace is threatened, lazy Po the panda discovers his destiny as the \"chosen one\" and trains 
        to become a kung fu hero, but transforming the unsleek slacker into a brave warrior won't be easy. It's up to Master Shifu and the 
        Furious Five -- Tigress, Crane, Mantis, Viper and Monkey -- to give it a try.'''},
    {'id':168672,'name':'American Hustle','image_url':'https://image.tmdb.org/t/p/w500/mhB7C62lSMpGO2HYNaW6d7W3TVH.jpg','rating':6.8,'release_date':datetime.date(2013,12,12),
        'description':'''A conman and his seductive partner are forced to work for a wild FBI agent, who pushes them into a world of Jersey 
        power-brokers and the Mafia.'''}
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