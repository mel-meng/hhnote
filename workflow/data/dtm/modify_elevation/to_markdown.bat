set filename=readme
REM export the images to the media folder
pandoc -s "%filename%.docx" -t gfm -o "%filename%.md" --extract-media="." --self-contained --wrap=none 
REM export the markdown file using relative path for images
REM pandoc -s "%filename%.docx" -t gfm -o "%filename%.md" --wrap=none 



set filename=Exercise 1 Compare 2D grid with DEM
REM export the images to the media folder
pandoc -s "%filename%.docx" -t gfm -o "%filename%.md" --extract-media="./ex1" --self-contained --wrap=none 
REM export the markdown file using relative path for images
REM pandoc -s "%filename%.docx" -t gfm -o "%filename%.md" --wrap=none 


set filename=Exercise 2 Create Breakline
REM export the images to the media folder
REM pandoc -s "%filename%.docx" -t gfm -o "%filename%.md" --extract-media="./ex2" --self-contained --wrap=none 
REM export the markdown file using relative path for images
REM pandoc -s "%filename%.docx" -t gfm -o "%filename%.md" --wrap=none 