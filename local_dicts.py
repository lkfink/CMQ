'''
Local functions that we might want to use in multiple scripts throughout the
Music-Coronavirus project
# Lauren Fink
# lauren.fink@ae.mpg.de
'''

# Imports
import math

#------------------------------------------------------------------------------#
#                 Column Headers Dictionary (Qualtrics data)
#------------------------------------------------------------------------------#

column_dict = {
  # Survey Info
  'Progress':'Survey Info_Progress', 'Duration (in seconds)':'Survey Info_Duration',
  'RecordedDate':'Survey Info_RecordedDate', 'EndDate': 'Survey Info_EndDate',

  # Demographics -- General
  '1':'Demographics_General_Age', '2':'Demographics_General_Gender',
  '3':'Demographics_General_Years of School', '4':'Demographics_General_Years of Post-School',

  # Demographics -- COVID
  '5':'Demographics_COVID_Employement Before COVID', '6':'Demographics_COVID_Profession',
  '7':'Demographics_COVID_Living Situation', '7_9_TEXT':'Demographics_COVID_Living Situation Free Response',
  '8a':'Demographics_COVID_Current Country', '8b':'Demographics_COVID_Current City Type',
  '8c_state':'Demographics_COVID_Current State',
  '9':'Demographics_COVID_Current Place Home', '10':'Demographics_COVID_Number Times Leave',
  '11':'Demographics_COVID_Ways Work Affected',

  # Activities
  '12_1':'Activities_Making Music', '12_2':'Activities_Music Listening',
  '12_3':'Activities_Searching for Music Info', '12_4':'Activities_Thinking About Music',
  '12_5':'Activities_Exercise Indoors', '12_6':'Activities_Exercise Outdoors',
  '12_7':'Activities_Visit People in Person', '12_8':'Activities_Call People',
  '12_9':'Activities_Cooking', '12_10':'Activities_Shopping Online',
  '12_11':'Activities_Watching Movies', '12_12':'Activities_Meditating',
  '12_13':'Activities_Learning New Skills', '12_14':'Activities_Reading Books',
  '12_15':'Activities_Virtual Exhibitions', '12_16':'Activities_Social Media',
  '12_17':'Activities_Playing Games', '12_18':'Activities_Watching News',
  '12_19':'Activities_Drugs or Alcohol', '12_20':'Activities_Volunteering',
  '12_21':'Activities_Gardening', '12_22':'Activities_Writing',
  '12_23':'Activities_Photography', '12_24':'Activities_Create Online Content',
  '12_25':'Activities_Sexual Activity', '12_26':'Activities_Cleaning',
  '12_27':'Activities_Crafting', '12_28':'Activities_Fashion',
  '12_29':'Activities_Online Dating',

  # Music Listening -- Formats
  '13_1':'Music Listening_Formats_Radio', '13_2':'Music Listening_Formats_TV Broadcasts',
  '13_3':'Music Listening_Formats_Owned Physical Music', '13_4':'Music Listening_Formats_Owned Digital Music',
  '13_5':'Music Listening_Formats_Free Streaming Others Playlists', '13_6':'Music Listening_Formats_Free Streaming Own Playlists',
  '13_7':'Music Listening_Formats_Paid Streaming Others Playlists', '13_8':'Music Listening_Formats_Paid Streaming Own Playlists',
  '13_9':'Music Listening_Formats_Free Livestreams', '13_10':'Music Listening_Formats_Paid Livestreams',
  '13_11':'Music Listening_Formats_Limited Time Programs', '13_12':'Music Listening_Formats_Always Available Programs',

  # Music Listening -- Situations
  '14_1':'Music Listening_Situations_Traveling', '14_2':'Music Listening_Situations_Housework',
  '14_3':'Music Listening_Situations_Working', '14_4':'Music Listening_Situations_Other Activities',
  '14_5':'Music Listening_Situations_Doing Nothing Else', '14_6':'Music Listening_Situations_Exercising',
  '14_7':'Music Listening_Situations_Dining', '14_8':'Music Listening_Situations_With Others',
  '14_9':'Music Listening_Situations_Alone', '14_10':'Music Listening_Situations_Morning',
  '14_11':'Music Listening_Situations_Evening', '14_12':'Music Listening_Situations_Sexual Activity',

  # Active Music Making -- Situations
  '15_1':'Making Music_Situations_Sing Alone', '15_2':'Making Music_Situations_Sing Together',
  '15_3':'Making Music_Situations_Sing Internet', '15_4':'Making Music_Situations_Balconies',
  '15_5':'Making Music_Situations_Play Alone', '15_6':'Making Music_Situations_Play Together',
  '15_7':'Making Music_Situations_Play Internet', '15_8':'Making Music_Situations_Perform For Others',
  '15_9':'Making Music_Situations_Dance Alone', '15_10':'Making Music_Situations_Dance Together',
  '15_11':'Making Music_Situations_Dance Internet', '15_12':'Making Music_Situations_Post Recordings',
  '15_13':'Making Music_Situations_Make Own Music',

  # Music Engagement during COVID
  '16':'Music Engagement_Engaging With Music Differently YN',
  '17':'Music Engagement_Engaging With Music Differently List',
  '18':'Music Engagement_Diversity of Music',
  '19':'Music Engagement_Nostalgic Music',
  '20_1':'Music Engagement_Interest in Others Music',

  # Active Music Making -- Hypotheses
  '21_1':'Making Music_Hypotheses_Feel Connected to Others',
  '21_2':'Making Music_Hypotheses_Serve as Social Interaction',
  '21_3':'Making Music_Hypotheses_Helps Me Cope',

  # Active Music Making -- Functions
  '22_1':'Making Music_Functions_Puts Me in a Good Mood', '22_2':'Making Music_Functions_Supports Me in a Bad Mood',
  '22_3':'Making Music_Functions_Helps Me Relax', '22_4':'Making Music_Functions_Energizes Me',
  '22_5':'Making Music_Functions_Provides an Aesthetic Experience', '22_6':'Making Music_Functions_Helps Me Understand My Feelings',
  '22_7':'Making Music_Functions_Is Enjoyable', '22_8':'Making Music_Functions_Provides a Good Background',
  '22_9':'Making Music_Functions_Makes Me Want to Move', '22_10':'Making Music_Functions_Helps Me Express My Identity',
  '22_11':'Making Music_Functions_Provides a Spiritual Experience', '22_12':'Making Music_Functions_Helps Distract Me',
  '22_13':'Making Music_Functions_Helps Me Identify with the Artist', '22_14':'Making Music_Functions_Stimulates Me Intellectually',
  '22_15':'Making Music_Functions_Reduces My Stress', '22_16':'Making Music_Functions_Enables Me to Vent Negative Emotions',
  '22_17':'Making Music_Functions_Provides Comfort', '22_18':'Making Music_Functions_Gives Meaning to My Life',
  '22_19':'Making Music_Functions_Creates a Personal Space', '22_20':'Making Music_Functions_Gives Me Sense of Control',
  '22_21':'Making Music_Functions_Makes Me Feel Good About Myself', '22_22':'Making Music_Functions_Helps Me Concentrate',
  '22_23':'Making Music_Functions_Helps Time Pass Quickly', '22_24':'Making Music_Functions_Helps Me Dwell on My Worries',
  '22_25':'Making Music_Functions_Gives Me New Perspectives', '22_26':'Making Music_Functions_Helps Me Accept My Situation',
  '22_27':'Making Music_Functions_Feel Like I Have Company', '22_28':'Making Music_Functions_Reminiscent of Positive Times',
  '22_29':'Making Music_Functions_Feel Like I Am Sharing My Experience', '22_30':'Making Music_Functions_Moves Me Emotionally',
  '22_31':'Making Music_Functions_Feel Like I Understand Others', '22_32':'Making Music_Functions_Feel Connected to My Culture',
  '22_33':'Making Music_Functions_Feel Like Part of a Bigger Group', '22_34':'Making Music_Functions_Helps Me Fall Asleep',
  '22_35':'Making Music_Functions_Feel Less Lonely', '22_36':'Making Music_Functions_Lets Me Daydream',
  '22_37':'Making Music_Functions_Helps Keep a Routine', '22open':'Making Music_Functions_Free Response',

  # Music Listening -- Hypotheses
  '23_1':'Music Listening_Hypotheses_Feel Connected to Others',
  '23_2':'Music Listening_Hypotheses_Serve as Social Interaction',
  '23_3':'Music Listening_Hypotheses_Helps Me Cope',

  # Music Listening -- Functions
  '24_1':'Music Listening_Functions_Puts Me in a Good Mood', '24_2':'Music Listening_Functions_Supports Me in a Bad Mood',
  '24_3':'Music Listening_Functions_Helps Me Relax', '24_4':'Music Listening_Functions_Energizes Me',
  '24_5':'Music Listening_Functions_Provides an Aesthetic Experience', '24_6':'Music Listening_Functions_Helps Me Understand My Feelings',
  '24_7':'Music Listening_Functions_Is Enjoyable', '24_8':'Music Listening_Functions_Provides a Good Background',
  '24_9':'Music Listening_Functions_Makes Me Want to Move', '24_10':'Music Listening_Functions_Helps Me Express My Identity',
  '24_11':'Music Listening_Functions_Provides a Spiritual Experience', '24_12':'Music Listening_Functions_Helps Distract Me',
  '24_13':'Music Listening_Functions_Helps Me Identify with the Artist', '24_14':'Music Listening_Functions_Stimulates Me Intellectually',
  '24_15':'Music Listening_Functions_Reduces My Stress', '24_16':'Music Listening_Functions_Enables Me to Vent Negative Emotions',
  '24_17':'Music Listening_Functions_Provides Comfort', '24_18':'Music Listening_Functions_Gives Meaning to My Life',
  '24_19':'Music Listening_Functions_Creates a Personal Space', '24_20':'Music Listening_Functions_Gives Me Sense of Control',
  '24_21':'Music Listening_Functions_Makes Me Feel Good About Myself', '24_22':'Music Listening_Functions_Helps Me Concentrate',
  '24_23':'Music Listening_Functions_Helps Time Pass Quickly', '24_24':'Music Listening_Functions_Helps Me Dwell on My Worries',
  '24_25':'Music Listening_Functions_Gives Me New Perspectives', '24_26':'Music Listening_Functions_Helps Me Accept My Situation',
  '24_27':'Music Listening_Functions_Feel Like I Have Company', '24_28':'Music Listening_Functions_Reminiscent of Positive Times',
  '24_29':'Music Listening_Functions_Feel Like I Am Sharing My Experience', '24_30':'Music Listening_Functions_Moves Me Emotionally',
  '24_31':'Music Listening_Functions_Feel Like I Understand Others', '24_32':'Music Listening_Functions_Feel Connected to My Culture',
  '24_33':'Music Listening_Functions_Feel Like Part of a Bigger Group', '24_34':'Music Listening_Functions_Helps Me Fall Asleep',
  '24_35':'Music Listening_Functions_Feel Less Lonely', '24_36':'Music Listening_Functions_Lets Me Daydream',
  '24_37':'Music Listening_Functions_Helps Keep a Routine', '24open':'Music Listening_Functions_Free Response',

  # Music Engagement Open Ended
  '25':'Music Engagement_Other Ways Use Music Differently Free Response',
  '26':'Music Listening_Examples_Free Response',
  'Q105':'Making Music_Examples_Free Response',

  # Demographics -- Music
  '27':'Demographics_Music_Ollen', '28':'Demographics_Music_Make Music Alone or Together',
  '29_1':'Demographics_Music_Music Importance', '30':'Demographics_Music_Number of Concerts',

  # Demographics -- Health
  '31':'Demographics_Health_Infected with COVID', '32':'Demographics_Health_General Health',
  '33_1':'Demographics_Health_Positive Valence', '33_2':'Demographics_Health_Negative Valence',
  '33_3':'Demographics_Health_Stressed', '33_4':'Demographics_Health_Lonely',
  '33_5':'Demographics_Health_Anxious', '33_6':'Demographics_Health_Arousal',
  '33_7':'Demographics_Health_Depressed',
  '33_8':'Demographics_Health_Bored', # Melanie added bored for Ipsos versions

  # Demographics -- Personality (Big 5)
  '34_1':'Demographics_Personality_Reserved', '34_2':'Demographics_Personality_Trusting',
  '34_3':'Demographics_Personality_Thorough', '34_4':'Demographics_Personality_Relaxed',
  '34_5':'Demographics_Personality_Imaginative', '34_6':'Demographics_Personality_Outgoing',
  '34_7':'Demographics_Personality_Faults Others', '34_8':'Demographics_Personality_Lazy',
  '34_9':'Demographics_Personality_Nervous', '34_10':'Demographics_Personality_Few Artistic Interests',

  # Code for ESM Study
  '8a.1':'ESM_Mother', '8b.1':'ESM_Father',
  '8c':'ESM_Middle', '8d':'ESM_Town',
  'Random ID':'ESM_ID'
}

