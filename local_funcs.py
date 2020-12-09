'''
Local functions that we might want to use in multiple scripts throughout the
Music-Coronavirus project
# Lauren Fink
# lauren.fink@ae.mpg.de
'''

import os
from IPython.display import Image, HTML
import numpy as np
from collections import Counter
import seaborn as sns
import pandas as pd
import math
import local_dicts
import statistics
import matplotlib.pyplot as plt



# ---------------------------------------------------------------------------- #
#                            Cleaning Functions
# ---------------------------------------------------------------------------- #

''' Check for any word in specific col of a data frame.
Input:
- string to check for
- dataframe
- column to check
Output:
- indices of rows containing the string'''
def check_for_word(val, df, col):
    a = df.index[df[col].str.contains(val, na=False)]
    if a.empty:
        return 'not found'
    elif len(a) > 1:
        return a.tolist()
    else:
        return a.item()


#------------------------------------------------------------------------------#
'''Function of LW to determine if any values are outliers.
# A good *a priori* rationale to delete participants is if they are outliers in some pre-defined way.
# Here, outlier is defined as a value more than 3 interquartile ranges away from the mean.

Takes a dataframe df of features and returns a list of the indices
corresponding to the observations containing more than n outliers according
to the Tukey method.'''
def detect_outliers(df, n, features):

    outlier_indices = []
    # iterate over features(columns)
    for col in features:
        # 1st quartile (25%)
        Q1 = np.percentile(df[col], 25)
        # 3rd quartile (75%)
        Q3 = np.percentile(df[col], 75)
        # Interquartile range (IQR)
        IQR = Q3 - Q1
        # outlier step
        outlier_step = 3 * IQR
        # Determine a list of indices of outliers for feature col
        outlier_list_col = df[(df[col] < Q1 - outlier_step) | (df[col] > Q3 + outlier_step )].index
        # append the found outlier indices for col to the list of outlier indices
        outlier_indices.extend(outlier_list_col)
    # select observations containing more than 2 outliers
    outlier_indices = Counter(outlier_indices)
    multiple_outliers = list( k for k, v in outlier_indices.items() if v > n )
    return multiple_outliers




#------------------------------------------------------------------------------#
'''
Clean up free responses
Input:
- dataframe
- column to clean
Output:
- cleaned column


Clean the text columns using these steps:
- Make everything lower case
- Replace new line symbols (\n) with dashes (-) to make it easier to read
- Delete non-ASCII characters
- Remove some characters like * and „ because sometimes Excel doesn't handle these characters well
- Remove the white spaces at the beginning and ends of responses
'''
def textCleaning(data, colName):
    colName = data.columns.get_loc(colName)

    data.iloc[:,colName] = data.iloc[:,colName].str.lower()
    data.iloc[:,colName] = data.iloc[:,colName].str.replace(r'\n', '-', regex=True)
    data.iloc[:,colName] = data.iloc[:,colName].str.replace(r'[^\x00-\x7f]', '')
    data.iloc[:,colName] = data.iloc[:,colName].str.replace(r"[\/*„:;?<>{}]", "", regex=True)
    data.iloc[:,colName] = data.iloc[:,colName].str.strip()

    return(data.iloc[:,colName])


#------------------------------------------------------------------------------#
def melt_category(df, key):
# function to organize by question with sub questions
# key input should be the unique header in the col name, e.g. 'Activities_'
# output will be long from df with country still included

    # get all col names with this keyword
    newcols = [col for col in df.columns if col.startswith(key)]

    # deal with some bad keys (TODO could consider renaming all cols but don't want to break other code)
    if key == 'Demographics_Health_':
        newcols = [x for x in newcols if not x.startswith('Demographics_Health_Infected')]

    # extract relevant data
    newcols.append('Demographics_COVID_Current Country') # keep country
    new_df = df[newcols]

    # clean up any missing values
    new_df = new_df.replace({99:np.nan})
    new_df = new_df.replace({0:np.nan})

    # melt to long form for future plotting
    final_df = new_df.melt(id_vars='Demographics_COVID_Current Country')
    return final_df



# ---------------------------------------------------------------------------- #
# Convert 7pt ratings to change scores
def to_change_score(df, cols, label):

    # Input:
    # - dataframe
    # - columns to convert
    # - label for new column to add to the data frame (which will be label + '_changeScore')

    # Output:
    # - same df with columns converted to change scores and new column added.
    for col in cols:
