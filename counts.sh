#!/bin/bash
#Script to count the number of images we have
 
echo -n "Brass"
echo " "
echo -n "Trumpet "
ls music_instruments_images/Brass/Trumpet | wc -l
echo -n "Tuba "
ls music_instruments_images/Brass/Tuba | wc -l
echo -n "Trombone "
ls music_instruments_images/Brass/Trombone | wc -l
echo -n "FrenchHorn "
ls music_instruments_images/Brass/FrenchHorn | wc -l
echo " "

echo -n "Woodwind"
echo " "
echo -n "Clarinet "
ls music_instruments_images/Woodwind/Clarinet | wc -l
echo -n "Bagpipes "
ls music_instruments_images/Woodwind/Bagpipes | wc -l
echo -n "Flute "
ls music_instruments_images/Woodwind/Flute | wc -l
echo -n "Saxophone "
ls music_instruments_images/Woodwind/Saxophone | wc -l
echo " "

echo -n "Percussion"
echo " "
echo -n "BassDrum "
ls music_instruments_images/Percussion/BassDrum | wc -l
echo -n "Conga "
ls music_instruments_images/Percussion/Conga | wc -l
echo -n "Piano "
ls music_instruments_images/Percussion/Piano | wc -l
echo -n "SnareDrum "
ls music_instruments_images/Percussion/SnareDrum | wc -l
echo " "

echo -n "Strings "
echo " "
echo -n "Banjo "
ls music_instruments_images/Strings/Banjo | wc -l
echo -n "Guitar "
ls music_instruments_images/Strings/Guitar | wc -l
echo -n "Harp "
ls music_instruments_images/Strings/Harp | wc -l
echo -n "Violin "
ls music_instruments_images/Strings/Violin | wc -l

