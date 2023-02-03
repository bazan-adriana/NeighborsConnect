from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model
import os





class Address:
    def __init__(self, data):
        self.id = data['id']
        self.street = data['street']
        self.city = data['city']
        self.state = data['state']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']


#  =============    CREATE    ============
    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO addresses (street, city, state)
            VALUES (%(street)s,%(city)s,%(state)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data) 


#  ===========  READ ALL  =============
    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM addresses
                JOIN users
                ON addresses.user_id = users.id;
            """
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        all_addresses = []
        if results:
            for row in results:
            # create each address
                this_address = cls(row)         # instantiate a address
            # create the user for this post
                user_data = {                # prepare the dict for the user constructor
                    'id': row['users.id'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at'],
                    **row
                }
# now we can make a user
                this_user = user_model.User(user_data)
            # add new attribute
                this_address.planner = this_user
                all_addresses.append(this_address)
        return all_addresses


# #  ============    READ ONE   ==================
#     @classmethod
#     def get_by_id(cls, data):
#         query = """
#             SELECT * FROM addresses
#             JOIN posts
#             ON addresses.id = posts.address_id
#             JOIN users ON users.id = posts.user_id
#             WHERE posts.id = %(id)s;
#         """
#         results = connectToMySQL(DATABASE).query_db(query, data)
#         print(results)
#         if results:
#             # init the address
#             this_address = cls(results[0])
# # init the user and attach the address
#             row = results[0]
#             user_data = {
#                 **row,
#                 'id': row['users.id'],
#                 'created_at': row['users.created_at'],
#                 'updated_at': row['users.updated_at']
#             }
#             # create a User obj here
#             this_user = user_model.User(user_data)
#             this_address.planner = this_user    # adding a new attribute to the address
#             return this_address
#         return False

