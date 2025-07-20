import os.path
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# 如果修改了这些范围，请删除 token.json 文件。
SCOPES = ['https://www.googleapis.com/auth/blogger']

def authenticate_blogger():
    creds = None
    # token.json 存储了用户上次成功登录时生成的凭据，并自动刷新。
    if os.path.exists('token.json'):
        with open('token.json', 'rb') as token:
            creds = pickle.load(token)
    # 如果没有有效的（或过期的）凭据，让用户登录。
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # 将凭据保存起来，以便下次运行。
        with open('token.json', 'wb') as token:
            pickle.dump(creds, token)
    
    service = build('blogger', 'v3', credentials=creds)
    return service

if __name__ == '__main__':
    print("正在进行 Blogger API 认证...")
    service = authenticate_blogger()
    print("认证成功！您现在可以使用 'service' 对象与 Blogger API 交互。")
    # 您可以在这里添加一些测试代码，例如获取您的博客列表
    # try:
    #     blogs = service.blogs().listByUser(userId='self').execute()
    #     print("您的博客列表:")
    #     for blog in blogs['items']:
    #         print(f"- {blog['name']} (ID: {blog['id']})")
    # except Exception as e:
    #     print(f"获取博客列表失败: {e}")
