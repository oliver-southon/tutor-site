from wtforms import SubmitField, BooleanField, StringField, PasswordField, SelectField, TextAreaField, validators
from flask_wtf import Form

class ContactForm(Form):
    firstName = StringField('Your First Name', [validators.DataRequired()])
    lastName = StringField('Your Last Name', [validators.DataRequired()])
    email = StringField('Your Email Address', [validators.DataRequired(), validators.Email(), validators.Length(min=6, max=35)])
    primLang = SelectField('What language are you primarily using?', [validators.DataRequired()], choices=[
        ('py', 'Python'), ('sql', 'SQL'), ('java', 'Java'), 
        ('c', 'C'), ('html', 'HTML'), ('css', 'CSS'), 
        ('js', "JavaScript"), ('other', 'Other')
        ])
    desc = TextAreaField('Describe your query (leave blank if already sent on instagram)', 
    render_kw={'rows': 4, 'cols': 10}
    )
    submit = SubmitField('Submit')

    