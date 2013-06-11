<?php

$school = $_POST["school"];
/*$address = $_POST["address"];
$phone = $_POST["phone"];
$fax = $_POST["fax"];
*/

echo "yep";

//print_r($schoolz);


//echo "school are " . $school;
//echo $schools[$phone];
/*
$schools["Abbott&#039s Coll. Claremont"]["Address"]="P O Box 2317
CLAREINCH
7740";	$schools["Abbott&#039s Coll. Claremont"]["Phone"]="021 671 1173";	$schools["Abbott&#039s Coll. Claremont"]["Fax"]="021 671 2630";
$schools["Abbott&#039s Coll. Milnerton"]["Address"]="8 Eddison Way
Century Gate
Century Cit
7441";	$schools["Abbott&#039s Coll. Milnerton"]["Phone"]="021 551 4090";	$schools["Abbott&#039s Coll. Milnerton"]["Fax"]="021 551 4093";
$schools["Alexander Sinton High"]["Address"]="Thornton Road
Crawford
7764";	$schools["Alexander Sinton High"]["Phone"]="021 697 1350";	$schools["Alexander Sinton High"]["Fax"]="021 696 1756";
$schools["Arcadia Sec. School"]["Address"]="03 Karee Road
BONTEHEUWEL
7764";	$schools["Arcadia Sec. School"]["Phone"]="021 694 9941";	$schools["Arcadia Sec. School"]["Fax"]="021 694 1736";
$schools["Athlone High School"]["Address"]="Calendula Road
SILVERTOWN
0184";	$schools["Athlone High School"]["Phone"]="021 637 6930";	$schools["Athlone High School"]["Fax"]="021 637 4151";
$schools["Atlantis Sek. Skool"]["Address"]="P O Box 3019
Atlantis
7349";	$schools["Atlantis Sek. Skool"]["Phone"]="021 572 3330";	$schools["Atlantis Sek. Skool"]["Fax"]="021 572 7963";
$schools["Belgravia High School"]["Address"]="Veld Road
BELGRAVIA ESTATE
7764
";	$schools["Belgravia High School"]["Phone"]="021 696 5118";	$schools["Belgravia High School"]["Fax"]="021 697 0370";
$schools["Bellville South S. School"]["Address"]="P O Box 367
KASSELSVLEI
BELLVILLE SOUTH
7533";	$schools["Bellville South S. School"]["Phone"]=" 021 951 6600";	$schools["Bellville South S. School"]["Fax"]="021 951 5270";
$schools["Bellville H S"]["Address"]="De La Haye Laan
BELLVILLE
7530";	$schools["Bellville H S"]["Phone"]="021 948 4140";	$schools["Bellville H S"]["Fax"]="021 948 1801";
$schools["Bellville Technical H S"]["Address"]="Private Bag X4
SANLAMHOF
7532";	$schools["Bellville Technical H S"]["Phone"]="021 948 6951";	$schools["Bellville Technical H S"]["Fax"]="021 946 3752";
$schools["Bergvliet High School"]["Address"]="Firgrove Way
BERGVLIET
7945";	$schools["Bergvliet High School"]["Phone"]="021 712 0284";	$schools["Bergvliet High School"]["Fax"]="021 715 0631";
$schools["Bloemhof H Meisiesskool"]["Address"]="Posbus 188
STELLENBOSCH
7599";	$schools["Bloemhof H Meisiesskool"]["Phone"]=" 021 887 3067";	$schools["Bloemhof H Meisiesskool"]["Fax"]="021 887 3044";
$schools["Boland Landbouskool "]["Address"]="Privaatsak X01
WINDMEUL
7630";	$schools["Boland Landbouskool "]["Phone"]="021 869-8143";	$schools["Boland Landbouskool "]["Fax"]="021869-8144";
$schools["Bredasdorp H S"]["Address"]="Posbus 255
BREDASDORP
7280";	$schools["Bredasdorp H S"]["Phone"]="028 424 2207";	$schools["Bredasdorp H S"]["Fax"]="028 424 1210";
$schools["Bridge House College"]["Address"]="P O Box 444
FRANSCHHOEK
7690";	$schools["Bridge House College"]["Phone"]="021 874-1790";	$schools["Bridge House College"]["Fax"]="021 874-1923";
$schools["Buren Hoerskool"]["Address"]="Poole Street
YSTERPLAAT
7405";	$schools["Buren Hoerskool"]["Phone"]="021 511-1912";	$schools["Buren Hoerskool"]["Fax"]="021 510 8206";
$schools["Camps Bay High School"]["Address"]="Lower Kloof Road
CAMPS BAY
8005";	$schools["Camps Bay High School"]["Phone"]="021 438 1507";	$schools["Camps Bay High School"]["Fax"]="021 438 5912";
$schools["Cathkin High School"]["Address"]="5th Street
HEIDEVELD
7764";	$schools["Cathkin High School"]["Phone"]="021 637 5366";	$schools["Cathkin High School"]["Fax"]="021 633 2701";
$schools["Ned Doman H S"]["Address"]="Buckley Avenue
ATHLONE
7764";	$schools["Ned Doman H S"]["Phone"]="021 696 5114";	$schools["Ned Doman H S"]["Fax"]="021 696 6275";
$schools["Ocean View Sec School"]["Address"]="Hydra Avenue
OCEAN VIEW
7995";	$schools["Ocean View Sec School"]["Phone"]="021 783 1623";	$schools["Ocean View Sec School"]["Fax"]="021 783 3593";
$schools["Paarl Boys&#039 H S"]["Address"]="P O Box 11
PAARL
7646";	$schools["Paarl Boys&#039 H S"]["Phone"]="021 872 2875";	$schools["Paarl Boys&#039 H S"]["Fax"]="021 872 5246";
$schools["Paarl Gimnasium "]["Address"]="Posbus 281
PAARL
7620";	$schools["Paarl Gimnasium "]["Phone"]="021 872 1541";	$schools["Paarl Gimnasium "]["Fax"]="021 872 8654";
$schools["Paarl Girls&#039 High School"]["Address"]="Posbus 50
PAARL
7622";	$schools["Paarl Girls&#039 High School"]["Phone"]="021 872 1730";	$schools["Paarl Girls&#039 High School"]["Fax"]="021 872 9102";
$schools["Parel Vallei High School"]["Address"]="Posbus 400
SOMERSET WES
7129";	$schools["Parel Vallei High School"]["Phone"]="021 852 1228";	$schools["Parel Vallei High School"]["Fax"]="021 852 5005";
$schools["Parklands College of Educ."]["Address"]="P O Box 11546
BLOUBERGRANDT
7443";	$schools["Parklands College of Educ."]["Phone"]="021 557 8428";	$schools["Parklands College of Educ."]["Fax"]="021 557 8421";
$schools["Paul Roos Gymnasium"]["Address"]="Suidwal Road
STELLENBOSCH
7600";	$schools["Paul Roos Gymnasium"]["Phone"]="021 887 0017";	$schools["Paul Roos Gymnasium"]["Fax"]="021 883 8461";
$schools["Pinelands H S"]["Address"]="Forest Drive
PINELANDS
7405";	$schools["Pinelands H S"]["Phone"]="021 531 7410";	$schools["Pinelands H S"]["Fax"]="021 531 7415";
$schools["Plumstead High School"]["Address"]="Basil Road
PLUMSTEAD
7800";	$schools["Plumstead High School"]["Phone"]="021 761 8066";	$schools["Plumstead High School"]["Fax"]="021 797 8494";
$schools["Portland High School"]["Address"]="C/O Merrydale &
Morgenster Roads
PORTLAND
7785";	$schools["Portland High School"]["Phone"]="021 374 4141/2";	$schools["Portland High School"]["Fax"]="021 374 3107";
$schools["President H S "]["Address"]="Tygerbergstraaat
VRIJZEE
7460";	$schools["President H S "]["Phone"]="021 591 5183";	$schools["President H S "]["Fax"]="021 591 5181";
$schools["Proteus Senior Sek Skool"]["Address"]="P O Box 952
REYGERSDAL
ATLANTIS
7352";	$schools["Proteus Senior Sek Skool"]["Phone"]="021 572 6277";	$schools["Proteus Senior Sek Skool"]["Fax"]="021 572 1540";
$schools["Queens Park High School"]["Address"]="Balfour Road
WOODSTOCK
7945";	$schools["Queens Park High School"]["Phone"]="021 448 1997/8";	$schools["Queens Park High School"]["Fax"]="021 448 3043";
$schools["Reddam Coll. Constantia"]["Address"]="Private Bag X14
CONSTANTIA
7848";	$schools["Reddam Coll. Constantia"]["Phone"]="021 702 2322";	$schools["Reddam Coll. Constantia"]["Fax"]="021 702 2366";
$schools["Rhenish Girls&#039 H S"]["Address"]="P O Box 87
STELLENBOSCH
7599";	$schools["Rhenish Girls&#039 H S"]["Phone"]="021 887 6807";	$schools["Rhenish Girls&#039 H S"]["Fax"]="021 887 8090";
$schools["Rhodes High School"]["Address"]="Montreal Avenue
MOWBRAY
7700";	$schools["Rhodes High School"]["Phone"]="021 689 8228";	$schools["Rhodes High School"]["Fax"]="021 689 2404";
$schools["Cedar House"]["Address"]="5 Ascot Road
KENILWORTH
7708";	$schools["Cedar House"]["Phone"]="021 762 0649";	$schools["Cedar House"]["Fax"]="021 761 8556";
$schools["Citrusdal H S"]["Address"]="Privaatsak X2
CITRUSDAL
7340";	$schools["Citrusdal H S"]["Phone"]="022 921 3931";	$schools["Citrusdal H S"]["Fax"]="022 921 2100";
$schools["Constantia Waldorf"]["Address"]="Spaanschemat River Rd
CONSTANTIA
7806";	$schools["Constantia Waldorf"]["Phone"]="021 794 2103";	$schools["Constantia Waldorf"]["Fax"]="021 794 1105";
$schools["Curro Private School"]["Address"]="P O Box 2436
DURBANVILLE
7530";	$schools["Curro Private School"]["Phone"]="021 975 6377";	$schools["Curro Private School"]["Fax"]="021 975 7539";
$schools["De Kuilen H S "]["Address"]="Posbus 301
KUILSRIVIER
7579";	$schools["De Kuilen H S "]["Phone"]="021 903 5121";	$schools["De Kuilen H S "]["Fax"]="021 903 0317";
$schools["D F Malan H S "]["Address"]="Frans Conradieierylaan
BELLVILLE
7530";	$schools["D F Malan H S "]["Phone"]="021 948 2996";	$schools["D F Malan H S "]["Fax"]="021 948 8781";
$schools["Deutsche Schule Kapstadt"]["Address"]="28 Bayview Avenue
TAMBOERSKLOOF
8001";	$schools["Deutsche Schule Kapstadt"]["Phone"]="021 423 6325";	$schools["Deutsche Schule Kapstadt"]["Fax"]="021 423 8349";
$schools["Bishops "]["Address"]="Campground road
RONDBOSCH
7700";	$schools["Bishops "]["Phone"]="021 659 1000";	$schools["Bishops "]["Fax"]="021 659 1013";
$schools["Durbanville H S"]["Address"]="Posbus 417
DURBANVILLE
7551";	$schools["Durbanville H S"]["Phone"]="021 976 3189";	$schools["Durbanville H S"]["Fax"]="021 976 3188";
$schools["Eben Donges High School"]["Address"]="Van der Bijlstraat
KRAAIFONTEIN
7570";	$schools["Eben Donges High School"]["Phone"]="021 988 7439";	$schools["Eben Donges High School"]["Fax"]="021 988 1441";
$schools["Edgemead High School"]["Address"]="Letchworth Drive
EDGEMEAD
7441";	$schools["Edgemead High School"]["Phone"]="021 558 1132";	$schools["Edgemead High School"]["Fax"]="021 558 4407";
$schools["El Shaddai Christian Sch"]["Address"]="P O Box 1980
DURBANVILLE
7551";	$schools["El Shaddai Christian Sch"]["Phone"]="021 975 1980";	$schools["El Shaddai Christian Sch"]["Fax"]="021 975 1985";
$schools["Fairbairn College"]["Address"]="Hugo Street
GOODWOOD
7460";	$schools["Fairbairn College"]["Phone"]="021 591 7117";	$schools["Fairbairn College"]["Fax"]="021 591 0107";
$schools["Fish Hoek Middle School"]["Address"]="Recreation Road
FISH HOEK
7975";	$schools["Fish Hoek Middle School"]["Phone"]="021 782 6121";	$schools["Fish Hoek Middle School"]["Fax"]="021 782 6171";
$schools["Fish Hoek High School"]["Address"]="13th Avenue
FISH HOEK
7975";	$schools["Fish Hoek High School"]["Phone"]="021 782 1107";	$schools["Fish Hoek High School"]["Fax"]="021 782 5438";
$schools["Garlandale High School"]["Address"]="General Street
ATHLONE
7780";	$schools["Garlandale High School"]["Phone"]="021 696 7908";	$schools["Garlandale High School"]["Fax"]="021 696 9313";
$schools["Cosat (Centre Science & T)"]["Address"]="P O Box 376
MITCHELLS PLAIN
7789";	$schools["Cosat (Centre Science & T)"]["Phone"]="021 361 3430";	$schools["Cosat (Centre Science & T)"]["Fax"]="021 361 8880";
$schools["Good Hope Seminary H S"]["Address"]="Hope Street
GARDENS  Cape Town
8000";	$schools["Good Hope Seminary H S"]["Phone"]="021 465 2330";	$schools["Good Hope Seminary H S"]["Fax"]="021 461 3902";
$schools["Rocklands Sec School"]["Address"]="c/o Cedar & Eisleben Roads
Rocklands MITCHELL&#039S PLAIN 
7798";	$schools["Rocklands Sec School"]["Phone"]="021 392 7139/0";	$schools["Rocklands Sec School"]["Fax"]="021 391 1653";
$schools["Rondebosch Boys&#039 H S"]["Address"]="Canigou Avenue
RONDEBOSCH
7700";	$schools["Rondebosch Boys&#039 H S"]["Phone"]="021 686 3987";	$schools["Rondebosch Boys&#039 H S"]["Fax"]="021 689 9726";
$schools["Rustenburg High School"]["Address"]="Camp Ground Road
RONDEBOSCH
7700";	$schools["Rustenburg High School"]["Phone"]="021 686 4066";	$schools["Rustenburg High School"]["Fax"]="021 686 7114";
$schools["Sama High School"]["Address"]="75 Main Road
DIEP RIVER
7940";	$schools["Sama High School"]["Phone"]="021 715 4777";	$schools["Sama High School"]["Fax"]="021 715 2112";
$schools["Sans Souci Girls&#039 H S"]["Address"]="Sans Souci Girls’ High School
PO Box 44330
Claremont 
7735

";	$schools["Sans Souci Girls&#039 H S"]["Phone"]="021 671 7188";	$schools["Sans Souci Girls&#039 H S"]["Fax"]="021 683 4090";
$schools["Sarepta High School"]["Address"]="P O Box 22
KUILS RIVER
7579";	$schools["Sarepta High School"]["Phone"]="021 903 2179";	$schools["Sarepta High School"]["Fax"]="021 903 8298";
$schools["Settlers High School"]["Address"]="P O Box 599
BELLVILLE
7535";	$schools["Settlers High School"]["Phone"]="021 948 6116";	$schools["Settlers High School"]["Fax"]="021 949 0859";
$schools["Simunye High School"]["Address"]="P O Box 3050
DELFT
7102";	$schools["Simunye High School"]["Phone"]="021 955 2056";	$schools["Simunye High School"]["Fax"]="021 955 0106";
$schools["SA College High School"]["Address"]="Newlands Avenue
NEWLANDS
7800";	$schools["SA College High School"]["Phone"]="021 689 4164";	$schools["SA College High School"]["Fax"]="021 685 2669";
$schools["Table View High School"]["Address"]="Janssens Avenue
TABLEVIEW
7441";	$schools["Table View High School"]["Phone"]="021 557 3602";	$schools["Table View High School"]["Fax"]="021 557 7779";
$schools["Somerset College"]["Address"]="P O Box 2440
SOMERSET WEST
7129";	$schools["Somerset College"]["Phone"]="021 842 3035";	$schools["Somerset College"]["Fax"]="021 842 3908";
$schools["South Peninsula H S"]["Address"]="Old Kendal Road
DIEP RIVER
7945
";	$schools["South Peninsula H S"]["Phone"]="021 712 9318";	$schools["South Peninsula H S"]["Fax"]="021 715 0291";
$schools["Springfield Convent"]["Address"]="St Johns Road
WYNBERG
7800";	$schools["Springfield Convent"]["Phone"]="021 797 6169";	$schools["Springfield Convent"]["Fax"]="021 762 7930";
$schools["Star International H S"]["Address"]="P O Box 10
ATHLONE
7760";	$schools["Star International H S"]["Phone"]="021 697 1094";	$schools["Star International H S"]["Fax"]="021 697 0536";
$schools["St Cyprian&#039s School"]["Address"]="Belmont Avenue
ORANJEZICHT
8001";	$schools["St Cyprian&#039s School"]["Phone"]="021 461 1090";	$schools["St Cyprian&#039s School"]["Fax"]="021 461 8473";
$schools["St Joseph&#039s Marist College"]["Address"]="Belmont Road
RONDEBOSCH
7700";	$schools["St Joseph&#039s Marist College"]["Phone"]="021 685 7334";	$schools["St Joseph&#039s Marist College"]["Fax"]="021 689 1205";
$schools["Steenberg High School"]["Address"]="Cnr Symphony &
Orchestra Street
STEENBERG
7945";	$schools["Steenberg High School"]["Phone"]="021 701 2281";	$schools["Steenberg High School"]["Fax"]="021 702 882";
$schools["Stellenberg H S"]["Address"]="Privaatsak X2
TYGERPARK
7536";	$schools["Stellenberg H S"]["Phone"]="021 919 3420";	$schools["Stellenberg H S"]["Fax"]="021 919 1029";
$schools["Stellenbosch H S"]["Address"]="P/Bag 5025
STELLENBSOCH
7600";	$schools["Stellenbosch H S"]["Phone"]="021 887 3082";	$schools["Stellenbosch H S"]["Fax"]="021 887 6758";
$schools["Strand H S"]["Address"]="Sarel Cilliersstraat 205
STRAND
7140";	$schools["Strand H S"]["Phone"]="021 854 6759";	$schools["Strand H S"]["Fax"]="021 853 1056";
$schools["Strandfontein Sec. S"]["Address"]="Frigate Road
STRANDFONTEIN
7798";	$schools["Strandfontein Sec. S"]["Phone"]="021 393 2100";	$schools["Strandfontein Sec. S"]["Fax"]="021 393 4165";
$schools["Swartland H S"]["Address"]="Posbus 253
MALMESBURY
7299";	$schools["Swartland H S"]["Phone"]="022 482 1469";	$schools["Swartland H S"]["Fax"]="022 482 2177";
$schools["Tygerberg H S"]["Address"]="Fairfieldweg-Noord
PAROW
7500";	$schools["Tygerberg H S"]["Phone"]="021 939 2023";	$schools["Tygerberg H S"]["Fax"]="021 930 6833";
$schools["Van Riebeeckstrand Mid."]["Address"]="Dromedarisstraat
MELKBOSSTRAND
7441";	$schools["Van Riebeeckstrand Mid."]["Phone"]="021 553 3409";	$schools["Van Riebeeckstrand Mid."]["Fax"]="021 553 4396";
$schools["Victoria-West High School"]["Address"]="P O Box 163
VICTORIA WEST
7070";	$schools["Victoria-West High School"]["Phone"]="053 621 0553";	$schools["Victoria-West High School"]["Fax"]="053 621 0553";
$schools["Voorbrug Sec School"]["Address"]="Voorbrug Road
VOORBRUG
DELFT
7100";	$schools["Voorbrug Sec School"]["Phone"]="021 954 3040";	$schools["Voorbrug Sec School"]["Fax"]="021 954 4400";
$schools["Vredenburg H S"]["Address"]="Posbus 96
VREDENBURG
7380";	$schools["Vredenburg H S"]["Phone"]="022 713 1151";	$schools["Vredenburg H S"]["Fax"]="022 713 3277";
$schools["Westerford High School"]["Address"]="Main Road
RONDEBOSCH
7700";	$schools["Westerford High School"]["Phone"]="021 689 9154";	$schools["Westerford High School"]["Fax"]="021 685 5675";
$schools["Weston H S"]["Address"]="Posbus 519
VREDENBURG
7380";	$schools["Weston H S"]["Phone"]="021 713 2083";	$schools["Weston H S"]["Fax"]="021 713 5279";
$schools["Westridge High School"]["Address"]="Silversands Avenue
WESTRIDGE
7785";	$schools["Westridge High School"]["Phone"]="021 371 7400";	$schools["Westridge High School"]["Fax"]="021 374 6395";
$schools["Wittebome High School"]["Address"]="Ottery Road
WYNBERG
7800
";	$schools["Wittebome High School"]["Phone"]="021 761 1535";	$schools["Wittebome High School"]["Fax"]="021 797 7819";
$schools["Worcester Gymnasium"]["Address"]="P O Box 210
WORCESTER
6850
";	$schools["Worcester Gymnasium"]["Phone"]="023 342 2700";	$schools["Worcester Gymnasium"]["Fax"]="023 347 1129";
$schools["Wynberg Boys&#039 H S"]["Address"]="Lovers Walk
WYNBERG
7800
";	$schools["Wynberg Boys&#039 H S"]["Phone"]="021 797 4247";	$schools["Wynberg Boys&#039 H S"]["Fax"]="021 761 0959";
$schools["Wynberg Girls&#039 H S"]["Address"]="Aliwal Road
WYNBERG
7800
";	$schools["Wynberg Girls&#039 H S"]["Phone"]="021 797 4163";	$schools["Wynberg Girls&#039 H S"]["Fax"]="021 797 2846";
$schools["Zeekoevlei High School"]["Address"]="7th Avenue
LOTUS RIVER
7941";	$schools["Zeekoevlei High School"]["Phone"]="021 793 3797";	$schools["Zeekoevlei High School"]["Fax"]="021 704 1692";
$schools["Grabouw H S"]["Address"]="Posbus 23
GRABOUW
7160";	$schools["Grabouw H S"]["Phone"]="021 859 3629";	$schools["Grabouw H S"]["Fax"]="021 859 4203/4";
$schools["Grassy Park High School"]["Address"]="Victoria Road
GRASSY PARK
7945";	$schools["Grassy Park High School"]["Phone"]="021 706 2393/69";	$schools["Grassy Park High School"]["Fax"]="021 706 3360";
$schools["Groenberg Secondary"]["Address"]="P O Box 116
GRABOUW
7160";	$schools["Groenberg Secondary"]["Phone"]="021 859 2127";	$schools["Groenberg Secondary"]["Fax"]="021 859 3806";
$schools["Groote Schuur H S"]["Address"]="Palmyra Road
NEWLANDS
7700";	$schools["Groote Schuur H S"]["Phone"]=" 021 671 9436";	$schools["Groote Schuur H S"]["Fax"]="021 674 2165";
$schools["Harold Cressy High School"]["Address"]="103 Roeland Street
CAPE TOWN
8001";	$schools["Harold Cressy High School"]["Phone"]="021 461 3810";	$schools["Harold Cressy High School"]["Fax"]="021 461 6157";
$schools["Hebrew Academy"]["Address"]="2 Foyle Road
CLAREMONT
7700";	$schools["Hebrew Academy"]["Phone"]="021";	$schools["Hebrew Academy"]["Fax"]="021";
$schools["Heideveld Sekondere Sch"]["Address"]="Waterbergweg
HEIDEVELD
7764";	$schools["Heideveld Sekondere Sch"]["Phone"]="021 637 8530";	$schools["Heideveld Sekondere Sch"]["Fax"]="";

$schools["Helderberg High School"]["Address"]="P O Box 22
SOMERSET WEST
7129";	$schools["Helderberg High School"]["Phone"]="021 855 4949";	$schools["Helderberg High School"]["Fax"]="021 855 4955";
$schools["Hermanus High School"]["Address"]="P O Box 132
HERMANUS
7200";	$schools["Hermanus High School"]["Phone"]="028 312 3760";	$schools["Hermanus High School"]["Fax"]="028 313 0814";
$schools["Herschel High School"]["Address"]="21 Herschel Road
CLAREMONT
7708";	$schools["Herschel High School"]["Phone"]="021 671 7500";	$schools["Herschel High School"]["Fax"]="921 674 2575";
$schools["Herzlia Middle School"]["Address"]="P O Box 3508
CAPE TOWN
8000";	$schools["Herzlia Middle School"]["Phone"]="021 464 3305";	$schools["Herzlia Middle School"]["Fax"]="021 461 8647";
$schools["Herzlia Senior H S"]["Address"]="P O Box 3508
CAPE TOWN
8000
";	$schools["Herzlia Senior H S"]["Phone"]="021 461 1035";	$schools["Herzlia Senior H S"]["Fax"]="021 461 8834";
$schools["Holy Cross Convent H S"]["Address"]="165 Coronation Road
MAITLAND
7405";	$schools["Holy Cross Convent H S"]["Phone"]="021 511 9365";	$schools["Holy Cross Convent H S"]["Fax"]="021 7991";
$schools["Hopefield High School"]["Address"]="P O Box 23
HOPEFIELD
7355

";	$schools["Hopefield High School"]["Phone"]="022 723 0040";	$schools["Hopefield High School"]["Fax"]="022 723 0369";
$schools["Hottentots Holland H S"]["Address"]="P O Box 358
SOMERSET WEST
7129";	$schools["Hottentots Holland H S"]["Phone"]="021 852 1405";	$schools["Hottentots Holland H S"]["Fax"]="021 851 3901";
$schools["Hugenot Hoerskool"]["Address"]="Privaatsak X9
WELLINGTON
7654";	$schools["Hugenot Hoerskool"]["Phone"]="021 873 2111";	$schools["Hugenot Hoerskool"]["Fax"]="021 873 2941";
$schools["Int. School of Cape Town"]["Address"]="Woodland Heights
Edinburgh Close
WYNBERG
7800";	$schools["Int. School of Cape Town"]["Phone"]="021 761-6202";	$schools["Int. School of Cape Town"]["Fax"]="021 761 0129";
$schools["Isaiah Christian Academy"]["Address"]="P O Box 30476
TOKAI
7966";	$schools["Isaiah Christian Academy"]["Phone"]="021 843 3923";	$schools["Isaiah Christian Academy"]["Fax"]="021 843 3013";
$schools["Islamia Boys&#039 College"]["Address"]="409 Lansdowne Road
LANSDOWNE
7780";	$schools["Islamia Boys&#039 College"]["Phone"]="021 696 5600";	$schools["Islamia Boys&#039 College"]["Fax"]="021 696 5537";
$schools["J G Meiring"]["Address"]="Merrimanweg
GOODWOOD
6450";	$schools["J G Meiring"]["Phone"]="021 592-2920";	$schools["J G Meiring"]["Fax"]="021 591 3131";
$schools["Klein Nederburg"]["Address"]="c/o Paarl School Gov. Bodies
11 Tanner Street
Paarl
7646";	$schools["Klein Nederburg"]["Phone"]="021 862 2720";	$schools["Klein Nederburg"]["Fax"]="021 862 7272";
$schools["Labori H S"]["Address"]="Privaatsak X3013
PAARL
7620";	$schools["Labori H S"]["Phone"]="021 872 7810";	$schools["Labori H S"]["Fax"]="021 872 8293";
$schools["Lavender Hill Secondary"]["Address"]="Depsiton Crescent
RETREAT
7945";	$schools["Lavender Hill Secondary"]["Phone"]="021 701 9000";	$schools["Lavender Hill Secondary"]["Fax"]="021 701 9791";
$schools["Livingstone High School"]["Address"]="100 Lansdowne Road
CLAREMONT
7700";	$schools["Livingstone High School"]["Phone"]="021 671 5986";	$schools["Livingstone High School"]["Fax"]="021 671 8552";
$schools["Luckhoff S S School"]["Address"]="Posbus 4033
IDASVALLEI
7599";	$schools["Luckhoff S S School"]["Phone"]="021 886 4766";	$schools["Luckhoff S S School"]["Fax"]="021 887 7209";
$schools["Malibu High School"]["Address"]="P O Box 451
Eerste River
7103";	$schools["Malibu High School"]["Phone"]="021 909 1105";	$schools["Malibu High School"]["Fax"]="021 909 5500";
$schools["Scottsdene H S"]["Address"]="P O Box 321
Kraaifontein
7569";	$schools["Scottsdene H S"]["Phone"]="021 988-2835";	$schools["Scottsdene H S"]["Fax"]="021 987-3501";
$schools["Mandlenkosi Sec. Sch."]["Address"]="P O Box 606
BEAUFORT WEST
6970";	$schools["Mandlenkosi Sec. Sch."]["Phone"]="023 415 2400";	$schools["Mandlenkosi Sec. Sch."]["Fax"]="023 415 2400";
$schools["Manzomthombo S S School"]["Address"]="P O Box 161
BLACKHEATH
7581";	$schools["Manzomthombo S S School"]["Phone"]="021 909 2010";	$schools["Manzomthombo S S School"]["Fax"]="021 909 2016";
$schools["Michael Oak Waldorf Sch"]["Address"]="4 Marlow Road
KENILWORTH
7708";	$schools["Michael Oak Waldorf Sch"]["Phone"]="021 797 9728";	$schools["Michael Oak Waldorf Sch"]["Fax"]="021 797 1207";
$schools["Milnerton High School"]["Address"]="Pienaar Road
MILNERTON
7441";	$schools["Milnerton High School"]["Phone"]="021 551 2217";	$schools["Milnerton High School"]["Fax"]="021 551 3248";
$schools["Mitchell&#039s Plain Islamic H"]["Address"]="37 Baobob Street
Eastridge
MITCHELL&#039S PLAIN
7785";	$schools["Mitchell&#039s Plain Islamic H"]["Phone"]="021 391 5730";	$schools["Mitchell&#039s Plain Islamic H"]["Fax"]="021 392 5529";
$schools["Mondale Senior Sec S"]["Address"]="Merrydale Avenue
Portlands
MITCHELL&#039S PLAIN
7785";	$schools["Mondale Senior Sec S"]["Phone"]="021 392 7031";	$schools["Mondale Senior Sec S"]["Fax"]="021 392 6988";
$schools["Muizenberg H S"]["Address"]="P O Box 6
MUIZENBERG
7950";	$schools["Muizenberg H S"]["Phone"]="021 788 1424";	$schools["Muizenberg H S"]["Fax"]="021 788 6635";
$schools["Bosmansdam H S"]["Address"]="Adam Tas Avenue
BOTHASIG
7441";	$schools["Bosmansdam H S"]["Phone"]="021 558 1070";	$schools["Bosmansdam H S"]["Fax"]="021 558 6380";
$schools["Brackenfell H S"]["Address"]="Privaatsak
BRACKENFELL
7560";	$schools["Brackenfell H S"]["Phone"]="021 981 5522";	$schools["Brackenfell H S"]["Fax"]="021 981 6023";
$schools["Bulumko High School"]["Address"]="P O Box 64
KHAYELITSHA
7784";	$schools["Bulumko High School"]["Phone"]="021 361 0257";	$schools["Bulumko High School"]["Fax"]="021 361 3662";
$schools["Cape Town High School"]["Address"]="P O Box 12207
MILL STREET
CAPE TOWN
8010";	$schools["Cape Town High School"]["Phone"]="021 424 2168";	$schools["Cape Town High School"]["Fax"]="021 424 4618";
$schools["Chris Hani Sec. School"]["Address"]="P O Box 35015
KHAYELITSHA
7784";	$schools["Chris Hani Sec. School"]["Phone"]="021 362 1838";	$schools["Chris Hani Sec. School"]["Fax"]="021 362 4120";
$schools["Diazville Sek Skool"]["Address"]="Posbus 1221
SALDANHA
7395";	$schools["Diazville Sek Skool"]["Phone"]="022 714 1909";	$schools["Diazville Sek Skool"]["Fax"]="022 714 1909";
$schools["Fairmont High School"]["Address"]="Private Bag X11
DURBANVILLE
7550
";	$schools["Fairmont High School"]["Phone"]="021 976 1147";	$schools["Fairmont High School"]["Fax"]="021 976 8735";
$schools["Jan Van Riebeeck H S"]["Address"]="Kloofstraat 129
KAAPSTAD
8001
";	$schools["Jan Van Riebeeck H S"]["Phone"]="021 423 6347";	$schools["Jan Van Riebeeck H S"]["Fax"]="021 424 5520";
$schools["Kasselsvlei Comprehensive"]["Address"]="P O Box 723
KASSELSVLEI
7535";	$schools["Kasselsvlei Comprehensive"]["Phone"]="021 951 3427";	$schools["Kasselsvlei Comprehensive"]["Fax"]="021 951 3910";
$schools["La Rochelle H S"]["Address"]="Posbus 21
PAARL
7622";	$schools["La Rochelle H S"]["Phone"]="021 872 4367 ";	$schools["La Rochelle H S"]["Fax"]="021 872 7812";
$schools["Norman Henshilwood H S"]["Address"]="Constantia Road
CONSTANTIA
7800";	$schools["Norman Henshilwood H S"]["Phone"]="021 797 8043";	$schools["Norman Henshilwood H S"]["Fax"]="021 797 3049";
$schools["Rylands High School"]["Address"]="P O Box 9
GATESVILLE
7764";	$schools["Rylands High School"]["Phone"]="021 637 4407";	$schools["Rylands High School"]["Fax"]="021 638 7472";
$schools["Simon&#039s Town H S"]["Address"]="Harrington Road
SEAFORTH
7995";	$schools["Simon&#039s Town H S"]["Phone"]="021 786 1056";	$schools["Simon&#039s Town H S"]["Fax"]="021 786 1065";
$schools["St George&#039s Grammar S"]["Address"]="Bloemendal Road
MOWBRAY
7700";	$schools["St George&#039s Grammar S"]["Phone"]="021 689 9354";	$schools["St George&#039s Grammar S"]["Fax"]="021 689 9361";
$schools["Phakama Sec. School"]["Address"]="P O Box 23223
CLAREMONT
7735";	$schools["Phakama Sec. School"]["Phone"]="021 372-5749";	$schools["Phakama Sec. School"]["Fax"]="021 372-0219";
$schools["CBC St John&#039s Parklands"]["Address"]="Post Net Suite #34
Private Bag X3
BLOUBERGRANT
7443";	$schools["CBC St John&#039s Parklands"]["Phone"]="021 556-5969";	$schools["CBC St John&#039s Parklands"]["Fax"]="021 556-1160";
$schools["Cannons Creek H S"]["Address"]="P O Box 38578
PINELANDS
7430";	$schools["Cannons Creek H S"]["Phone"]="021 531-0912";	$schools["Cannons Creek H S"]["Fax"]="021 531-0912";
$schools["Cravenby Sec. School"]["Address"]="P O Box 6348
PAROW EAST
7501";	$schools["Cravenby Sec. School"]["Phone"]="021 931-4470";	$schools["Cravenby Sec. School"]["Fax"]="021 933-4388";
$schools["Drostdy H T S"]["Address"]="Privaatsak X3037
WORCESTER
6849";	$schools["Drostdy H T S"]["Phone"]="023 342-2320";	$schools["Drostdy H T S"]["Fax"]="023 347-3996";
$schools["Esangweni S S S"]["Address"]="P O Box 22
LINGELETHU
7765";	$schools["Esangweni S S S"]["Phone"]="082 4321 987";	$schools["Esangweni S S S"]["Fax"]="021 361 9886";
$schools["Heritage College"]["Address"]="225 Lansdowne Road  
CLAREMONT
7700
";	$schools["Heritage College"]["Phone"]="021 683-5544";	$schools["Heritage College"]["Fax"]="021 671-8153";
$schools["John Wycliffe Christian S"]["Address"]="P O Box 92
Plumstead
7801";	$schools["John Wycliffe Christian S"]["Phone"]="797-9661";	$schools["John Wycliffe Christian S"]["Fax"]="762-3399";
$schools["Reddam House A. S. B."]["Address"]="P O Box 50608
WATERFRONT
8002";	$schools["Reddam House A. S. B."]["Phone"]="021 433-0105";	$schools["Reddam House A. S. B."]["Fax"]="021 433-0109";
$schools["Saili"]["Address"]="House Vincent
Wynberg Mews
10 Brodie Street
Wynberg
7800";	$schools["Saili"]["Phone"]="021 763-7163";	$schools["Saili"]["Fax"]="021 763-7176";
$schools["Sea Point High School"]["Address"]="P O Box 27177
RHINE ROAD
8050";	$schools["Sea Point High School"]["Phone"]="021 434-9141";	$schools["Sea Point High School"]["Fax"]="021 439-8462";
$schools["Somerset Wes Privaat"]["Address"]="P O Box 3585
SOMERSET WEST
7129";	$schools["Somerset Wes Privaat"]["Phone"]="021 852 8451";	$schools["Somerset Wes Privaat"]["Fax"]="021 851-2076";
$schools["Windsor High School"]["Address"]="Smuts Road
RONDEBOSCH EAST
7780";	$schools["Windsor High School"]["Phone"]="021 696-2974";	$schools["Windsor High School"]["Fax"]="021 697-4775";
$schools["Woodlands High School"]["Address"]="Mitchell Avenue
WOODLANDS
MITCHELLS PLAIN
7785";	$schools["Woodlands High School"]["Phone"]="021 371-0610";	$schools["Woodlands High School"]["Fax"]="021 374-1445";
$schools["Wynberg Secondary S"]["Address"]="Cheddar Road
WYNBERG
7800";	$schools["Wynberg Secondary S"]["Phone"]="021 797-00117";	$schools["Wynberg Secondary S"]["Fax"]="021 762-0615";
$schools["Spes Bona"]["Address"]="P O Box 47
ATHLONE
7764";	$schools["Spes Bona"]["Phone"]="021 697-1100";	$schools["Spes Bona"]["Fax"]="021 6969653";
$schools["American Int. C T"]["Address"]="42 Soetvlei Laan
Constantia
7806";	$schools["American Int. C T"]["Phone"]="021 713-2220";	$schools["American Int. C T"]["Fax"]="021 713-2240";
$schools["Boston House College"]["Address"]="P O Box 4506
CAPE TOWN
8000";	$schools["Boston House College"]["Phone"]="021 424-7222";	$schools["Boston House College"]["Fax"]="021 424-6657";
$schools["Cape Acad. of Maths, Sci"]["Address"]="Private Bag X3
TOKAI
7966";	$schools["Cape Acad. of Maths, Sci"]["Phone"]="021 794-5104";	$schools["Cape Acad. of Maths, Sci"]["Fax"]="021 794-0824";
$schools["Elkanah House"]["Address"]="P O Box 50479
WEST BEACH
7449";	$schools["Elkanah House"]["Phone"]="021 556-2730";	$schools["Elkanah House"]["Fax"]="021 556-2732";
$schools["Harry Gwala High School"]["Address"]="Hlehla Street
Makhaza
KHAYELITSHA
7784";	$schools["Harry Gwala High School"]["Phone"]="021  362-7500";	$schools["Harry Gwala High School"]["Fax"]="021 362-7557";
$schools["Ikamvalethu Secondary Sch"]["Address"]="Off Wash Drive 
Zone 27
LANGA
7455";	$schools["Ikamvalethu Secondary Sch"]["Phone"]="021 694-9933";	$schools["Ikamvalethu Secondary Sch"]["Fax"]="021 694-7242";
$schools["Immaculata Sec. School"]["Address"]="Clare Road
WITTEBOME
7800";	$schools["Immaculata Sec. School"]["Phone"]="021 797-8711";	$schools["Immaculata Sec. School"]["Fax"]="021 761-1930";
$schools["Langenhoven Gimnasium"]["Address"]="Privaatsak X611
OUDTSHOORN
6620";	$schools["Langenhoven Gimnasium"]["Phone"]="044 272-2151/2";	$schools["Langenhoven Gimnasium"]["Fax"]="044 272-6254";
$schools["Leap Science & Maths No.1"]["Address"]="P O Box 2229
Clareinch
7740";	$schools["Leap Science & Maths No.1"]["Phone"]="021 531-9715";	$schools["Leap Science & Maths No.1"]["Fax"]="021 532-3714";
$schools["Montana H S"]["Address"]="Posbus 1356
WORCESTER
6849";	$schools["Montana H S"]["Phone"]="023 347-0476";	$schools["Montana H S"]["Fax"]="023 347-5021";
$schools["Zwartberg H S"]["Address"]="Pastorie Street
PRINCE ALBERT
6930";	$schools["Zwartberg H S"]["Phone"]="023 541-1570";	$schools["Zwartberg H S"]["Fax"]="023 541-1739";
$schools["French School"]["Address"]="101 Hope Street
Gardens
Cape Town
8001";	$schools["French School"]["Phone"]="021 461-2508";	$schools["French School"]["Fax"]="021 461-5312";
$schools["Int. School of Hout Bay"]["Address"]="Suite 164
Private Bag X14
Hout Bay
7872";	$schools["Int. School of Hout Bay"]["Phone"]="021 790-6285";	$schools["Int. School of Hout Bay"]["Fax"]="021 790-5814";
$schools["Ladismith Sec. School"]["Address"]="P O Box 139
Ladismith
6655";	$schools["Ladismith Sec. School"]["Phone"]="028 551-1655";	$schools["Ladismith Sec. School"]["Fax"]="028 551-1402";
$schools["Lentegeur Senior S S"]["Address"]="Rooikransweg
Lentegeur
Mitchells Plain
7785";	$schools["Lentegeur Senior S S"]["Phone"]="021 371 4161";	$schools["Lentegeur Senior S S"]["Fax"]="021 371-3317";
$schools["Oakhill School"]["Address"]="Private Bag X081
Knysna
6570";	$schools["Oakhill School"]["Phone"]="044 382-6506";	$schools["Oakhill School"]["Fax"]="044 382 5753";
$schools["Porterville High School"]["Address"]="P O Box 22
Porterville
6810";	$schools["Porterville High School"]["Phone"]="022 931 2174";	$schools["Porterville High School"]["Fax"]="022 931 3321";
$schools["Worcester Sek. Skool"]["Address"]="Posbus 581
Worcester
6850
";	$schools["Worcester Sek. Skool"]["Phone"]="023 342-0857";	$schools["Worcester Sek. Skool"]["Fax"]="023 347-2894";
$schools["Wynberg High School"]["Address"]="Cheddar Road
Wynberg
7800";	$schools["Wynberg High School"]["Phone"]="021 797-0017";	$schools["Wynberg High School"]["Fax"]="021 762-0615";
$schools["Darul Arqam Islamic H"]["Address"]="P O Box 207
Mitchells Plain
7789";	$schools["Darul Arqam Islamic H"]["Phone"]="021 391-5730";	$schools["Darul Arqam Islamic H"]["Fax"]="021 392-5229";
$schools["Progress College"]["Address"]="P O Box 113
Newlands
7725";	$schools["Progress College"]["Phone"]="021 689-2952";	$schools["Progress College"]["Fax"]="021 686-3914";
$schools["Roodezant"]["Address"]="Posbus 10
Saron
6812";	$schools["Roodezant"]["Phone"]="";	$schools["Roodezant"]["Fax"]="";

$schools["Qhayiya Secondary S"]["Address"]="P O Box 493
Hermanus
7200";	$schools["Qhayiya Secondary S"]["Phone"]="028 315-0001";	$schools["Qhayiya Secondary S"]["Fax"]="028 313-2436";
$schools["Sinaka High School"]["Address"]="Khayelitsha";	$schools["Sinaka High School"]["Phone"]="021 365-0600/1";	$schools["Sinaka High School"]["Fax"]="";
$schools["Christel House SA"]["Address"]="P O Box 767
Howard Place
7450";	$schools["Christel House SA"]["Phone"]="021 697-3037";	$schools["Christel House SA"]["Fax"]="021 697 3017";
$schools["Chesterhouse"]["Address"]="P O Box 3915
Durbanville
7551";	$schools["Chesterhouse"]["Phone"]="(021)975-6650";	$schools["Chesterhouse"]["Fax"]="(021)975-6649";
$schools["Al-Azhar High School"]["Address"]="Cnr. Newton Avenue & Birdwood Road
Athlone
7764
";	$schools["Al-Azhar High School"]["Phone"]="021 696-5475";	$schools["Al-Azhar High School"]["Fax"]="021 696-5478";
$schools["Bridgetown Secondary"]["Address"]="Brushwood Road
Bridgetown
Athlone";	$schools["Bridgetown Secondary"]["Phone"]="021 637-1435";	$schools["Bridgetown Secondary"]["Fax"]="021 637-5922";
$schools["Fezeka High School"]["Address"]="C/O Bishops
Campground School
Rondebosch
7700";	$schools["Fezeka High School"]["Phone"]="021 659-1000";	$schools["Fezeka High School"]["Fax"]="";
$schools["Intlanganiso Secondary"]["Address"]="P O Box 40396
Elonwabeni
7791";	$schools["Intlanganiso Secondary"]["Phone"]="021 387-5143";	$schools["Intlanganiso Secondary"]["Fax"]="021 387-3147";
$schools["Thembelihle S. S. School"]["Address"]="P O Box 3873
Cape Town
8000";	$schools["Thembelihle S. S. School"]["Phone"]="021 364-2144/5";	$schools["Thembelihle S. S. School"]["Fax"]="021 364-2312";
$schools["New Orleans S S School"]["Address"]="Suikerboslaan
New Orleans
Paarl 
7646";	$schools["New Orleans S S School"]["Phone"]="021 862-0900";	$schools["New Orleans S S School"]["Fax"]="021 862-4978";
$schools["Paulus Joubert S S School"]["Address"]="c/o Paarl School of Gov. Bodies
11 Tanner Street
7646";	$schools["Paulus Joubert S S School"]["Phone"]="021 862-3480";	$schools["Paulus Joubert S S School"]["Fax"]="021 862-3611";
$schools["Weltevrede Sekonder"]["Address"]="c/o Paarl School of Gov. Bodies
11 Tanner Street
Paarl
7646";	$schools["Weltevrede Sekonder"]["Phone"]="021 873-1559";	$schools["Weltevrede Sekonder"]["Fax"]="021 864-2759";
$schools["Beacon Hill High"]["Address"]="P O Box 148
Beacon Valley
7785";	$schools["Beacon Hill High"]["Phone"]="021 376-1300";	$schools["Beacon Hill High"]["Fax"]="021 376-7536";
$schools["Schoonspruit Sec. S"]["Address"]="P O Box 1046
Malmesbury
7299";	$schools["Schoonspruit Sec. S"]["Phone"]="022 486-4598";	$schools["Schoonspruit Sec. S"]["Fax"]="022 486-5639";
$schools["Cape Town Studies"]["Address"]="70 Birkenhead Road
Table View
7441";	$schools["Cape Town Studies"]["Phone"]="021 556-3494";	$schools["Cape Town Studies"]["Fax"]="021 556-3494";
$schools["Oude Molen T H S"]["Address"]="Private Bag X5
Howard Place
7450";	$schools["Oude Molen T H S"]["Phone"]="021 531-2109";	$schools["Oude Molen T H S"]["Fax"]="021 531-0758";
$schools["Islamia Girls&#039 College"]["Address"]="409 Lansdown Road
Lansdowne
7780";	$schools["Islamia Girls&#039 College"]["Phone"]="021 696-5600";	$schools["Islamia Girls&#039 College"]["Fax"]="021 696-5537";
$schools["Kleinvlei H S"]["Address"]="Izialaan
Kleinvlei
7100";	$schools["Kleinvlei H S"]["Phone"]="021 904-1217";	$schools["Kleinvlei H S"]["Fax"]="021 904-9600";
$schools["Leap Science & Maths No.2"]["Address"]="P O Box 2229
Clareinch
7740";	$schools["Leap Science & Maths No.2"]["Phone"]="021 531-9762";	$schools["Leap Science & Maths No.2"]["Fax"]="021 532-3714";
$schools["Vuyiseka  Secondary"]["Address"]="Shefield Road
Phillipi East
7585";	$schools["Vuyiseka  Secondary"]["Phone"]="021 371-3008";	$schools["Vuyiseka  Secondary"]["Fax"]="021 372-7566";
$schools["Kwamfundo H S"]["Address"]="P O Box 35322
Lingelethu West
Khayeletsha
7765";	$schools["Kwamfundo H S"]["Phone"]="021 361-9347";	$schools["Kwamfundo H S"]["Fax"]="021 361-9348";
$schools["Khanyolwethu Sen.Sec.Sch."]["Address"]="P O Box 441
Strand
7140";	$schools["Khanyolwethu Sen.Sec.Sch."]["Phone"]="021 845-5290";	$schools["Khanyolwethu Sen.Sec.Sch."]["Fax"]="021 845-9446";
$schools["Melkbosstrand Private Sch"]["Address"]="P O Box 441
Melkbosstrand
7437";	$schools["Melkbosstrand Private Sch"]["Phone"]="021 553-1530";	$schools["Melkbosstrand Private Sch"]["Fax"]="021 553-0610";
$schools["Imizamo Yethu Sec. School"]["Address"]="P O Box 2092
George
6530";	$schools["Imizamo Yethu Sec. School"]["Phone"]="044 880 1122";	$schools["Imizamo Yethu Sec. School"]["Fax"]="044 880 2280";
$schools["Strand Secondary School"]["Address"]="P O Box 612
Strand
7140";	$schools["Strand Secondary School"]["Phone"]="021 853-2413";	$schools["Strand Secondary School"]["Fax"]="021 854-4045";
$schools["Sophumelela"]["Address"]="c/o Oliver Tambo & Vanguard Drives
Somora Machel
7785";	$schools["Sophumelela"]["Phone"]="021 372-1953";	$schools["Sophumelela"]["Fax"]="021 372-1953";
$schools["Grassdale High School"]["Address"]="4th Avenue
Grassy Park
7941";	$schools["Grassdale High School"]["Phone"]="021 706-1816";	$schools["Grassdale High School"]["Fax"]="021 706-0871";
$schools["Hout Bay High School"]["Address"]="Marlin Crescent
Hout Bay
7872";	$schools["Hout Bay High School"]["Phone"]="021 790-4917";	$schools["Hout Bay High School"]["Fax"]="021 790-5918";
$schools["Rusthof Secondary School"]["Address"]="Broadlandspark
Strand
7140";	$schools["Rusthof Secondary School"]["Phone"]="021 845-7081";	$schools["Rusthof Secondary School"]["Fax"]="021 845-8015";
$schools["Vista High School"]["Address"]="Military Road
Off Upper Whitford Street
Bo-Kaap, Cape Town
8001
";	$schools["Vista High School"]["Phone"]="021 424-7430";	$schools["Vista High School"]["Fax"]="021 423-1705";
$schools["Cloetesville H S"]["Address"]="P O Box 2327
Dennisig
7601";	$schools["Cloetesville H S"]["Phone"]="021 889-5424";	$schools["Cloetesville H S"]["Fax"]="021 889-6303";
$schools["Florida H S"]["Address"]="Stroebelstraat
Ravensmead
7493";	$schools["Florida H S"]["Phone"]="021 931-8922";	$schools["Florida H S"]["Fax"]="021 931 9152";
$schools["Mondeor Eco School"]["Address"]="P O Box 1015
Strand
7139";	$schools["Mondeor Eco School"]["Phone"]="021 858-1309";	$schools["Mondeor Eco School"]["Fax"]="021 858-1883";
$schools["Spine Road H School"]["Address"]="Cnr. Spine & Merrydale Roads
Rocklands
Mitchells Plain
7785";	$schools["Spine Road H School"]["Phone"]="021 392-9463";	$schools["Spine Road H School"]["Fax"]="021 391-4965";
$schools["Trafalgar H School"]["Address"]="P O Box 556
Cape Town
8000";	$schools["Trafalgar H School"]["Phone"]="021 465-2969";	$schools["Trafalgar H School"]["Fax"]="021 461-3680";
$schools["Gardens Commercial H S"]["Address"]="Paddock Avenue
Gardens
Cape Town
8000";	$schools["Gardens Commercial H S"]["Phone"]="021 465-1236";	$schools["Gardens Commercial H S"]["Fax"]="021 465-1448";
$schools["Oracle Academy"]["Address"]="P O Box 24287
Lansdowne
7779";	$schools["Oracle Academy"]["Phone"]="021 704-4915";	$schools["Oracle Academy"]["Fax"]="021 704-4916";

*/
?>