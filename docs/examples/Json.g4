/**
 * JSON (JavaScript Object Notation) is a lightweight data-interchange format.
 */
grammar Json;

/**
 * On top level, JSON consists of a single value. That value can be either
 * a complex structure (such as an `object` or an `array`) or a primitive
 * type (a `STRING` in double quotes, a `NUMBER`,
 * or ``true`` or ``false`` or ``null``).
 */
value
    : object
    | array
    | STRING
    | NUMBER
    | TRUE
    | FALSE
    | NULL
    ;

/**
 * Object is a collection of name/value pairs. In various languages,
 * this is realized as an object, record, struct, dictionary,
 * hash table, keyed list, or associative array.
 */
object
    : '(' (STRING ':' value (',' STRING ':' value)*)? ')'
    ;

/**
 * Array is an ordered list of values. In most languages, this is realized as
 * vector, list, array or sequence.
 */
array
    : '[' (value (',' value)*)? ']'
    ;

/**
 * A number is very much like a C or Java number,
 * except that the octal and hexadecimal formats are not used.
 */
//@ doc:name number
NUMBER
    : '-'? ('0' | [1-9] [0-9]*) ('.' [0-9]+)? EXPONENT?
    ;

//@ doc:inline
//@ doc:importance 0
fragment EXPONENT
    : ('e' | 'E')? ('+' | '-')? [0-9]+
    ;

/**
 * A string is a sequence of zero or more Unicode characters,
 * wrapped in double quotes, using backslash escapes.
 * A character is represented as a single character string.
 * A string is very much like a C or Java string.
 *
 * .. railroad-diagram::
 *
 *    - terminal: '"'
 *    - zero_or_more:
 *      - choice:
 *        - terminal: 'Any unicode character except " and \'
 *        - sequence:
 *          - terminal: '\'
 *          - choice:
 *              - [terminal: '"', comment: quotation mark]
 *              - [terminal: '\', comment: reverse solidus]
 *              - [terminal: '/', comment: solidus]
 *              - [terminal: 'b', comment: backspace]
 *              - [terminal: 'f', comment: formfeed]
 *              - [terminal: 'n', comment: newline]
 *              - [terminal: 'r', comment: carriage return]
 *              - [terminal: 't', comment: horizontal tab]
 *              - [terminal: 'u', terminal: 4 hexdecimal digits]
 *    - terminal: '"'
 */
//@ doc:name string
//@ doc:no-diagram
STRING
   : '"' (ESC | SAFECODEPOINT)* '"'
   ;

//@ doc:nodoc
fragment ESC
   : '\\' (["\\/bfnrt] | UNICODE)
   ;

//@ doc:nodoc
fragment UNICODE
   : 'u' HEX HEX HEX HEX
   ;

//@ doc:nodoc
fragment HEX
   : [0-9a-fA-F]
   ;

//@ doc: nodoc
fragment SAFECODEPOINT
   : ~ ["\\\u0000-\u001F]
   ;

//@ doc:nodoc
//@ doc:name true
TRUE
    : 'true'
    ;

//@ doc:nodoc
//@ doc:name false
FALSE
    : 'false'
    ;

//@ doc:nodoc
//@ doc:name null
NULL
    : 'null'
    ;
