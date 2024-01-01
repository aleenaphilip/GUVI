#import build from the google API libraries
# import API client

from googleapiclient.discovery import build
# !pip install pymongo

import pymongo
import pandas as pd

#  -------------Channel Data------------------


# function fetch channel data

def channel_details(channel_id):
 api_service_name = "youtube"
 api_version = "v3"
 api_key = "AIzaSyDFz7xnffNVxmPSsZbf6Xppqlm1aaBpIgk" 
# channel details
# build connect youtube data and API keys
 youtube = build(api_service_name, api_version, developerKey=api_key)#api key assigned as the developer key
 request = youtube.channels().list(
       part="snippet,contentDetails,statistics",
       id=channel_id
 )
 response = request.execute()   # execute the requested response.
 channel_name= response['items'][0]['snippet']['title']
 channel_description= response['items'][0]['snippet']['description']
 channel_pat= response['items'][0]['snippet']['publishedAt']
 channel_playlist= response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
 channel_scount = response['items'][0]['statistics']['subscriberCount']
 channel_vcount = response['items'][0]['statistics']['videoCount']
 channel_viewcount = response['items'][0]['statistics'][ 'viewCount']

     # for display the channel details and extract relevent information
    # dictionary format
 cd = {
    'channel_name':channel_name,
    'channel_description':channel_description,
    'channel_published':channel_pat,
    'playlist_id':channel_playlist,
    'subscribers_count':channel_scount,
    'video_count':channel_vcount,
    'view_count' :channel_viewcount
     }
 
 return cd

# to call  each channel with id
channel_1 = channel_details("UCeoRAN5sr02w8_9aFWxIM4g")
channel_1
# channel_2 = channel_details("UC2UWtuZR3kH-5C26HVMMB6A")
# channel_2
# channel_3 = channel_details("UCVv-y0k91qAA-uI_K46UBvg")
# channel_3
# channel_4 = channel_details("UCHJRfHlINisqkfJMXzTp9TQ")
# channel_5 = channel_details("UCfyulcK9tP84epquAb460UQ")
# channel_6 = channel_details("UC2w8rA29Q3iGs92pjlIsC_w")
# channel_7 = channel_details("UCOH_ioSD8yxFCfKNuiWiloQ")
# channel_8 = channel_details("UCCRfkpYF70QoUffbC5emuyw")
# channel_9 = channel_details("UCbalRQtxlcSFjKCqgWkhpvA")
# channel_10 = channel_details ("UCjEUp2OLhBZT-17SYQWLd-g")

# ----------Video IDs------------

# Function to fetch video id
def select_video_id(playlist_id):
 video_ids = []
 api_service_name = "youtube"
 api_version = "v3"
 api_key = "AIzaSyDFz7xnffNVxmPSsZbf6Xppqlm1aaBpIgk" 
 youtube = build(api_service_name, api_version, developerKey=api_key)#api key assigned as the developer key   
   

# Fetch playlist_id
 video_response = youtube.playlistItems().list(
        part='contentDetails',
        playlistId=playlist_id,
        maxResults=50
    )
 response_2= video_response.execute()
    
# to fetch 50 video id using above channlel_id 
 for i in  range(len(response_2['items'])):
  video_ID = response_2['items'][i]['contentDetails']['videoId']
  video_ids.append(video_ID)
    
 return video_ids

v_id = select_video_id("UUeoRAN5sr02w8_9aFWxIM4g")
v_id


  # ----------Video Data--------------

# fetch video details using video id
def video_details(v_id):
  videos = [] 
  api_service_name = "youtube"
  api_version = "v3"
  api_key = "AIzaSyDFz7xnffNVxmPSsZbf6Xppqlm1aaBpIgk" 
  youtube = build(api_service_name, api_version, developerKey=api_key)#api key assigned as the developer key   

# fetch video data
  for video_id in v_id:
    
    video_data= youtube.videos().list(
      part="snippet,contentDetails,statistics",
      id=video_id
    )
    response_3 = video_data.execute()
      