#         df[col] = df[col].replace({99:np.nan}) # NOTE: 20201111 - don't think we use this function in anything for the paper but since we have added this recoding to preproc script, no longer need it here. 
#         df[col] = df[col].replace({0:np.nan})
        #df[col] = abs(df[col] - 4)
        df[col] = df[col] - 4
        newstr = label + '_changeScore'
        df[newstr] = df[cols].sum(axis = 1, skipna=True, numeric_only=True)

    # rearrange columns to be in alphabetical order
    df = df.reindex(sorted(df.columns), axis=1)

    return df






#------------------------------------------------------------------------------#
#                       Plotting Functions
#------------------------------------------------------------------------------#
# function to map numeric categorical data back onto labels and plot sns countplot
# Input: data frame, column of interest, x axis label to plot, title to plot, flag whether plot should be percent or count (1 if percent)
def map_and_plot(df, col, xlab, title, percent):

    if percent:
        ax = sns.barplot(x=col, y=col, data=df, estimator=lambda x: len(x) / len(df) * 100)
        if 'edu' in col:
            ax.set(xticklabels=local_dicts.edu_dict[col].values())
        else:
            ax.set(xticklabels=local_dicts.answer_code_dict[col].values())
        ax.set(xlabel=xlab, ylabel='Percent',title=title)
    else:
        newcol = df[col].map(local_dicts.answer_code_dict[col])
        newcol.fillna('Other', inplace = True)
        ax = sns.countplot(newcol)
        ax.set(xlabel=xlab, ylabel='Count',title=title)

    for p in ax.patches:
        ax.text(p.get_x() + p.get_width()/2., p.get_height(), '{0:.2f}'.format(p.get_height()),
            fontsize=12, color='black', ha='center', va='bottom')
    sns.despine()

    return ax


#------------------------------------------------------------------------------#
# function to map numeric categorical data back onto labels and plot sns countplot
# Input: data frame, column of interest, x axis label to plot, title to plot, flag whether plot should be percent or count (1 if percent)
def map_and_plot_byCountry(df, col, xlab, title, ptype, standard):
    # Specify ptype as:
    # - perc = percentage of col of interest for each country
    # - mean = mean and std of col of interest for each country
    # - standard is flag as to whether we should look in dictionary for x labels (no if standard = 1)

    # initialize figure
    f,ax = plt.subplots(figsize=(11, 9))

    # map country to string (easier for plot legends)
    df['Country'] = df['Demographics_COVID_Current Country'].map(local_dicts.answer_code_dict['Demographics_COVID_Current Country'])
    df = df.sort_values(by=['Country']) # do this to ensure country always plotted in same color

    # plot by requested type

    # percentage by country
    if ptype == 'perc' or ptype == 'count':

        if ptype == 'perc':
            #ax = sns.barplot(x=col, y=col, data=df, hue='Country', estimator=lambda x: len(x) / len(df) * 100)
            #ax = sns.barplot(x=col, y=col, data=df, estimator=lambda x: len(x) / len(df) * 100)
            # AHH NOTE TODO CHECK - can't do length df because need to do len by country

            prop_df = (df[col]
               .groupby(df['Country'])
               .value_counts(normalize=True)
               .rename('prop')
               .reset_index())
            prop_df['prop'] = prop_df['prop'] * 100

            ax = sns.barplot(x=col, y='prop', hue='Country', data=prop_df)

            ylab = 'Percent'

        if ptype == 'count':
            ax = sns.countplot(x=col, data=df, hue='Country')
            ylab = 'Count'

        # print number at top of bar
        for p in ax.patches:
            ax.text(p.get_x() + p.get_width()/2., p.get_height(), '{0:.1f}'.format(p.get_height()),
                fontsize=12, color='black', ha='center', va='bottom')


    elif ptype == 'violin':
        ax = sns.violinplot(x='Country', y=col, data=df)
        ylab = 'Mean Rating'

    # mean by country
    elif ptype == 'mean':
        # md = pd.melt(df, id_vars="Country", value_vars=col)
        # ax = sns.barplot(x="value", y="value", hue='Country', data=md);
        ax = sns.barplot(x='Country', y=col, data=df)#, hue='Country')#, estimator=lambda x: statistics.mean(x))
        ax.set(ylabel='Mean Rating',title=title)


    else:
        raise Warning('unrecognized plot type')

    # remap labels if this is education plot
    if not standard:
        if 'edu' in col:
            ax.set(xticklabels=local_dicts.edu_dict[col].values())
        else:
            ax.set(xticklabels=local_dicts.answer_code_dict[col].values())
            ax.set(xlabel=xlab, ylabel=ylab,title=title)



    # add additional elements to plot
    sns.despine()
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right');
    f.tight_layout()

    # legend
    # TODO - only deal with legend if we have one
    # leg = ax.get_legend()
    # leg.set_title("Country")

    return f, ax

