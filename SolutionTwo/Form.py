from wtforms import Form, StringField
from wtforms.validators import DataRequired, Email, Length, Regexp, EqualTo


class Information(Form):
    tests = StringField('Total tests: ',
                        validators=[DataRequired(), Length(3, 80),
                                    Regexp('^{1,4}$')])
    phoneModel = StringField('Phone Model: ',
                             validators=[DataRequired(), Length(3, 80),
                                         Regexp('^[A-Za-z_]{3,}$')])
    phoneOS = StringField('Phone OS: ',
                          validators=[DataRequired(), Length(3, 80),
                                      Regexp('^[A-Za-z_]{3,}$')])
    device = StringField('Device: ',
                         validators=[DataRequired(), Length(3, 80),
                                     Regexp('^[A-Za-z_]{3,}$')])
    firmwareVersion = StringField('Firmware Version: ',
                                  validators=[DataRequired(), Length(3, 80),
                                              Regexp('^[A-Za-z_]{3,}$')])