# convert video details into dictionary format  
    vd = {
      'video_name': response_3['items'][0]['snippet']['title'],
      'video_Id': response_3['items'][0]['id'],
      'video_description':response_3['items'][0]['snippet']['description'],
      'published_date': response_3['items'][0]['snippet']['publishedAt'],
      'view_count': response_3['items'][0]['statistics']['viewCount'],
# get fn used to get data if it is present otherwie display 'None'.
      'like_count': response_3['items'][0]['statistics'].get('likeCount'),
      'dislike_Count': response_3['items'][0]['statistics'].get('dislikeCount'),
      'favorite_Count': response_3['items'][0]['statistics'].get('favoriteCount'),
      'comment_count': response_3['items'][0]['statistics'].get('commentCount'),
      'duration': response_3['items'][0]['contentDetails']['duration'],
      'thumbnail': response_3['items'][0]['snippet']['thumbnails']['default']['url'],
      'caption_status': response_3['items'][0]['contentDetails']['caption']
        
         }
    videos.append(vd)
  return videos

# pprint() for readable and prettyway
# from pprint import pprint
video_details(v_id)

 #--------Comment Data--------------

# function to fetch comment details
def comment_details(v_id):
  comment_data = [] 
  api_service_name = "youtube"
  api_version = "v3"
  api_key = "AIzaSyDFz7xnffNVxmPSsZbf6Xppqlm1aaBpIgk" 
  youtube = build(api_service_name, api_version, developerKey=api_key)#api key assigned as the developer key   

# fetch comment data
  for i in v_id:
    
    comment_request = youtube.commentThreads().list(
      part="snippet",
      videoId=i,
      maxResults=50
    )
    response_4 = comment_request.execute()
# convert comment details into dictionary format      
    cmd={
         'Video_id':response_4['items'][0]['snippet']['videoId'],
         'Comment_Id':response_4['items'][0]['snippet']['topLevelComment']['id'],
         'Comment_Text':response_4['items'][0]['snippet']['topLevelComment']['snippet']['textOriginal'],
         'Comment_Author':response_4['items'][0]['snippet']['topLevelComment']['snippet']['authorDisplayName'],
        'Comment_Published':response_4['items'][0]['snippet']['topLevelComment']['snippet']['publishedAt']
        }
    
    comment_data.append(cmd) 
  return comment_data

# pprint() for readable and prettyway
# from pprint import pprint
comment_details(v_id)


#Main Function

def main(channel_id):

 d = {

   'channel_data':channel_details(channel_id),
   'video_data':video_details(v_id),
   'comment_data':comment_details(v_id)
   }
 return d

main("UCeoRAN5sr02w8_9aFWxIM4g")

#-------------------------------------MongoDB connection---------------------------------------------------

import pymongo
# mongodb connection
client = pymongo.MongoClient('mongodb://localhost:27017/')
#create a database for connection
mydb = client['Youtube_db']

def full_details(channel_id):
    ch_de = channel_details(channel_id)
    vi_de = video_details(v_id)
    co_de = comment_details(v_id)

    
    collection_1 = mydb['Youtube_data']

    collection_1.insert_one({"channel_information":ch_de,
                             "video_information":vi_de,
                            "comment_information":co_de})
    return "updated"

full_details("UCeoRAN5sr02w8_9aFWxIM4g")

#--------------------MySQL Connection---------------------------------------

#--------------- create channel table-----------------------

#!pip install mysql-connector-python

import mysql.connector

# database connecton 
 # connect with mysql
mydb = mysql.connector.connect(     # here the mydb is a variable
           host="localhost",
            user="root",
            password="",
            database= "Youtube"
)

#mycursor = mydb.cursor()
# # create table for channel data


# Demo = '''create table Channel(
#     channel_name varchar(100), 
#     channel_description text,
#     channel_published timestamp,
#     playlist_id varchar(100),
#     subscribers_count int,
#     video_count int,
#     view_count int)'''
# mycursor.execute(Demo)                
# mydb.commit()

#-------------Convert details info dataframe (row and column format)-----------------
# calling the mongodb database
mydb = client["Youtube_db"]       
collection_1 = mydb['Youtube_data']


# database connecton 
 # connect with mysql
mydb = mysql.connector.connect(     # here the mydb is a variable
           host="localhost",
            user="root",
            password="",
            database= "Youtube"
)

mycursor = mydb.cursor()
# create table for channel data

                   
ch_list = []
for ch_de in collection_1.find({},{"_id":0,"channel_information":1}):
  ch_list.append(ch_de["channel_information"]) 