# ---------------------------------------------------------------------------- #
# Correlation matrix
def corr_mat_plot(df):
    corr = df.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=np.bool))

    # Plot
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    ax = sns.heatmap(corr, mask=mask, cmap=cmap,
                square=True, linewidths=.5, cbar_kws={"shrink": .5}, annot=True, vmin=-1, vmax=1, center=0)

    return ax


# ---------------------------------------------------------------------------- #
# horizontal bar plot
def hor_bar_plot(df, ylab, title, scale_dict, dictmin, dictmax):
    ax = sns.barplot(x="value", y="variable", data=pd.melt(df));
    ax.set(xlabel='Rating', ylabel=ylab,title=title);
    #ax.set(xlim=(1,7))
    xlabs = list(scale_dict.values())
    xlabs = xlabs[dictmin:dictmax]
    ax.set(xticklabels=xlabs);
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90);
    return ax


# ---------------------------------------------------------------------------- #
# horizontal bar plot
def hor_bar_plot_byCountry(df, ylab, title, scale_dict, dictmin, dictmax):
    # NOTE: using dictmin and max because some scales have ends that we might not want to keep, like "never do this" or "prefer not to say"
    # TODO: could grab values from scale dict right? although still might want more control

    # initialize figure
    f,ax = plt.subplots(figsize=(11, 45))

    # map country to string (easier for plot legends)
    df['Demographics_COVID_Current Country'] = df['Demographics_COVID_Current Country'].map(local_dicts.answer_code_dict['Demographics_COVID_Current Country'])
    df = df.sort_values(by=['Demographics_COVID_Current Country'])

    # plot
    ax = sns.barplot(x="value", y="variable", hue = 'Demographics_COVID_Current Country', data=df);

    # add labels
    ax.set(xlabel='Rating', ylabel=ylab,title=title);
    xlabs = list(scale_dict.values())
    xlabs = xlabs[dictmin:dictmax]
    ax.set(xticklabels=xlabs);
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right');
    # legend
    leg = ax.get_legend()
    leg.set_title("Country")

    return f, ax


def hor_bar_plot_byCountry_and_musBehave(len, wid, df1_playing, df2_listening, ylab, title, scale_dict, dictmin, dictmax):
    # TODO
    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(len, wid))

    plt.subplot(121)
    ax1 = sns.barplot(x="value", y="variable", data=df1_playing, hue = 'Demographics_COVID_Current Country')#, ax = ax2)
    plt.subplot(122)
    ax2 = sns.barplot(x="value", y="variable", data=df2_listening, hue = 'Demographics_COVID_Current Country')#, ax = ax1)

    #ax1.set(xlabel='Rating', ylabel='Function',title='Functions of music listening and playing');
    ax1.set(xlim=(1,7))
    ax1.set(xlabel='Rating', ylabel=ylab,title=title);
    xlabs = list(scale_dict.values())
    xlabs = xlabs[dictmin:dictmax]
    ax1.set(xticklabels=xlabs);
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right');

    # legend
    leg = ax1.get_legend()
    leg.set_title("Country")

    # clean up


    return f, ax1, ax2

# ---------------------------------------------------------------------------- #
# print value counts
# important to have these output in question text order, otherwise jarbled. That is why dropping NA (because no NA mapping in answer code dicts)
def map_and_print(df, col, printstr):
    print(printstr, '\n')

    keys = df[col].value_counts(normalize=True, sort=False).sort_index().keys().tolist()
    counts = df[col].value_counts(normalize=True, sort=False).sort_index().tolist()

    for k,c in zip(keys,counts):
        print(k, ':', local_dicts.answer_code_dict[col][k], ':', round(c*100,2), '%', '\n')

    print('\n')




