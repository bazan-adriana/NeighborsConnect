from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model
from flask_app.models import address_model




class Post:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.descriptions = data['descriptions']
        self.comments = data['comments']
        self.date = data['date']
        self.currentmonth = data['currentmonth']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.address_id = data['address_id']
        self.address = None
        self.poster = None


#  =============    CREATE    ============
    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO posts (name, descriptions, comments, date, currentmonth, user_id, address_id)
            VALUES (%(name)s,%(descriptions)s,%(comments)s,%(date)s,%(currentmonth)s,%(user_id)s,%(address_id)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data)  


#  ===========  READ ALL  =============
    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM posts
                JOIN users
                ON posts.user_id = users.id
                JOIN addresses
                ON addresses.id = posts.address_id;
            """
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        all_posts = []
        if results:
            for row in results:
            # create each post
                this_post = cls(row)         # instantiate a post
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
                this_post.planner = this_user
                all_posts.append(this_post)
        return all_posts


#  ============    READ ONE   ==================
    @classmethod
    def get_by_id(cls, data):
        query = """
            SELECT * FROM posts
            JOIN users
            ON posts.user_id = users.id
            JOIN addresses ON addresses.id = posts.address_id
            WHERE posts.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        print(results)
        this_post = cls(results[0])
        if results:
            # init the post
# init the user and attach the post
            row = results[0]
            user_data = {
                **row,
                'id': row['users.id'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            address_data = {
                **row,
                'id': row['addresses.id'],
                'created_at': row['addresses.created_at'],
                'updated_at': row['addresses.updated_at']
            }
            
            # create a User obj here
            this_address = address_model.Address(address_data)
            this_post.address = this_address
            this_user = user_model.User(user_data)
            this_post.poster = this_user # adding a new attribute to the post
            return this_post
        return False



#=====================  GET ALL posts VIEW  ======================

    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM posts
            JOIN users
            ON posts.user_id = users.id
            JOIN addresses ON addresses.id = posts.address_id;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        
        all_posts = []
        if results:
            for row in results:
            # init the post
    # init the user and attach the post SELECT * FROM posts
                this_post = cls(row)
                user_data = {
                    **row,
                    'id': row['users.id'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at']
                }
                address_data = {
                    **row,
                    'id': row['addresses.id'],
                    'created_at': row['addresses.created_at'],
                    'updated_at': row['addresses.updated_at']
                }
                
                # create a User obj here
                this_address = address_model.Address(address_data)
                this_post.address = this_address
                this_user = user_model.User(user_data)
                this_post.poster = this_user # adding a new attribute to the post
                all_posts.append(this_post)
            return all_posts
        return False












#  ===============    UPDATE   ==================
    @classmethod
    def update(cls, data):
        query = """
            UPDATE posts
            SET
            name = %(name)s,
            descriptions = %(descriptions)s,
            comments = %(comments)s,
            date = %(date)s,
            currentmonth = %(currentmonth)s
            WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)



#  ===============    DELETE   ===========================
    @classmethod
    def delete(cls, data):
        query = """
        DELETE FROM posts
        Where id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)




#  ===================  VALIDATOR  =========================
    @staticmethod
    def validator(form_data):
        is_valid = True

        if len(form_data['name']) < 1:
            is_valid = False
            flash("Name must not be blank", 'form_validate')

        if len(form_data['descriptions']) < 1:
            is_valid = False
            flash("Description must not be blank", 'form_validate')

        if len(form_data['comments']) < 1:
            is_valid = False
            flash("Comments must not be blank", 'form_validate')
            
        if len(form_data['street']) < 1:
            is_valid = False
            flash("Street must not be blank", 'form_validate')
            
        if len(form_data['city']) < 1:
            is_valid = False
            flash("City must not be blank", 'form_validate')
            
        if len(form_data['state']) < 1:
            is_valid = False
            flash("State must not be blank", 'form_validate')

        if len(form_data['date']) < 1:
            is_valid = False
            flash("Date must not be blank", 'form_validate')

        if 'currentmonth' not in form_data:
            is_valid = False
            flash("Current Month? must not be blank", 'form_validate')

        return is_valid