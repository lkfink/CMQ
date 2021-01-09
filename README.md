# Coronavirus Music Questionnaire (CMQ)

*Fink, L., *Warrenburg, L. A., Howlin, C., Randall, W., +Hansen, N. C., & +Wald-Fuhrmann, M. (submitted). Viral Tunes: Changes in Musical Behaviours and Interest in Coronamusic Predict Socio-Emotional Coping During COVID-19 Lockdown. <a href="https://psyarxiv.com/7mg2v" target="_blank">`https://psyarxiv.com/7mg2v`</a>

*+ indicate equal contribution

If using anything from this repository, please cite the paper.

___
## Overview

- [Project Description](#description)
- [Participants](#participants)
- [Musical Behaviours: Ranked Importance](#Ranked-changes-in-lockdown-behaviors-across-people)
- [Musical Behaviours: Individual Differences](#Individual-differences-in-lockdown-behavior)
- [Socio-emotional Coping: LGBM Modeling](#Music-as-a-tool-for-socio-emotional-coping)
- [Contact](#contact)

___
## Description

Beyond immediate health risks, the COVID-19 pandemic poses a variety of additional stressors, which may require expensive or unavailable strategies during a pandemic (e.g., therapy, socializing). In this study, we ask whether music might serve as a tool for socio-emotional coping. We surveyed the music listening and making behavior of over 5000 people, with representative samples from 6 countries (3 continents). We find that people with increased positive emotions used music as a proxy for social interaction, whereas people with increased negative emotions used music as a form of emotional regulation. Using a machine learning approach, we tested the importance of demographic/personality traits and various musical behaviors in predicting socio-emotional coping. Our models explain over 50% of the variance in participants’ self-reported use of music to cope and indicate the importance of individually tailored adaptive behaviors (rather than a one-size-fits-all) approach to using music to meet socio-emotional needs. 

### Main Takeaways

 1. **During the COVID-19 lockdown, people have turned to music for regulating their emotions.**

 2. **People experiencing different degrees of emotional changes showed different patterns of musical engagement.**

 3. **Music listening and music making may provide different coping potentials.**

 4. **Coronamusic played a key role in socio-emotional coping.**

[Back to Overview](#overview)
___
## Participants

We surveyed 5113 participants with representative samples (in terms of gender, age, and education) in 6 countries on 3 continents.

The survey took place during the first lockdown of the COVID-19 pandemic, from mid-April through mid-May, 2020.

Country | Number of Participants
:-------------: | :-------------:
France | 983
Germany | 872
India | 891
Italy | 892
UK | 621
USA | 854

_Complete demographic information can be found in_ `Descriptive_Statistics.ipynb`.

[Back to Overview](#overview)
___
## Ranked changes in lockdown behaviors across people

We asked people, _**"Compared to before the onset of the coronavirus crisis, how important are the following 1) leisure activities and 2) functions of music listening to you?"**_

We ranked the importance of all surveyed items across individuals, within each country. The image below shows 1) which activities became most important to people during lockdown, and 2) which functions of music listening became more important. 

We can see that the most important _activities_ included calling people, cleaning, cooking, and engaging with media (reading/watching news, movies or television, and listening to music). The most important functions people felt _music listening_ should serve were that it is enjoyable, puts them in a good mood or energizes them, helps them to relax or reduces their stress, and helps support them in a bad mood.

The importance of activities and music listening behaviors is largely similar across the six countries, but you can see some differences by looking at the spread of the color-coded dots. 

![image](/images/rank_plot.png)
**A: Lockdown activities and B: functions of listening to music ranked by mean change in importance of each item, within country.**

_More information about this ranking process is in_ `Ranks.ipynb`.

[Back to Overview](#overview)

___
## Individual differences in lockdown behavior

### Overview

In order to explore whether musical behaviors differed across people with different personality or demographic traits, we used a three step process. 

  1.  Regression
  2.  Factor analysis
  3.  Evaluation of individual differences

#### Regression

First, we wanted to see if coronavirus-related variables could predict changes in people's _Positive Emotions_ (positive valence, energetic arousal, general health/wellbeing) and _Negative Emotions_ (depression, stress, anxiety, loneliness, negative valence).

The coronavirus-related variables were **contact with the COVID-19 virus**, **work situations due to the pandemic**, and **living situations during the pandemic**.

We found that:
  - These coronavirus-related variables affect changes in a person's positive emotions more than their negative emotions
  - A person's contact with the COVID-19 virus affects changes in emotion more than a person's living or work situation. 
  - The variability in a person's changing emotions explained by pandemic-related factors is small -- this suggests the importance of other variables, as well.

_Complete regression information is in_ `Predicting_Negative_Positive_Emotions.ipynb`.

#### Factor Analysis

Because of the low variability explained by coronavirus-related measures (contact with the COVID-19 virus and changes in living and work situation during the pandemic), an exploratory factor analysis was conducted on the demographic and personality variables, resulting in six latent variables.

These factors were interpreted as changes in _Negative Emotion_ during the pandemic, changes in _Positive Emotion_ during the pandemic, _Age_, _Living Situation_ (alone or with others), _Employment_, and _City Type_ (urban, suburban, rural).

_Details of the factor analysis can be found in_ `Factor_Analysis.ipynb`.

#### Evaluation of individual differences

Finally, we looked into the differences in how people engage with music when they are experiencing increased/decreased Positive and Negative emotions during the pandemic. The following table describes the most important findings:
  > People who reported increased _Negative Emotions_ used music listening and making music to reduce negative affect and to provide a sense of comfort and support. 

  > People whose _Positive Emotions_ increased during the lockdown reported making music as a form of social interaction and way to cope during the crisis.

 . | Changes in Negative Emotions | Changes in Negative Emotions | Changes in Positive Emotions  | Changes in Positive Emotions 
| :-------------: | :-------------: | :-------------: | :-------------: | :-------------:
. | _Music Listening_ | _Making Music_ | _Music Listening_ | _Making Music_
**Coping** |  |  |  | 
Feel connected to others | 0.69 | 0.62 | 0.93 | 1.38
Cope emotionally | 0.93 | 0.91 | 0.33 | 1.01
Serve as social interaction | 0.77 | 0.78 | 0.93 | 1.40
**Functions (Top 6)** |  |  |  | 
_1._ | Helps distract (0.90) | Feel less lonely (0.94) | Provides a spiritual experience (0.93) | Provides a spiritual experience (1.23)
_2._ | Reduces stress (0.85) | Provides comfort (0.92) | Provides a spiritual experience (0.88) | Helps identify with the artist (1.15)
_3._ | Provides comfort (0.78) | Reduces stress (0.92) | Provides an aesthetic experience  (0.88) | Helps dwell on worries (1.15)
_4._ | Supports in bad mood (0.78) | Lets daydream (0.82) | Feel connected to culture  (0.85) | Provides an aesthetic experience (1.13)
_5._ | Feel less lonely (0.77) | Vent negative emotions (0.80) | Helps identify with the artist  (0.84) | Gives new perspectives (1.09)
_6._ | Vent negative emotions (0.75) | Helps distract (0.79) |Feel like sharing one's experience  (0.82) | Feel like part of a bigger group (1.09)
**Situations (Top 3)** |  |  |  | 
_1._ | While doing other activities (0.71) | Dance with others on the internet (0.85) | With others (0.75) | Play together (0.98)
_2._ | While alone (0.68) | Dance alone (0.84) | In the evening (0.69) | Perform for others (0.97)
_3._ | While doing housework (0.63) | Dance with others (0.79) | While traveling (0.65) | Sing with others on the internet (0.94)
**Music Selection** |  |  |  | 
Diverse music | 0.42 | 0.52 | 0.30 | 0.44
Coronamusic interest | 0.88 | 0.95 | 1.05 | 1.41
Nostalgic music | 0.58 | 0.55 | 0.42 | 0.53

**Overview of individual differences in music-related coping, functions, situations, and selection for two latent variables that describe changes in positive and negative emotion during the coronavirus crisis. All values represent mean differences between the top vs. bottom 25% of scorers on each factor (7-point scales). Positive values indicate that the mean score was larger for high scorers than for low scorers.**


_Music listening script:_ `Music_Listening_Individual_Differences.ipynb`.

_Music making script:_ `Music_Making_Individual_Differences.ipynb`.

[Back to Overview](#overview)
___
## Music as a tool for socio-emotional coping

During the pandemic, people are less able to rely on some methods of coping, like ones that may be expensive (therapy) or unavailable (socializing inside). We used a machine learning approach to investigate how people are using music to cope with the stress of the coronavirus crisis.

We defined music-related coping as listening to or making music in order to:
  > Feel connected to others

  > Serve as a replacement for social interaction

  > Cope emotionally with the present situation

Two LGBM regression analyses were conducted: one about _**music listening**_ and the other about _**making music**_. The results are summarized in the SHAP value plots below.

![image](/images/shap_plot.png)
**Top 20 features predicting socio-emotional coping via (A) music listening and (B) making music. Data points represent SHAP values for every person on each of the top 20 most predictive features.**

_Music listening script:_ `Music_Listening_LGBM.ipynb`.

_Music making script:_ `Music_Making_LGBM.ipynb`.

[Back to Overview](#overview)
___
## Contact
Feel free to reach out to co-first authors Dr. Lauren Fink and Dr. Lindsay Warrenburg:
- Lauren Fink: <a href="https://lkfink.github.io/" target="_blank">`https://lkfink.github.io/`</a>
- Lindsay Warrenburg: <a href="https://www.lindsaywarrenburg.com/" target="_blank">`https://www.lindsaywarrenburg.com/`</a>