# ---------------------------------------------------------------------------- #
# View tab (Taken from Martin: https://stackoverflow.com/users/2575273/martin)
def View(df):
    css = """<style>
    table { border-collapse: collapse; border: 3px solid #eee; }
    table tr th:first-child { background-color: #eeeeee; color: #333; font-weight: bold }
    table thead th { background-color: #eee; color: #000; }
    tr, th, td { border: 1px solid #ccc; border-width: 1px 0 0 1px; border-collapse: collapse;
    padding: 3px; font-family: monospace; font-size: 10px }</style>
    """
    s  = '<script type="text/Javascript">'
    s += 'var win = window.open("", "Title", "toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=yes, resizable=yes, width=780, height=200, top="+(screen.height-400)+", left="+(screen.width-840));'
    s += 'win.document.body.innerHTML = \'' + (df.to_html() + css).replace("\n",'\\') + '\';'
    s += '</script>'
    return(HTML(s+css))
files = os.listdir(os.curdir)


# ---------------------------------------------------------------------------- #
# Function to rank items in category
# Input:
# - df, category keyword (e.g. 'Activities_'), new column label, flag to rank based on mean change score or absolute value of change score
# Output:
# - column of rankings, rank at which the mean switches from positive to negative (if any)
def rank_cols(data, keyword_str, colstring, abs_flag):
    ml = [col for col in data.columns if col.startswith(keyword_str)]
    mld = data[ml]
    # NOTE - double check scales of variables inputting into function
    # mld = mld.replace({99:np.nan, 0:4}) # replace never do this with 4 (no change) 
    # ^ don't need this anymore because added to preproc script
    mld = mld.dropna()
    mld = mld.reset_index(drop = True)
    mld = mld - 4

    # Display size of data frame and percent responses no change
    print(mld.shape)
    print('percent no change:', mld.isin([0]).sum().sum() / (mld.shape[0]*mld.shape[1]))

    # if user wants ranks from absolute values, rather than change scores with directionality
    if abs_flag:
        mld = abs(mld)
    ranked = mld.mean().rank(ascending=False)
    ranked = pd.DataFrame(ranked, columns=[colstring])

    means = mld.mean()

    # check for means that are negative
    if any(means < 0):
        print('Some means < 0')
        changepoint = max(means[means<0]) # find value where we switch to negative
        changeind = list(means).index(changepoint)
        changerank = ranked[colstring][changeind]
    else:
        changerank = 99 # no change flag

    return ranked, changerank



# ---------------------------------------------------------------------------- #
# Function to return rankings to user
# Input:
# - df, category keyword (e.g. 'Activities_')
# Output:
# - rankings for each country
def return_ranks(data, keyword):

    #all_ranks_abs = rank_cols(data, keyword, 'All_Countries', 1)
    all_ranks_change, chgrank = rank_cols(data, keyword, 'All_Countries', 0)\

    # find change point where across all countries things get negative

    # loop through all countries
    countries = data['Country_Country Name'].unique()
    for i in countries:
        print('\n',i)
        newdata = data[data['Country_Country Name'] == i]
        #ranked_abs = rank_cols(newdata, keyword, i, 1)[0]
        ranked_change = rank_cols(newdata, keyword, i, 0)[0]
        #all_ranks_abs = all_ranks_abs.join(ranked_abs)
        all_ranks_change = all_ranks_change.join(ranked_change)

    # drop all country rank (don't need)
    #all_ranks_abs = all_ranks_abs.drop(columns = ['All_Countries'], axis = 1)
    all_ranks_change = all_ranks_change.drop(columns = ['All_Countries'], axis = 1)

    # remove tag from index labels
    #all_ranks_abs.index = all_ranks_abs.index.str.split(keyword).str[1].str.lower()
    all_ranks_change.index = all_ranks_change.index.str.split(keyword).str[1].str.lower()

    return all_ranks_change, chgrank#, all_ranks_abs




