<p> test11</p>
<h1>Preparing Data for Joey NMT Toolkit</h1>

<h2>Introduction</h2>

<p>Joey NMT is a neural machine translation toolkit that aims to be accessible to novice learners.
 Joey NMT requires parallel text of the source language immediately followed by a translation from the       target language. This tutorial focuses on preparing data from less-resources languages through examples of  data preperation for the Tohono O'odham language. 
</p>

<h2> Parallel Text Sources</h2>  

<p>Many translations of the Bible have been made for less-resourced and endangered languges. If you are interested in using Joey NMT for a less-resourced languages, you might begin by searching for a Bible translaion. For training Tohono O'odham I used a translation of the New Testement from Wycliffe Bible Translators, Inc. It can be viewed here: https://ebible.org/find/details.php?id=oodNT 
</p>

<h2> Expected Format</h2>

 <p>This parallel text is provided in verses. The text of the source language is first, followed by the target language. Triple bars are used to divide the two languages. This is an example of the first 3 parallel verses in the train set after being processed.
</p>

<pre><code> I'm always thanking God for you because of the grace of God given to you in Christ Jesus. ||| Chum ani hekid ab si hoꞌigeꞌid g Jiosh em-hekaj. Ab amt i s-wohoch g Christ. T g Jiosh ab i em-mah g geꞌe i wehmtadag.
    Through him you have been made rich in everything, in all that you say and every aspect of what you know. ||| M heg hekaj s-mahch mo haschu s-apꞌe ch s-ap haꞌichu am hab junihim ch s-ap haꞌichu k amjed neneok.
    In fact the testimony of Christ was proved valid in your experience, ||| Am o e chehgidch mam s-wihnam an uꞌukch g haꞌichu t-ahga ab amjed g Christ.
</code></pre>
    
<p> The tag <sax> is used here becasue the target language data was provided in two orthographies. The New Testement text is in the Saxton-Saxton orthography <sax>, while parallel additional parallel texts was taken from dictionary examples in the Alvares-Hale orthography <ah>. The tag marks which orthography the source text are in. Using tags like this is only relevant if you are using data in multiple orthograhies. 
</p>
  
<h2> Creating Parallel Text</h2> 

<p>start with a tsv (Tab Separated Values) file of the source and target language. Each verse in English is separated by a tab and then the coresponding verse in Tohono O'odham 
</p>

<p>Here is an example of the eng-ood.tsv file.
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

<p> The last step is spliting the data in train, test, and dev sets. Here the data is split 80% train, 10% test, and %10 dev. 
</p>

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

<p> If we print the length of each list we see there are 5728 parallel verses in train, 716 in test, and 716 in dev.</p> 

<p>running this code in the same directory as eng-ood_NT.tsv writes and returns 3 txt files contianing the preprocessed train, test, and dev sets</p>

<p> if you download eng-ood_NT.tsv and extract_NT_verses.py to the same directory and then run extract_NT_verses.py, it will call eng-ood_NT.tsv and return a preprocessed train, test, and dev file.
</p>


<i>This research was funded by NSF-DEL and NSF-GRFP. Other contributers include Dr. Graham Neubig and Dr. Antonios Anastasopoulos. 
</i>
