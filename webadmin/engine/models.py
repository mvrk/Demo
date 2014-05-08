#!/usr/bin/python
#-*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
import datetime

SEX_CHOICES = (
    ('0','Boy'),
    ('1','Girl'),
)

LEVEL_CHOICES = (
    ('0','学校'),
    ('1','学院'),
)

EVALUATE_CHOICES = (
    ('0','A'),
    ('1','B'),
    ('2','C'),
    ('3','Null'),
)

DEVELOPMENT_LEVEL_CHOICES = (
    ('0','组织Management'),
    ('1','创新'),
    ('2','其他'),
)

class Class(models.Model):
    classid = models.CharField(u"Class ID",unique=True,max_length=10)
    classname = models.CharField(u"Class Name",max_length=20)

    def __unicode__(self):
        return self.classid

    class Meta:
        db_table = u"class"
        verbose_name_plural = 'Class'
        
class Student(models.Model):
    user = models.OneToOneField(User)
    realname = models.CharField(u'Name',max_length=16)
    theclass = models.ForeignKey(Class,verbose_name="Class")
    sex = models.CharField(u'Gender',choices = SEX_CHOICES,max_length = 1)

    def __unicode__(self):
        return self.user.username

    class Meta:
        db_table = u"student"
        verbose_name_plural = '学生'

class Assessment(models.Model):
    begindate = models.DateField(u"开始日期")
    enddate = models.DateField(u"结束日期")
    term = models.CharField(u'学期',unique=True,max_length=16)
    excellent = models.IntegerField(u"A")
    good = models.IntegerField(u"B")
    ordinary = models.IntegerField(u"C")

    def __unicode__(self):
        return self.term

    class Meta:
        db_table = u"assessment"
        verbose_name_plural = '互评设置'

class AssessmentRecord(models.Model):
    assessment = models.ForeignKey(Assessment,verbose_name="互评")
    ostudent = models.ForeignKey(Student,verbose_name="评价Student",related_name = 'ostuent')
    dstudent = models.ForeignKey(Student,verbose_name="被评价Student",related_name = 'dstuent')
    result = models.CharField(u'评价结果',choices=EVALUATE_CHOICES,max_length=1)

    def __unicode__(self):
        return self.assessment.term + self.ostudent.realname + "-" + self.dstudent.realname

    class Meta:
        db_table = u"assessmentrecord"
        verbose_name_plural = '互评记录'

class AssessmentRow(models.Model):
    assessment = models.ForeignKey(Assessment,verbose_name="互评")
    student = models.ForeignKey(Student,verbose_name="被评价Student")
    excellent = models.IntegerField(u"A")
    good = models.IntegerField(u"B")
    ordinary = models.IntegerField(u"C")

    def __unicode__(self):
        return self.assessment.term + "--" +self.student.realname

    class Meta:
        db_table = u"assessmentrow"
        verbose_name_plural = '每人互评记录'

class Grade(models.Model):
    term = models.CharField(u'学期',max_length=16)
    student = models.ForeignKey(Student,verbose_name="Student")
    score = models.FloatField(u"分数")
    
    def __unicode__(self):
        return  self.term + "  " + self.student.user.username + "-->" + str(self.score)

    class Meta:
        db_table = u"grade"
        verbose_name_plural = 'GPA'

class Behavior(models.Model):
    actlevel = models.CharField(u'Level',choices = LEVEL_CHOICES,max_length = 1)
    name = models.CharField(u'Name',max_length=16)
    
    def __unicode__(self):
        return self.name

    class Meta:
        db_table = u"behavior"
        verbose_name_plural = '日常行为活动'

class Development(models.Model):
    parent = models.CharField(u'个性发展大类',choices = DEVELOPMENT_LEVEL_CHOICES,max_length = 1,null=True,blank=True)
    name = models.CharField(u'个性发展Name',max_length=11)
    
    def __unicode__(self):
        return self.name

    class Meta:
        db_table = u"development"
        verbose_name_plural = 'Talent Development Activity'

class Comperformance(models.Model):
    excellent = models.FloatField(u"A分数")
    good = models.FloatField(u"B分数")
    ordinary = models.FloatField(u"C分数")
    physical = models.FloatField(u"体能分数")
    behavior = models.FloatField(u"日常行为分基础分")
    development = models.FloatField(u"Form项最高分")
    moral = models.FloatField(u"互评最高分")
    behaviorup = models.FloatField(u"日常行为分最高")
    term = models.CharField(u'学期',unique=True,max_length=16)

    def __unicode__(self):
        return self.term

    class Meta:
        db_table = u"comperformance"
        verbose_name_plural = '综合测评设置'

class ComperformanceDevelopmentScore(models.Model):
    student = models.ForeignKey(Student,verbose_name="Student")
    comperformance = models.ForeignKey(Comperformance,verbose_name="综合GPAManagement")
    development = models.ForeignKey(Development,verbose_name="个性发展")
    score = models.FloatField(u"分数",null=True, blank=True)
    
    def __unicode__(self):
        return self.student.user.username + u"-->个性发展分数:" + str(self.score)

    class Meta:
        db_table = u"comperformancedevelopmentscore"
        verbose_name_plural = '个性发展加分'

class ComperformanceBehaviorScore(models.Model):
    student = models.ForeignKey(Student,verbose_name="Student")
    comperformance = models.ForeignKey(Comperformance,verbose_name="综合GPAManagement")
    behavior = models.ForeignKey(Behavior,verbose_name="日常行为")
    score = models.FloatField(u"分数",null=True, blank=True)
    
    def __unicode__(self):
        return self.student.user.username + u"-->日常行为分数:" + str(self.score)

    class Meta:
        db_table = u"comperformancebehaviorscore"
        verbose_name_plural = '日常活动加分'

class ComperformancePhysicalScore(models.Model):
    student = models.ForeignKey(Student,verbose_name="Student")
    comperformance = models.ForeignKey(Comperformance,verbose_name="综合GPAManagement")
    score = models.FloatField(u"分数",null=True, blank=True)
    
    def __unicode__(self):
        return self.student.user.username + u"-->体能分数：" + str(self.score)

    class Meta:
        db_table = u"comperformancephysicalscore"
        verbose_name_plural = '体能加分'
        
class ComperformanceScore(models.Model):
    student = models.ForeignKey(Student,verbose_name="Student")
    comperformance = models.ForeignKey(Comperformance,verbose_name="综合GPAManagement")
    score = models.FloatField(u"综合GPA分数",null=True, blank=True)
    assessmentscore = models.FloatField(u"互评分数",null=True, blank=True)
    
    def __unicode__(self):
        return self.student.user.username + u"-->综合GPA分数：" + str(self.score) + u"互评分数：" + str(self.assessmentscore)

    class Meta:
        db_table = u"comperformancescore"
        verbose_name_plural = '综合测评分数'
