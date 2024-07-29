'''
2. Parse request response
Rebuild accepted languages headers in your coding language of choice.

Stage 1: Create a function that requests languages in string format and return an array of the supported languages

Stage 2: Support non-region specific requests. ie "en" returns ["en-US", "en-CA", "en-GB"]

Stage 3: Support wildcard matching to return the rest of the supported languages

3.

4. Part 1 In an HTTP request, the Accept-Language header describes the list of languages that the requester would like content to be returned in.
The header takes the form of a comma-separated list of language tags.
For example: Accept-Language: en-US, fr-CA, fr-FR means that the reader would accept:
1. English as spoken in the United States (most preferred)
2. French as spoken in Canada
3. French as spoken in France (least preferred)

We're writing a server that needs to return content in an acceptable language for the requester, and we want to make use of this header.
Our server doesn't support every possible language that might be requested (yet!), but there is a set of languages that we do support.
Write a function that receives two arguments: an Accept-Language header value as a string and a set of supported languages,
and returns the list of language tags that will work for the request.
The language tags should be returned in descending order of preference (the same order as they appeared in the header).
In addition to writing this function, you should use tests to demonstrate that it's correct, either via an existing testing system or one you create.
Examples: parse_accept_language( "en-US, fr-CA, fr-FR", # the client's Accept-Language header, a string ["fr-FR", "en-US"] # the server's supported languages,
a set of strings ) returns: ["en-US", "fr-FR"]

parse_accept_language("fr-CA, fr-FR", ["en-US", "fr-FR"]) returns: ["fr-FR"]
parse_accept_language("en-US", ["en-US", "fr-CA"]) returns: ["en-US"]


Phone interview: How do you build an "accept-language" parser with region/language/wildcard filtering
'''

def parse_accept_language_complete(header_value, supported_languages):
    #TODO 1. Add support for non matching cases
    # 2. can do just .split(' ,') instead
    requested_languages = header_value.replace(" ", '').split(",")
    supported_languages = set(supported_languages)

    result = []

    for elem in requested_languages:
        if elem in supported_languages:
            result.append(elem)

    return result

def parse_accept_language_region(header_value, supported_languages):
    return [x for x in supported_languages if x.startswith(header_value)]


def parse_wildcard_starting(header_value):
    i = 0
    result = ''
    while i < len(header_value):
        if header_value[i] == '*':
            break
        result += header_value[i]
        i += 1
    return result
def parse_accept_header(header_value, supported_language):
    #TODO: Add support for checking invalid values in header_value
    if '*' in header_value:
        wildcard_starting = parse_wildcard_starting(header_value)
        if wildcard_starting:
            return parse_accept_language_region(wildcard_starting, supported_language)
        else:
            return supported_language
    else:
        return parse_accept_language_complete(header_value, supported_language)


if __name__ == '__main__':
    assert (parse_accept_header("en-US, fr-CA, fr-FR", ["fr-FR", "en-US"])) == ["en-US", "fr-FR"]
    assert (parse_accept_header("fr-CA, fr-FR", ["en-US", "fr-FR"])) == ["fr-FR"]
    assert (parse_accept_header("en-US", ["en-US", "fr-CA"])) == ["en-US"]

    assert (parse_accept_header("en-*", ["en-US", "en-CA", "en-GB", "fr-FR"])) == ["en-US", "en-CA", "en-GB"]
    assert (parse_accept_header("*", ["en-US", "en-CA", "en-GB", "fr-FR"])) == ["en-US", "en-CA", "en-GB", "fr-FR"]
    assert (parse_accept_header("*", ["en-US", "en-CA", "en-GB", "fr-FR"])) == ["en-US", "en-CA", "en-GB", "fr-FR"]







