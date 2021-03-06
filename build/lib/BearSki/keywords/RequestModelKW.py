# -*- encoding: utf-8 -*-
'''
@File    :   requestModel.py
@Time    :   2020/01/30 11:22:59
@Author  :   chenjiusi 
'''
import json
import logging
from BearSki.CommonData import SkiGlobalData
import requests
from BearSki.keywords.DataTreating import BaseDataTreating
class RequestModelCommondKW(object):

  def __init__(self):
    self.logger=logging.getLogger("kw.RequestModelCommondKW")
    self.BASE_URL=SkiGlobalData().get_global_data('BASE_URL')
    self.MODEL_PATH=SkiGlobalData().get_global_data('MODEL_PATH')

  def run(self,jstr):
    self.logger.info("运行json：{0}".format(jstr))
    url = jstr['name']
    self.logger.info("url is :"+url)
    method=jstr['request']['method']
    headers_data = {}
    bdt=BaseDataTreating()
    h_ds=jstr['request']['headers']
    for hname in h_ds:
      # 使用通用数据替换方法替换消息头
      headers_data[hname]=bdt.treating(hname,h_ds[hname])
    print(headers_data)

    if method=='POST':
      # logger.info('in login！')
      post_data=jstr['request']['json']
      print(self.BASE_URL+url)
      r = requests.post(url=self.BASE_URL+url,headers=headers_data,json=post_data)   
      self.logger.info("response is : {0}".format(r))
      # logger.info("response is : {0}".format(r.text))
      # result=json.loads(r.text)
    # global jwt_access
    # jwt_access[login_user['username']]=result['data']['access']
    # if method=='GET':
    if method == 'GET':
      post_data=jstr['request']['params']
      print(self.BASE_URL+url)
      r = requests.get(url=self.BASE_URL+url,headers=headers_data,params=post_data)   
      self.logger.info("response is : {0}".format(r))
    return r