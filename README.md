基于requests库实现的爬取笔趣阁网站（https://www.bqg683.xyz/#/），实现搜索，下载小说一键操作
目前问题：
服务器可能因为短时间内建立太多新连接而断开，触发反爬机制

class TxtCopy:
    # 小说搜索url
    search_url = "https://apibi.cc/api/search?"
    # 小说介绍url
    introduce_url = "https://apibi.cc/api/book?"
    # 小说内容url
    content_url = "https://apibi.cc/api/chapter?"
    # UA伪装
    headers = {
        "User-Agent":
            "填入自己的hd",
    }

def __init__(self, txt_name):
初始化对象

def search_id(self, txt_name):
通过输入的小说名称查找对应的id
def search(self):
查找小说
再接着使用search_introduce()和search_content()方法来查询小说信息接着使用search_introduce()和search_content()方法来查询小说信息

def search_introduce(self):
通过id来查找小说的介绍
直接保存在小说文件中

def search_content(self):
通过id来查找小说的内容
每章查找完后保存在小说文件中

def save_txt(self, content):
保存小说内容（write 'a'模式）

def create_file(self):
以搜索到的小说名称创建小说文件（write 'w'模式）
