from app import app
from flask import render_template, request
from .forms import LoginForm, SignUpForm
from .models import db, User

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/signup", methods=["GET", "POST"])
def signup_page():
    form = SignUpForm()
    if request.method == 'POST':
        print("POST REQUEST MADE!")
        if form.validate():
            pokemon_name = form.username.data
            email = form.email.data
            password = form.password.data

            # does a user with that username already exist?
            # does a user with that email already exist?

            user = User(pokemon_name, email, password)
            
            db.session.add(user)
            db.session.commit()


        else:
            print("FORM INVALID! :(")

    return render_template('signup.html', form=form)



@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    small_dictionary = None

    if request.method == 'POST':
        if form.validate():
            #username = form.username.data
            #password = form.password.data
            pokemon_name = form.pokemon_name.data


            small_dictionary = {'name': 'Pikachu', 'ability': 'Thunder Shock'}

            return redirect(url_for('display_pokemon', name=pokemon_name))

        return render_template('login.html', form=form, pokemon=small_dictionary)

    return render_template('login.html', form=form, pokemon=small_dictionary)





           













