#!/bin/bash
# Tiitulo: Limpieza de whitespace 
#
# Entrada: 
#   1 - El directorio principal de trabajo
#   2 - El archivo de terminación .txt que se va a modificar
#   3 - El nombre de la carpeta donde se guardará el output
#


WORKDIR=$1
FILE=$2
OUTPUTDIR=$3

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
    echo $FILE
    echo "File provided does not exist."
    exit 1
fi

if [ -d "$OUTPUTDIR" ]; then
    echo "Output dir exists"
else
    mkdir -p "$OUTPUTDIR" # The output directory is the only onw we create if non-existent
fi

name=$(basename "${2}" .txt)


# Read from step1_raw.txt and output cleaned version
awk '{ gsub(/^[ \t]+|[ \t]+$/, "", $0); print tolower($0) }' "${FILE}" > ${OUTPUTDIR}/${name}_cleaned.txt


echo "Created ${name}_cleaned.txt in $OUTPUTDIR"
