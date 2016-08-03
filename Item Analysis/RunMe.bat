@echo off
echo Conversion from Item Analysis to TEX format

echo See the file Readme.txt for more details.

python ItemAnalysis.py INDGR8.ITM PRSGR8.ITM > ALLGR8.TEX
python ItemAnalysis.py INDGR9.ITM PRSGR9.ITM > ALLGR9.TEX
python ItemAnalysis.py INDGR10.ITM PRSGR10.ITM > ALLGR10.TEX
python ItemAnalysis.py INDGR11.ITM PRSGR11.ITM > ALLGR11.TEX
python ItemAnalysis.py INDGR12.ITM PRSGR12.ITM > ALLGR12.TEX

pause