#------------------------------------------------------------------------------#
#                       Issues with specific questions
#------------------------------------------------------------------------------#
french_Q33_dict = {
    '1':1,
    '8':2,
    #(missing 3)
    '2':4,
    '10':5,
    '3':6,
    '4':7}

# q33 order of choices (rows) mixed up in German (but not french), wrt to english
# Normal order:
  # '33_1':'Demographics_Health_Positive Valence', '33_2':'Demographics_Health_Negative Valence',
  # '33_3':'Demographics_Health_Stressed', '33_4':'Demographics_Health_Lonely',
  # '33_5':'Demographics_Health_Anxious', '33_6':'Demographics_Health_Arousal',
  # '33_7':'Demographics_Health_Depressed',
  # '33_8':'Demographics_Health_Bored',
# german order
# 1 pos
# 2 neg
# 3 Niedergeschlagenheit depressed   3->7
# 4 energy 4->6
# 5 lonely 5->4
# 6 anxiety 6-> 5
# 7 stress 7->3
# 8 Boredom

#ger.rename(columns={'33_3': '33_7', '33_4': '33_6', '33_5': '33_4', '33_6':'33_5', '33_7':'33_3'}, inplace=True)


# other issues

# gender
# should be woman, man, diverse, no response
# man /woman were flipped in some versions..
# applies to italian and french
frenchItal_gender_dict = {
'1': 2,
'2': 1,
'3': 3,
'4': 4
}

