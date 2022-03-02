import requests,json,time,threading,random

# no = int(input("Total No of Channels?"))
ChannelCodes = ["922534448342401087","338017726394138624"] #here you add the channel id from where you forward message
# for i in range(no):
#     ChannelCodes.append(input(f"{i+1}: ChannelCode?"))
userIDS = ["922517239251476491"]
# no = int(input("Input Total no of Users?"))
# for i in range(no):
#     userIDS.append(input(f"{i+1}: UserId?"))


ForwardWebHook = "https://discord.com/api/webhooks/948442292052717608/_2WQ2sw_e5vz6Kh4_ZfMwFjlA9dv9zfshafp1-ehkeBIy6L1sxc57I2G3zYsZInDG3-h" # Here enter the webhook link in which you want to forward messages
token = "OTIyNTE3MjM5MjUxNDc2NDkx.Yh-YPQ.VoklmdcXL6U-jSiwxtusunLAyKo" # Here you add TOKEN of your account. Add you token in the double qouts

#Don't change the below code

header = {"authorization": token,
          "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}
def checkUsers(id):
    for userid in userIDS:
        if userid == id:
            return True
    return False
def delay():
    time.sleep(random.randint(1,4))

    
def sendSms(message,embeds):
    data = {
        "content":message,
        "embeds":embeds
    }
    while True:
        r = requests.post(f'{ForwardWebHook}',json=data)
        if str(r) == "<Response [204]>":
            break
def get_Data(header,channelID,userID,arr):
    r = requests.get(f'https://discord.com/api/v9/channels/{channelID}/messages?&limit=50',headers=header)
    try:
        jsonn = json.loads(r.text)
        i = len(jsonn)
        while i>=0:
            i-=1
            if jsonn[i]["id"] not in arr:
                if checkUsers(str(jsonn[i]['author']['id'])):
                    embeds = jsonn[i]['embeds']
                    content = f"[{jsonn[i]['author']['username']}]",jsonn[i]['content']
                    print(content)
                    sendSms(jsonn[i]['content'],embeds)
                arr.append(jsonn[i]['id'])
    except:
        pass
def main(ChannelCode):
    arr = []
    r = requests.get(f'https://discord.com/api/v9/channels/{ChannelCode}/messages?&limit=50',headers=header)
    try:
        jsonn = json.loads(r.text)
        for i in jsonn:
            arr.append(i['id'])
        while True:
            get_Data(header=header,channelID=ChannelCode,userID="922517239251476491",arr=arr)
            delay()
    except:
        pass

if __name__ =="__main__":
    for ChannelCode in ChannelCodes:
        t = threading.Thread(target=main,args = (ChannelCode,))
        t.start()
