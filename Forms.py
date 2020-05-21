from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp


class Information(FlaskForm):
    tests = StringField('Total tests: ',
                        validators=[DataRequired(), Length(1, 5),
                                    Regexp('^[A-Za-z_1-9]{1,}$')])
    phoneModel = StringField('Phone Model: ',
                             validators=[DataRequired(), Length(3, 80),
                                         Regexp('^[A-Za-z_1-9]{3,}$')])
    phoneOS = StringField('Phone OS: ',
                          validators=[DataRequired(), Length(3, 80),
                                      Regexp('^[A-Za-z_1-9]{3,}$')])
    device = StringField('Device: ',
                         validators=[DataRequired(), Length(3, 80)])
    firmwareVersion = StringField('Firmware Version: ',
                                  validators=[DataRequired(), Length(1, 5),
                                              Regexp('^[A-Za-z_1-9]{2,}$')])
    submit = SubmitField()
