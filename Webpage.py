#!/usr/bin/env python
# coding: utf-8

# The city of New York, created a program in 2014 called the *Vision Zero*. It was created by New York City Mayor Bill de Blasio, which goal was and still is to eliminate all traffic deaths and serious injuries in New York City by 2024. The basis for the theory hypothesizes was that pedestrian deaths are not as much "accidents" as they are a failure of street design.
# Consequently, in order to analysis the effect and improve upon *Vision Zero* the dataset Motor Vehicle Collisions has been used, as this dataset contains details on the crash event. Each row represents a crash event, which is data going back from 2012 until 2021. Each accidents contains the date and time of the event, as well as road user type involved, number of injuries and fatalities, which types of vehicles were invovled, as well as the contribution factors.
# 
# The program has been running for 5-6 years now, and initiatives have been brough about to in order to achive *Vision Zero*
# Among those are lowering of the New York City speed limit from 30mph to 20mph, which was introduced in 2015. Moreover, by advice of Zero advocates in Sweden, an increased amount of speed cameras, together with serveal other laws has been introduced to change the culture of driving in New York. Among those are increased penalties for failing to yield for pedestrians, bikes or other soft road users, which is considered as a criminal misdemeanor. This is due to increased risk of these accidents happening prior to *Vision Zero*, and thus pedestrians, will be a focus of this project. Besides incrased penalties, are slow zones (20mph), and an obligation by the city to fix traffic lights within 24 hours. There has been especially focus on improving conditions for soft road users, which will also be the overall focus of this project 
# 
# To goal of the final project, and the visualzation created is to provide the city of New York with a tools and insights to help decision makers to determine dangerous causues, vehicles, time intervals, as well as which parts of the city are in need of safer designs, in order to achive vision Zero.[1]. 

# First the dataset provided from NYC Open Data, has been through an google API, to help determine coordinates for those intersection, where the streets were listed, but the coordinates were not. Unfortunately the API does not provide the possibility to be used for all of the inherent rows, and only a limited amount, due to the free nature of a trail version ;) 
# https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95
# 

# In[43]:


from IPython.display import display, Image


# ### Accidents, injuries and fatalities throughout the years

# After the dataset has been updated, first order of business is to check, if the initiatives implemented so far, have had a positiv impact of number of accidents, and to which extend there has been a decrease of fatal injuries. 

# In[38]:


display(Image(filename='TotalAcci1221.png'))


# As can be seen the number of accidents has not decreased since the beginning of the oberservation from the dataset, expect in 2020, and 2021, which is due to partly the COVID-19 having a substantial impact on road users, throughout 2020 and 2021. In 2021, there is only data until april, which explains the low number of accidents. Taking those factors out, the number of accidents has been slowly increasing, which is worrisome, but can also be linked to the number of users on road, since congestions and traffic has increased the last couple of years [2] The more frequently the roads are used, the more likely there is to be an accident. 
# https://ny.curbed.com/2018/2/6/16979696/new-york-city-traffic-congestion-second-worst

# The goal of vision zero was to decrease injures and fatalities, so even though there was an increase of accidents, the new bills, laws, speedtraps and decrease of speed limit, should be visual in the number of injuries and fatalities: 

# In[39]:


display(Image(filename='injfat1221.png'))


# By looking the injurys to the left, the number of injuries relevative to the number of accident are somewhat staple, around 25-30%, with a sligth decrease from 13-15, which the rises again in from 2016. Interestring is the number of injuries and fatalities in accidents compared to non harmful accidents, where it can be seen, there was a substainal increase, around 10% points for injuries, and almost a 100% in 2020 for fatalities.    

# In[1]:


from IPython.display import IFrame

IFrame(src='./choropleth_map1.html', width=1000, height=700)


# Further investigation of the data, revelaed an interstring analysis, which can be seem from the figure below:

# In[41]:


display(Image(filename='TotalAccihourly.png'))


# In[42]:


display(Image(filename='injfathourly.png'))


# As can be seen from the figure above, the number of accicents over a 24 hour span, are different from the rate of injuries and fatalities. Even though there are more accidents throughout the day, there are a higher risk of injury or death assocaited with accicents during the nigth. 