# yes and no flipped for engaging with music differently question
frenchGer_YN_musDiff_dict = {
'0':1,
'1':0
}

# social replacement and emotional coping flipped compared to other versions
# this was only true for hypotheses for listening, not making

# # normal version
#   # Music Listening -- Hypotheses
#   '23_1':'Music Listening_Hypotheses_Feel Connected to Others',
#   '23_2':'Music Listening_Hypotheses_Serve as Social Interaction',
#   '23_3':'Music Listening_Hypotheses_Helps Me Cope',

# french has 2 and 3 flipped
#fra.rename(columns={'23_2': '23_3', '23_3': '23_2'}, inplace=True)

#------------------------------------------------------------------------------#
#                       Columns we can drop
#------------------------------------------------------------------------------#
# Define columns that we can drop from dataframe
# delete some columns we no longer need
dropCols = ['Status', 'Finished', 'DistributionChannel',
            'Info', 'Q_BallotBoxStuffing', 'DeviceIdentifier', 'Q_TerminateFlag', 'uid', 'Q_TotalDuration', 'Q_Language', 'ipaddress',
            'PanelID', 'iisID', 'UserLanguage', 'Q110', 'Q107', 'Q108']
            # NOTE: these last Qs were filters for getting into the ESM section (are you interested in follow-up study, y/n)
            # NOTE: we no longer need to keep state because it is only relevant for NY and anyone who selected anything other than NY got screened out
            # NOTE: no longer dropping ResponseID because that is what Will used in his cleaning.


