# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：MyDjango -> sms
@IDE    ：PyCharm
@Author ：ruochen
@Date   ：2020/6/21 15:57
@Desc   ：
=================================================='''

import ssl

# ssl._create_default_https_context = ssl._create_unverified_context
from qcloudsms_py import SmsMultiSender, SmsSingleSender
from qcloudsms_py.httpclient import HTTPError


def send_sms_single(phone_num, template_id, template_param_list):
    """
    单条发送短信
    :param phone_num: 手机号
    :param template_id: 腾讯云短信模板ID
    :param template_param_list: 短信模板所需参数列表，例如:【验证码：{1}，描述：{2}】，则传递参数 [888,666]按顺序去格式化模板
    :return:
    """
    appid = '1400517986'  # 自己应用ID
    appkey = '06edcce4212e53d94a6ed5cbd33068e8'  # 自己应用Key
    sms_sign = '寝室智能管理系统'  # 自己腾讯云创建签名时填写的签名内容（使用公众号的话这个值一般是公众号全称或简称）
    sender = SmsSingleSender(appid, appkey)
    try:
        response = sender.send_with_param(86, phone_num, template_id, template_param_list, sign=sms_sign)
    except HTTPError as e:
        response = {'result': 1000, 'errmsg': "网络异常发送失败"}
    return response


def send_sms_multi(phone_num_list, template_id, param_list):
    """
    批量发送短信
    :param phone_num_list:手机号列表
    :param template_id:腾讯云短信模板ID
    :param param_list:短信模板所需参数列表，例如:【验证码：{1}，描述：{2}】，则传递参数 [888,666]按顺序去格式化模板
    :return:
    """
    appid = '1400517986'  # 自己应用ID
    appkey = '06edcce4212e53d94a6ed5cbd33068e8'  # 自己应用Key
    sms_sign = '寝室智能管理系统'  # 自己腾讯云创建签名时填写的签名内容（使用公众号的话这个值一般是公众号全称或简称）
    sender = SmsMultiSender(appid, appkey)
    try:
        response = sender.send_with_param(86, phone_num_list, template_id, param_list, sign=sms_sign)
    except HTTPError as e:
        response = {'result': 1000, 'errmsg': "网络异常发送失败"}
    return response


# phone_num_list = ['15888494869', '13567737175', '19106859233', '13757703075']
# print(send_sms_multi(phone_num_list, '953419', ['隔壁寝室僵尸入侵']))