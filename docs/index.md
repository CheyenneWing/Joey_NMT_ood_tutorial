<h1>Preparing Data for Joey NMT Toolkit</h1>

<h2>Introduction </h2>
  <p>Joey NMT is a neural machine translation toolkit that aims to be accessible to novice learners.
Joey NMT requires parallel text of the source language immediately followed by a translation from the target language. This tutorial focuses on preparing data from less-resources languages through examples of data preperation for the Tohono O'odham language. </p>

<h2> Parallel Text Sources </h2>  
  <p>https://ebible.org/find/details.php?id=oodNT
this parallel text is split in verses </p>
<p>show data before being processes </p>

<h2> Expected Format </h2>
   <p>Here the parallel sentences are provided in verses. The text of the source language is first, followed by the target language. Triple bars are used to divide the two languages. This is an example of the first 3 parallel verses in the train set after being processed. </p>
    <sax> I'm always thanking God for you because of the grace of God given to you in Christ Jesus. ||| Chum ani hekid ab si hoꞌigeꞌid g Jiosh em-hekaj. Ab amt i s-wohoch g Christ. T g Jiosh ab i em-mah g geꞌe i wehmtadag.
    <sax> Through him you have been made rich in everything, in all that you say and every aspect of what you know. ||| M heg hekaj s-mahch mo haschu s-apꞌe ch s-ap haꞌichu am hab junihim ch s-ap haꞌichu k amjed neneok.
    <sax> In fact the testimony of Christ was proved valid in your experience, ||| Am o e chehgidch mam s-wihnam an uꞌukch g haꞌichu t-ahga ab amjed g Christ.
  <p>The tag <sax> is used here becasue two target language data was provided in two orthographies. The New Testement parallel text is in the Saxton-Saxton orthographie, while parallel sentences taken from dictionary examples were in the Alvares-Hale orthography. The tag marks which orthograohy the Tohono O'odham examples are in. The tags at the beginning of the verses here are only relevant if you are uses sources from multiple orthograhies. </p>
  
<h2> Creating Parallel Text </h2> 
  <p>start with a tsv file, a tsv file is... </p>
  <p>Here is an example of the parallel text in a tsv file. </p>
    1CO01:2	It is sent to the church of God in Corinth, those who are being made right in Christ Jesus, called to live holy lives—and to everyone who worships the Lord Jesus Christ everywhere, the Lord both of them and of us.  Jiosh at ab i em-gawulkai mamt d wo hemajkamgajk. Kumt heg hekaj ab i e hemakoj wehsijj t-wehm ahchim mach hab waꞌap ab ihm g t-kownalig Jesus Christ.
    1CO01:3	May you have grace and peace from God our Father and the Lord Jesus Christ.  	Ab o wa si s-em-hoꞌigeꞌid g t-ohg Jiosh g t-kownalig Jesus Christ wehm ch ab wo wa baꞌich i em-mahkad g i wehmtadag ch s-ap tahhadkam.
    1CO01:4	I'm always thanking God for you because of the grace of God given to you in Christ Jesus.  	Chum ani hekid ab si hoꞌigeꞌid g Jiosh em-hekaj. Ab amt i s-wohoch g Christ. T g Jiosh ab i em-mah g geꞌe i wehmtadag.
  <p>To finish preprocessing the data and making it look like the example above we need to: </p> 
<ol>
<li>truecased </li>
<li>remove verse numbers and non-alphabet characters </li>
<li>incert tripple bars between the source and target languages </li>
<li>split data into train, test, and dev sets </li>  
</ol>


<i>This research was funded by NSF-DEL and NSF-GRFP. Other contributers include Dr. Graham Neubig and Dr. Antonios Anastasopoulos. <i/>
