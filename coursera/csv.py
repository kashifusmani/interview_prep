"""
Problem Description: In a standard CSV file, each line is a string containing one or more string fields, separated by commas.
Each field may be optionally surrounded on both sides by single quotes(').
In some cases, however, a field may internally contain a comman (,); in these cases, the quotes are mandatory in order
to clarify that the internal comma should not be considered a field separator.

Given a string reresentating a line from a CSV file, write a function that parses the string and returns a list whose
first entry in the string START, whose last entry is the string END and who other entries correspond to each of the separate fields from the string in order.

if input = "a,b", OUTPUT = ['START', 'a', 'b', 'END']
if input = "'a',b,'c,d'", OUTPUT = ['START', 'a', 'b','c,d','END']
"""
def parse(x):
    result = ['START']
    i = 0
    elem = ''
    quote_start = False
    comma_start = False
    while (i<len(x)):
        if x[i] == "'" and not quote_start:
            quote_start = True
            while quote_start:
                i += 1
                if x[i] != "'":
                    elem += x[i]
                else:
                    quote_start = False
                    result.append(elem)
                    elem = ''
                    break


        elif x[i] == ",":

            #if not comma_start:
            #    comma_start = True
            #    elem += x[i]
            #else:
            #    result.append(elem)
            #    elem = ''
            result.append(elem)
            elem = ''
        elif x[i] != ",":
            elem = x[i]
            #result.append(x[i])
        #elif x[i] == "," and elem != '':
        #    result.append(elem)
        #    elem = ''
        i += 1

    if elem != '':
        result.append(elem)
    result.append('END')
    return result

def parse_2(x):
    splitted = x.split(',')

    result = ['START']
    i = 0
    interim = ''

    while i <len(splitted):
        elem = splitted[i]
        if "'" not in elem and interim =='':
            result.append(elem)
        elif "'" not in elem and not interim =='':
            interim = interim + elem + ","
        elif elem.startswith("'") and interim == '':
            interim = elem[1:] + ','
        elif elem.endswith("'") and not interim == '':
            interim = interim + elem[:len(elem)-1]
            result.append(interim)
        i += 1
    result.append('END')
    return result


def parse_3(x):
    result = ['START']
    i = 0
    elem = ''
    quote_start = False
    prev_comma = True
    while (i<len(x)):
        if x[i] == "'" and not quote_start:
            quote_start = True
            while quote_start:
                i += 1
                if x[i] != "'":
                    elem += x[i]
                else:
                    quote_start = False
                    result.append(elem)
                    elem = ''
                    break
        elif x[i] == "," and prev_comma:
            result.append(elem)
            prev_comma = False
            elem = ''
        elif x[i] != ",":
            elem = x[i]
            prev_comma = True
        i += 1

    if elem != '':
        result.append(elem)
    result.append('END')
    return result

def parse_4(x):
    result = ['START']
    i = 0
    elem = ''
    quote_start = False
    prev_comma = True
    while (i<len(x)):
        if x[i] == "'" and not quote_start:
            quote_start = True
            while quote_start:
                i += 1
                if x[i] != "'":
                    elem += x[i]
                else:
                    quote_start = False
                    result.append(elem)
                    elem = ''
                    break
        elif x[i] == "," and prev_comma:
            result.append(elem)
            prev_comma = False
            elem = ''
        elif x[i] != ",":
            elem += x[i]
            prev_comma = True
        i += 1

    if elem != '':
        result.append(elem)
    result.append('END')
    return result

if __name__ == '__main__':
    """
    print(parse_3('a,b'))
    print(parse_3("a,b,'c,d'"))
    print(parse_3(",a"))
    print(parse_3("a,b,'c,d','e'"))
    print(parse_3("a,b,'c','e'"))
    print(parse_3("a,b,'c,d','e','g,h'"))
    """
    print(parse_4(',rocks'))
    print(parse_4("'a',b,'c,d'"))