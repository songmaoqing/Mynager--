from django.utils import timezone

from wechat.wrapper import WeChatView, WeChatLib
from wechat.handlers import *
from wechat.models import Meeting
from Mynager.settings import WECHAT_TOKEN, WECHAT_APPID, WECHAT_SECRET


class CustomWeChatView(WeChatView):

    lib = WeChatLib(WECHAT_TOKEN, WECHAT_APPID, WECHAT_SECRET)

    handlers = [
        HelpHandler,
        AboutHandler,
        UnbindOrUnsubscribeHandler,
        BindAccountHandler,
        GetMeetingHandler,
    ]
    error_message_handler = ErrorHandler
    default_handler = DefaultHandler

    event_keys = {
        'account_bind': 'SERVICE_BIND',
        'help': 'SERVICE_HELP',
        'about': 'SERVICE_ABOUT',
        'notice': 'MEETING_NOTICE',
    }

    menu = {
        'button': [
            {
                "name": "服务",
                "sub_button": [
                    {
                        "type": "click",
                        "name": "绑定/解绑",
                        "key": event_keys['account_bind'],
                    },
                    {
                        "type": "click",
                        "name": "帮助",
                        "key": event_keys['help'],
                    },
                    {
                        "type": "click",
                        "name": "关于",
                        "key": event_keys['about'],
                    }
                ]
            },
            {
                "type": "click",
                "name": "我的通知",
                "key": event_keys['notice']
            }
        ]
    }

    @classmethod
    def update_menu(cls):
        cls.lib.set_wechat_menu(cls.menu)