# Another interstring point would be to investigate, if accidents more often occurh in different weather conditions, as one could imagine a motorist having more diffuculties spoting a predistrian, or cyclist in tough weather conditions, or slippe roads. To investiagte this matter, weather data from 2012-2021 were gathered from New York, and matched with dates, to give an overview of how weather conditions effected accidents. 
# The different weather conditions werer divided into
# - Dry road with plus degress =*Dry road+*
# - Dry road with minus degress =*Dry road-*
# - Road with none to little rain throughout the day(10mm) = *Ligth wet road*
# - Road with moderate to heavy rain throughout the day(+10mm) = *Heavy wet road*
# - Road with none to little snow throughout the day(10mm) = *Ligth snowy road*
# - Road with moderate to heavy snow throughout the day(+10mm) = *Heavy snowy road*
# 
# The results are demostrated below through graphics: 
# 

# In[115]:


display(Image(filename='weather_summary_accidentscyc.png'))


# As can be seen the number of accicents occuring in good weather condtions are higher, which is due to the fact, that there are more days with sun in New York, than any other, consequently more accidents will occur. 

# In[116]:


display(Image(filename='weather_inj_fat_rate.png'))


# From the above plot it can be observed how to distribution of different kind of weather data can be observed, as well as the injury and fataility % is 

# An important note, is that the data has been filtered so it does not containt data prior to 2016, as some of the causes have not been reported throughly. This was due to the old system TAMS, installed at every precints, as the did not allow for automatic fill out, and required basic intersection traffic crash statistics which included the number of accidents, injuries and fatalities, to be downloaded manually. With the Citywide traffic safety initiative, Vision Zero beginning in the year 2014, it further emphasized the need for the collection of more traffic data. Therefore in March 2016 the. NYPD replaced the TAMS with the new Finest Online Records Management System (FORMS).  FORMS enables the police officers to electronically, using a Department cellphone or computer, enter all of the data fields. (Dscription of data by https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95). 
# So before investigating possible factors, the dateset is cleaned so it only contains the valud data reported from FORMS.
# 

# 

# ## PLOT HEATMAP?

# In[ ]:





# ## Why pedestrians and bikes

# As the focus of the project is to analyse and improve conditions for soft road users, the same graphs are constructed for pedestrians, and cyclist. The reasons why to investigate soft road users as cyclists or pedestrians, was due to the fact, that they were exposed to a significant higher amount of risk, than their counterparties, in cars, 

# In[67]:


display(Image(filename='vehicle_inj_fat_rate.png'))


# As can be seen when comparing the highest rates of injuries,  bikes where ranked nr 5, and by comparing that to the number accidents they are invovled with it further underlines the risk of bicycling in New York City. This figure is based on number of accidents for the most injury prone types of vehicles

# In[68]:


display(Image(filename='vehicle_type_accidents.png'))


# To investiage the cyclist and pedistrisn further, the cyclist and pedistrians crashes and accicendts are shown throught the years - an important mention in this, is the data shoud be relative to the number of pedestrians and cyclist involved. Thus two seperate dataframes are created containing accidents were pedestrians has been involved as well cyclists. **The creation of these two notebooks are elaborated in the explainer Jupyter Notebook**

# In[45]:


display(Image(filename='pdcyyear.png'))


# By looking at the reasons, in terms of contribution factors, the folling plot demostrates, what factors plays a part in accidents in general as well as what type of accidents occuring for bikes and pedestrians

# In[134]:


IFrame(src='./causes_frequency_datasets.html', width=1000, height=700)


# As can be seen from the plot, driver distractions and and failure to yield rigth are common accidents occuring for pedestrians and also cyclist, thus putting them in huge counterparty risk, especially for pedestrians, as these two factors contribute to almost 50% of all of accidents happening to pedestrians. 
# From the cyclists perspective similar trends can be observed, but also other factors as vehicles passings lanes improper or traffic controls disregarded (both players). 

# By investigating the different types of vehicles, not major surprises where hidden here, as Sedan, and Station wagon were the two most commenly in frequency of accidents, which makes intuitively sense as these are also the most commone cars, seen on the roads of New York City

# In[138]:


IFrame(src='./vehicles_frequency_datasets.html', width=1000, height=700)


# ## Cyclist

# Firstly the cyclists are investiagted for any potential insigths. The following section will highligth some of the inisghts discovred from the notebook. 

# In[151]:


IFrame(src='./choropleth_map3.html', width=1000, height=700)


