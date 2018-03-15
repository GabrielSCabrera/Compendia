# File writing is efficiently done by 'here documents'

cat > myfile <<EOF
multi-line text
can now be inserted here,
and variable substitution such as
$myvariable is
supported.
EOF # the final EOF must start in column 1 of the script file (EOF = End Of File)
