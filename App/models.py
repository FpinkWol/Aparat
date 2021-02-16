class User:
    username = CharField(max_length=100)
    firstname = CharField(max_length=100)
    lastname = CharField(max_length=100)
    province = CharField(max_length=100)
    city = CharField(max_length=100)
    email = EmailField()
    phone_no = InegerField()


class Follow:
    follower = ForeginKey(User)
    folloing = ForeginKey(User)

    class Meta:
        unique_together = ((follower, folloing),)


class PlayList:
    title = CharField(max_length=100)
    user = ForeginKey(User)


class Category:
    title = CharField(max_length=100)


class Film:
    _quality = [
            ('High', '1080'),
            ('Medium', '720'),
            ('Low', '240'),
        ]
    title = CharField(max_length=100)
    duration = CharField(max_length=100)
    quality = ChoiceField(_quality)
    playlist = ForeginKey(PlayList)
    user = ForeginKey(User)
    category = ForeginKey(Category)
    
    
class Comment:
    body = TextField()
    film = ForeginKey(Film)
    user = ForeginKey(User)


class Like:
    user = ForeginKey(User)
    film = ForeginKey(Film)

    class Meta:
        unique_together((user, film),)


class View:
    user = ForeginKey(User)
    film = ForeginKey(Film)
    
    class Meta:
        unique_together = ((user, film),)
