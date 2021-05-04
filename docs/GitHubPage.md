<p>test28</p>
<h1><span style="color:SteelBlue">Preparing Data for Joey NMT Toolkit</span></h1>

<h2><span style="color:SteelBlue">Introduction</span></h2>

<p>Joey NMT is a neural machine translation toolkit that aims to be accessible to novice learners.
 Joey NMT requires parallel text of the source language immediately followed by a translation from the       target language. This tutorial focuses on preparing data from less-resources languages through examples of  data preperation for the Tohono O'odham language (ISO code ood). Tohono O'odham is an endangered and less-resourced Native American language originating from southern Arizona and north-western Mexico.
</p>

<h2><span style="color:SteelBlue">Parallel Text Sources</span></h2>  

<p>Many translations of the Bible have been made for less-resourced. When looking for data for a less-resourced languages, searching for a Bible translaion can be a good place to start. For preparing ood data for Joey NMT I used the "Jiosh Wechij O'ohana" and English (ISO code eng) to ood translation of the New Testament from Wycliffe Bible Translators, Inc. "Jiosh Wechij O'ohana" can be viewed here: <a>https://ebible.org/find/details.php?id=oodNT</a> 
</p>

<h2><span style="color:SteelBlue">Expected Format</span></h2>

 <p>The text below is parallel eng to ood text. The text of the source language is first, followed by the target language. Triple bars are used to divide the two languages. This is an sample of 3 parallel verses after being correctly preprocessed.
</p>

<pre><code>&lt;sax&gt; In fact the testimony of Christ was proved valid in your experience, ||| Am o e chehgidch mam s-wihnam an uꞌukch g haꞌichu t-ahga ab amjed g Christ.
&lt;sax&gt; so that you're not missing any spiritual gift as you wait for the coming of our Lord Jesus Christ. ||| Kum wehs ab i neid g hoꞌigeꞌidadgaj ch ep nenida mat ep wo jiwia.
&lt;sax&gt; I came to you in weakness, fearful and trembling. ||| ch heg hekaj si s‑gihug ch gigiwuk.
</code></pre>
    
<p> The tag &lt;sax&gt; is used here becasue the target data was collected in two orthographies. "Jiosh Wechij O'ohana" is written in the Saxton-Saxton orthography &lt;sax&gt;, while additional parallel texts were sourced from a ood dictionary examples written in the Alvares-Hale orthography &lt;ah&gt;. Tagging the beginning of each verse is only necessary if you are using data in multiple orthograhies. 
</p>
 
 <p><span style="color:SteelBlue"><b>A Note on Tokenization and Truecasing: For the purposes of Joey NMT it is not necessary to tokenize or truecase data like when preparing real tranlation data. To respect the copyright on the Tohono O'odham New Testament translation, "Jiosh Wechij O'ohana", I have not applied tokenization or truecased the data.</b></span></p> 
  
<h2><span style="color:SteelBlue">Creating Parallel Text</span></h2> 

<p>Start with a tsv (Tab Separated Values) file of the source and target language. Each eng verse is separated by a tab followed by the coresponding verse in ood. 
</p>

<p>Following is an sample of the eng-ood data in a tsv file format.
</p>
  
<pre><code>1CO01:2	It is sent to the church of God in Corinth, those who are being made right in Christ Jesus, called to live holy lives—and to everyone who worships the Lord Jesus Christ everywhere, the Lord both of them and of us.  Jiosh at ab i em-gawulkai mamt d wo hemajkamgajk. Kumt heg hekaj ab i e hemakoj wehsijj t-wehm ahchim mach hab waꞌap ab ihm g t-kownalig Jesus Christ.
1CO01:3	May you have grace and peace from God our Father and the Lord Jesus Christ.  	Ab o wa si s-em-hoꞌigeꞌid g t-ohg Jiosh g t-kownalig Jesus Christ wehm ch ab wo wa baꞌich i em-mahkad g i wehmtadag ch s-ap tahhadkam.
1CO01:4	I'm always thanking God for you because of the grace of God given to you in Christ Jesus.  	Chum ani hekid ab si hoꞌigeꞌid g Jiosh em-hekaj. Ab amt i s-wohoch g Christ. T g Jiosh ab i em-mah g geꞌe i wehmtadag.
</code></pre>
    
<p> To finish preprocessing the data in the tsv file and make it look like the expected format we need to: 
</p> 
  
<ol>
  <li>Remove book name, chapter number, and verse numbers from the beginning of each verse</li>
  <li>Incert tripple bars between the source and target languages </li> 
  <li>Separate data into train, test, and dev sets</li>
