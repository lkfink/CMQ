# Coronavirus Music Questionnaire (CMQ)
Viral Tunes: Changes in Musical Behaviours Predict Socio-Emotional Coping During the COVID-19 Pandemic

**Fink, L., Warrenburg, L.**, Howlin, C., Randall, W., Christian-Hansen, N.+ & Wald-Fuhrmann, M.+ (submitted). Viral Tunes: Changes in musical behaviours predict socio-emotional coping during the COVID-19 pandemic.

If using anything from this repository, please cite the paper.

## Table of Contents

- [Project Description](#description)
- [Participants](#participants)
- [Musical Behaviours: Ranked Importance](#ranks)
- [Musical Behaviours: Individual Differences](#individual)
- [Socio-emotional Coping: LGBM Modeling](#coping)
- [Contact](#contact)

___
## Description
### Summary
Beyond immediate health risks, the COVID-19 pandemic poses a variety of additional stressors, which may require expensive or unavailable strategies during a pandemic (e.g., therapy, socializing). In this study, we ask whether music might serve as a tool for socio-emotional coping. We surveyed the music listening and making behavior of over 5000 people, with representative samples from 6 countries (3 continents). We find that people with increased positive emotions used music as a proxy for social interaction, whereas people with increased negative emotions used music as a form of emotional regulation. Using a machine learning approach, we tested the importance of demographic/personality traits and various musical behaviors in predicting socio-emotional coping. Our models explain over 50% of the variance in participants’ self-reported use of music to cope and indicate the importance of individually tailored adaptive behaviors (rather than a one-size-fits-all) approach to using music to meet socio-emotional needs. 

### Main Takeaways

 1. **During the COVID-19 lockdown, people have turned to music for regulating their emotions.**

 2. **People experiencing different degrees of emotional changes showed different patterns of musical engagement.**

 3. **Music listening and music making may provide different coping potentials.**

 4. **Coronamusic played a key role in socio-emotional coping.**

___
## Participants

We surveyed 5113 participants with representative samples (in terms of gender, age, and education) in 6 countries on 3 continents.

Country | Number of Participants
:-------------: | :-------------:
France | 983
Germany | 872
India | 891
Italy | 892
UK | 621
USA | 854

_Complete demographic information can be found in_ `Descriptive_Statistics.ipynb`.

___
## Ranks

![image](/images/rank_plot.png)
**A: Lockdown activities and B: functions of listening to music ranked by mean change in importance of each item, within country.**

_Ranking script:_ `Ranks.ipynb`.

___
## Individual

### Overview
  1.  Factor analysis
  2.  Regression
  3.  Evaluation of individual differences

#### Factor Analysis

Text

_Factor analysis script:_ `Factor_Analysis.ipynb`.

#### Regression

Text

_Regression script:_ `Predicting_Negative_Positive_Emotions.ipynb`.

#### Evaluation of individual differences

**Change in Negative and Positive Emotions
During the Coronavirus Crisis**

Variable | Negative Music Listening | Negative Making Music | Positive Music Listening | Positive Making Music
| :-------------: | :-------------: | :-------------: | :-------------: | :-------------:
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








_Music listening script:_ `Music_Listening_Individual_Differences.ipynb`.

_Music making script:_ `Music_Making_Individual_Differences.ipynb`.

___
## Coping

![image](/images/shap_plot.png)
**Top 20 features predicting socio-emotional coping via (A) music listening and (B) making music. Data points represent SHAP values for every person on each of the top 20 most predictive features.**

_Music listening script:_ `Music_Listening_LGBM.ipynb`.

_Music making script:_ `Music_Making_LGBM.ipynb`.

___
## Contact
Feel free to reach out to co-first authors Dr. Lauren Fink and Dr. Lindsay Warrenburg:
- Lauren Fink: <a href="https://lkfink.github.io/" target="_blank">`https://lkfink.github.io/`</a>
- Lindsay Warrenburg: <a href="https://www.lindsaywarrenburg.com/" target="_blank">`https://www.lindsaywarrenburg.com/`</a>