# As can be seen from the three plots above, it is not the same places, where accidents occur in genereal, and if pedestrian or cyclists are involved. Especally Lower east side, Williamsburg and around flushing avenue, alot of cyclist are involved in accidents. 

# By looking at the 24 hour plot of the injruries and fatalities of cyclists, the following was observed:

# In[111]:


display(Image(filename='injfathourlypdcy.png'))


# The same tendency as seen in the total number of accidents are observed as  cyclist are more prone to getting killed in the traffic during the nigth and early hours of the morning, with quite alarming figures that ranges from 2-5 time more likely. 
# Also when cyclist are involved in an accident, it is almost with a 100% certainty, that they are getting injured, putting them at an exstensive risk. By keeping the 24 hour span the contribution factors to which causes the accidents where further investigated, as from here it could be observed, that some factors played a part in the distribution seen above.

# In[124]:


IFrame(src='./hour_cyclist_causes.html', width=950, height=700)


# As can be seen alcohol involvment play a vital factor during the nigth, and by comparing this with the graph below it can be observed that driving under the influence, is linked with and has an influence on fatal injuries, and very often occurs in a injury for the cyclist involved. In terms of factors prone to accidents is also glare, which in almost 90% of the cases results in either an injury or death for the cyclist involved. 

# In[128]:


IFrame(src='./distibution_causes_cyclist.html', width=1000, height=700)


# Thus it can be derived from the two figures, that cyclist are more prone to fataility during the nigth, which often is linked to alcohol involvement. The consumption of alcohol. The consumption of alcohol and rate of accidents for bike, was especially a problem in the beginning of 2016, (FORMS), as can be seen from the figure below. An interstring outtake, as this has since declined, throughout the years, which can partly be due to their sobriety-checkpoints, and their increased focus on drunk driving. [x] https://www.cdc.gov/motorvehiclesafety/pdf/impaired_driving/Drunk_Driving_in_NY.pdf

# In[129]:


IFrame(src='./year_cyclist_causes.html', width=950, height=700)


# To give an overview how the weather conditions were relative to the amount of injuries and fatalities, the days with each weather conditions were divided with the total number of injuries/fatalities, and the resulting graphs are shown below:

# In[135]:


display(Image(filename='weather_inj_fat_ratecyc.png'))


# Interestringly enough, the amount of accidents, injuries or deaths, does not increase as a consequence of weather conditions, which was the initial thoughth. Dry road with plus degress, has the most injuries, and is also the most common one, decipted from Weather conditions vs Number of Accidents. By comparing the data to graph blow it can also observed that accidents on bikes occur mostly in the time spans with good weather, during summers. This intuitively is logic, since riding a bike in the winther or during bad weather is unpleasent, and is often avoided.

# In[137]:


IFrame(src='./month_cyclist_causes.html', width=950, height=700)


# ## Pedestrians

# Firstly the cyclists are investiagted for any potential insigths. The following section will highligth some of the inisghts discovred from the notebook. 

# In[152]:


IFrame(src='./choropleth_map2.html', width=1000, height=700)


# From the plot above, it can be observed, that from a pedestrians point of view the major hotspots for accidents and fatalities are around East New York and near prospect hill. (Brooklyn - lovely park btw)

# In[112]:


display(Image(filename='injfathourlypdcy1.png'))


# As cyclist, pedestrians are in more danger of getting killed during in traffic, during the nigth, and early hours of the morning, with quite alarming figures that ranges from 2-5 time more likelyhood. To understand why, similar plots as for the cyclists are conducted to give a insigths to what causes these accidents, and why are they more likely during the nigth. 

# In[142]:


IFrame(src='./hour_pedestrian_causes.html', width=950, height=700)


# From the Figure above, it can be observed that some of the factors that are playing a part in the increased number of accidents, as unsafe speed, alcohol involvment, pavement slippery and glare all are happening throughout the day, but some of them being mostly allocated during the same timespan, as the fataility ratio of pedestrians. By looking at the contributions factors distribution of accidents, injuries and deaths, it further emphasis this point.

# In[145]:


IFrame(src='./distibution_causes_pedestrians.html', width=1000, height=700)


# The same point as stated for cyclists, is present for pedestrians, as the severity of accidents are much higher for accidents involving alcohol, and as this was one of the major contributors for accidents occuring during the span, from which pedestrians were much in dangers of dying in traffic, it plays a vital part in been one of the root causes to why pedestrains are more prone to death in traffic during the nigth. 

