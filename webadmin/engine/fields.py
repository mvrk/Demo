#!/usr/bin/python
#-*-coding:utf-8-*-

from django.forms.fields import Field,CharField
from validators import username,password,classid,classname,studentid,studentname,term

class UsernameField(CharField):
    default_error_messages = {
        'invalid':u'Student: your student ID; Admin: 6-12 digits. (numbers, letters, and underscore.)',
        'required':u'Required(Student: your student ID; Admin: 6-12 digits. (numbers, letters, and underscore.))',
        'max_length':u'Maximum digits: 12',
        'min_length':u'Minimum digits: 6'
    }
    default_validators = [username]

    def clean(self,value):
        value = self.to_python(value).strip()
        return super(UsernameField, self).clean(value)

class PasswordField(CharField):
    default_error_messages = {
        'invalid':u'password由字母数字下划线组成的字符串，最少为8位',
        'required':u'password必须要填(由字母数字下划线组成的字符串，最少为6位)',
        'max_length':u'password至多为16位',
        'min_length':u'password至少为8位'
    }
    default_validators = [password]

class ClassnameField(CharField):
    default_error_messages = {
        'invalid':u'ClassName必须是2-6个汉字',
        'required':u'ClassName必须要填（2-6个汉字）',
    }
    default_validators = [classname]

    def clean(self,value):
        value = self.to_python(value).strip()
        return super(ClassnameField, self).clean(value)

class ClassidField(CharField):
    default_error_messages = {
        'invalid':u'Class ID Form with 7 digit numbers',
        'required':u'Class ID必须要填(7位数数字)',
    }
    default_validators = [classid]

    def clean(self,value):
        value = self.to_python(value).strip()
        return super(ClassidField, self).clean(value)
        
class StudentidField(CharField):
    default_error_messages = {
        'invalid':u'Student ID由9位数数字组成',
        'required':u'Student ID必须要填(9位数数字)',
    }
    default_validators = [studentid]

    def clean(self,value):
        value = self.to_python(value).strip()
        return super(StudentidField, self).clean(value)
        
class StudentnameField(CharField):
    default_error_messages = {
        'invalid':u'StudentName必须是2-4个汉字',
        'required':u'StudentName必须要填（2-4个汉字）',
    }
    default_validators = [studentname]

    def clean(self,value):
        value = self.to_python(value).strip()
        return super(StudentnameField, self).clean(value)
        
class TermField(CharField):
    default_error_messages = {
        'invalid':u'要按照(2014Fall)格式填',
        'required':u'学期必须填',
    }
    default_validators = [term]

    def clean(self,value):
        value = self.to_python(value).strip()
        return super(TermField, self).clean(value)
