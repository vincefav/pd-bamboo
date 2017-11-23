def absolute_correlations(col, df=data):
    #absolute_values = np.abs(df[col])
    corrs = pd.DataFrame(df.select_dtypes(include=[np.number]).corrwith(df[col]), columns=['correlation'])
    corrs['absol'] = np.abs(corrs['correlation'])
    return corrs.sort_values('absol', ascending=False).drop('absol', axis=1).tail(len(corrs)-1)

def numeric(self):
    return self.select_dtypes(include=[np.number])
pd.DataFrame.numeric = numeric
	
def correlation_matrix(df, figsize=(15,7)):
    # Generate a mask for the upper triangle
    mask = np.zeros_like(df.corr(), dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    # Resize and display
    plt.figure(figsize=figsize)
    sns.heatmap(df.corr(), annot=True, fmt='.2f', mask=mask, cmap='seismic_r')
	
def tts(x_data=x, y_data=y, test_size=.2):
    from sklearn.model_selection import train_test_split
    global xtrain
    global xtest
    global ytrain
    global ytest
    xtrain, xtest, ytrain, ytest = train_test_split(x_data, y_data, test_size=test_size)
	
def sort_dict(user_dict, ascending=False):
	import operator
	return sorted(user_dict.items(), key=operator.itemgetter(1), reverse=not ascending)

def clean_column_names(df=data):
	from string import punctuation
    df.columns = df.columns.str.strip().str.lower()
    for i in list(punctuation):
        if i != '_':
            df.columns = df.columns.str.replace(i, '')

    df.columns = df.columns.str.replace(" ", '_')
    return df