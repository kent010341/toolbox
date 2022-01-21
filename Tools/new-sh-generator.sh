#!/bin/bash

filename="new-sh"

while (($#)); do
    case $1 in
        "--filename" | "-f")
            shift
            filename=$1
            shift
        ;;
        "--help" | "-h")
            echo "Usage: ./new-sh-generator.sh [options...]"
            echo "    --filename <file name>, -f <file name>"    
            echo "        name of this new script"
            exit 0
        ;;
        *)
            echo "unknown argument '$1'"
            echo "Use --help (or -h) to get the usage information."
            exit 1
        ;;
    esac
done

if [ "$(echo $filename | grep -E ".sh$")" != "" ]; then
    filename=$(echo $filename | cut -d"." -f 1)
fi

while [ -f ""$filename".sh" ]; do
    echo -e "\033[1;91m[WARNING] file '$filename' has already exist, renaming the new file to "$filename"_1 \033[0m"
    filename="$filename"_1
done

cat > ""$filename".sh" <<EOF
#!/bin/bash

# default
param_1=default_param_1

while ((\$#)); do
    case \$1 in
        "--param_1" | "-p")
            shift
            param_1=\$1
            shift
        ;;
        "--help" | "-h")
            echo "Usage: ./$filename.sh [options...]"
            echo "    --param_1 <value>, -p <value>"
            echo "        description"
            exit 0
        ;;
        *)
            echo "unknown argument '$1'"
            echo "Use --help (or -h) to get the usage information."
            exit 1
        ;;
    esac
done

EOF

chmod +x ""$filename".sh"

echo -e "\033[1;93m[SUCCESS] Creating file succeed. \033[0m"