# As observed from weather date and accidents involving cyclists, the same graphs are created from a pedestrian viewpoint. Maybe this changes for pedestrains, as they cannot choice not to walk from A to B, if they need to go shopping, accidents occuring to pedestrians are pretty consistent throughout the year. 

# In[148]:


display(Image(filename='weather_inj_fat_rateped.png'))


# From this graph it can be observed, that weather conditions do play a vital part in when pedestrians are most likely to be injured or killed in traffic. As can be seen from the graphs above, that even though dry roads is the most common of weather conditions for accidents, injuries and deaths, the most dangerous conditions in terms of injuries, wet and snowy roads, as these pose a great prone to injruies among pedestrians. In terms of fatalities, heavy wet road, is the most dangerous one, with a average fataility per day of 0.2, though closely followed by dry road + 

# ## Subconclusion 

# From the analysis of pedestrians and cyclist, the following can be concluded:
# - Soft road users as bikes and pedestrians are prone to accidents, and when involved, they are often associcated with higher risk of injury and fatality, than counterparties, like vehicles
#  - Moreover there are substantially higher rates of fataility during certain peaks hours, especially at nigth. This is both the case for cyclist and pedestraisn
#    - Mainly due to high number of accidents invovling alcohol, which is the predominant causing high fatality rates during the night. Also unsafe speed (speeding), causes high rates of fataility    
# - Driver distractions and and failure to yield rigth is the predominant contribution factors to cyclist and pedestria accident, thus putting them in huge counterparty risk. 
#  - Almost 50% of accidents invovling pedestrians are due to driver distractions and and failure to yield rigth
#  - Around 35% of accidents invovling cyclist are due to driver distractions and and failure to yield rigth
# - Lower east side, Williamsburg are hot stops for accidents happening to cyclists, while pedestrians are prone to accidents occuring around Bushwick (part of Brooklyn), as well as Prospect park
# - Weather conditions does play a part, in terms of severity of accidents, but mostly for pedestrains, as the more rain and snows causes higer rates of fataility. 
#  - Cyclist, according to the data, uses their bike less frequently during months of cold weather, thus most of accidents occur when the weather is good, allowing for a bikeride.
#  
# Most interstring takeaways from the analysis is the hours of which soft road users are most prone to fatality, but especially the contribution factors. Remebering the motivation for the project, was to provide an overview, where, when and why accidents occured, and moreover to provide the city of New York with a tools and insights to utilized to update current street design. 
# By using the knowlegde of the contribution factors, this is then further linked, with where these accidents takes place, which then will be pint pointed out, thus providing the where, to which street designs should be updated. 

# In[ ]:





# ### Currently missing 
# 
# Plot why we choose bikes and pedetrian. 
# Explanation to why

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


from IPython.display import IFrame

IFrame(src='./test900.html', width=950, height=700)


# In[3]:


from IPython.display import IFrame

IFrame(src='./hour_cyclist_causes.html', width=950, height=700)


# In[97]:





# In[4]:


IFrame(src='./month_pedestrian_causes.html', width=950, height=700)


# In[99]:


IFrame(src='./weekday_cyclist_vehicles.html', width=950, height=700)


# In[100]:


IFrame(src='./weekday_cyclist_causes.html', width=950, height=700)


# In[101]:


IFrame(src='./weekday_pedestrian_causes.html', width=950, height=700)


# In[105]:


IFrame(src='./hour_pedestrian_vehicles.html', width=950, height=700)


# In[103]:


IFrame(src='./year_pedestrian_causes.html', width=950, height=700)


# By co

# In[104]:


IFrame(src='./hour_pedestrian_causes.html', width=950, height=700)


# In[118]:


IFrame(src='./month_cyclist_causes.html', width=950, height=700)


# In[119]:


IFrame(src='./distibution_vehicles_cyclist.html', width=950, height=700)


# In[120]:


IFrame(src='./distibution_vehicles_pedestrians.html', width=950, height=700)


# In[121]:


IFrame(src='./distibution_causes_cyclist.html', width=950, height=700)


# In[2]:


IFrame(src='./distibution_causes_pedestrians.html', width=950, height=700)


# In[ ]:




