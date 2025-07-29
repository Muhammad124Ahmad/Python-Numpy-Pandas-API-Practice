import requests
import pandas as pd

URL="https://official-joke-api.appspot.com/jokes/ten"
jokes=requests.get(URL)

results=jokes.json()

df=pd.DataFrame(results)

print(df.head())




























# data = requests.get("https://fruityvice.com/api/fruit/all")

# results=data.json()

# df=pd.DataFrame(results)

# df2=pd.json_normalize(results)


# cherry=df2.loc[df2['name']=='Cherry']


# banana=df2.loc[df2['name']=='Banana']
# print(banana.iloc[0]['nutritions.calories'])


































# from randomuser import RandomUser
# import pandas as pd




# def get_users():
#     users =[]
     
#     for user in RandomUser.generate_users(10):
#         users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
#     return pd.DataFrame(users)   

# print(get_users())   