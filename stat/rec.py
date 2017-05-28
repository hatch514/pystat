import pandas as pd
import numpy as np
import scipy.spatial.distance as sci
import pdb


def read_file():
  rows = ['user_id', 'movie_id', 'rating', 'timestamp']
  df = pd.read_csv('../ml-100k/u.data', sep='\t', names=rows)
  df = df.sort_values(['user_id', 'movie_id'])
  df = df.pivot(index='user_id', columns='movie_id', values='rating')
  return df


def calc_similarity(df):
  tupple = df.shape
  users = tupple[0]
  movies = tupple[1]
  res_array = np.array([])
  for user in xrange(1, users + 1):
    print user
    non_zero_part = np.array([sci.pdist(df.loc[[user, other_user]].dropna(axis=1)) for other_user in xrange(user+1, users+1)])
    res_array =  np.append(res_array, non_zero_part)
  result_df = pd.DataFrame(sci.squareform(resarray))
  return result_df



def main():
  df = read_file()  
  df = calc_similarity(df)
  print df


if __name__ == "__main__":
  count = 0
  main()