#------------------------------------------------------------------------------#
#                       Answer Code Dictionary
#------------------------------------------------------------------------------#
# Here, we map the variable codes associated with each answer in Qualtrics.
# We will use 'open' for any question that had an open-ended text response.
# We will use 'num_input' for any question with an open-ended numeric response

# Define grid scales common to multiple questions

activities_scale = {
    0:'I never do this (neither now or before)',
    1:'Much less important than before',
    2:'2',
    3:'3',
    4:'About equally important as before',
    5:'5',
    6:'6',
    7:'Much more important than before',
    99:'Dont know / Prefer not to say'}

    # NOTE: functions of listening and playing scales are exactly the same as activities scale

formats_scale = {
    0:'I almost never do this',
    1:'Significantly Less',
    2:'2',
    3:'3',
    4:'About the same',
    5:'5',
    6:'6',
    7:'Significantly more'}

    # NOTE: Listening and active music making situations scales are exactly the same as formats scale

diversity_scale = {
    1:'Significantly less diverse',
    2:'Moderately less diverse',
    3:'Slightly less diverse',
    4:'About the same',
    5:'Slightly more diverse',
    6:'Moderately more diverse',
    7:'Significantly more diverse'}

hypotheses_scale = {
    1:'Strongly disagree',
    2:'Disagree',
    3:'Somewhat disagree',
    4:'Neither agree nor disagree',
    5:'Somewhat agree',
    6:'Agree',
    7:'Strongly agree'}

    # NOTE: Big5 scale is the same

valence_scale = {
    1:'Much less',
    2:'Less',
    3:'Sligthly less',
    4:'About the same',
    5:'Slightly more',
    6:'More',
    7:'Much more'}


# Define answer code dictionary

