from flask import Flask, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm
from secrets import ACCESS_TOKEN
import requests

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoptionAgency' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_ECHO'] = True 
app.config['SECRET_KEY'] = "Secret_key"

toolbar = DebugToolbarExtension(app)
connect_db(app)
db.create_all()

@app.route('/')
def home_page():
    pets = Pet.query.all()

    # headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}

    resp = requests.get(
            "https://api.petfinder.com/v2/animals", 
            headers={'Authorization': f'Bearer {ACCESS_TOKEN}'}
       )

    response = resp.json()

    animals = response["animals"]


    pf_name = animals[0]["name"]
    pf_photo = animals[0]["photos"][0]["medium"]
    pf_age = animals[0]["age"]


    return render_template('home.html', pets=pets, pf_name=pf_name, pf_photo=pf_photo, pf_age=pf_age)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = True
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')

    else:
        return render_template('add-pet.html', form=form)

@app.route('/<pet_id>', methods=["GET", "POST"])
def show_pet_profile(pet_id):
    pet = Pet.query.get(pet_id)

    edit_form = EditPetForm(obj=pet)

    if edit_form.validate_on_submit():

        pet.photo_url = edit_form.photo_url.data
        pet.notes = edit_form.notes.data
        pet.available = edit_form.available.data

        db.session.add(pet)
        db.session.commit()
        return redirect(f"/{pet_id}")

    else:
        return render_template('pet-profile.html', pet=pet, edit_form=edit_form)

    

