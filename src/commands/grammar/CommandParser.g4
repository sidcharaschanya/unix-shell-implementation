parser grammar CommandParser;
options {tokenVocab = CommandLexer;}

cmdline: command? EOF;

command: pipe #nonSeq | left=command SEQ right=command #seq | call #nonSeq;

pipe: left=call PIPE right=call #singlePipe | left=pipe PIPE right=call #nestedPipe;

call: WS? (redirections+=redirection WS)* app=argument (WS atoms+=atom)* WS?;

atom: redirection | argument;

argument: contents+=argumentContent+;

argumentContent: quoted #quotedArg | UNQUOTED #unquoted ;

redirection: LT WS? argument #inRedirection | GT WS? argument #outRedirection;

quoted: singleQuoted | doubleQuoted | backQuoted;

singleQuoted: SQ SQ_CONTENT SQ;

backQuoted: BQ BQ_CONTENT BQ;

doubleQuoted: DQ contents+=doubleQuotedContent* DQ;

doubleQuotedContent: backQuoted #bqInDq | DQ_CONTENT #dqContent;
