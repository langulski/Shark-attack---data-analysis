<p align="center">
  <a href="https://imgbb.com/"><img src="https://www.imagenspng.com.br/wp-content/uploads/2019/03/daddy-shark-png-02.png" width="20%" alt="shark5" border="0"></a>
</p>
<h1 align="center" Project 02 | Data Cleaning </h>

## Project Status
:heavy_check_mark: Complete

## Table of Contents:

- [Objective](#Objective)
- [Motivation](#motivation)
- [Process](#process)
- [Results](#results)
- [Learning Process](#learning-process)
- [Author](#Author)

## Objective

- Apply different cleaning and manipulation techniques to generate a cleaner CSV version of the dataset and analyse the data.
<a href="http://www.sharkattackfile.net/whystudy.htm">SharkAttackFile</a>.<br>

### Business question
> Is surfing a dangerous sport ?

> Are these attacks fatal ?

> What are the areas/countries that most attacks happened while surfing?

### Motivation

- Sharks in fact do not intend to attack humans, the chances of being attacked by a shark is 1 in 5 million, says Katherine Maslenikov, manager of the UW Fish Collection at the Burke Museum. When they bite humans, they are most likely trying to figure out what they are. So safe to say that we are not included in their diet. 
- Surfing is a very popular sport in water, we will check if the attacks are more likely to be linked to this activity. 


## Process
1. Import database, analyse the shape,analyse the sample and store a backup;<br>
2. Clean the lines (drop if NaN mean>0.9);<br>
3. Clean the columns (drop if NaN mean>0.9);<br>
4. Drop duplicates; <br>
5. Drop unnecessary columns; <br>
6. Analyse the columns  'Activity',  'Fatal (Y/N)' 'Years' and 'Country':<br>
    
    - Type of data: <br>
      The column 'Activity' has over 1,5k categories, using regex we will reduce it to 13.</br>
      Aplling the function we get:
      | 'Activity'        | 'Value counts' |
      |-------------------|----------------|
      | surfing           | 1394           |
      | swimming          | 1159           |
      | fishing           | 1137           |
      | other             | 1101           |
      | diving            | 603            |
      | sailing           | 269            |
      | walking           | 220            |
      | bathing           | 192            |
      | floating in water | 102            |
      | ep_boats          | 72             |
      | kiting            | 43             |
      | feeding           | 12             |
      | Photoshooting     | 8              |
   
    


    - Cleaning columns 'Fatals':<br>

    |   Original             |    Transform    |  
    | ----------             | ----------------| 
    |N,M, n;                 |      N          |   
    |Y, y                    |      Y          | 
    |UNKNOWN, 2017, NaN      |    UNKNOWN      | 

7. Analyse the column 'Years':<br>
 dropped Years below 1900.
8. Export the database to CSV (Exported_Files path):<br>


## Results 
Most of the attacks are non lethal: </br>
| Qty Fatal  |    Qty Non-Fatal    |
| ---------- | -----------------   |
|   1389     |       4373          |
 </br>

Using the library matplotlib:</br>
<p align="center"><img align="center" src="https://user-images.githubusercontent.com/85833899/135141955-4fadab3d-9c5a-4918-9de6-1c17c9808d4a.png", width="80%"><br></p>

> Conclusion: Death by shark attack is uncommon .</br>

</br>
Considering the attacks since 1900s, we get an average of <b>26</b> attacks every year in the world. From these "26" attacks, every year only 6 are fatal ones.
</br>
</br>


> In the GSAF (Global Shark Attack Files) website, affirms that more people drown every year than are killed by sharks. According to <a href="https://www.cdc.gov/drowning/facts/index.html#:~:text=While%20children%20are%20at%20highest,11%20drowning%20deaths%20per%20day.">CDC</a> around 3960 people drown every year in USA which give us an average of 22 drowns <b>every day</b>. The fatal shark rate of Entire World is lower than drowns per year on USA.</br>

### Deadliest Activities
Analising the the activities that had death related we can see that people killed by shark while "surfing" are rare.  </br>

| Activity          | death rate |
|-------------------|------------|
| ep_boats          | 51.85%     |
| bathing           | 40.32%     |
| swimming          | 31.97%     |
| floating in water | 23.73%     |
| diving            | 19.72%     |
| other             | 16.34%     |
| sailing           | 16.06%     |
| fishing           | 10.90%     |
| walking           | 7.26%      |
| surfing           | 7.24%      |

> This result highlights that the shark attacks out of curiosity or unintentionally, more than by revenge.</br>

## Activity

 Although surfing has a low death by shark attack rate, most of the attacks happened while people were surfing. However, we cannot determine if surfing is a dangerous activity by only looking at this variable. According to <a href="https://sma.org.au/resources-advice/surfing/#:~:text=Surfing%20is%20regarded%20as%20a,of%20injuries%20are%20not%20serious.&text=Surfers%20most%20often%20sustain%20injuries%20to%20the%20leg%20(46%25).">SMA</a> Surfing has a very low injury rate (and that includes shark attacks ). Further more, as pointed before shark attacks are rare. 
 </br>

 Using the library seaborn:</br>
<p align="center"><img align="center" src="https://user-images.githubusercontent.com/85833899/135145231-de229003-725f-49e6-be86-556400649521.png", width="80%"><br></p>
 
> Again sharks are not likely to attack humans, a probable cause for the majority of shark attacks occur near the shore, in the surf zone and sandbars, because their natural preys live in these areas.</br>


## Countries 

It is common to hear people saying "do not surf in Australia because it has a high shark attack rate". Diving into the data set we can prove that this is untrue. 
USA alone has almost twice as much attacks than Australia, in fact both countries (USA and Australia) holds over 60% of the total attacks in the world.</br>

| Country          | Value Count |
|------------------|-------------|
| USA              | 1906        |
| AUSTRALIA        | 1084        |
| SOUTH AFRICA     | 487         |
| PAPUA NEW GUINEA | 128         |
| BRAZIL           | 100         |
| BAHAMAS          | 95          |
| NEW ZEALAND      | 89          |
| MEXICO           | 70          |
| REUNION          | 58          |
| PHILIPPINES      | 55          |


<br>
Attacks by country while surfing. Attacks while surfing are common in USA but this data is not necessary worrisome (the avg of attacks every year still very low comparing to other accidents).
 <br>
Using the library Matplotlib:</br>
<p align="center"><img align="center" src="https://user-images.githubusercontent.com/85833899/135147498-d0d515bb-7323-4207-a2d4-b886e58b7e40.png", width="80%"><br></p>


> Having the countries and the locations from the attacks we can plot a map where the attacks happened <b>while surfing</b>. <br>
Using the library folium:</br>
<p align="center"><img align="center" src="https://user-images.githubusercontent.com/85833899/135148582-e477b75e-5616-49e5-9869-e680bf87c8ab.png", width="80%"><br></p>



## Learning Process
### Theory Applied
- [x]  Pandas (Import and Export data)<br>
- [x] Explore Analysis Data<br>
- [x] Data Manipulation (Filtering)<br>
- [x] Data Cleaning <br>

### Challenges
- Understand the dataset;
- Choose which columns explore;
- Defining functions in other to clean the dataset;

### New Learnings
- Display information visually (matplotlib).

### Improvements
- There are some columns that are unexplored and could help adding further information about the attacks.</br>

## Author
Lucas Angulski
