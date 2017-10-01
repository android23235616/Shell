# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 23:22:44 2017

@author: Tanmay
"""

from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField

from wtforms import validators, ValidationError

class ContactForm(Form):
   name = TextField("Name Of Student",[validators.Required("Please enteryour name.")])
   Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
   Address = TextAreaField("Address")

   email = TextField("Email",[validators.Required("Please enter your email address."),
      validators.Email("Please enter your email address.")])

   Age = IntegerField("age")
   language = SelectField('Languages', choices = [('cpp', 'C++'),
      ('py', 'Python')])
   submit = SubmitField("Send")
