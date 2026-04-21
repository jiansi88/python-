# 小说内容
# https://apibi.cc/api/chapter?  id=144332&    chapterid=1
# https://apibi.cc/api/chapter?  id=144332&    chapterid=2
# 小说介绍
# https://apibi.cc/api/book?id=144332
# 小说搜索
# https://apibi.cc/api/search?q= %E5%AE%BF%E5%91%BD%E4%B9%8B%E7%8E%AF
import requests


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
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36",
    }

    def __init__(self, txt_name):
        self.txt_name = ''
        self.id = ''
        self.search_id(txt_name)

        self.content = []

    def search_id(self, txt_name):
        params = {
            'q': txt_name
        }
        # 访问网站
        response = requests.get(url=self.search_url, params=params, headers=self.headers)
        # 获取响应数据
        content = response.json()
        # print(search_content)
        self.txt_name = content["data"][0]['title']  # 返回搜索到的小说名称
        self.id = content["data"][0]['id']  # 返回搜索的id


    def search(self):
        self.search_introduce()
        self.search_content()

    def search_introduce(self):
        params = {
            'id': self.id
        }
        # 指定url
        response = requests.get(url=self.introduce_url, params=params, headers=self.headers)
        # 获取响应数据
        content = response.json()
        # print(content["intro"].strip())
        temp_content = content["intro"].replace('　　', '')
        # print(temp_content)
        self.save_txt(temp_content.strip())

    def search_content(self):
        page = 1

        while True:
            # 清空内容
            content = []

            params = {
                'id': self.id,
                "chapterid": str(page)
            }
            # 指定url
            response = requests.get(url=self.content_url, params=params, headers=self.headers)
            # 获取响应数据
            total_content = response.json()
            # 检测是否到达最后章
            if total_content.get("chaptername") in [None, "null", ""]:
                break
            # else:
            #     print(total_content["chaptername"])
            # 储存内容
            content.append('\n' + total_content["chaptername"] + '\n')
            content.append(total_content["txt"] + '\n')

            self.save_txt(content)

            print(page, end=' ')
            page += 1

        print("读取完成")

    def save_txt(self, content):
        with open("./save_txt/"+self.txt_name + ".txt", 'a', encoding='utf-8') as fp:
            for insert in content:
                fp.write(insert)

    def create_file(self):
        # 安全声明
        safe_head = "内容仅可用于个人学习，禁止传播、商用、二次分发\n"
        with open("./save_txt/"+self.txt_name + ".txt", 'w', encoding='utf-8') as fp:
            fp.write(safe_head)


if __name__ == "__main__":
    search_name = input("请输入要搜索的小说名")
    copy = TxtCopy(search_name)
    flag = "0"
    if copy.id != '':
        print(f"找到小说：{copy.txt_name}")

        print("是否下载小说")

        while True:
            flag = input("1.下载  0.退出\n")
            match flag:
                case "1":
                    copy.create_file()
                    copy.search()
                    print("下载完成")
                    break
                case "0":
                    print("退出")
                    break
                case _:
                    print("请重试")

    else:
        print(f"未找到小说：{search_name}")