# convert to dataframe
df1 = pd.DataFrame(ch_list)
df1


# # insert channel details into mysql table 'channel'
# for index,row in df1.iterrows():    # 
 
#   insert_ch = '''INSERT into channel(channel_name,
#                                    channel_description,
#                                    channel_published,
#                                    playlist_id,
#                                    subscribers_count,
#                                    video_count,
#                                     view_count)
#                 values(%s,%s,%s,%s,%s,%s,%s)'''

#   values =(
#         row['channel_name'],
#         row['channel_description'],
#         row['channel_published'],
#         row['playlist_id'],
#         row['subscribers_count'],
#         row['video_count'],
#         row['view_count'])
    
# mycursor.execute(insert_ch,values)                
# mydb.commit()

#--------------- create video table-----------------------

# database connecton 
 # connect with mysql
mydb = mysql.connector.connect(     # here the mydb is a variable
           host="localhost",
            user="root",
            password="",
            database= "Youtube"
 )

mycursor = mydb.cursor()
# create table for channel data


# v_table = '''create table video(
#     video_name varchar(500), 
#     video_Id varchar(255) primary key,
#     video_description text,
#     published_date datetime,
#     view_count int,
#     like_count int,
#     dislike_Count int,
#     favorite_Count int,
#     comment_count int,
#     duration int,
#     thumbnail varchar(255),
#     caption_status varchar (255))'''
# mycursor.execute(v_table)                
# mydb.commit()


mydb = mysql.connector.connect(     # here the mydb is a variable
           host="localhost",
            user="root",
            password="",
            database= "Youtube"
   )


mycursor = mydb.cursor()


# convert to data frame
vi_list = []
for vi_de in collection_1.find({},{"_id":0,"video_information":1}):
    for i in range(len(vi_de["video_information"])):
       vi_list.append(vi_de["video_information"][i]) 

# convert to dataframe
df2 = pd.DataFrame(vi_list)
df2
#  #insert video details into mysql table 'video'
# for index, row in df2.iterrows():    

#     insert_vi ='''INSERT into video(video_name, 
#                                   video_Id,
#                                   video_description,
#                                   published_date,
#                                   view_count,
#                                   like_count,
#                                   dislike_Count,
#                                   favorite_Count,
#                                   comment_count,
#                                   duration,
#                                   thumbnail,
#                                   caption_status)           
#                     values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''

#     values =(
#            row['video_name'],
#            row['video_Id'],
#            row['video_description'],
#            row['published_date'],
#            row['view_count'],
#            row['like_count'], 
#            row['dislike_Count'],
#            row['favorite_Count'],
#            row['comment_count'],
#            row['duration'],
#            row['thumbnail'],
#            row['caption_status'])
          
    
# mycursor.execute(insert_vi,values)                
# mydb.commit()

#------------------------------------comment table -------------------------------------------------

mydb = mysql.connector.connect(     # here the mydb is a variable
           host="localhost",
           user="root",
           password="",
           database= "Youtube"
)

# mycursor = mydb.cursor()

# c_table = '''create table comment(Video_id varchar(255), 
#                                  Comment_Id varchar(255) primary key,
#                                  Comment_Text text,
#                                  Comment_Author varchar(255),
#                                  Comment_Published datetime)'''
    
# mycursor.execute(c_table)                
# mydb.commit()

mydb = client["Youtube_db"]       
collection_1 = mydb['Youtube_data']

mydb = mysql.connector.connect(     # here the mydb is a variable
           host="localhost",
            user="root",
            password="",
            database= "Youtube"
)


mycursor = mydb.cursor()

com_list = []
for co_de in collection_1.find({},{"_id":0,"comment_information":1}):
 for i in range(len(co_de["comment_information"])):
    com_list.append(co_de["comment_information"][i])
df3 = pd.DataFrame(com_list)
df3
# for index, row in df3.iterrows():    
#  insert_co  = '''INSERT into comment(Video_id,
#                                   Comment_Id, 
#                                   Comment_Text,
#                                   Comment_Author,
#                                   Comment_Published) 
#                         VALUES(%s, %s, %s, %s, %s) '''
    
