#import jwt
##payload={'name':'varun sharma','password':243542,'user_id':23}
#token=jwt.encode(payload,key='varun123',algorithm='HS256')
##print(token)
#ans=jwt.decode(token,key='varun123',algorithms='HS256')
#print('token has decode it',ans)
import requests 
data={
'username': 'varun123',
'email': 'varun941068@gmail.com',
}
url='http://127.0.0.1:8000/user/login'
url2='http://127.0.0.1:8000/user/validation'
#get=requests.post(url,data=data1)
get=requests.post(url,data={'username':'varun','email':'vs008278@gmail.com'})
print(get.json())
token=get.json()
print(token['token'])
get2=requests.post(url2,data={'token':token['token']})
print(get2.json())