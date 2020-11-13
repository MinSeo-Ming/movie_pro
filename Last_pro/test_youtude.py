from pytchat import LiveChat
import pafy
import pandas as pd

pafy.set_api_key('AIzaSyBVcDkUJnBLYaHHKgj5igSSEaLlxmhFKBk')
#https://www.youtube.com/watch?v=SX7EnUYfb1I&ab_channel=%EC%9C%A0%ED%80%B4%EC%A6%88%EC%98%A8%EB%8D%94%ED%8A%9C%EB%B8%8C
video_id='SX7EnUYfb1I'
v = pafy.new(video_id)
title = v.title
author = v.author
published = v.published

print(title)
print(author)
print(published)

empty_frame = pd.DataFrame(columns=['제목', '채널 명', '스트리밍 시작 시간', '댓글 작성자', '댓글 내용', '댓글 작성 시간'])
empty_frame.to_csv('./youtube.csv')
