from flask import Flask, render_template, request, redirect, Blueprint
from models.destination import Destination
from repositories import destination_repository, user_repository
import pdb

bucketlist_blueprint = Blueprint("Travel Bucketlist", __name__)

@bucketlist_blueprint.route('/')
def bucketlist():
    return render_template('index.html')

@bucketlist_blueprint.route('/destinations')
def destination_to_visit():
        destinations = destination_repository.select_all()
        for d in destinations:
             print(d.__dict__) 
        return render_template('destinations/show.html', destinations=destinations)

@bucketlist_blueprint.route('/destinations/add')
def add_destination():
    users = user_repository.select_all()
    return render_template('/destinations/new.html', users=users)

@bucketlist_blueprint.route("/destinations/new",  methods=['POST'])
def create_to_visit():
    # pdb.set_trace()
    visited = request.form['visited']
    city  = request.form['city']
    country = request.form['country']
    user_id = request.form['user_id']
    name = user_repository.select(user_id)
    destination = Destination(city, country, name,  visited)
    destination_repository.save(destination)
    return redirect('/destinations')

@bucketlist_blueprint.route("/destinations/<id>", methods=['GET'])
def show_destination(id):
    destination = destination_repository.select(id)
    return render_template('destinations/index.html', destination = destination)

@bucketlist_blueprint.route('/destinations/<id>/delete', methods=['POST'])
def delete_destination(id):
    destination_repository.delete(id)
    return redirect('/destinations')

@bucketlist_blueprint.route("/destinations/<id>", methods=['POST'])
def update_visited(id):
    # pdb.set_trace()
    # get the destingation I want to update
    destination = destination_repository.select(id)
    # modifty the destination visited property to be the opposite of what it originally was
    if destination.visited == True:
         destination.visited = False
    else:
         destination.visited = True
    destination_repository.update(destination)
    return redirect(f"/destinations/{destination.id}")







