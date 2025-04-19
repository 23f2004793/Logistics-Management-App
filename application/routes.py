from flask import current_app as app
from flask_security import auth_required, roles_required
from flask_security import current_user

@app.route('/admin')
@auth_required('token') # Authentication.
@roles_required('admin') # RBAC/Authorization.
def admin_home():
    return '<h1>This is admin</h1>'

@app.route('/user')
@auth_required('token')
@roles_required('user')
def user_home():
    user = current_user # session based retrieval.
    return ({"username": user.username,
            "email": user.email,
            "password": user.password})

                    
