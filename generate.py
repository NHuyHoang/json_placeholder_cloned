import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
django.setup()

from api.v1.models.staff import Staff
from api.v1.models.company import Company
from api.v1.models.user import User
from api.v1.models.post import Post
from api.v1.models.comment import Comment
from faker.providers import lorem, date_time, person, person, phone_number
from faker import Faker
from random import randint



fake = Faker()
fake.add_provider(lorem)
fake.add_provider(date_time)


def generate():
    print(gen_post())


def ran_user():
    users = User.objects.all()
    return users[randint(0, len(users) - 1)]


def ran_company():
    companies = Company.objects.all()
    return companies[randint(0, len(companies) - 1)]


def gen_user():
    username = fake.user_name()
    password = 'huyhoang123'
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.ascii_email()
    phone = fake.phone_number()

    user = User(username=username, password=password,
                first_name=first_name, last_name=last_name, email=email)
    user.save()

    company = ran_company()
    Staff.objects.create(companies=user, company_staff=company,)
   # company.staffs.add(user)

    print(user)


def gen_post():
    title = fake.sentence(nb_words=5,)
    body = fake.text(max_nb_chars=randint(500, 700), ext_word_list=None)
    author = ran_user()

    post = Post(title=title, body=body, author=author)
    post.save()

    for i in range(randint(2, 7)):
        gen_comment(post)

    print(post)

    # return (title,body,author)


def gen_comment(post):
    message = fake.sentence(nb_words=randint(6, 16),)
    date_add = fake.date_time_between(
        start_date="-2month", end_date="+2month", tzinfo=None)
    user = ran_user()
    comment = Comment(message=message, date_add=date_add, user=user, post=post)
    comment.save()


if __name__ == '__main__':
    print('populating script!')
    # populate process
    for i in range(1000):
       gen_post()
    print('populating complete')
