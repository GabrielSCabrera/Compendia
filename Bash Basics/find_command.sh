#Very useful command! "find" visits all files in a directory tree and can
#execute one or more commands for every file

#Basic example: find the "oscillator" codes:

find $scripting/src -name "oscillator*" -print

#Or find all PostScript files:

find $HOME \( -name '*.ps' -o -name '*.eps' \) -print

#We can also run a command for each file:

find rootdir -name filenamespec -exec command {} \;
  -print
# {} is the current filename, command should be replaced with a command
