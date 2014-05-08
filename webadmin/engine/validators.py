#!/usr/bin/python
#-*-coding:utf-8-*-

import re
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

username_re = re.compile(r'^([\w]{9}|[a-zA-Z]{1}[\w]+?)$')
username = RegexValidator(username_re,u'Student: your student ID; Admin: 6-12 digits. (numbers, letters, and underscore.)','invalid')

password_re = re.compile(r'^[\w]+?$')
password = RegexValidator(password_re,u'password由字母数字下划线组成的字符串，最少为6位','invalid')

classid_re = re.compile(r'^[\w]{7}$')
classid = RegexValidator(classid_re,u'Class ID Form with 7 digit numbers','invalid')

classname_re = re.compile(r'^[\u4e00-\u9fa5]{2,6}$')

class ClassnameValidator(object):
    message = u'ClassName必须是2-6个汉字'
    code = 'invalid'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self,value):
        if not all([True if i >= u'\u4e00' and i <= u'\u9fa5' else False for i in value]):
            raise ValidationError(self.message, code=self.code)

classname = ClassnameValidator()

studentid_re = re.compile(r'^[\w]{9}$')
studentid = RegexValidator(studentid_re,u'Student ID由9位数数字组成','invalid')

class StudentnameValidator(ClassnameValidator):
    message = u'StudentName必须是2-4个汉字'

studentname = StudentnameValidator()

class TermValidator(object):
    message = u'要按照(2014Fall)格式填'
    code = 'invalid'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self,value):
        if not (all([True if i >= u'\u4e00' and i <= u'\u9fa5' else False for i in value[4:]]) and all([True if i in ['0','1','2','3','4','5','6','7','8','9'] else False for i in value[:4]])):
            raise ValidationError(self.message, code=self.code)

term = TermValidator()
