from flask_wtf import FlaskForm 
from wtforms import SelectField,StringField,SubmitField,TextAreaField,PasswordField,BooleanField
from wtforms.validators import InputRequired,Email,EqualTo
from wtforms import ValidationError

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')

class NewBlog(FlaskForm):
    title = StringField('Blog title',validators=[InputRequired()])
    blog_content = TextAreaField('Blog to post',validators=[InputRequired()])
    author = StringField('Author',validators=[InputRequired()])
    submit = SubmitField('submit')

class MyComment(FlaskForm):
    description = TextAreaField('Tell us what you think',validators=[InputRequired()])
    submit = SubmitField('submit')

class UpdateBlog(FlaskForm):
    updates = TextAreaField('update your blog',validators=[InputRequired()])
    submit = SubmitField('submit')

class SubscribeForm(FlaskForm):
    email = StringField('Your email address',validators=[InputRequired(),Email()])
    submit = SubmitField('submit')