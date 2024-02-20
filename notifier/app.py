import os
from wxpusher import WxPusher


token = os.environ['WXPUSHER_TOKEN']
topic_ids = os.environ['WXPUSHER_TOPIC_IDS']
# Initial DingTalk handler

def lambda_handler(event, context):
    print(event)
    msg = msg_format(event)
    print(msg)

    ret = WxPusher.send_message(msg,
                                topic_ids=topic_ids,
                                token=token,
                                url='')
    return ret

def msg_format(event):
    try:
        print('event:', event)
        # 消息来源是SNS，取 $.Records[0].Sns.Message，并对字符串进行一些处理，确保发送时可以正常显示
        msg = event['Records'][0]['Sns']['Message']

        # 进行字符串处理后返回，以确保IM客户端正确显示
        msg = msg.replace("\\n", "\n")
        if msg[0] == '\"' and msg[-1] == '\"':
            msg = msg[1:-1]

        return msg
    except:
        # 消息来源不是SNS，直接返回
        return event
