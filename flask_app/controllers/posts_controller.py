# ==== ROUTING  ====
import requests
from flask_app import app 
import os
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models.post_model import Post
from flask_app.models.address_model import Address



#  ================== Add a New Post!  CREATE page    - VIEW
@app.route('/posts/new')
def new_post():
    return render_template("post_new.html")



#  ===================  CREATE  - ACTION  method (POST)
@app.route('/posts/create', methods=['POST'])
def create_post():
    print(f"-------{request.form}---------")
#  validate the model
    if not Post.validator(request.form):
        return redirect("/posts/new")
    address_id = Address.create(request.form)
    post_data = {
        **request.form,
        'user_id': session['user_id'],
        'address_id': address_id
    }
    Post.create(post_data)
    return redirect('/dashboard')


#  ============    UPDATE  - EDIT PAGE  ========
@app.route('/posts/<int:id>/edit')
def edit_post(id):

    data = {
        "id": id
    }
    this_post = Post.get_by_id(data)
    return render_template("post_edit.html",
                            this_post=this_post)


#  ===================  UPDATE   - ACTION  method (POST)
@app.route('/posts/<int:id>/update', methods=['POST'])
def update_post(id):
    #  validate the model
    if not Post.validator(request.form):
        return redirect(f"/posts/{id}/edit")

    data = {
        'id': id,
        **request.form
    }

    Post.update(data)
    return redirect('/dashboard')


#  =============  READ ONE -- post page --  show   ============
@app.route("/posts/<int:id>")
def show_one_post(id):
    this_post = Post.get_by_id({'id': id})
    api = os.environ.get("FLASK_APP_API_KEY")

    return render_template("post_one.html",
                        this_post = this_post, api = api)



#  =================    DELETE     ============
@app.route('/posts/<int:id>/delete')
def delete_post(id):
    Post.delete({'id': id})
    return redirect('/dashboard')





