#! /bin/tcsh

# section for test.wsj

# name of the output file 
set FILE = "test-set-wsj"

echo Processing section wsj

zcat test.wsj/words/test.wsj.words.gz > /tmp/$$.words
zcat test.wsj/props/test.wsj.props.gz > /tmp/$$.props

## Choose syntax
# zcat test.wsj/synt.col2/test.wsj.synt.col2.gz > /tmp/$$.synt
# zcat test.wsj/synt.col2h/test.wsj.synt.col2h.gz > /tmp/$$.synt
# zcat test.wsj/synt.upc/test.wsj.synt.upc.gz > /tmp/$$.synt
zcat test.wsj/synt.cha/test.wsj.synt.cha.gz > /tmp/$$.synt

zcat test.wsj/senses/test.wsj.senses.gz > /tmp/$$.senses
zcat test.wsj/ne/test.wsj.ne.gz > /tmp/$$.ne

paste -d ' ' /tmp/$$.words /tmp/$$.synt /tmp/$$.ne /tmp/$$.senses /tmp/$$.props | gzip> /tmp/$$.section.gz

#echo Generating gzipped file $FILE.gz
zcat /tmp/$$.section* > $FILE.txt

echo Cleaning files
rm -f /tmp/$$*


# name of the output file
set FILE = "test-set-brown"

echo Processing section brown

zcat test.brown/words/test.brown.words.gz > /tmp/$$.words
zcat test.brown/props/test.brown.props.gz > /tmp/$$.props

## Choose syntax
# zcat test.brown/synt.col2/test.brown.synt.col2.gz > /tmp/$$.synt
# zcat test.brown/synt.col2h/test.brown.synt.col2h.gz > /tmp/$$.synt
# zcat test.brown/synt.upc/test.brown.synt.upc.gz > /tmp/$$.synt
zcat test.brown/synt.cha/test.brown.synt.cha.gz > /tmp/$$.synt

zcat test.brown/senses/test.brown.senses.gz > /tmp/$$.senses
zcat test.brown/ne/test.brown.ne.gz > /tmp/$$.ne

paste -d ' ' /tmp/$$.words /tmp/$$.synt /tmp/$$.ne /tmp/$$.senses /tmp/$$.props | gzip> /tmp/$$.section.gz

#echo Generating gzipped file $FILE.gz
#zcat /tmp/$$.section* | gzip -c > $FILE.gz
zcat /tmp/$$.section* > $FILE.txt

echo Cleaning files
rm -f /tmp/$$*