#  values =(
#            row['Video_id'],
#            row['Comment_Id'],
#            row['Comment_Text'],
#            row['Comment_Author'],
#            row['Comment_Published'])
          
    
# mycursor.execute(insert_co,values)                
# mydb.commit()

#---------------Queries-----------

import streamlit as st

def show_channels_table():
    ch_list = []
    for ch_de in collection_1.find({},{"_id":0,"channel_information":1}):
      ch_list.append(ch_de["channel_information"]) 
    
    # convert to dataframe
    df1 = st.dataframe(ch_list)

    return df1
def show_videos_table():
    vi_list = []
    for vi_de in collection_1.find({},{"_id":0,"video_information":1}):
        for i in range(len(vi_de["video_information"])):
           vi_list.append(vi_de["video_information"][i]) 
    
    # convert to dataframe
    df2 = st.dataframe(vi_list)

    return df2
def show_comments_table():
    com_list = []
    for co_de in collection_1.find({},{"_id":0,"comment_information":1}):
     for i in range(len(co_de["comment_information"])):
       com_list.append(co_de["comment_information"][i])
    df3 = st.dataframe(com_list)

    return df3

#--------------------Streamlit part------------------------------------------

with st.sidebar:
    st.title(":blue[YOUTUBE DATA HARVESTING AND WAREHOUSING]")
    st.header("Skills About Python")
    st.caption('Python coding')
    st.caption("Data Collection")
    st.caption("MongoDB")
    st.caption("API Integration")
    st.caption(" Data Managment using MongoDB and SQL")

channel_ID = st.text_input("Enter the Channel id")

if st.button("Collect and Store data"):
    ch_ids = []
    mydb = client["Youtube_db"]       
    collection_1 = mydb['Youtube_data']

    for ch_de in collection_1.find({},{"_id":0,"channel_information":1}):
      ch_ids.append(ch_de["channel_information"]["channel_id"])
    if channel_ID in ch_ids:
       st.success("Channel details of the given channel id: " + channel + " already exists")
    else:
        insert = Youtube_data(channel_ID)
        st.success(insert)



if st.button("Migrate to SQL"):
 display = tables()
 st.success(display)

show_table = st.radio("SELECT THE TABLE FOR VIEW",(":green[channels]",":red[videos]",":blue[comments]"))

if show_table == ":green[channels]":
    show_channels_table()
elif show_table ==":red[videos]":
    show_videos_table()
elif show_table == ":blue[comments]":
    show_comments_table()
#sql connection
mydb = mysql.connector.connect(     # here the mydb is a variable
           host="localhost",
           user="root",
           password="",
           database= "Youtube"
)

mycursor = mydb.cursor()

question = st.selectbox(
    'Please Select Your Question',
    ('1. All the videos and the Channel Name',
     '2. Channels with most number of videos',
     '3. 10 most viewed videos',
     '4. Comments in each video',
     '5. Videos with highest likes'))
     

     
if question == "1. All the videos":
    query1 = "select video_name from video;"
    cursor.execute(query1)
    mydb.commit()
    t1=cursor.fetchall()
    st.write(pd.DataFrame(t1, columns=["video_name"]))

elif question == '2. Channels with most number of videos':
    query2 = "select channel_name,video_count from channel order by video_count desc;"
    cursor.execute(query2)
    mydb.commit()
    t2=cursor.fetchall()
    st.write(pd.DataFrame(t2, columns=["Channel Name","No Of Videos"]))

elif question == '3. 10 most viewed videos':
    query3 = '''select view_count,video_name from video 
                        where view_count is not null order by view_count desc limit 10;'''
    cursor.execute(query3)
    mydb.commit()
    t3 = cursor.fetchall()
    st.write(pd.DataFrame(t3, columns = ["views","video title"]))

elif question == '4. Comments in each video':
    query4 = "select comments_text from comments;"
    cursor.execute(query4)
    mydb.commit()
    t4=cursor.fetchall()
    st.write(pd.DataFrame(t4, columns=["No Of Comments"]))

elif question == '5. Videos with highest likes':
    query5 = '''select video_name,like_count from videos 
                       order by like_count desc;'''
    cursor.execute(query5)
    mydb.commit()
    t5 = cursor.fetchall()
    st.write(pd.DataFrame(t5, columns=["video Title","like count"]))

























