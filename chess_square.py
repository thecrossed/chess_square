
# coding: utf-8

# In[1]:


# https://www.kaggle.com/datasnaek/chess
import numpy as np
import pandas as pd # pandas
import csv
import re


# In[2]:


# 棋谱数据
# 切割每一局棋谱，得each_move
# 从每局的each_move list，提取square list
# 建 dict key(square) : value (count)
# 建新表， columns a,b,c,d,e,f,g,h；每一列为square occupied count
# 画图


# In[3]:


chess = pd.read_csv('games.csv')


# In[4]:


chess.head()


# In[5]:


# 棋谱数据
chess_moves = chess[['moves']].copy()


# In[6]:


chess_moves.head()


# In[7]:


# 切割每一局棋谱，得each_move list
def each_move(chess_moves):
    each = (chess_moves['moves']).split(' ')

    return each
chess_moves['each_move'] = chess_moves.apply(each_move, axis=1)


# In[8]:


chess_moves.head()


# In[9]:


# 从每局的each_move list，提取square list
def square(chess_moves):
    squares = []
    for m in chess_moves['each_move']:
        if m == 'O-O' or m == 'O-O+':
            if chess_moves['each_move'].index(m)%2 == 0:
                squares.append('g1')
                squares.append('f1')
            elif chess_moves['each_move'].index(m)%2 == 1:
                squares.append('g8')
                squares.append('f8')            
        elif m == 'O-O-O' or m =='O-O-O+':
            if chess_moves['each_move'].index(m)%2 == 0:
                squares.append('c1')
                squares.append('d1')
            elif chess_moves['each_move'].index(m)%2 == 1:
                squares.append('c8')
                squares.append('d8')             
        else:
            if '=' in m:
                squares.append(m.split('=')[0][-2:])
            elif m[-1] == '+' or m[-1] =='#':
                squares.append(m[-3:-1])           
            else:
                squares.append(m[-2:])

    return squares
chess_moves['square'] = chess_moves.apply(square, axis=1)

                if m == 'O-O':
                    if chess_moves['each_move'].index(m)%2 == 0:
                        squares.append('g1')
                        squares.append('f1')
                    elif chess_moves['each_move'].index(m)%2 == 1:
                        squares.append('g8')
                        squares.append('f8')
                elif m == 'O-O-O':  
                    if chess_moves['each_move'].index(m)%2 == 0:
                        squares.append('c1')
                        squares.append('d1')
                    elif chess_moves['each_move'].index(m)%2 == 1:
                        squares.append('c8')
                        squares.append('d8')  
                else:
                    squares.append(m[-3:-1])
# In[10]:


chess_moves.head()


# In[11]:


# 建 dict key(square) : value (count)
sq_count = {}
for s in chess_moves['square']:
    for i in s:
        sq_count[i] = sq_count.get(i, 0) + 1

for i in chess_moves['each_move']:
    for d in i:
        if '=' in d:
            print (d)
# In[14]:


sq_count

