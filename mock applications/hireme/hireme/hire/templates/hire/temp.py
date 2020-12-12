df_bow = df-bow.merge(df_popular, left_index = True, right_index = True)
df_bow[‘high_interest’] = df_bow[‘target_reg’] + df_bow[‘total_c’] > 100
df_word_prob = df_bow.groupby(‘high_interest’).agg([‘sum’])
df_word_prob = df_word_prob.transpose()
df_word_prob['prob']=df_word_prob.iloc[:,1]/(df_word_prob.iloc[:,0]+df_word_prob.iloc[:,1])
df_word_prob.drop(['target_reg','total_c'], axis=0, inplace= True)
df_word_prob['word']= range(0,200,1)
plt.figure(figsize=(8,5))
plt.bar(df_word_prob['word'], df_word_prob['prob'])
plt.xlabel('Keywords', size = 14)
plt.ylabel('Probability of high internet posts', size = 14)
plt.show()

original_probablility=df3.high_interest['sum'].sum()/df3.Day_P['count'].sum()

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
new_probability_d = df3.loc[weekdays].high_interest['sum'].sum()/df3.loc[weekdays].Day['count'].sum()
df_length['optimal'] = ((df_length.length > 4000) & (df_length.length < 6500))
original_probability = df_length.high_interest.sum()/df_length.shape[0]
new_probability_l = df_length[df_length.optimal == True].high_interest.sum()/df_length.optimal.sum()

original_probability = df_bow.high_interest.sum()/df_bow.shape[0]
topwords = df_word_prob.sort_values('prob', ascending = False).iloc[0:20].word
df_bow['twenty_top'] = df_bow.iloc[:,topwords].sum(axis = 1) > 0
df_prob2 = df_bow.groupby('twenty_top').agg({'high_interest':'sum'})
new_probability_w = df_prob2.iloc[1].sum()/df_bow['twenty_top'].sum()

df_comb = df_weekday_P[['Day', 'high_interest']]
df_comb['optimal_l'] = df_length.loc[:,'optimal']
df_comb['twenty_top'] = df_bow.loc[:,'twenty_top']
df_comb['All'] = df_comb.loc[:,'optimal_l'] & df_comb.loc[:,'twenty_top'] & df_comb.Day.isin(weekdays)
hits = df_comb[df_comb.All == True].high_interest.sum()
all_posts = df_comb[df_comb.All == True].high_interest.count()
final_probability = hits/all_posts


print('Baseline probability of popular post:'+str(original_probablility)+ '\n')
print('Probability of popular post published on weekdays only:'+str(new_probablility_d)+ '\n')
print('Probability of popular post with 4500 - 6500 words only:'+str(new_probablility_l)+ '\n')
print('Probability of popular post with 20 top keywords:'+str(new_probablility_w)+ '\n')
print('Probability of popular post if all of above satisfied:'+str(final_probablility)+ '\n')