answer_code_dict = {
    # Demographics -- General
    'Demographics_General_Age':'num_input',

    'Demographics_General_Gender':
        {1:'woman', 2:'man', 3:'diverse', 4:'prefer not to say'},

    'Demographics_General_Years of School':'num_input', # NOTE ISSUE. This was open for some and closed value choices for others

    'Demographics_General_Years of Post-School':'num_input', # NOTE ISSUE. This was open for some and closed value choices for others

    # Demographics -- COVID
    'Demographics_COVID_Employement Before COVID':
        {4:'employed full time',
        5:'employed part-time casual',
        6:'self-employed',
        7:'studying or in vocational training',
        8:'home-maker caregiver',
        9:'not employed',
        10:'retired',
        11:'prefer not to say'},

    'Demographics_COVID_Profession': 'open',

    'Demographics_COVID_Living Situation':{
        1:'I live alone',
        2:'I live with a pet',
        3:'I live with a partner spouse',
        4:'I live with a child children',
        5:'I live with a parent parents',
        6:'I live with an elderly relative relatives',
        10:'I live with siblings cousins other relatives',
        7:'I live with a friend friends',
        8:'I live in a shared house apartment',
        9:'Other (please specify)'},

    'Demographics_COVID_Living Situation Free Response': 'open',

    'Demographics_COVID_Current Country':{
        3414: 'France',
        3418: 'Germany',
        3430: 'India',
        3436: 'Italy',
        3535: 'UK',
        3537: 'USA'},

    'Demographics_COVID_Current City Type':{
        4:'Rural area (e.g., countryside)',
        5:'Suburban area (e.g., small town)',
        6:'Urban area (e.g., large city)'},

    'Demographics_COVID_Current Place Home':
        {0:'no', 1:'yes'},

    'Demographics_COVID_Number Times Leave':'num_code-1', # convert this to num and subtract 1

    'Demographics_COVID_Ways Work Affected':{
        1:'My situation has not changed (I continue to go to work as normal)',
        2:'My situation has not changed (I continue to work from home)',
        3:'I have changed my work routines to primarily or entirely work from home',
        4:'I have to work reduced hours',
        5:'I am suffering from a lower income',
        6:'I have lost my primary source of income',
        7:'My job is at risk',
        8:'I have to home-school and/or take care of my child(ren)'},

    # Activities
    'Activities_Making Music': activities_scale,
    'Activities_Music Listening': activities_scale,
    'Activities_Searching for Music Info': activities_scale,
    'Activities_Thinking About Music': activities_scale,
    'Activities_Exercise Indoors': activities_scale,
    'Activities_Exercise Outdoors': activities_scale,
    'Activities_Visit People in Person': activities_scale,
    'Activities_Call People': activities_scale,
    'Activities_Cooking': activities_scale,
    'Activities_Shopping Online': activities_scale,
    'Activities_Watching Movies': activities_scale,
    'Activities_Meditating': activities_scale,
    'Activities_Learning New Skills': activities_scale,
    'Activities_Reading Books': activities_scale,
    'Activities_Virtual Exhibitions': activities_scale,
    'Activities_Social Media': activities_scale,
    'Activities_Playing Games': activities_scale,
    'Activities_Watching News': activities_scale,
    'Activities_Drugs or Alcohol': activities_scale,
    'Activities_Volunteering': activities_scale,
    'Activities_Gardening': activities_scale,
    'Activities_Writing': activities_scale,
    'Activities_Photography': activities_scale,
    'Activities_Create Online Content': activities_scale,
    'Activities_Sexual Activity': activities_scale,
    'Activities_Cleaning': activities_scale,
    'Activities_Crafting': activities_scale,
    'Activities_Fashion': activities_scale,
    'Activities_Online Dating': activities_scale,

    # Music Listening -- Formats
    'Music Listening_Formats_Radio': formats_scale,
    'Music Listening_Formats_TV Broadcasts': formats_scale,
    'Music Listening_Formats_Owned Physical Music': formats_scale,
    'Music Listening_Formats_Owned Digital Music': formats_scale,
    'Music Listening_Formats_Free Streaming Others Playlists': formats_scale,
    'Music Listening_Formats_Free Streaming Own Playlists': formats_scale,
    'Music Listening_Formats_Paid Streaming Others Playlists': formats_scale,
    'Music Listening_Formats_Paid Streaming Own Playlists': formats_scale,
    'Music Listening_Formats_Free Livestreams': formats_scale,
    'Music Listening_Formats_Paid Livestreams': formats_scale,
    'Music Listening_Formats_Limited Time Programs': formats_scale,
    'Music Listening_Formats_Always Available Programs': formats_scale,

    # Music Listening -- Situations
    'Music Listening_Situations_Traveling': formats_scale,
    'Music Listening_Situations_Housework': formats_scale,
    'Music Listening_Situations_Working': formats_scale,
    'Music Listening_Situations_Other Activities': formats_scale,
    'Music Listening_Situations_Doing Nothing Else': formats_scale,
    'Music Listening_Situations_Exercising': formats_scale,
    'Music Listening_Situations_Dining': formats_scale,
    'Music Listening_Situations_With Others': formats_scale,
    'Music Listening_Situations_Alone': formats_scale,
    'Music Listening_Situations_Morning': formats_scale,
    'Music Listening_Situations_Evening': formats_scale,
    'Music Listening_Situations_Sexual Activity': formats_scale,

     # Active Music Making -- Situations
    'Making Music_Situations_Sing Alone': formats_scale,
    'Making Music_Situations_Sing Together': formats_scale,
    'Making Music_Situations_Sing Internet': formats_scale,
    'Making Music_Situations_Balconies': formats_scale,
    'Making Music_Situations_Play Alone': formats_scale,
    'Making Music_Situations_Play Together': formats_scale,
    'Making Music_Situations_Play Internet': formats_scale,
    'Making Music_Situations_Perform For Others': formats_scale,
    'Making Music_Situations_Dance Alone': formats_scale,
    'Making Music_Situations_Dance Together': formats_scale,
    'Making Music_Situations_Dance Internet': formats_scale,
    'Making Music_Situations_Post Recordings': formats_scale,
    'Making Music_Situations_Make Own Music': formats_scale,

    # Music Engagement during COVID
    'Music Engagement_Engaging With Music Differently YN':{0:'no',1:'yes'},

    'Music Engagement_Engaging With Music Differently List':{
        11:'Other pieces from the same musicians/composers',
        12:'Music by other musicians/composers from the same',
        13:'Music from other genres/styles'},

    'Music Engagement_Diversity of Music': diversity_scale,

    'Music Engagement_Nostalgic Music': diversity_scale,

    'Music Engagement_Interest in Others Music':{
        1:'Not at all interested',
        2:'2',
        3:'3',
        4:'Moderately interested',
        5:'5',
        6:'6',
        7:'Extremely interested'},

    # Active Music Making -- Hypotheses
    'Making Music_Hypotheses_Feel Connected to Others': hypotheses_scale,
    'Making Music_Hypotheses_Serve as Social Interaction': hypotheses_scale,
    'Making Music_Hypotheses_Helps Me Cope': hypotheses_scale,

    # Active Music Making -- Functions
    'Making Music_Functions_Puts Me in a Good Mood': activities_scale,
    'Making Music_Functions_Supports Me in a Bad Mood': activities_scale,
    'Making Music_Functions_Helps Me Relax': activities_scale,
    'Making Music_Functions_Energizes Me': activities_scale,
    'Making Music_Functions_Provides an Aesthetic Experience': activities_scale,
    'Making Music_Functions_Helps Me Understand My Feelings': activities_scale,
    'Making Music_Functions_Is Enjoyable': activities_scale,
    'Making Music_Functions_Provides a Good Background': activities_scale,
    'Making Music_Functions_Makes Me Want to Move': activities_scale,
    'Making Music_Functions_Helps Me Express My Identity': activities_scale,
    'Making Music_Functions_Provides a Spiritual Experience': activities_scale,
    'Making Music_Functions_Helps Distract Me': activities_scale,
    'Making Music_Functions_Helps Me Identify with the Artist': activities_scale,
    'Making Music_Functions_Stimulates Me Intellectually': activities_scale,
    'Making Music_Functions_Reduces My Stress': activities_scale,
    'Making Music_Functions_Enables Me to Vent Negative Emotions': activities_scale,
    'Making Music_Functions_Provides Comfort': activities_scale,
    'Making Music_Functions_Gives Meaning to My Life': activities_scale,
    'Making Music_Functions_Creates a Personal Space': activities_scale,
    'Making Music_Functions_Gives Me Sense of Control': activities_scale,
    'Making Music_Functions_Makes Me Feel Good About Myself': activities_scale,
    'Making Music_Functions_Helps Me Concentrate': activities_scale,
    'Making Music_Functions_Helps Time Pass Quickly': activities_scale,
    'Making Music_Functions_Helps Me Dwell on My Worries': activities_scale,
    'Making Music_Functions_Gives Me New Perspectives': activities_scale,
    'Making Music_Functions_Helps Me Accept My Situation': activities_scale,
    'Making Music_Functions_Feel Like I Have Company': activities_scale,
    'Making Music_Functions_Reminiscent of Positive Times': activities_scale,
    'Making Music_Functions_Feel Like I Am Sharing My Experience': activities_scale,
    'Making Music_Functions_Moves Me Emotionally': activities_scale,
    'Making Music_Functions_Feel Like I Understand Others': activities_scale,
    'Making Music_Functions_Feel Connected to My Culture': activities_scale,
    'Making Music_Functions_Feel Like Part of a Bigger Group': activities_scale,
    'Making Music_Functions_Helps Me Fall Asleep': activities_scale,
    'Making Music_Functions_Feel Less Lonely': activities_scale,
    'Making Music_Functions_Lets Me Daydream': activities_scale,
    'Making Music_Functions_Helps Keep a Routine': activities_scale,

    'Making Music_Functions_Free Response':'open',

    # Music Listening -- Hypotheses
    'Music Listening_Hypotheses_Feel Connected to Others': hypotheses_scale,
    'Music Listening_Hypotheses_Serve as Social Interaction': hypotheses_scale,
    'Music Listening_Hypotheses_Helps Me Cope': hypotheses_scale,

    # Music Listening -- Functions
    'Music Listening_Functions_Puts Me in a Good Mood': activities_scale,
    'Music Listening_Functions_Supports Me in a Bad Mood': activities_scale,
    'Music Listening_Functions_Helps Me Relax': activities_scale,
    'Music Listening_Functions_Energizes Me': activities_scale,
    'Music Listening_Functions_Provides an Aesthetic Experience': activities_scale,
    'Music Listening_Functions_Helps Me Understand My Feelings': activities_scale,
    'Music Listening_Functions_Is Enjoyable': activities_scale,
    'Music Listening_Functions_Provides a Good Background': activities_scale,
    'Music Listening_Functions_Makes Me Want to Move': activities_scale,
    'Music Listening_Functions_Helps Me Express My Identity': activities_scale,
    'Music Listening_Functions_Provides a Spiritual Experience': activities_scale,
    'Music Listening_Functions_Helps Distract Me': activities_scale,
    'Music Listening_Functions_Helps Me Identify with the Artist': activities_scale,
    'Music Listening_Functions_Stimulates Me Intellectually': activities_scale,
    'Music Listening_Functions_Reduces My Stress': activities_scale,
    'Music Listening_Functions_Enables Me to Vent Negative Emotions': activities_scale,
    'Music Listening_Functions_Provides Comfort': activities_scale,
    'Music Listening_Functions_Gives Meaning to My Life': activities_scale,
    'Music Listening_Functions_Creates a Personal Space': activities_scale,
    'Music Listening_Functions_Gives Me Sense of Control': activities_scale,
    'Music Listening_Functions_Makes Me Feel Good About Myself': activities_scale,
    'Music Listening_Functions_Helps Me Concentrate': activities_scale,
    'Music Listening_Functions_Helps Time Pass Quickly': activities_scale,
    'Music Listening_Functions_Helps Me Dwell on My Worries': activities_scale,
    'Music Listening_Functions_Gives Me New Perspectives': activities_scale,
    'Music Listening_Functions_Helps Me Accept My Situation': activities_scale,
    'Music Listening_Functions_Feel Like I Have Company': activities_scale,
    'Music Listening_Functions_Reminiscent of Positive Times': activities_scale,
    'Music Listening_Functions_Feel Like I Am Sharing My Experience': activities_scale,
    'Music Listening_Functions_Moves Me Emotionally': activities_scale,
    'Music Listening_Functions_Feel Like I Understand Others': activities_scale,
    'Music Listening_Functions_Feel Connected to My Culture': activities_scale,
    'Music Listening_Functions_Feel Like Part of a Bigger Group': activities_scale,
    'Music Listening_Functions_Helps Me Fall Asleep': activities_scale,
    'Music Listening_Functions_Feel Less Lonely': activities_scale,
    'Music Listening_Functions_Lets Me Daydream': activities_scale,
    'Music Listening_Functions_Helps Keep a Routine': activities_scale,

    'Music Listening_Functions_Free Response': 'open',

    # Music Engagement Open Ended
    'Music Engagement_Other Ways Use Music Differently Free Response':'open',
    'Music Listening_Examples_Free Response':'open',
    'Making Music_Examples_Free Response':'open',

    # Demographics -- Music
    'Demographics_Music_Ollen':{
        1:'Non-musician',
        2:'Music-loving non-musician',
        3:'Amateur musician',
        4:'Serious amateur musician',
        5:'Semi-professional musician',
        6:'Professional musician'},

    'Demographics_Music_Make Music Alone or Together':{
        1:'Primarily alone',
        2:'Primarily together with others (e.g., band, orchestra, choir)',
        3:'Both more or less equally'},

    'Demographics_Music_Music Importance':{
        1:'Not at all', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'Extremely important'},

    'Demographics_Music_Number of Concerts':{
        1:'0',
        2:'1',
        3:'2',
        4:'3',
        5:'4-6',
        6:'7-10',
        7:'11 or more'},

    # Demographics -- Health
    'Demographics_Health_Infected with COVID':{
        1:'I was am infected',
        2:'Someone I live with was is infected',
        3:'Because of my profession, I have contact with infected people',
        4:'Someone I am close to (friend or family member) has been infected',
        5:'I am mourning the loss of a loved one from COVID-19',
        0:'None of the above',
        99:'Prefer not to say'},

    'Demographics_Health_General Health':{
        1:'Much worse',
        2:'Worse',
        3:'Slightly worse',
        4:'About the same',
        5:'Slightly better',
        6:'Better',
        7:'Much better'},

    'Demographics_Health_Positive Valence': valence_scale,
    'Demographics_Health_Negative Valence': valence_scale,
    'Demographics_Health_Stressed': valence_scale,
    'Demographics_Health_Lonely': valence_scale,
    'Demographics_Health_Anxious': valence_scale,
    'Demographics_Health_Arousal': valence_scale,
    'Demographics_Health_Depressed': valence_scale,
    'Demographics_Health_Bored': valence_scale, # Melanie added bored for Ipsos versions

    # Demographics -- Personality (Big 5)
    'Demographics_Personality_Reserved': hypotheses_scale,
    'Demographics_Personality_Trusting': hypotheses_scale,
    'Demographics_Personality_Thorough': hypotheses_scale,
    'Demographics_Personality_Relaxed': hypotheses_scale,
    'Demographics_Personality_Imaginative': hypotheses_scale,
    'Demographics_Personality_Outgoing': hypotheses_scale,
    'Demographics_Personality_Faults Others': hypotheses_scale,
    'Demographics_Personality_Lazy': hypotheses_scale,
    'Demographics_Personality_Nervous': hypotheses_scale,
    'Demographics_Personality_Few Artistic Interests': hypotheses_scale,

    # Code for ESM Study
    'ESM_Mother':'open',
    'ESM_Father':'open',
    'ESM_Middle':'open',
    'ESM_Town':'open',
    'ESM_ID':'assigned_num',
}

