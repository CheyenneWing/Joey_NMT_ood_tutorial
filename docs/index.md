<p> test14</p>
<h1>Preparing Data for Joey NMT Toolkit</h1>

<h2>Introduction</h2>

<p>Joey NMT is a neural machine translation toolkit that aims to be accessible to novice learners.
 Joey NMT requires parallel text of the source language immediately followed by a translation from the       target language. This tutorial focuses on preparing data from less-resources languages through examples of  data preperation for the Tohono O'odham language (ISO code ood). Tohono O'odham is an endangered and less-resourced Native American language originating from southern Arizona and north-western Mexico.
</p>

<h2> Parallel Text Sources</h2>  

<p>Many translations of the Bible have been made for less-resourced and endangered languges. If you looking for data for a less-resourced languages, searching for Bible translaion can be a good place to start. For preparing data for Joey NMT in Tohono O'odham I used the "Jiosh Wechij O'ohana" English to Tohono O'odham translation of the New Testament from Wycliffe Bible Translators, Inc. The English to Tohono O'odham translation of the New Testament "Jiosh Wechij O'ohana" can be viewed by following this link: https://ebible.org/find/details.php?id=oodNT 
</p>

<h2> Expected Format</h2>

 <p>The text below is parallel text is provided from scripture verses. The text of the source language is first, followed by the target language. Triple bars are used to divide the two languages. This is an example of the first 3 parallel verses in the train set after being correctly preprocessed.
</p>

<pre><code> I'm always thanking God for you because of the grace of God given to you in Christ Jesus. ||| Chum ani hekid ab si hoꞌigeꞌid g Jiosh em-hekaj. Ab amt i s-wohoch g Christ. T g Jiosh ab i em-mah g geꞌe i wehmtadag.
    Through him you have been made rich in everything, in all that you say and every aspect of what you know. ||| M heg hekaj s-mahch mo haschu s-apꞌe ch s-ap haꞌichu am hab junihim ch s-ap haꞌichu k amjed neneok.
    In fact the testimony of Christ was proved valid in your experience, ||| Am o e chehgidch mam s-wihnam an uꞌukch g haꞌichu t-ahga ab amjed g Christ.
</code></pre>
    
<p> The tag <sax> is used here becasue the target language data was provided in two orthographies. "Jiosh Wechij O'ohana" is written in the Saxton-Saxton orthography <sax>, while additional parallel texts used were gather from an dictionary examples written in the Alvares-Hale orthography <ah>. The tag at the beginning of each verse marks which orthography the target text is in. Using tags like this is only necessary if you are using data in multiple orthograhies. 
</p>
  
<h2> Creating Parallel Text</h2> 

<p>Start with a tsv (Tab Separated Values) file of the source and target language. Each verse in English is separated by a tab and then the coresponding verse in ood. 
</p>

<p>Following is an example data in a tsv file format.
</p>
  
<pre><code>1CO01:2	It is sent to the church of God in Corinth, those who are being made right in Christ Jesus, called to live holy lives—and to everyone who worships the Lord Jesus Christ everywhere, the Lord both of them and of us.  Jiosh at ab i em-gawulkai mamt d wo hemajkamgajk. Kumt heg hekaj ab i e hemakoj wehsijj t-wehm ahchim mach hab waꞌap ab ihm g t-kownalig Jesus Christ.
    1CO01:3	May you have grace and peace from God our Father and the Lord Jesus Christ.  	Ab o wa si s-em-hoꞌigeꞌid g t-ohg Jiosh g t-kownalig Jesus Christ wehm ch ab wo wa baꞌich i em-mahkad g i wehmtadag ch s-ap tahhadkam.
    1CO01:4	I'm always thanking God for you because of the grace of God given to you in Christ Jesus.  	Chum ani hekid ab si hoꞌigeꞌid g Jiosh em-hekaj. Ab amt i s-wohoch g Christ. T g Jiosh ab i em-mah g geꞌe i wehmtadag.
</code></pre>
    
<p> To finish preprocessing the data in the tsv file and make it look like the expected format example we need to: 
</p> 
  
<ol>
  <li>Truecase </li>
  <li>Remove verse numbers and non-alphabet characters </li>
  <li>Incert tripple bars between the source and target languages </li> 
</ol>

