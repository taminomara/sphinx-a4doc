grammar test;


test
     (A B | A B C) (',' (A B | A B C))*
    ;


module
    : moduleItem* EOF
    ;

moduleItem
    : item=moduleAnnotation # moduleItemAnnotation
    | item=importStatement # moduleItemImport
    | item=documentation # moduleItemDocumentation
    | (annotations+=statementAnnotation)* item=annotatedModuleItem # moduleItemEntity
    ;

//@ doc:inline
//@ doc:importance 2
annotatedModuleItem
    : value=structDefinition # annotatedModuleItemStruct
    | value=enumDefinition # annotatedModuleItemEnum
    ;

// Annotations

moduleAnnotation
    : '#![' annotationContent ']'
    ;

//@ doc:importance 0
statementAnnotation
    : '#[' annotationContent ']'
    ;

annotationContent
    : (items+=annotationContentItem (',' items+=annotationContentItem)* ','?)?
    ;

//@ doc:inline
annotationContentItem
    : name=ID                                 # annotationContentItemFlag
    | name=ID '=' value=ID                    # annotationContentItemId
    | name=ID '=' value=literal               # annotationContentItemLiteral
    | name=ID '(' value=annotationContent ')' # annotationContentItemNested
    ;


// Imports

importStatement
    : 'import' path+=ID ('.' path+=ID)* ('as' alias=ID)? ';'
    ;


// Structs

structDefinition
    : 'struct' name=ID ('[' typevars+=ID (',' typevars+=ID)* ']')? '{' body+=structItem* '}'
    ;

structItem
    : documentation # structItemDocumentation
    | value=INTEGER_LITERAL ':' # structItemVersionSpec
    | annotations+=statementAnnotation* name=ID ':' type=typeRef ';' # structItemField
    ;


// Enums

enumDefinition
    : 'enum' name=ID '{' body+=enumItem* '}'
    ;

enumItem
    : documentation # enumItemDocumentation
    | value=INTEGER_LITERAL ':' # enumItemVersionSpec
    | annotations+=statementAnnotation* name=ID ';' # enumItemElement
    ;


// Vars

typeRef
    : path+=ID ('.' path+=ID)* typevars=typeRefGenerics? postfix+='?'*
    ;

typeRefGenerics
    : '[' (typevars+=typeRef | version=INTEGER_LITERAL) (',' typevars+=typeRef)* ']'
    ;


// Literals

literal
    : value=BOOLEAN_LITERAL # literalBoolean
    | value=INTEGER_LITERAL # literalInteger
    | value=FLOAT_LITERAL   # literalFloat
    | value=STRING_LITERAL  # literalString
    ;


// Docs

documentation
    : DOC_COMMENT
    ;



IMPORT
    : 'import'
    ;

FROM
    : 'from'
    ;

AS
    : 'as'
    ;

EXPORT
    : 'export'
    ;

DEF
    : 'def'
    ;

LET
    : 'let'
    ;

STRUCT
    : 'struct'
    ;

ENUM
    : 'enum'
    ;

TYPE
    : 'type'
    ;

EVENT
    : 'event'
    ;

LOG
    : 'log'
    ;

EXTENDS
    : 'extends'
    ;

BASED
    : 'based'
    ;

ON
    : 'on'
    ;

PRIVATE
    : 'private'
    ;

PUBLIC
    : 'public'
    ;

PROTECTED
    : 'proteted'
    ;

IF
    : 'if'
    ;

ELSE
    : 'else'
    ;

FOR
    : 'for'
    ;

MAP
    : 'map'
    ;

FILTER
    : 'filter'
    ;

SUBGRAPH
    : 'subgraph'
    ;

AND
    : 'and'
    ;

OR
    : 'or'
    ;

NOT
    : 'not'
    ;

L_PAREN
    : '('
    ;

L_BRACK
    : '['
    ;

L_BRACE
    : '{'
    ;

R_PAREN
    : ')'
    ;

R_BRACK
    : ']'
    ;

R_BRACE
    : '}'
    ;

S_EXPR_START
    : '`'
    ;

BOOLEAN_LITERAL
    : 'true'
    | 'false'
    ;

INTEGER_LITERAL
    : [0-9]+
    | '0' [bB] [01]+
    | '0' [oO] [0-7]+
    | '0' [xX] [0-9a-fA-F]+
    ;

FLOAT_LITERAL
    : [0-9]+ EXPONENT
    | [0-9]+ '.' EXPONENT?
    | [0-9]* '.' [0-9]+ EXPONENT?
    ;

fragment EXPONENT
    : (('e' | 'E') ('+' | '-')? [0-9]+)?
    ;

STRING_LITERAL
    : '"' (~[\\\r\n"] | '\\' .)* '"'
    | '\'' (~[\\\r\n'] | '\\' .)* '\''
    ;

ID
    : [a-zA-Z_] [a-zA-Z0-9_]*
    ;

EQUAL
    : '='
    ;

COMMA
    : ','
    ;

DOT
    : '.'
    ;

COLON
    : ':'
    ;

SEMICOLON
    : ';'
    ;

DOUBLE_COLON
    : '::'
    ;

HASH
    : '#'
    ;

ANNOTATION_START
    : '#['
    ;

MODULE_ANNOTATION_START
    : '#!['
    ;

QUESTION
    : '?'
    ;

EXCLAMATION
    : '!'
    ;

TILDE
    : '~'
    ;

AT
    : '@'
    ;

PLUS
    : '+'
    ;

MINUS
    : '-'
    ;

STAR
    : '*'
    ;

SLASH
    : '/'
    ;

PERCENT
    : '%'
    ;

AMPERSAND
    : '&'
    ;

PIPE
    : '|'
    ;

CARET
    : '^'
    ;

DOUBLE_AMPERSAND
    : '&&'
    ;

DOUBLE_PIPE
    : '||'
    ;

DOUBLE_EQUAL
    : '=='
    ;

EXCLAMATION_EQUAL
    : '!='
    ;

GREATER
    : '>'
    ;

LESSER
    : '<'
    ;

GREATER_EQUAL
    : '>='
    ;

LESSER_EQUAL
    : '<='
    ;

GREATER_GREATER
    : '>>'
    ;

LESSER_LESSER
    : '<<'
    ;

L_ARROW
    : '<-'
    ;

R_ARROW
    : '->'
    ;

R_FAT_ARROW
    : '=>'
    ;

BIND
    : '>>='
    ;

BACKSLASH
    : '\\'
    ;

DOC_COMMENT
    : '/*' ('*' | '!') .*? ('*/' | EOF)
    ;

BLOCK_COMMENT
    : '/*' .*? ('*/' | EOF)
    ;

LINE_COMMENT
    : '//' ~[\r\n]*
    ;

WHITESPACE
    : [ \t\r\n] -> skip
    ;