# prolific and social answer dict for education question.
prolific_school_dict = {
    9308:0,
    9291:1,
    9292:2,
    9293:3,
    9294:4,
    9295:5,
    9296:6,
    9297:7,
    9298:8,
    9299:9,
    9300:10,
    9301:11,
    9302:12,
    9303:13,
    9304:14,
    9305:15,
    9306:16}

prolific_post_school_dict = {
    9310:0,
    9291:1,
    9292:2,
    9293:3,
    9294:4,
    9295:5,
    9296:6,
    9297:7,
    9298:8,
    9299:9,
    9300:10,
    9301:11,
    9307:12,
    9308:13,
    9309:14}

# Education categories
edu_dict = {
    'edu_cat':{'low':1,'med':2,'high':3,'not_captured':99,'no_country_mapping':99},
    'edu_num':{1:'low',2:'med',3:'high',99:'not_captured',99:'no_country_mapping'}
    }

#------------------------------------------------------------------------------#
#                        One Hot Columns
#------------------------------------------------------------------------------#

# Define columns that will need to be converted to one hot encoding
# i.e. columns where participants could select multiple answer choices
oneHotCols = {'Demographics_COVID_Living Situation', 'Demographics_COVID_Ways Work Affected', 'Demographics_Health_Infected with COVID'}


