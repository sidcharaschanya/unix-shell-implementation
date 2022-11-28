parser grammar CommandParser;
options {tokenVocab = CommandLexer;}

cmdline: command EOF;

command: pipe #pipeCommand | left=command SEQ right=command #seq | call #callCommand;

pipe: left=call PIPE right=call #singlePipe | left=pipe PIPE right=call #nestedPipe;

call: WS? (redirections+=redirection WS)* argument (WS atoms+=atom)* WS?;

atom: redirection | argument;

argument: elements+=argumentElement+;

argumentElement: quoted #quotedArgElem | UNQUOTED #unquoted ;

redirection: op=LT WS? argument | op=GT WS? argument;

quoted: singleQuoted | doubleQuoted | backQuoted;

singleQuoted: SQ_START SQ_CONTENT SQ_END;

backQuoted: BQ_START BQ_CONTENT BQ_END;

doubleQuoted: DQ_START elements+=doubleQuotedElement* DQ_END;

doubleQuotedElement: backQuoted #bqDqElem | DQ_CONTENT #dqContent;
