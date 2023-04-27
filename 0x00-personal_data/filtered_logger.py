#!/usr/bin/env python3
"""
Filtering logs
"""
import re

def filter_datum(fields, redaction, message, separator):
    """
    This function takes in four parameters: 
    fields, a list of strings representing all fields to be obfuscated;
    redaction, a string representing the character by which the field will be obfuscated;
    message, a string representing the log line; and
    separator, a string representing the character by which fields are separated in the log line.
    
    The function then uses a regular expression (regex) to find occurrences of the fields that need to be obfuscated. 
    It uses a positive lookbehind to make sure that it is only replacing fields that come after the separator character. 
    It then replaces these occurrences of the field value with the redaction character using re.sub().
    
    The function returns the obfuscated log message as a string.
    """
    return re.sub(fr'(?<={separator})([^{separator}]*(?:{separator}[^{separator}]*){{{fields.index(":")}}})', f'{redaction}\g<1>{redaction}', message)