#------------------------------------------------------------------------------#
#                        Yes / No Columns
#------------------------------------------------------------------------------#

# Define columns that will need to be binary
yesNoCols = {'Demographics_COVID_Current Place Home', 'Music Engagement_Engaging With Music Differently YN'}


#------------------------------------------------------------------------------#
#                        Rename dicts for plots
#------------------------------------------------------------------------------#


# rename labels for plots
activities_rename_dict = {
    'making music': 'Make music',
    'Music listening': 'Listen to music',
    'Searching for Music Info': 'Search for music info',
    'Thinking About Music': 'Read / write about music',
    'Exercise Indoors': 'Exercise indoors',
    'Exercise Outdoors': 'Exercise outdoors',
    'Visit People in Person': 'Visit people in person',
    'Call People': 'Call people',
    'Cooking': 'Cook',
    'Shopping Online': 'Shop online',
    'Watching Movies': 'Watch movies / series',
    'Meditating': 'Meditate / Pray',
    'Learning New Skills': 'Learn new skill',
    'Reading Books': 'Read / listen to books, podcasts, etc.',
    'Virtual Exhibitions': 'Browse virtual exhibitions',
    'Social Media': 'Browse social media',
    'Playing Games': 'Play games',
    'Watching News': 'Read / watch news',
    'Drugs or Alcohol': 'Consume drugs / alcohol',
    'Volunteering': 'Volunteer to help others',
    'Gardening': 'Garden',
    'Writing': 'Write / journal',
    'Photography': 'Take photos / videos',
    'Create Online Content': 'Create online content',
    'Sexual Activity': 'Engage in sexual activity (self or others)',
    'Cleaning': 'Clean',
    'Crafting': 'Craft (e.g. knit, wood-work)',
    'Fashion': 'Experiment with outfits / looks',
    'Online Dating': 'Date online (apps)',
}