<p> note the following code is not yet complete</p>
<pre class="line-number">
  <code class="language-python">
  
    import re
    # open, read, and truecase the English to Tohono O'odham tsv file
    #of the New Testament
    tsv = open('eng-ood_NT.tsv')
    new_testament = tsv.read().lower()
    
    # remove verse numbers and non-alphabet characters
    normalize_text = re.sub(r'(\d.*\d)*[^a-z\s]*','',new_testament)

    # remove the tab in each verse and replace it with triple bars
    # these triple bars separate the source and target language in each verse
    add_trip_bars = re.sub(r'\t','|||',normalize_text).strip()
    
    # split verses at newline
    verse_sep = add_trip_bars.split('\n')
    
  </code>
</pre>

<p> Now the final step in preprocessing is spliting the data in train, test, and dev sets. Here the data is split 80% train, 10% test, and %10 dev. Note that we don't want to split the data into train, test, and dev sets as it currently is. If we did then whole books would stay together in sets. Instead we want to diversify the data we write to the 3 sets for a more accurate view of all the whole dataset. One way to do this is to iterate through ten verses at a time, then append 1 verse to dev, 1 verse to test, and the remaining 8 to train. This accomplishes the task of splitting the data into 80% train, 10% test, and 10% dev while also ensurring that each set is an accurate representation of the whole data set. 
</p>

<p> note the following code is not yet complete</p>
<pre class="line-number">
  <code class="language-python">
  
    # make empty train, test, dev lists
    train = []
    test = []
    dev = []

    # use modulo operator in Python to sep 10% 10 % dump last 80% 
    for i,example in enumerate(verse_sep):
        if i % 10 == 1:
            dev.append(example)
        elif i % 10 == 2:
            test.append(example)
        else:
            train.append(example)
    print(len(dev))
    print(len(test))
    print(len(train))

    # write out the train, test, and dev lists to files
    with open('eng-ood_dev.txt', 'w') as filehandle:
        for listitem in dev:
            filehandle.write('%s\n' % listitem)
    with open('eng-ood_test.txt', 'w') as filehandle:
        for listitem in test:
            filehandle.write('%s\n' % listitem)
    with open('eng-ood_train.txt', 'w') as filehandle:
        for listitem in train:
            filehandle.write('%s\n' % listitem)
  
  </code>
</pre>

<p> If we print the length of each list we see there are 5728 parallel verses in train, 716 in test, and 716 in dev. This is the 80/10/10 division we want from the dataset! </p> 

Following are three examples from the dev data. You can see that it is closer to expected format example above, but not quite perfect. Here we have triple bars to the beginning of the eng verse when we only want triple bars inbetween the source and target code in each verse. It also leaves part of the reference in some verses.

<pre><code>
|||i hope to see you soon so we can talk face to face  |||nani pi am shimimk mant wo mneid k wo mwehm neo ab amjed 
act|||men of galilee why are you standing here staring at the sky they asked this same jesus who has been taken up from you to heaven shall come in the same way you saw him go into heaven |||ch hab kaij pi g ia hu wabsh wo gegokk ch am uhgk nenead mat hebai hih g jesus hema tash at wo wa uhpam jiwia hab masma mam hemuch am neid mat has i masma gam hu hih 
act|||so now we have to choose someone who has been with us the whole time that jesus was with us  from the time john was baptizing up until the day jesus was taken up to heaven from us one of these must be chosen to join together with us as we witness giving evidence of jesus resurrection  |||kut id hekaj hemho wa am hema wo i kekiwua twehm mat hab waap wo wohokamch mat uhpam e chegito g tkownalig jesus t hemho wa d wo hema tahchimk mach ga hujed i wehmajkahim g jesus am i amjed mat g john pahl wako am hugkam mat im hu hih dahm kahchim ch ed neh bash kaij g peter ch am i haasa neo 
</code></pre>


<p> following is an editted script that returns the correct output. I chose to include the broken script as well as this working script, because this working script is much less intuitive then the broken script, and doesn't make the necessary steps as clear. I have added comments to each step in the following script to descripe the code and make the process more transparent. <br> ADD EDITED SOURCE CODE HERE</p>

<p>running this code in the same directory as the tsv file writes and returns three txt files contianing the preprocessed train, test, and dev sets into the directory where the code was initialized.</p>

<p> The complete tsv file and working code can be accessed through this link:<br> https://github.com/CheyenneWing/Preparing-Data-for-Joey-NMT-Toolkit/tree/main/docs 
</p>



<i>This research was funded by NSF-DEL and NSF-GRFP. Other contributers include Dr. Graham Neubig and Dr. Antonios Anastasopoulos. Copywrite for the bible translation used is held by © 2010, Wycliffe Bible Translators, Inc. All rights reserved.
</i>