</ol>


<p> NOTE: the following code is <b>not</b> the finished working script</p>
<pre class="line-number"><code class="language-python">

    import re

    # open and read the English to Tohono O'odham verses from tsv file
    tsv = open('eng-ood_NT.tsv')
    NT = tsv.read()

    # remove chapter and verse number from beginning of each line
    rm_num = re.sub(r'(\d.*\d)','',NT)

    # remove the tab separating source and target language and replace it with triple bars
    add_trip_bars = re.sub(r'\t','|||',rm_num).strip()

    # split verses at newline
    verse_sep = add_trip_bars.split('\n')
    
</code></pre>

<p> The final step in preprocessing is to split the data into train, test, and dev sets. Here the data is split 80% train, 10% test, and %10 dev. Now we don't want to split the data into train, test, and dev sets as it currently is. If we did then entire books would be assigned to sets together. Instead we want to diversify the data we write to the 3 sets for a more accurate view of all the whole dataset. One way to do this is to iterate through ten verses at a time, then append 1 verse to dev, 1 verse to test, and the remaining 8 to train. This accomplishes the task of splitting the data into 80% train, 10% test, and 10% dev while also ensurring that each set is an accurate representation of the data set as a whole. 
</p>

<p>NOTE: the following code is <b>not</b> the finished working script</p>
<pre class="line-number"><code class="language-python">

    # make empty train, test, dev lists
    train = []
    test = []
    dev = []
    
    # use modulo operator in Python to sep 10% of data to dev, 10 % to test, 
    # and remaining 80% to train 
    for i,example in enumerate(verse_sep):
        # if modulo operator returns 1 append to dev set
        if i % 10 == 1:
            dev.append(example)
        # if modulo operator returns 2 append to test set
        elif i % 10 == 2:
            test.append(example)
        # append remaining 8 to train
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
</code></pre>

<p> If we print the length of each set we see there are 5728 parallel verses in train, 716 in test, and 716 in dev. This is the 80/10/10 division we want from the dataset! </p> 

Following is a sample of three verses after running this script. You can see that it is closer to expected format example above, but not quite perfect. Here we have triple bars at the beginning of the eng verse and ood verse, when we only want triple bars separating the source and target code in each verse. This script removes the chapter and verse numbers but not all the book names. We also haven't added the orthography tag
&lt;sax> 

<pre><code>|||Doesn't nature itself indicate that a man with long hair disgraces himself?  |||S‑mahch ach mo g cheꞌechew moꞌo s‑ta edama am wehhejed g cheoj 
JHN|||This was the third time Jesus had appeared to the disciples after being raised from the dead. |||Id o d waꞌi waikkokam mad am i e chehgi g Jesus t‑wui amjed mad ab i wuhsh muhkig amjed. 
HEB|||He was placed much higher than the angels since he received a greater name than them.  |||Neh, bo wa masma am e chehgidch mo id d alidaj g Jiosh. K heg hekaj tasho mo baꞌich d i si s-has haꞌichu mo hi g anghil.
</code></pre>

<p> following is an editted script that returns the correct output. I chose to include the script above, as well as this working script bellow, because this working script is much less intuitive. I have added comments to try and make the process more transparent.</p>

<pre class="line-number"><code class="language-python">
    Place Holder
</code></pre>

<p>running this code in the same directory as the tsv file will write three txt files contianing the preprocessed train, test, and dev sets into the directory where the code was initialized. </p>

Following is a final sample of successfully preprocessed data! 
<pre><code>&lt;sax&gt; If it works out for me to go too, they can come with me. ||| Kunt ahni am epai wo ha oi matp d wo Jiosh tatchuik mant am wo hih.
&lt;sax&gt; Whatever you do, do it in love. ||| ch ab wo e chehgidch wehs haꞌichu k ed mam ab si pihk e elid wehs ha hekaj.
&lt;sax&gt; My love to all of you in Christ Jesus. Amen. ||| Ab ani si pihk ni‑elid wehs em‑hekaj ahpim ni‑wehm wohochuddam.
</code></pre>

<p> The complete tsv file and working code can be accessed here <a>https://github.com/CheyenneWing/Preparing-Data-for-Joey-NMT-Toolkit/tree/main/docs</a> 
</p>
<p><span style="color:Black"><i>This research was funded by NSF-DEL and NSF-GRFP. Other contributers include Dr. Graham Neubig and Dr. Antonios Anastasopoulos. Copywrite for the bible translation used is held by © 2010, Wycliffe Bible Translators, Inc. All rights reserved.
 </i></span></p>
