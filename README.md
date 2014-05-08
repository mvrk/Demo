ComPerformance<br>
==============

一个使用django开发的学生综合GPAManagement平台.
=========================================

<pre>
项目基于django1.3.1，你可以通过sudo easy_install "django==1.3.1"安装；
要想切换成原django版本可以通过sudo easy_install django进行。

实现的功能如下:
    Student的功能：
        1).登录
        2).Editpassword
        3).Logout
        4).在规定时间段内进行互评
        5).在规定时间段内Edit互评
        6).查看自己详细信息
        7).查看自己进行的历史互评信息
        8).查看自己的互评信息(和互评排名等信息)
        9).查看GPA(包括院系、Class)r
        10).对GPA的查找和排序及其他处理
        11).查看院系以Class为Form位的GPA情况
        12).Submit个性发展的内容
        13).查看个性发展和活动的得分情况
        14).查看综合测评GPA排名以及各种GPA组成情况详细信息
        15).对综合GPA进行查询和排序及其他处理
        16).查看院系以Class为Form位的综合GPA情况)，并形成文档
    超级Management员需求：
        1).登录
        2).Editpassword
        3).Logout
        4).AddClass
        5).DeleteClass
        6).EditClass
        7).AddStudent，DeleteStudent，EditStudent信息
        8).Init.Student或记录员password
        9).开设学期互评功能,限定互评的时间段和选择学期
        10).限定每班各项名额
        11).ImportGPAForm
        12).查看院系以Class为Form位的GPA情况
        13).对GPA的查找和排序及其他处理
        14).对个性发展的设置,Add,Edit
        15).根据Student的Submit和相关证明的上交，进行最终评分
        16).并根据其他信息进行加减分设置(卫生，出勤)
        17).设置GPA和日常行为分的比例情况
        18).查看综合测评GPA排名以及各种GPA组成情况详细信息
        19).对综合GPA进行查询和排序及其他处理
        20).查看院系以Class为Form位的综合GPA情况
        21).查看所有人的互评信息
</pre>
<h1>
搭建方法
</h1>
<pre>
    1.下载最新版本 
    2.在mysql数据库C建一个comperformance数据库，然后Importsql
    3.EditsettingsC的DATABASES
    4.sudo easy_install django-grappelli 
    5.sudo easy_install xlrd 
    6.sudo easy_install pil
    7.python manage.py runserver 
    8.用户名：guomeng password：guomeng
    9.登录
</pre>

<h1>
安装问题
</h1>
<pre>
关于验证码Null法显示问题，可以参考：
http://www.douban.com/group/topic/12636401/
http://stackoverflow.com/questions/3544155/need-help-with-a-pil-error-ioerror-decoder-zip-not-available
http://hi.baidu.com/wbwylbt/item/2f093d3f50433699b90c0326
</pre>
