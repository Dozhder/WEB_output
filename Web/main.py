from flask import Flask, request, make_response
from data import db_session
from data.users import User
from data.jobs import Jobs
import datetime as dt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init('db/data_test.sqlite3')

db_sess = db_session.create_session()

user = User()
user.surname = 'Scott'
user.name = 'Ridley'
user.age = 21
user.position = 'captain'
user.speciality = 'research engineer'
user.address = 'module_1'
user.email = 'scott_chief@mars.org'
db_sess.add(user)
user_2 = User()
user_2.surname = 'Sparrow'
user_2.name = 'Jack'
user_2.age = 42
user_2.position = 'captain of Black Pearl'
user_2.speciality = 'research engineer'
user_2.address = 'module_2'
user_2.email = 'sparrow@mars.org'
db_sess.add(user_2)
user_3 = User()
user_3.surname = 'Johns'
user_3.name = 'Davi'
user_3.age = 500
user_3.position = 'captain of The Flying Dutchman'
user_3.speciality = 'research engineer'
user_3.address = 'module_3'
user_3.email = 'johns_chief@mars.org'
db_sess.add(user_3)
user_4 = User()
user_4.surname = 'Scott'
user_4.name = 'Bill'
user_4.age = 500
user_4.position = 'boatswain'
user_4.speciality = 'research engineer'
user_4.address = 'module_1'
user_4.email = 'billi_scott@mars.org'
db_sess.add(user_4)
# job = Jobs()
# job.team_leader =  1
# job.job = 'deployment of residential modules 1 and 2'
# job.work_size = 15
# job.collaborators = '2, 3'
# job.is_finished = False
# db_sess.add(job)
db_sess.commit()


def main():
    pass
    # app.run(host='127.0.0.1', port='8080')


@app.route('/test')
def test():
    return 'Good'


@app.route('/')
def home():
    return 'Good'


@app.route("/cookie_test")
def cookie_test():
    visits_count = int(request.cookies.get("visits_count", 0))
    if visits_count:
        res = make_response(
            f"Вы пришли на эту страницу {visits_count + 1} раз")
        res.set_cookie("visits_count", str(visits_count + 1),
                       max_age=60 * 60 * 24 * 365 * 2)
    else:
        res = make_response(
            "Вы пришли на эту страницу в первый раз за последние 2 года")
        res.set_cookie("visits_count", '1',
                       max_age=60 * 60 * 24 * 365 * 2)
    return res


if __name__ == '__main__':
    main()
