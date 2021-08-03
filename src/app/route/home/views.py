#################
#### imports ####
#################

from flask import render_template, Blueprint, request, flash, redirect, url_for   # pragma: no cover
from flask_login import login_required, current_user   # pragma: no cover

from app.route.home.forms import MessageForm   # pragma: no cover
from app.main import db   # pragma: no cover
from app.model.user import BlogPost   # pragma: no cover

################
#### config ####
################

bphome = Blueprint(
    'home', __name__,
    template_folder='templates'
)   # pragma: no cover


################
#### routes ####
################

# use decorators to link the function to a url
@bphome.route('/home', methods=['GET', 'POST'])   # pragma: no cover
@login_required   # pragma: no cover
def home():
    error = None
    form = MessageForm(request.form)
    if form.validate_on_submit():
        new_message = BlogPost(
            form.title.data,
            form.description.data,
            current_user.id
        )
        db.session.add(new_message)
        db.session.commit()
        flash('New entry was successfully posted. Thanks.')
        return redirect(url_for('home.home'))
    else:
        posts = db.session.query(BlogPost).all()
        return render_template('home/index.html', posts=posts, form=form, error=error)


@bphome.route('/welcome')   # pragma: no cover
def welcome():
    return render_template('home/welcome.html')  # render a template
