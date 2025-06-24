#!/bin/bash
# Título: Tokenización de las palabras 
#
# Entrada: 
#   1 - El directorio principal de trabajo
#   2 - El archivo de terminación .txt que se va a modificar
#   3 - El nombre de la carpeta donde se guardará el output

WORKDIR=$1
FILE=$WORKDIR/$2
OUTPUTDIR=$WORKDIR/$3

# Checks existence of provided directories 
if [ -d "$WORKDIR" ]; then
    echo "Directory exists."
else
    echo "Work Directory provided does not exist: $WORKDIR"
    exit 1
fi

if [ -f "$FILE" ]; then
    echo "File provided exists."
else
    echo "File provided does not exist."
    exit 1
fi

if [ -d "$OUTPUTDIR" ]; then
    echo "Output dir exists"
else
    mkdir -p "$OUTPUTDIR" # The output directory is the only onw we create if non-existent
fi

name=$(basename "${2}" .txt)


# Tokenize each line into individual words (non-alphanumeric as delimiter)
tr -s '[:space:][:punct:]' '\n' <  "${FILE}" | grep -v '^$' > ${OUTPUTDIR}/${name}_tokenized.txt

echo "Created ${name}_tokenized.txt in $OUTPUTDIR"
