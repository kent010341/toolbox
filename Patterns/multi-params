#!/bin/bash

default_a="default_a"
default_b="default_b"

while (($#)); do
    case $1 in
        "--param_a")
            shift
            default_a=$1
            shift
        ;;
        "--param_b")
            shift
            default_b=$1
            shift
        ;;
        "--help")
            echo "Usage"
            exit 1
        ;;
        *)
            echo "unknown argument '$1'"
            echo "Use --help to get the usage information."
            exit 1
        ;;
    esac
done

echo "param_a = $default_a"
echo "param_b = $default_b"
