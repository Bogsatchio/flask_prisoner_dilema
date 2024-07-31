from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField, DecimalField
from wtforms.validators import DataRequired, NumberRange


class ExperimentsForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    description = StringField("description")
    cooperation_points = IntegerField("cooperation points",
                                      validators=[DataRequired(),
                                                  NumberRange(min=0, max=50, message='Value must be between 0 and 50')])
    one_side_betrayal_points = IntegerField("one side betrayal points",
                                            validators=[DataRequired(), NumberRange(min=0, max=50,
                                                                    message='Value must be between 0 and 50')])
    two_side_betrayal_points = IntegerField("two side betrayal points",
                                            validators=[DataRequired(), NumberRange(min=0, max=50,
                                                                    message='Value must be between 0 and 50')])
    rounds = IntegerField("rounds",
                          validators=[DataRequired(),
                                      NumberRange(min=1, max=100, message='Value must be between 1 and 100')])
    matches = IntegerField("matches",
                           validators=[DataRequired(),
                                       NumberRange(min=1, max=5, message='Value must be between 1 and 5')])
    waves = IntegerField("waves",
                         validators=[DataRequired(),
                                     NumberRange(min=1, max=50, message='Value must be between 1 and 50')])
    num_eliminated = IntegerField("number eliminated",
                                  validators=[DataRequired(),
                                              NumberRange(min=1, max=5, message='Value must be between 1 and 5')])
    winners_premium = DecimalField("winners premium",
                                   validators=[DataRequired(),
                                               NumberRange(min=1, max=3, message='Value must be between 1 and 3')])

    rando_n = IntegerField("rando", default=0,
                           validators=[NumberRange(min=0, max=5, message='Value must be between 0 and 5')])
    forgiving_tft_n = IntegerField("forgivingtft", default=0,
                                   validators=[NumberRange(min=0, max=5, message='Value must be between 0 and 5')])
    defector_n = IntegerField("defector", default=0,
                              validators=[NumberRange(min=0, max=5, message='Value must be between 0 and 5')])
    cooperator_n = IntegerField("cooperator", default=0,
                                validators=[NumberRange(min=0, max=5, message='Value must be between 0 and 5')])
    rather_defector_n = IntegerField("rather_defector", default=0,
                                     validators=[NumberRange(min=0, max=5, message='Value must be between 0 and 5')])
    much_rather_defector_n = IntegerField("much_rather_defector", default=0,
                                          validators=[
                                              NumberRange(min=0, max=5, message='Value must be between 0 and 5')])
    grim_trigger_n = IntegerField("grim_trigger", default=0,
                                  validators=[NumberRange(min=0, max=5, message='Value must be between 0 and 5')])
    pavlov_n = IntegerField("pavlov", default=0,
                            validators=[NumberRange(min=0, max=5, message='Value must be between 0 and 5')])
    tft_n = IntegerField("tft", default=0,
                         validators=[NumberRange(min=0, max=5, message='Value must be between 0 and 5')])
    sus_tft_n = IntegerField("sus_tft", default=0,
                             validators=[NumberRange(min=0, max=5, message='Value must be between 0 and 5')])

    submit = SubmitField('Submit')


class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')
