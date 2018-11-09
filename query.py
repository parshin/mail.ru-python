from datetime import datetime

from django.db.models import Q, Count, Avg
from pytz import UTC

from db.models import User, Blog, Topic


def create():
    # Создать пользователя first_name = u1, last_name = u1.
    u1 = User(first_name='u1', last_name='u1')
    u1.save()

    # Создать пользователя first_name = u2, last_name = u2.
    u2 = User(first_name='u2', last_name='u2')
    u2.save()

    # Создать пользователя first_name = u3, last_name = u3.
    u3 = User(first_name='u3', last_name='u3')
    u3.save()

    # Создать блог title = blog1, author = u1.
    blog1 = Blog(title='blog1', author='u1')
    blog1.save()

    # Создать блог title = blog2, author = u1.
    blog2 = Blog(title='blog2', author='u1')
    blog2.save()

    # Подписать пользователей u1 u2 на blog1, u2 на blog2.
    blog1.subscribers.add(u1)
    blog1.subscribers.add(u2)
    blog2.subscribers.add(u2)

    # Создать топик title = topic1, blog = blog1, author = u1.
    topic1 = Topic(title='topic1', blog=blog1, author=u1)

    # Создать топик title = topic2_content, blog = blog1, author = u3, created = 2017-01-01.
    topic2_content = Topic(title='topic2_content', blog=blog1, author=u3, created='2017-01-01')

    # Лайкнуть topic1 пользователями u1, u2, u3.
    topic1.likes.add(u1)
    topic1.likes.add(u2)
    topic1.likes.add(u3)


def edit_all():
    # Поменять first_name на uu1 у всех пользователей(функция edit_all).
    all_users = User.objects.all()
    for user in all_users:
        user.first_name = 'uu1'
        user.save()


def edit_u1_u2():
    # Поменять first_name на uu1 у пользователей, у которых first_name u1 или u2(функция edit_u1_u2).
    users = User.objects.filter(Q(first_name='u1')|Q(first_name='u2'))
    for user in users:
        user.first_name = 'uu1'
        user.save()


def delete_u1():
    # удалить пользователя с first_name u1(функция delete_u1).
    User.objects.filter(first_name='u1').delete()


def unsubscribe_u2_from_blogs():
    # отписать пользователя с first_name u2 от блогов(функция unsubscribe_u2_from_blogs).
    Blog.objects.filter(subscribers__name='u2').delete()


def get_topic_created_grated():
    #Найти топики у которых дата создания больше 2018-01-01
    return Topic.objectd.filter(created__gt='2018-01-01')


def get_topic_title_ended():
    #Найти топик у которого title заканчивается на content
    return Topic.objects.filter(title__endswith='content')


def get_user_with_limit():
    #Получить 2х первых пользователей (сортировка в обратном порядке по id)
    User.objects.all()[:-2]


def get_topic_count():
    #Получить количество топиков в каждом блоге, назвать поле topic_count, отсортировать по topic_count по возрастанию


def get_avg_topic_count():
    pass


def get_blog_that_have_more_than_one_topic():
    pass


def get_topic_by_u1():
    pass


def get_user_that_dont_have_blog():
    pass


def get_topic_that_like_all_users():
    pass


def get_topic_that_dont_have_like():
    pass
