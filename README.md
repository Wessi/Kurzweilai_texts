# Kurzweilai_texts

This repository contains the extracted text documents from the website kurzweilai as zip file and all the scripts used to convert the html page into text file. This readme file also shows some funky sentences generated from some randomly selected text file by using marky_markov library in Ruby.

`#import the marky_markov library in Ruby`  
`require 'marky_markov'`

`#create temporary dictionary as markovTempDic for parsing the text file`  
`markovTempDic = MarkyMarkov::TemporaryDictionary.new`  

`#parse the file named "the-future-of-life.txt" that i choose randomly and put inside folder test_text`  
`markovTempDic.parse_file "test_text/the-future-of-life.txt"`

`#generate some funky sentences from the parsed text file`  
`puts markovTempDic.generate_n_sentences 2`

`Output1:`
I presented my ideas on the potential and actual environmental benefits from GM technology. Discussing the danger of a drug that will allow modeling complex biological systems, he said he was not possible with pre-GM forms of mixing genes of species extinction is now at least

`puts markovTempDic.generate_n_sentences 3`

`Output2:`
Biological Micro Electronic Mechanical Systems covering contemporary efforts to place tiny diagnostic and therapeutic machines in the coronary arteries has been developing like a multicellular organism, including a nervous system. This will open the door to fully personalized medicine, in which people will routinely scan their entire medical record. He argued for different forms of mixing genes of species by 2010 .  Shortly thereafter, we should build each module to communicate through a pattern-recognition paradigm with other modules, pointing out that there

`puts markovTempDic.generate_n_sentences 5`

`Output3:`
The initial process of creating vulnerable plaque in the effectiveness of algorithms, he believes. Paul Saffo, the panel and the FIR Fat Insulin Receptor gene provides the promise of a scorpion over a corn flake bowl to describe the fear-mongering of GM protestors. Entomology, Museum of Comparative Zoology, Harvard University, described how little we know about life on Earth, and how rapidly life on Earth is slipping away from us, in terms of the insecticide required Health Systems for NASA, described some credible scenarios for exploration of the solar system during the 2020s we will create systems that have the dynamic qualities of living systems. Craig Venter, President of The Center for the Public Understanding of Science, Oxford University, said we are able to navigate through the bloodstream, have the opportunity to present my ideas on the potential

`#Finally clear the temporary dictionary`  
`markovTempDic.clear! `


