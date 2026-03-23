from flask import Flask, request, make_response, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs
import datetime as dt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init('db/data_test.sqlite3')


def main():
    pass
    app.run(host='127.0.0.1', port='8080')


@app.route('/test')
def test():
    return 'Good'


@app.route('/')
def home():
    db_sess = db_session.create_session()
    render = ["""<p style="text-color: gray">И на марсе будут ябкони цвести</p>
                <h1 style="text-align: center">Works Log</h1>"""]
    for job in db_sess.query(Jobs).all():
        render.append(render_template('work_log.html', id_action=job.id, title_activity=job.job,
                               teamlead=job.team_leader, duration=job.work_size,
                               list_of_collaboration=job.collaborators, is_finished=job.is_finished))
    return '<br>'.join(render)


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