mus_lis_funcs_rename_dict = {
    'Puts Me in a Good Mood': 'Puts me in a good mood',
    'Supports Me in a Bad Mood': 'Supports me in a bad mood',
    'Helps Me Relax': 'Helps me relax',
    'Energizes Me': 'Energises me',
    'Provides an Aesthetic Experience': 'Provides an aesthetic experience',
    'Helps Me Understand My Feelings': 'Helps me understand my thoughts / feelings',
    'Is Enjoyable': 'Is enjoyable',
    'Provides a Good Background': 'Provides good background to other activities',
    'Makes Me Want to Move': 'Makes me want to move',
    'Helps Me Express My Identity': 'Helps me express my identity / values',
    'Provides a Spiritual Experience': 'Provides a spritual experience',
    'Helps Distract Me': 'Distracts me from problems / worries',
    'Helps Me Identify with the Artist': 'Enables me to identify with performer / composer',
    'Stimulates Me Intellectually': 'Stimulates me intellectually',
    'Reduces My Stress': 'Reduces my stress / anxiety',
    'Enables Me to Vent Negative Emotions': 'Enables me to vent negative emotions',
    'Provides Comfort': 'Provides comfort / support',
    'Gives Meaning to My Life': 'Gives meaning to my life',
    'Creates a Personal Space': 'Creates personal space for me',
    'Gives Me Sense of Control': 'Gives me sense of control',
    'Makes Me Feel Good About Myself': 'Makes me feel good about myself',
    'Helps Me Concentrate': 'Helps me concentrate',
    'Helps Time Pass Quickly': 'Helps me feel time is passing more quickly',
    'Helps Me Dwell on My Worries': 'Helps me dwell on my worries',
    'Gives Me New Perspectives': 'Helps me think about my situation from new perspective',
    'Helps Me Accept My Situation': 'Helps me accept my situation',
    'Feel Like I Have Company': 'Makes me feel like I have company',
    'Reminiscent of Positive Times': 'Makes me reminiscent of more positive times',
    'Feel Like I Am Sharing My Experience': 'Makes me feel I am sharing my experience with others',
    'Moves Me Emotionally': 'Moves me emotionally',
    'Feel Like I Understand Others': 'Makes me feel I understand others',
    'Feel Connected to My Culture': 'Makes me feel I am connected to my culture',
    'Feel Like Part of a Bigger Group': 'Makes me feel part of a bigger group',
    'Helps Me Fall Asleep': 'Helps me fall asleep',
    'Feel Less Lonely': 'Makes me feel less lonely',
    'Lets Me Daydream': 'Allows me to mind-wander / daydream',
    'Helps Keep a Routine': 'Helps me keep a routine',

}

mus_lis_situations_rename_dict = {
     'traveling': 'When on way (traveling, walking)',
     'working': 'When working or studying',
     'doing nothing else': 'When doing nothing else',
     'dining': 'When dining',
     'with others': 'When with family or friends',
     'alone': 'When alone',
     'morning':'In the morning (after waking)',
     'evening':'In the evening (before / while falling asleep)',
     'sexual activity':'When engaging in sexual / erotic / romantic activity',
     'other activities':'When performing other activities at home',
     'housework':'When doing housework',
     'exercising':'When exercising / playing sports',

}

mus_list_formats_rename_dict = {
    'free streaming others playlists':'Free streaming (existing or randomly generated playlists)',
    'free streaming own playlists':'Free streaming (self-made playlists)',
    'free livestreams':'Free live streams',
    'radio':'Radio',
    'tv broadcasts':'TV broadcasts',
    'paid streaming others playlists':'Paid streaming (existing or randomly generated playlists)',
    'owned digital music':'Owned digital files',
    'paid streaming own playlists':'Paid streaming (self-made playlists)',
    'always available programs':'Streamed programmes, accesible at any time',
    'limited time programs':'Streamed programmes, accesible for a limited time',
    'owned physical music':'Physical recordings (CD, DVD, etc.)',
    'paid livestreams':'Paid livestreams',
}

mus_make_forms = {
    'sing alone':'Sing at home alone',
    'dance alone':'Dance at home alone',
    'play alone':'Play instrument at home alone',
    'sing together':'Sing at home together',
    'sing internet':'Sing with others via internet',
    'dance internet':'Dance with others via internet',
    'make own music':'Make own music',
    'play internet':'Play instrument with others via internet',
    'play together':'Play instrument at home with others',
    'balconies':'Sing or play on balcony / outdoors',
    'post recordings':'Post recordings of self on internet',
    'dance together':'Dance at home with others',
    'perform for others':'Sing or play instrument for others',
}