# ---------------------------------------------------------------------------- #
''' Function to plot rankings
Input:
- df of ranks for each country in one category,
- category keyword (e.g. 'Activities_'),
- rank at which sign changes,
- flag whether using abs value or not
- figure file type to output (e.g. '.png')
- resolution of figure in dpi (e.g. 300)
Output:
- plot of ranks for each country, sorted by median rank across countries
'''
def plot_ranks(ranked_df, keyword, changerank, abs_flag, ftype, dpi):

    # Organize data for plotting
    means = ranked_df.median(axis=1)
    means.sort_values(ascending=True, inplace=True)
    df = ranked_df
    df['item'] = ranked_df.index
    df = df.melt(id_vars='item')

    # Plot
    f,ax = plt.subplots(figsize=(11,means.shape[0]/2))
    ax = sns.boxplot(x='value', y='item', data=df, order=means.index, color='white');
    ax = sns.swarmplot(y=df['item'], x=df['value'], hue=df['variable'], order=means.index, size=6)

    # Edit plot elements
    ax.set_yticks(np.arange(0, means.shape[0], step=1))
    ylabs = means.index.tolist()
    new_ylabs = []
    if keyword == 'Activities_':
        for string in ylabs:
            alphlower = {k.lower(): v for k, v in local_dicts.activities_rename_dict.items()}
            new_ylabs.append(alphlower[string])
    elif keyword == 'Music Listening_Functions_':
        for string in ylabs:
            alphlower = {k.lower(): v for k, v in local_dicts.mus_lis_funcs_rename_dict.items()}
            new_ylabs.append(alphlower[string])
    elif keyword == 'Making Music_Functions_':
        for string in ylabs:
            alphlower = {k.lower(): v for k, v in local_dicts.mus_lis_funcs_rename_dict.items()}
            new_ylabs.append(alphlower[string])
    elif keyword == 'Music Listening_Situations_':
        for string in ylabs:
            alphlower = {k.lower(): v for k, v in local_dicts.mus_lis_situations_rename_dict.items()}
            new_ylabs.append(alphlower[string])
    elif keyword == 'Music Listening_Formats_':
        for string in ylabs:
            alphlower = {k.lower(): v for k, v in local_dicts.mus_list_formats_rename_dict.items()}
            new_ylabs.append(alphlower[string])
    elif keyword == 'Making Music_Situations_':
        for string in ylabs:
            alphlower = {k.lower(): v for k, v in local_dicts.mus_make_forms.items()}
            new_ylabs.append(alphlower[string])
    else:
        for string in ylabs:
            new_string = string.replace(" i ", " I ")
            new_ylabs.append(new_string)

    ax.set_yticklabels(new_ylabs, ha='right');
    ax.set(ylabel=keyword.replace("_", " "), xlabel='Rank')#,title='Ranked change in importance, median-sorted');

    plt.xticks(np.arange(1, means.shape[0], step=5))
    ax.grid(False)
    sns.despine(left=True, bottom=True)
    ax.invert_xaxis()
    if 0 < changerank < 99:
        ax.axvline(x=changerank-.1, linestyle="dotted", color='0.5')
    if changerank == 0:
        ax.axvline(x=1, linestyle="dotted", color='0.5')
    leg = ax.get_legend()
    leg.set_title("Country")
    if means.shape[0]/2.5 >= 10:
        plt.legend(fontsize='medium', title='Country')
    else:
        plt.legend(fontsize='x-small', title='Country')

    f.tight_layout()

    # Create filename for plot
    if abs_flag:
        s =  '_ranked_abs'
    else:
        s = '_ranked'
    savestr = 'Figures/' + keyword + s + ftype
    #ax.get_legend().remove()
    f.savefig(savestr, dpi=dpi);

    return f, ax



# ---------------------------------------------------------------------------- #
''' Function to print spearman rank correlations, across countries / ratings
Input:
- df of ranks for each country in one category
Output:
- table and visualization of correlations
'''
def print_rank_corr(df):
    #print(all_ranks_change)
    res = df.corr(method='spearman')

    # Plot
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    ax = sns.heatmap(res, cmap=cmap,
                square=True, linewidths=.5, cbar_kws={"shrink": .5}, annot=True, vmin=-1, vmax=1, center=0)

    print('\nMean corr coef:', np.nanmean(res.values[np.triu_indices_from(res.values,1)]), '\n')

    print(df.rcorr(method='spearman', upper='pval', padjust='fdr_bh', stars = False))


# todo adjust all code in notebook to say local_funcs.function
# adjust plotting calls to include figtyp and dpi
