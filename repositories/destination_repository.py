from db.run_sql import run_sql

from models.destination import Destination
from models.user import User
from repositories import user_repository

def save(destination):
    sql = "INSERT INTO destinations (city, country, visited, user_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [destination.city, destination.country, destination.visited, destination.user.id]
    results = run_sql(sql, values)
    # if len(results) > 0:
    id = results[0]['id']
    destination.id = id
    return destination

def select_all():
    destinations = []

    sql = "SELECT * FROM destinations"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row['user_id'])
        destination = Destination(row['city'], row['country'],  user, row['visited'], row['id'] )
        destinations.append(destination)
    return destinations


def select(id):
    destination = None
    sql = "SELECT * FROM destinations WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if len(results) > 0:
        result = results[0]
        user = user_repository.select(result['user_id'])
        destination = Destination(result['city'], result['country'],user, result['visited'], result['id'])
    return destination

def delete_all():
    sql = "DELETE FROM destinations"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM destinations WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(destination):
    sql = "UPDATE destinations SET (city, country, user_id, visited) = (%s, %s, %s, %s) WHERE id = %s"
    values = [destination.city, destination.country, destination.user.id, destination.visited, destination.id]
    run_sql(sql, values)

def destinations_for_user(user):
    destinations = []

    sql = "SELECT * FROM destinations WHERE user_id = %s"
    values = [user.id]
    results = run_sql(sql, values)

    for row in results:
        destination = Destination(row['city'], row['country'], user, row['visited'], row['id'] )
        destinations.append(destination)
    return destinations