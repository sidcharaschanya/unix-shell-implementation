// Generated from C:/Users/aadis/python-shell-p22/src/commands/grammar\CommandLexer.g4 by ANTLR 4.10.1
package commands.grammar;
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class CommandLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.10.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		BQ_START=1, SEQ=2, PIPE=3, WS=4, UNQUOTED=5, LT=6, GT=7, SQ_START=8, DQ_START=9, 
		SQ_CONTENT=10, SQ_END=11, BQ_CONTENT=12, BQ_END=13, DQ_CONTENT=14, DQ_END=15;
	public static final int
		SINGLE_QUOTED=1, BACK_QUOTED=2, DOUBLE_QUOTED=3;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE", "SINGLE_QUOTED", "BACK_QUOTED", "DOUBLE_QUOTED"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"SQ_CHAR", "BQ_CHAR", "DQ_CHAR", "SEQ", "PIPE", "WS", "UNQUOTED", "LT", 
			"GT", "SQ_START", "BQ", "DQ_START", "SQ_CONTENT", "SQ_END", "BQ_CONTENT", 
			"BQ_END", "DQ_CONTENT", "DQ_END", "BQ_IN_DQ"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, "';'", "'|'", null, null, "'<'", "'>'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "BQ_START", "SEQ", "PIPE", "WS", "UNQUOTED", "LT", "GT", "SQ_START", 
			"DQ_START", "SQ_CONTENT", "SQ_END", "BQ_CONTENT", "BQ_END", "DQ_CONTENT", 
			"DQ_END"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public CommandLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "CommandLexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u000fo\u0006\uffff\uffff\u0006\uffff\uffff\u0006\uffff\uffff"+
		"\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002"+
		"\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0004\u0005"+
		"6\b\u0005\u000b\u0005\f\u00057\u0001\u0006\u0004\u0006;\b\u0006\u000b"+
		"\u0006\f\u0006<\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f\u0004\fQ\b\f\u000b\f\f\f"+
		"R\u0001\r\u0001\r\u0001\r\u0001\r\u0001\u000e\u0004\u000eZ\b\u000e\u000b"+
		"\u000e\f\u000e[\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u0010\u0004\u0010c\b\u0010\u000b\u0010\f\u0010d\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0000\u0000\u0013\u0004\u0000\u0006\u0000\b\u0000\n\u0002"+
		"\f\u0003\u000e\u0004\u0010\u0005\u0012\u0006\u0014\u0007\u0016\b\u0018"+
		"\u0000\u001a\t\u001c\n\u001e\u000b \f\"\r$\u000e&\u000f(\u0000\u0004\u0000"+
		"\u0001\u0002\u0003\u0005\u0002\u0000\t\t  \b\u0000\t\n  \"\"\'\';<>>`"+
		"`||\u0002\u0000\n\n\'\'\u0002\u0000\n\n``\u0003\u0000\n\n\"\"``m\u0000"+
		"\n\u0001\u0000\u0000\u0000\u0000\f\u0001\u0000\u0000\u0000\u0000\u000e"+
		"\u0001\u0000\u0000\u0000\u0000\u0010\u0001\u0000\u0000\u0000\u0000\u0012"+
		"\u0001\u0000\u0000\u0000\u0000\u0014\u0001\u0000\u0000\u0000\u0000\u0016"+
		"\u0001\u0000\u0000\u0000\u0000\u0018\u0001\u0000\u0000\u0000\u0000\u001a"+
		"\u0001\u0000\u0000\u0000\u0001\u001c\u0001\u0000\u0000\u0000\u0001\u001e"+
		"\u0001\u0000\u0000\u0000\u0002 \u0001\u0000\u0000\u0000\u0002\"\u0001"+
		"\u0000\u0000\u0000\u0003$\u0001\u0000\u0000\u0000\u0003&\u0001\u0000\u0000"+
		"\u0000\u0003(\u0001\u0000\u0000\u0000\u0004*\u0001\u0000\u0000\u0000\u0006"+
		",\u0001\u0000\u0000\u0000\b.\u0001\u0000\u0000\u0000\n0\u0001\u0000\u0000"+
		"\u0000\f2\u0001\u0000\u0000\u0000\u000e5\u0001\u0000\u0000\u0000\u0010"+
		":\u0001\u0000\u0000\u0000\u0012>\u0001\u0000\u0000\u0000\u0014@\u0001"+
		"\u0000\u0000\u0000\u0016B\u0001\u0000\u0000\u0000\u0018F\u0001\u0000\u0000"+
		"\u0000\u001aK\u0001\u0000\u0000\u0000\u001cP\u0001\u0000\u0000\u0000\u001e"+
		"T\u0001\u0000\u0000\u0000 Y\u0001\u0000\u0000\u0000\"]\u0001\u0000\u0000"+
		"\u0000$b\u0001\u0000\u0000\u0000&f\u0001\u0000\u0000\u0000(j\u0001\u0000"+
		"\u0000\u0000*+\u0005\'\u0000\u0000+\u0005\u0001\u0000\u0000\u0000,-\u0005"+
		"`\u0000\u0000-\u0007\u0001\u0000\u0000\u0000./\u0005\"\u0000\u0000/\t"+
		"\u0001\u0000\u0000\u000001\u0005;\u0000\u00001\u000b\u0001\u0000\u0000"+
		"\u000023\u0005|\u0000\u00003\r\u0001\u0000\u0000\u000046\u0007\u0000\u0000"+
		"\u000054\u0001\u0000\u0000\u000067\u0001\u0000\u0000\u000075\u0001\u0000"+
		"\u0000\u000078\u0001\u0000\u0000\u00008\u000f\u0001\u0000\u0000\u0000"+
		"9;\b\u0001\u0000\u0000:9\u0001\u0000\u0000\u0000;<\u0001\u0000\u0000\u0000"+
		"<:\u0001\u0000\u0000\u0000<=\u0001\u0000\u0000\u0000=\u0011\u0001\u0000"+
		"\u0000\u0000>?\u0005<\u0000\u0000?\u0013\u0001\u0000\u0000\u0000@A\u0005"+
		">\u0000\u0000A\u0015\u0001\u0000\u0000\u0000BC\u0003\u0004\u0000\u0000"+
		"CD\u0001\u0000\u0000\u0000DE\u0006\t\u0000\u0000E\u0017\u0001\u0000\u0000"+
		"\u0000FG\u0003\u0006\u0001\u0000GH\u0001\u0000\u0000\u0000HI\u0006\n\u0001"+
		"\u0000IJ\u0006\n\u0002\u0000J\u0019\u0001\u0000\u0000\u0000KL\u0003\b"+
		"\u0002\u0000LM\u0001\u0000\u0000\u0000MN\u0006\u000b\u0003\u0000N\u001b"+
		"\u0001\u0000\u0000\u0000OQ\b\u0002\u0000\u0000PO\u0001\u0000\u0000\u0000"+
		"QR\u0001\u0000\u0000\u0000RP\u0001\u0000\u0000\u0000RS\u0001\u0000\u0000"+
		"\u0000S\u001d\u0001\u0000\u0000\u0000TU\u0003\u0004\u0000\u0000UV\u0001"+
		"\u0000\u0000\u0000VW\u0006\r\u0004\u0000W\u001f\u0001\u0000\u0000\u0000"+
		"XZ\b\u0003\u0000\u0000YX\u0001\u0000\u0000\u0000Z[\u0001\u0000\u0000\u0000"+
		"[Y\u0001\u0000\u0000\u0000[\\\u0001\u0000\u0000\u0000\\!\u0001\u0000\u0000"+
		"\u0000]^\u0003\u0006\u0001\u0000^_\u0001\u0000\u0000\u0000_`\u0006\u000f"+
		"\u0004\u0000`#\u0001\u0000\u0000\u0000ac\b\u0004\u0000\u0000ba\u0001\u0000"+
		"\u0000\u0000cd\u0001\u0000\u0000\u0000db\u0001\u0000\u0000\u0000de\u0001"+
		"\u0000\u0000\u0000e%\u0001\u0000\u0000\u0000fg\u0003\b\u0002\u0000gh\u0001"+
		"\u0000\u0000\u0000hi\u0006\u0011\u0004\u0000i\'\u0001\u0000\u0000\u0000"+
		"jk\u0003\u0006\u0001\u0000kl\u0001\u0000\u0000\u0000lm\u0006\u0012\u0001"+
		"\u0000mn\u0006\u0012\u0002\u0000n)\u0001\u0000\u0000\u0000\t\u0000\u0001"+
		"\u0002\u00037<R[d\u0005\u0005\u0001\u0000\u0007\u0001\u0000\u0005\u0002"+
		"\u0000\u0005\u0003\u0000\u0004\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}