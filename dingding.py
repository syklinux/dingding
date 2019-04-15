
from dingtalkchatbot.chatbot import DingtalkChatbot, FeedLink, ActionCard
import json


class dingding(object):

    def __init__(self):
        self.webhook = 'hasjkdhajkhdkajhdkajhsdjkahd'
        self.ding = DingtalkChatbot(self.webhook)


    def send_msg(self,msg,at_mobiles=None):
        '''
            不指定at_mobiles，则@所有人;
            艾特指定的人，可以多个号码，用","隔开
            :param msg:
            :param at_mobiles: "1111111,2222222"
            :return:
        '''
        if at_mobiles:
            a = self.ding.send_text(msg=msg, at_mobiles=str(at_mobiles).split(","))
        else:
            a = self.ding.send_text(msg=msg, is_at_all=True)
        return a["errmsg"]


    def send_link(self,title,text,message_url):
        '''
            :param title: "msg"
            :param text: "xxxxxxx"
            :param message_url: "https://www.coderops.net"
            :return:
        '''
        a = self.ding.send_link(title=title, text=text, message_url=message_url)
        return a["errmsg"]


    def send_FeedCard(self,*args):
        '''
        发送FeedCard类型消息
        :param args: 传入列表
            [
                {
                    "title": "美女",
                    "message_url": "https://www.coderops.net/",
                    "pic_url": "https://www.coderops.net/media/image/blog/2019/04/BistiBadlands_ZH-CN5428677883_1920x1080_4Dl1EYc.jpg"
                },
                {
                    "title": "美女",
                    "message_url": "https://www.coderops.net/",
                    "pic_url": "https://www.coderops.net/media/image/blog/2019/04/BistiBadlands_ZH-CN5428677883_1920x1080_4Dl1EYc.jpg"
                },
                {
                    "title": "美女",
                    "message_url": "https://www.coderops.net/",
                    "pic_url": "https://www.coderops.net/media/image/blog/2019/04/BistiBadlands_ZH-CN5428677883_1920x1080_4Dl1EYc.jpg"
                },
            ]
        :return:
        '''
        links = []
        for index,value in enumerate(args[0]):
             links.append(FeedLink(title=value["title"],message_url=value["message_url"],pic_url=value["pic_url"]).get_data())
        a = self.ding.send_feed_card(links)
        return a["errmsg"]


    def send_ActionCard(self):
        btns1 = [{"title": "查看详情", "actionURL": "https://www.dingtalk.com/"}]
        actioncard1 = ActionCard(title='万万没想到，竟然...',
                                 text='![选择](http://www.songshan.es/wp-content/uploads/2016/01/Yin-Yang.png) \n### 故事是这样子的...',
                                 btns=btns1,
                                 btn_orientation=1,
                                 hide_avatar=1)
        self.ding.send_action_card(actioncard1)
        pass




a = dingding()
# print(a.send_msg("sasas",))
# print(a.send_msg("sasas","111111111"))
# print(a.send_link("sss","sss","ssa"))
# a.send_FeedCard(data)


