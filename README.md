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
_A: Lockdown activities and B: functions of listening to music ranked by mean change in importance of each item, within country._

_Ranking script:_ `Ranks.ipynb`.

___
## Individual

### Overview
  1.  Factor analysis
  2.  Regression
  3.  Evaluation of individual differences

**Factor Analysis**
Text

_Factor analysis script:_ `Factor_Analysis.ipynb`.

**Regression**
Text

_Regression script:_ `Predicting_Negative_Positive_Emotions.ipynb`.

**Evaluation of individual differences**
Text

_Music listening script:_ `Music_Listening_Individual_Differences.ipynb`.
_Music making script:_ `Music_Making_Individual_Differences.ipynb`.

___
## Coping

![image](/images/shap_plot.png)
_Top 20 features predicting socio-emotional coping via (A) music listening and (B) making music. Data points represent SHAP values for every person on each of the top 20 most predictive features._

_Music listening script:_ `Music_Listening_LGBM.ipynb`.
_Music making script:_ `Music_Making_LGBM.ipynb`.

___
## Contact
Feel free to reach out to co-first authors Dr. Lauren Fink and Dr. Lindsay Warrenburg:
- Lauren Fink: <a href="https://lkfink.github.io/" target="_blank">`https://lkfink.github.io/`</a>
- Lindsay Warrenburg: <a href="https://www.lindsaywarrenburg.com/" target="_blank">`https://www.lindsaywarrenburg.com/`</a>
