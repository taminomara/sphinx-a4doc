# Generated from /Users/amatanhead/Documents/sphinx-a4doc/sphinx_a4doc/syntax/ANTLRv4Lexer.g4 by ANTLR 4.7
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


from sphinx_a4doc.syntax.lexer_adaptor import LexerAdaptor


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u"?\u03ed\b\1\b\1\b\1\b\1\b\1\b\1\b\1\4\2\t\2\4\3\t\3\4")
        buf.write(u"\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t")
        buf.write(u"\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20")
        buf.write(u"\t\20\4\21\t\21\4\22\t\22\4\23\t\23\4\24\t\24\4\25\t")
        buf.write(u"\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31\4\32\t\32")
        buf.write(u"\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4")
        buf.write(u" \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4")
        buf.write(u"(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4/\t/\4\60\t")
        buf.write(u"\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64\4\65\t\65")
        buf.write(u"\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4")
        buf.write(u"=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE")
        buf.write(u"\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\tM\4N\t")
        buf.write(u"N\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\tU\4V\tV\4W")
        buf.write(u"\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4^\t^\4_\t")
        buf.write(u"_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4g\tg\4h")
        buf.write(u"\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\4n\tn\4o\to\4p\tp\4")
        buf.write(u"q\tq\4r\tr\4s\ts\4t\tt\4u\tu\4v\tv\4w\tw\4x\tx\4y\ty")
        buf.write(u"\4z\tz\4{\t{\4|\t|\4}\t}\4~\t~\4\177\t\177\4\u0080\t")
        buf.write(u"\u0080\4\u0081\t\u0081\4\u0082\t\u0082\4\u0083\t\u0083")
        buf.write(u"\4\u0084\t\u0084\4\u0085\t\u0085\4\u0086\t\u0086\4\u0087")
        buf.write(u"\t\u0087\4\u0088\t\u0088\4\u0089\t\u0089\4\u008a\t\u008a")
        buf.write(u"\4\u008b\t\u008b\4\u008c\t\u008c\4\u008d\t\u008d\4\u008e")
        buf.write(u"\t\u008e\4\u008f\t\u008f\4\u0090\t\u0090\4\u0091\t\u0091")
        buf.write(u"\4\u0092\t\u0092\4\u0093\t\u0093\4\u0094\t\u0094\4\u0095")
        buf.write(u"\t\u0095\4\u0096\t\u0096\4\u0097\t\u0097\4\u0098\t\u0098")
        buf.write(u"\4\u0099\t\u0099\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write(u"\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write(u"\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\7\n\u015b")
        buf.write(u"\n\n\f\n\16\n\u015e\13\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write(u"\13\3\13\3\13\3\13\3\13\3\13\3\13\7\13\u016d\n\13\f\13")
        buf.write(u"\16\13\u0170\13\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write(u"\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u0181\n\f\f\f\16\f")
        buf.write(u"\u0184\13\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write(u"\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17")
        buf.write(u"\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3")
        buf.write(u"\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write(u"\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3")
        buf.write(u"\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write(u"\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3")
        buf.write(u"\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write(u"\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3")
        buf.write(u"\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write(u"\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3")
        buf.write(u"\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&")
        buf.write(u"\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3")
        buf.write(u"/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\6\63\u0222\n")
        buf.write(u"\63\r\63\16\63\u0223\3\63\3\63\3\64\3\64\3\64\3\64\3")
        buf.write(u"\65\3\65\5\65\u022e\n\65\3\66\3\66\3\67\3\67\38\38\3")
        buf.write(u"8\38\78\u0238\n8\f8\168\u023b\138\38\38\38\58\u0240\n")
        buf.write(u"8\39\39\39\39\39\79\u0247\n9\f9\169\u024a\139\39\39\3")
        buf.write(u"9\59\u024f\n9\39\39\39\39\39\79\u0256\n9\f9\169\u0259")
        buf.write(u"\139\59\u025b\n9\3:\3:\3:\3:\7:\u0261\n:\f:\16:\u0264")
        buf.write(u"\13:\3;\3;\3;\3;\3;\5;\u026b\n;\3<\3<\3<\3=\3=\3=\3=")
        buf.write(u"\3=\5=\u0275\n=\5=\u0277\n=\5=\u0279\n=\5=\u027b\n=\3")
        buf.write(u">\3>\3>\7>\u0280\n>\f>\16>\u0283\13>\5>\u0285\n>\3?\3")
        buf.write(u"?\3@\3@\3A\3A\3A\3A\3A\3A\3A\3A\3A\5A\u0294\nA\3B\3B")
        buf.write(u"\3B\5B\u0299\nB\3B\3B\3C\3C\3C\7C\u02a0\nC\fC\16C\u02a3")
        buf.write(u"\13C\3C\3C\3D\3D\3D\7D\u02aa\nD\fD\16D\u02ad\13D\3D\3")
        buf.write(u"D\3E\3E\3E\7E\u02b4\nE\fE\16E\u02b7\13E\3F\3F\3F\3F\5")
        buf.write(u"F\u02bd\nF\3G\3G\3H\3H\3H\3H\3I\3I\3J\3J\3K\3K\3K\3L")
        buf.write(u"\3L\3M\3M\3N\3N\3O\3O\3P\3P\3Q\3Q\3R\3R\3S\3S\3T\3T\3")
        buf.write(u"T\3U\3U\3V\3V\3W\3W\3X\3X\3Y\3Y\3Z\3Z\3[\3[\3[\3\\\3")
        buf.write(u"\\\3]\3]\3^\3^\3_\3_\3`\3`\3a\3a\3b\3b\3b\3c\3c\3d\3")
        buf.write(u"d\3e\3e\3f\3f\3f\3f\3f\3g\3g\3g\3g\3h\3h\3h\3h\3i\3i")
        buf.write(u"\3i\3i\3j\3j\3j\3k\3k\3k\3k\3l\3l\3m\3m\3m\3m\3m\3n\3")
        buf.write(u"n\3n\3n\3o\3o\3o\3o\3p\3p\3p\3p\3q\3q\3q\3q\3r\3r\3r")
        buf.write(u"\3r\3s\3s\3s\3s\3t\3t\3t\3u\3u\3u\3u\3v\3v\3w\3w\3w\3")
        buf.write(u"w\3w\3x\3x\3x\3x\3x\3y\3y\3y\3y\3y\3z\3z\3z\3z\3{\3{")
        buf.write(u"\3{\3{\3{\3|\3|\3|\3|\3}\3}\3}\3}\3~\3~\3~\3~\3\177\3")
        buf.write(u"\177\3\177\3\177\3\u0080\3\u0080\3\u0080\3\u0080\3\u0081")
        buf.write(u"\3\u0081\3\u0081\3\u0081\3\u0082\3\u0082\3\u0082\3\u0082")
        buf.write(u"\3\u0083\6\u0083\u0378\n\u0083\r\u0083\16\u0083\u0379")
        buf.write(u"\3\u0083\3\u0083\3\u0083\3\u0084\3\u0084\3\u0084\3\u0084")
        buf.write(u"\3\u0084\3\u0085\3\u0085\3\u0085\3\u0085\3\u0085\3\u0086")
        buf.write(u"\3\u0086\3\u0086\3\u0086\3\u0086\3\u0087\3\u0087\3\u0087")
        buf.write(u"\3\u0087\3\u0088\3\u0088\3\u0088\3\u0088\3\u0088\3\u0089")
        buf.write(u"\3\u0089\3\u0089\3\u0089\3\u008a\3\u008a\3\u008a\3\u008a")
        buf.write(u"\3\u008b\3\u008b\3\u008b\3\u008b\3\u008c\6\u008c\u03a4")
        buf.write(u"\n\u008c\r\u008c\16\u008c\u03a5\3\u008c\3\u008c\3\u008c")
        buf.write(u"\3\u008d\3\u008d\3\u008d\3\u008d\3\u008d\3\u008e\3\u008e")
        buf.write(u"\3\u008e\3\u008e\3\u008e\3\u008f\3\u008f\3\u008f\3\u008f")
        buf.write(u"\3\u008f\3\u0090\3\u0090\3\u0090\3\u0090\3\u0091\3\u0091")
        buf.write(u"\3\u0091\3\u0091\3\u0091\3\u0092\3\u0092\3\u0092\3\u0092")
        buf.write(u"\3\u0093\3\u0093\3\u0093\3\u0093\3\u0094\3\u0094\3\u0094")
        buf.write(u"\3\u0094\3\u0095\6\u0095\u03d0\n\u0095\r\u0095\16\u0095")
        buf.write(u"\u03d1\3\u0095\3\u0095\3\u0095\3\u0096\3\u0096\6\u0096")
        buf.write(u"\u03d9\n\u0096\r\u0096\16\u0096\u03da\3\u0096\3\u0096")
        buf.write(u"\3\u0097\3\u0097\3\u0097\3\u0097\3\u0098\3\u0098\3\u0098")
        buf.write(u"\3\u0098\3\u0099\3\u0099\7\u0099\u03e9\n\u0099\f\u0099")
        buf.write(u"\16\u0099\u03ec\13\u0099\4\u0239\u0248\2\u009a\t\6\13")
        buf.write(u"\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write(u"\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write(u"\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write(u"_\61a\62c\63e\64g\65i\66k\67m8o\2q\2s\2u\2w\2y\2{\2}")
        buf.write(u"\2\177\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089\2\u008b")
        buf.write(u"\2\u008d\2\u008f\2\u0091\2\u0093\2\u0095\2\u0097\2\u0099")
        buf.write(u"\2\u009b\2\u009d\2\u009f\2\u00a1\2\u00a3\2\u00a5\2\u00a7")
        buf.write(u"\2\u00a9\2\u00ab\2\u00ad\2\u00af\2\u00b1\2\u00b3\2\u00b5")
        buf.write(u"\2\u00b7\2\u00b9\2\u00bb\2\u00bd\2\u00bf\2\u00c1\2\u00c3")
        buf.write(u"\2\u00c5\2\u00c7\2\u00c9\2\u00cb\2\u00cd\2\u00cf\2\u00d1")
        buf.write(u"\2\u00d3\2\u00d5\2\u00d7\2\u00d99\u00db:\u00dd;\u00df")
        buf.write(u"\2\u00e1\2\u00e3\2\u00e5\2\u00e7\2\u00e9\2\u00eb\2\u00ed")
        buf.write(u"<\u00ef=\u00f1>\u00f3\2\u00f5\2\u00f7\2\u00f9\2\u00fb")
        buf.write(u"\2\u00fd\2\u00ff\2\u0101\2\u0103\2\u0105\2\u0107\2\u0109")
        buf.write(u"\2\u010b\2\u010d\2\u010f\2\u0111\2\u0113\2\u0115\2\u0117")
        buf.write(u"\2\u0119\2\u011b\2\u011d\2\u011f\2\u0121\2\u0123\2\u0125")
        buf.write(u"\2\u0127\2\u0129\2\u012b\2\u012d\2\u012f\2\u0131\2\u0133")
        buf.write(u"\5\u0135?\u0137\2\t\2\3\4\5\6\7\b\17\5\2\13\f\16\17\"")
        buf.write(u"\"\4\2\13\13\"\"\4\2\f\f\16\17\4\2\f\f\17\17\n\2$$))")
        buf.write(u"^^ddhhppttvv\3\2\63;\5\2\62;CHch\3\2\62;\6\2\f\f\17\17")
        buf.write(u"))^^\6\2\f\f\17\17$$^^\5\2\u00b9\u00b9\u0302\u0371\u2041")
        buf.write(u"\u2042\17\2C\\c|\u00c2\u00d8\u00da\u00f8\u00fa\u0301")
        buf.write(u"\u0372\u037f\u0381\u2001\u200e\u200f\u2072\u2191\u2c02")
        buf.write(u"\u2ff1\u3003\ud801\uf902\ufdd1\ufdf2\uffff\3\2^_\2\u03da")
        buf.write(u"\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write(u"\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write(u"\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write(u"!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write(u"\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write(u"\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2")
        buf.write(u"\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3")
        buf.write(u"\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write(u"O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write(u"\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2")
        buf.write(u"\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2")
        buf.write(u"\2\2\2m\3\2\2\2\3\u00d1\3\2\2\2\3\u00d3\3\2\2\2\3\u00d5")
        buf.write(u"\3\2\2\2\3\u00d7\3\2\2\2\3\u00d9\3\2\2\2\3\u00db\3\2")
        buf.write(u"\2\2\3\u00dd\3\2\2\2\4\u00df\3\2\2\2\4\u00e1\3\2\2\2")
        buf.write(u"\4\u00e3\3\2\2\2\4\u00e5\3\2\2\2\4\u00e7\3\2\2\2\4\u00e9")
        buf.write(u"\3\2\2\2\4\u00eb\3\2\2\2\4\u00ed\3\2\2\2\4\u00ef\3\2")
        buf.write(u"\2\2\4\u00f1\3\2\2\2\5\u00f3\3\2\2\2\5\u00f5\3\2\2\2")
        buf.write(u"\5\u00f7\3\2\2\2\5\u00f9\3\2\2\2\5\u00fb\3\2\2\2\5\u00fd")
        buf.write(u"\3\2\2\2\5\u00ff\3\2\2\2\5\u0101\3\2\2\2\5\u0103\3\2")
        buf.write(u"\2\2\5\u0105\3\2\2\2\5\u0107\3\2\2\2\5\u0109\3\2\2\2")
        buf.write(u"\5\u010b\3\2\2\2\6\u010d\3\2\2\2\6\u010f\3\2\2\2\6\u0111")
        buf.write(u"\3\2\2\2\6\u0113\3\2\2\2\6\u0115\3\2\2\2\6\u0117\3\2")
        buf.write(u"\2\2\6\u0119\3\2\2\2\6\u011b\3\2\2\2\6\u011d\3\2\2\2")
        buf.write(u"\7\u011f\3\2\2\2\7\u0121\3\2\2\2\7\u0123\3\2\2\2\7\u0125")
        buf.write(u"\3\2\2\2\7\u0127\3\2\2\2\7\u0129\3\2\2\2\7\u012b\3\2")
        buf.write(u"\2\2\7\u012d\3\2\2\2\7\u012f\3\2\2\2\b\u0131\3\2\2\2")
        buf.write(u"\b\u0133\3\2\2\2\b\u0135\3\2\2\2\t\u0139\3\2\2\2\13\u013b")
        buf.write(u"\3\2\2\2\r\u013f\3\2\2\2\17\u0143\3\2\2\2\21\u0145\3")
        buf.write(u"\2\2\2\23\u0147\3\2\2\2\25\u0149\3\2\2\2\27\u014c\3\2")
        buf.write(u"\2\2\31\u0150\3\2\2\2\33\u0163\3\2\2\2\35\u0175\3\2\2")
        buf.write(u"\2\37\u0189\3\2\2\2!\u0190\3\2\2\2#\u0199\3\2\2\2%\u019f")
        buf.write(u"\3\2\2\2\'\u01a6\3\2\2\2)\u01ae\3\2\2\2+\u01b8\3\2\2")
        buf.write(u"\2-\u01bf\3\2\2\2/\u01c7\3\2\2\2\61\u01cf\3\2\2\2\63")
        buf.write(u"\u01d6\3\2\2\2\65\u01dd\3\2\2\2\67\u01e3\3\2\2\29\u01eb")
        buf.write(u"\3\2\2\2;\u01f0\3\2\2\2=\u01f2\3\2\2\2?\u01f4\3\2\2\2")
        buf.write(u"A\u01f6\3\2\2\2C\u01f8\3\2\2\2E\u01fa\3\2\2\2G\u01fc")
        buf.write(u"\3\2\2\2I\u01fe\3\2\2\2K\u0200\3\2\2\2M\u0202\3\2\2\2")
        buf.write(u"O\u0204\3\2\2\2Q\u0206\3\2\2\2S\u0208\3\2\2\2U\u020a")
        buf.write(u"\3\2\2\2W\u020c\3\2\2\2Y\u020e\3\2\2\2[\u0210\3\2\2\2")
        buf.write(u"]\u0212\3\2\2\2_\u0214\3\2\2\2a\u0216\3\2\2\2c\u0218")
        buf.write(u"\3\2\2\2e\u021a\3\2\2\2g\u021c\3\2\2\2i\u021e\3\2\2\2")
        buf.write(u"k\u0221\3\2\2\2m\u0227\3\2\2\2o\u022d\3\2\2\2q\u022f")
        buf.write(u"\3\2\2\2s\u0231\3\2\2\2u\u0233\3\2\2\2w\u025a\3\2\2\2")
        buf.write(u"y\u025c\3\2\2\2{\u0265\3\2\2\2}\u026c\3\2\2\2\177\u026f")
        buf.write(u"\3\2\2\2\u0081\u0284\3\2\2\2\u0083\u0286\3\2\2\2\u0085")
        buf.write(u"\u0288\3\2\2\2\u0087\u0293\3\2\2\2\u0089\u0295\3\2\2")
        buf.write(u"\2\u008b\u029c\3\2\2\2\u008d\u02a6\3\2\2\2\u008f\u02b0")
        buf.write(u"\3\2\2\2\u0091\u02bc\3\2\2\2\u0093\u02be\3\2\2\2\u0095")
        buf.write(u"\u02c0\3\2\2\2\u0097\u02c4\3\2\2\2\u0099\u02c6\3\2\2")
        buf.write(u"\2\u009b\u02c8\3\2\2\2\u009d\u02cb\3\2\2\2\u009f\u02cd")
        buf.write(u"\3\2\2\2\u00a1\u02cf\3\2\2\2\u00a3\u02d1\3\2\2\2\u00a5")
        buf.write(u"\u02d3\3\2\2\2\u00a7\u02d5\3\2\2\2\u00a9\u02d7\3\2\2")
        buf.write(u"\2\u00ab\u02d9\3\2\2\2\u00ad\u02db\3\2\2\2\u00af\u02de")
        buf.write(u"\3\2\2\2\u00b1\u02e0\3\2\2\2\u00b3\u02e2\3\2\2\2\u00b5")
        buf.write(u"\u02e4\3\2\2\2\u00b7\u02e6\3\2\2\2\u00b9\u02e8\3\2\2")
        buf.write(u"\2\u00bb\u02ea\3\2\2\2\u00bd\u02ed\3\2\2\2\u00bf\u02ef")
        buf.write(u"\3\2\2\2\u00c1\u02f1\3\2\2\2\u00c3\u02f3\3\2\2\2\u00c5")
        buf.write(u"\u02f5\3\2\2\2\u00c7\u02f7\3\2\2\2\u00c9\u02f9\3\2\2")
        buf.write(u"\2\u00cb\u02fc\3\2\2\2\u00cd\u02fe\3\2\2\2\u00cf\u0300")
        buf.write(u"\3\2\2\2\u00d1\u0302\3\2\2\2\u00d3\u0307\3\2\2\2\u00d5")
        buf.write(u"\u030b\3\2\2\2\u00d7\u030f\3\2\2\2\u00d9\u0313\3\2\2")
        buf.write(u"\2\u00db\u0316\3\2\2\2\u00dd\u031a\3\2\2\2\u00df\u031c")
        buf.write(u"\3\2\2\2\u00e1\u0321\3\2\2\2\u00e3\u0325\3\2\2\2\u00e5")
        buf.write(u"\u0329\3\2\2\2\u00e7\u032d\3\2\2\2\u00e9\u0331\3\2\2")
        buf.write(u"\2\u00eb\u0335\3\2\2\2\u00ed\u0339\3\2\2\2\u00ef\u033c")
        buf.write(u"\3\2\2\2\u00f1\u0340\3\2\2\2\u00f3\u0342\3\2\2\2\u00f5")
        buf.write(u"\u0347\3\2\2\2\u00f7\u034c\3\2\2\2\u00f9\u0351\3\2\2")
        buf.write(u"\2\u00fb\u0355\3\2\2\2\u00fd\u035a\3\2\2\2\u00ff\u035e")
        buf.write(u"\3\2\2\2\u0101\u0362\3\2\2\2\u0103\u0366\3\2\2\2\u0105")
        buf.write(u"\u036a\3\2\2\2\u0107\u036e\3\2\2\2\u0109\u0372\3\2\2")
        buf.write(u"\2\u010b\u0377\3\2\2\2\u010d\u037e\3\2\2\2\u010f\u0383")
        buf.write(u"\3\2\2\2\u0111\u0388\3\2\2\2\u0113\u038d\3\2\2\2\u0115")
        buf.write(u"\u0391\3\2\2\2\u0117\u0396\3\2\2\2\u0119\u039a\3\2\2")
        buf.write(u"\2\u011b\u039e\3\2\2\2\u011d\u03a3\3\2\2\2\u011f\u03aa")
        buf.write(u"\3\2\2\2\u0121\u03af\3\2\2\2\u0123\u03b4\3\2\2\2\u0125")
        buf.write(u"\u03b9\3\2\2\2\u0127\u03bd\3\2\2\2\u0129\u03c2\3\2\2")
        buf.write(u"\2\u012b\u03c6\3\2\2\2\u012d\u03ca\3\2\2\2\u012f\u03cf")
        buf.write(u"\3\2\2\2\u0131\u03d8\3\2\2\2\u0133\u03de\3\2\2\2\u0135")
        buf.write(u"\u03e2\3\2\2\2\u0137\u03e6\3\2\2\2\u0139\u013a\5w9\2")
        buf.write(u"\u013a\n\3\2\2\2\u013b\u013c\5u8\2\u013c\u013d\3\2\2")
        buf.write(u"\2\u013d\u013e\b\3\2\2\u013e\f\3\2\2\2\u013f\u0140\5")
        buf.write(u"y:\2\u0140\u0141\3\2\2\2\u0141\u0142\b\4\2\2\u0142\16")
        buf.write(u"\3\2\2\2\u0143\u0144\5\u0081>\2\u0144\20\3\2\2\2\u0145")
        buf.write(u"\u0146\5\u008bC\2\u0146\22\3\2\2\2\u0147\u0148\5\u008f")
        buf.write(u"E\2\u0148\24\3\2\2\2\u0149\u014a\5\u00a9R\2\u014a\u014b")
        buf.write(u"\b\b\3\2\u014b\26\3\2\2\2\u014c\u014d\5\u00a5P\2\u014d")
        buf.write(u"\u014e\3\2\2\2\u014e\u014f\b\t\4\2\u014f\30\3\2\2\2\u0150")
        buf.write(u"\u0151\6\n\2\2\u0151\u0152\7q\2\2\u0152\u0153\7r\2\2")
        buf.write(u"\u0153\u0154\7v\2\2\u0154\u0155\7k\2\2\u0155\u0156\7")
        buf.write(u"q\2\2\u0156\u0157\7p\2\2\u0157\u0158\7u\2\2\u0158\u015c")
        buf.write(u"\3\2\2\2\u0159\u015b\t\2\2\2\u015a\u0159\3\2\2\2\u015b")
        buf.write(u"\u015e\3\2\2\2\u015c\u015a\3\2\2\2\u015c\u015d\3\2\2")
        buf.write(u"\2\u015d\u015f\3\2\2\2\u015e\u015c\3\2\2\2\u015f\u0160")
        buf.write(u"\7}\2\2\u0160\u0161\3\2\2\2\u0161\u0162\b\n\5\2\u0162")
        buf.write(u"\32\3\2\2\2\u0163\u0164\6\13\3\2\u0164\u0165\7v\2\2\u0165")
        buf.write(u"\u0166\7q\2\2\u0166\u0167\7m\2\2\u0167\u0168\7g\2\2\u0168")
        buf.write(u"\u0169\7p\2\2\u0169\u016a\7u\2\2\u016a\u016e\3\2\2\2")
        buf.write(u"\u016b\u016d\t\2\2\2\u016c\u016b\3\2\2\2\u016d\u0170")
        buf.write(u"\3\2\2\2\u016e\u016c\3\2\2\2\u016e\u016f\3\2\2\2\u016f")
        buf.write(u"\u0171\3\2\2\2\u0170\u016e\3\2\2\2\u0171\u0172\7}\2\2")
        buf.write(u"\u0172\u0173\3\2\2\2\u0173\u0174\b\13\6\2\u0174\34\3")
        buf.write(u"\2\2\2\u0175\u0176\6\f\4\2\u0176\u0177\7e\2\2\u0177\u0178")
        buf.write(u"\7j\2\2\u0178\u0179\7c\2\2\u0179\u017a\7p\2\2\u017a\u017b")
        buf.write(u"\7p\2\2\u017b\u017c\7g\2\2\u017c\u017d\7n\2\2\u017d\u017e")
        buf.write(u"\7u\2\2\u017e\u0182\3\2\2\2\u017f\u0181\t\2\2\2\u0180")
        buf.write(u"\u017f\3\2\2\2\u0181\u0184\3\2\2\2\u0182\u0180\3\2\2")
        buf.write(u"\2\u0182\u0183\3\2\2\2\u0183\u0185\3\2\2\2\u0184\u0182")
        buf.write(u"\3\2\2\2\u0185\u0186\7}\2\2\u0186\u0187\3\2\2\2\u0187")
        buf.write(u"\u0188\b\f\7\2\u0188\36\3\2\2\2\u0189\u018a\7k\2\2\u018a")
        buf.write(u"\u018b\7o\2\2\u018b\u018c\7r\2\2\u018c\u018d\7q\2\2\u018d")
        buf.write(u"\u018e\7t\2\2\u018e\u018f\7v\2\2\u018f \3\2\2\2\u0190")
        buf.write(u"\u0191\7h\2\2\u0191\u0192\7t\2\2\u0192\u0193\7c\2\2\u0193")
        buf.write(u"\u0194\7i\2\2\u0194\u0195\7o\2\2\u0195\u0196\7g\2\2\u0196")
        buf.write(u"\u0197\7p\2\2\u0197\u0198\7v\2\2\u0198\"\3\2\2\2\u0199")
        buf.write(u"\u019a\7n\2\2\u019a\u019b\7g\2\2\u019b\u019c\7z\2\2\u019c")
        buf.write(u"\u019d\7g\2\2\u019d\u019e\7t\2\2\u019e$\3\2\2\2\u019f")
        buf.write(u"\u01a0\7r\2\2\u01a0\u01a1\7c\2\2\u01a1\u01a2\7t\2\2\u01a2")
        buf.write(u"\u01a3\7u\2\2\u01a3\u01a4\7g\2\2\u01a4\u01a5\7t\2\2\u01a5")
        buf.write(u"&\3\2\2\2\u01a6\u01a7\7i\2\2\u01a7\u01a8\7t\2\2\u01a8")
        buf.write(u"\u01a9\7c\2\2\u01a9\u01aa\7o\2\2\u01aa\u01ab\7o\2\2\u01ab")
        buf.write(u"\u01ac\7c\2\2\u01ac\u01ad\7t\2\2\u01ad(\3\2\2\2\u01ae")
        buf.write(u"\u01af\7r\2\2\u01af\u01b0\7t\2\2\u01b0\u01b1\7q\2\2\u01b1")
        buf.write(u"\u01b2\7v\2\2\u01b2\u01b3\7g\2\2\u01b3\u01b4\7e\2\2\u01b4")
        buf.write(u"\u01b5\7v\2\2\u01b5\u01b6\7g\2\2\u01b6\u01b7\7f\2\2\u01b7")
        buf.write(u"*\3\2\2\2\u01b8\u01b9\7r\2\2\u01b9\u01ba\7w\2\2\u01ba")
        buf.write(u"\u01bb\7d\2\2\u01bb\u01bc\7n\2\2\u01bc\u01bd\7k\2\2\u01bd")
        buf.write(u"\u01be\7e\2\2\u01be,\3\2\2\2\u01bf\u01c0\7r\2\2\u01c0")
        buf.write(u"\u01c1\7t\2\2\u01c1\u01c2\7k\2\2\u01c2\u01c3\7x\2\2\u01c3")
        buf.write(u"\u01c4\7c\2\2\u01c4\u01c5\7v\2\2\u01c5\u01c6\7g\2\2\u01c6")
        buf.write(u".\3\2\2\2\u01c7\u01c8\7t\2\2\u01c8\u01c9\7g\2\2\u01c9")
        buf.write(u"\u01ca\7v\2\2\u01ca\u01cb\7w\2\2\u01cb\u01cc\7t\2\2\u01cc")
        buf.write(u"\u01cd\7p\2\2\u01cd\u01ce\7u\2\2\u01ce\60\3\2\2\2\u01cf")
        buf.write(u"\u01d0\7n\2\2\u01d0\u01d1\7q\2\2\u01d1\u01d2\7e\2\2\u01d2")
        buf.write(u"\u01d3\7c\2\2\u01d3\u01d4\7n\2\2\u01d4\u01d5\7u\2\2\u01d5")
        buf.write(u"\62\3\2\2\2\u01d6\u01d7\7v\2\2\u01d7\u01d8\7j\2\2\u01d8")
        buf.write(u"\u01d9\7t\2\2\u01d9\u01da\7q\2\2\u01da\u01db\7y\2\2\u01db")
        buf.write(u"\u01dc\7u\2\2\u01dc\64\3\2\2\2\u01dd\u01de\7e\2\2\u01de")
        buf.write(u"\u01df\7c\2\2\u01df\u01e0\7v\2\2\u01e0\u01e1\7e\2\2\u01e1")
        buf.write(u"\u01e2\7j\2\2\u01e2\66\3\2\2\2\u01e3\u01e4\7h\2\2\u01e4")
        buf.write(u"\u01e5\7k\2\2\u01e5\u01e6\7p\2\2\u01e6\u01e7\7c\2\2\u01e7")
        buf.write(u"\u01e8\7n\2\2\u01e8\u01e9\7n\2\2\u01e9\u01ea\7{\2\2\u01ea")
        buf.write(u"8\3\2\2\2\u01eb\u01ec\7o\2\2\u01ec\u01ed\7q\2\2\u01ed")
        buf.write(u"\u01ee\7f\2\2\u01ee\u01ef\7g\2\2\u01ef:\3\2\2\2\u01f0")
        buf.write(u"\u01f1\5\u0099J\2\u01f1<\3\2\2\2\u01f2\u01f3\5\u009b")
        buf.write(u"K\2\u01f3>\3\2\2\2\u01f4\u01f5\5\u00c3_\2\u01f5@\3\2")
        buf.write(u"\2\2\u01f6\u01f7\5\u00c5`\2\u01f7B\3\2\2\2\u01f8\u01f9")
        buf.write(u"\5\u00a1N\2\u01f9D\3\2\2\2\u01fa\u01fb\5\u00a3O\2\u01fb")
        buf.write(u"F\3\2\2\2\u01fc\u01fd\5\u00a5P\2\u01fdH\3\2\2\2\u01fe")
        buf.write(u"\u01ff\5\u00a7Q\2\u01ffJ\3\2\2\2\u0200\u0201\5\u00ad")
        buf.write(u"T\2\u0201L\3\2\2\2\u0202\u0203\5\u00afU\2\u0203N\3\2")
        buf.write(u"\2\2\u0204\u0205\5\u00b1V\2\u0205P\3\2\2\2\u0206\u0207")
        buf.write(u"\5\u00b3W\2\u0207R\3\2\2\2\u0208\u0209\5\u00b5X\2\u0209")
        buf.write(u"T\3\2\2\2\u020a\u020b\5\u00b7Y\2\u020bV\3\2\2\2\u020c")
        buf.write(u"\u020d\5\u00bb[\2\u020dX\3\2\2\2\u020e\u020f\5\u00b9")
        buf.write(u"Z\2\u020fZ\3\2\2\2\u0210\u0211\5\u00bf]\2\u0211\\\3\2")
        buf.write(u"\2\2\u0212\u0213\5\u00c1^\2\u0213^\3\2\2\2\u0214\u0215")
        buf.write(u"\5\u00c9b\2\u0215`\3\2\2\2\u0216\u0217\5\u00c7a\2\u0217")
        buf.write(u"b\3\2\2\2\u0218\u0219\5\u00cbc\2\u0219d\3\2\2\2\u021a")
        buf.write(u"\u021b\5\u00cdd\2\u021bf\3\2\2\2\u021c\u021d\5\u00cf")
        buf.write(u"e\2\u021dh\3\2\2\2\u021e\u021f\5\u0137\u0099\2\u021f")
        buf.write(u"j\3\2\2\2\u0220\u0222\5o\65\2\u0221\u0220\3\2\2\2\u0222")
        buf.write(u"\u0223\3\2\2\2\u0223\u0221\3\2\2\2\u0223\u0224\3\2\2")
        buf.write(u"\2\u0224\u0225\3\2\2\2\u0225\u0226\b\63\2\2\u0226l\3")
        buf.write(u"\2\2\2\u0227\u0228\13\2\2\2\u0228\u0229\3\2\2\2\u0229")
        buf.write(u"\u022a\b\64\b\2\u022an\3\2\2\2\u022b\u022e\5q\66\2\u022c")
        buf.write(u"\u022e\5s\67\2\u022d\u022b\3\2\2\2\u022d\u022c\3\2\2")
        buf.write(u"\2\u022ep\3\2\2\2\u022f\u0230\t\3\2\2\u0230r\3\2\2\2")
        buf.write(u"\u0231\u0232\t\4\2\2\u0232t\3\2\2\2\u0233\u0234\7\61")
        buf.write(u"\2\2\u0234\u0235\7,\2\2\u0235\u0239\3\2\2\2\u0236\u0238")
        buf.write(u"\13\2\2\2\u0237\u0236\3\2\2\2\u0238\u023b\3\2\2\2\u0239")
        buf.write(u"\u023a\3\2\2\2\u0239\u0237\3\2\2\2\u023a\u023f\3\2\2")
        buf.write(u"\2\u023b\u0239\3\2\2\2\u023c\u023d\7,\2\2\u023d\u0240")
        buf.write(u"\7\61\2\2\u023e\u0240\7\2\2\3\u023f\u023c\3\2\2\2\u023f")
        buf.write(u"\u023e\3\2\2\2\u0240v\3\2\2\2\u0241\u0242\7\61\2\2\u0242")
        buf.write(u"\u0243\7,\2\2\u0243\u0244\7,\2\2\u0244\u0248\3\2\2\2")
        buf.write(u"\u0245\u0247\13\2\2\2\u0246\u0245\3\2\2\2\u0247\u024a")
        buf.write(u"\3\2\2\2\u0248\u0249\3\2\2\2\u0248\u0246\3\2\2\2\u0249")
        buf.write(u"\u024e\3\2\2\2\u024a\u0248\3\2\2\2\u024b\u024c\7,\2\2")
        buf.write(u"\u024c\u024f\7\61\2\2\u024d\u024f\7\2\2\3\u024e\u024b")
        buf.write(u"\3\2\2\2\u024e\u024d\3\2\2\2\u024f\u025b\3\2\2\2\u0250")
        buf.write(u"\u0251\7\61\2\2\u0251\u0252\7\61\2\2\u0252\u0253\7B\2")
        buf.write(u"\2\u0253\u0257\3\2\2\2\u0254\u0256\n\5\2\2\u0255\u0254")
        buf.write(u"\3\2\2\2\u0256\u0259\3\2\2\2\u0257\u0255\3\2\2\2\u0257")
        buf.write(u"\u0258\3\2\2\2\u0258\u025b\3\2\2\2\u0259\u0257\3\2\2")
        buf.write(u"\2\u025a\u0241\3\2\2\2\u025a\u0250\3\2\2\2\u025bx\3\2")
        buf.write(u"\2\2\u025c\u025d\7\61\2\2\u025d\u025e\7\61\2\2\u025e")
        buf.write(u"\u0262\3\2\2\2\u025f\u0261\n\5\2\2\u0260\u025f\3\2\2")
        buf.write(u"\2\u0261\u0264\3\2\2\2\u0262\u0260\3\2\2\2\u0262\u0263")
        buf.write(u"\3\2\2\2\u0263z\3\2\2\2\u0264\u0262\3\2\2\2\u0265\u026a")
        buf.write(u"\5\u0097I\2\u0266\u026b\t\6\2\2\u0267\u026b\5\177=\2")
        buf.write(u"\u0268\u026b\13\2\2\2\u0269\u026b\7\2\2\3\u026a\u0266")
        buf.write(u"\3\2\2\2\u026a\u0267\3\2\2\2\u026a\u0268\3\2\2\2\u026a")
        buf.write(u"\u0269\3\2\2\2\u026b|\3\2\2\2\u026c\u026d\5\u0097I\2")
        buf.write(u"\u026d\u026e\13\2\2\2\u026e~\3\2\2\2\u026f\u027a\7w\2")
        buf.write(u"\2\u0270\u0278\5\u0083?\2\u0271\u0276\5\u0083?\2\u0272")
        buf.write(u"\u0274\5\u0083?\2\u0273\u0275\5\u0083?\2\u0274\u0273")
        buf.write(u"\3\2\2\2\u0274\u0275\3\2\2\2\u0275\u0277\3\2\2\2\u0276")
        buf.write(u"\u0272\3\2\2\2\u0276\u0277\3\2\2\2\u0277\u0279\3\2\2")
        buf.write(u"\2\u0278\u0271\3\2\2\2\u0278\u0279\3\2\2\2\u0279\u027b")
        buf.write(u"\3\2\2\2\u027a\u0270\3\2\2\2\u027a\u027b\3\2\2\2\u027b")
        buf.write(u"\u0080\3\2\2\2\u027c\u0285\7\62\2\2\u027d\u0281\t\7\2")
        buf.write(u"\2\u027e\u0280\5\u0085@\2\u027f\u027e\3\2\2\2\u0280\u0283")
        buf.write(u"\3\2\2\2\u0281\u027f\3\2\2\2\u0281\u0282\3\2\2\2\u0282")
        buf.write(u"\u0285\3\2\2\2\u0283\u0281\3\2\2\2\u0284\u027c\3\2\2")
        buf.write(u"\2\u0284\u027d\3\2\2\2\u0285\u0082\3\2\2\2\u0286\u0287")
        buf.write(u"\t\b\2\2\u0287\u0084\3\2\2\2\u0288\u0289\t\t\2\2\u0289")
        buf.write(u"\u0086\3\2\2\2\u028a\u028b\7v\2\2\u028b\u028c\7t\2\2")
        buf.write(u"\u028c\u028d\7w\2\2\u028d\u0294\7g\2\2\u028e\u028f\7")
        buf.write(u"h\2\2\u028f\u0290\7c\2\2\u0290\u0291\7n\2\2\u0291\u0292")
        buf.write(u"\7u\2\2\u0292\u0294\7g\2\2\u0293\u028a\3\2\2\2\u0293")
        buf.write(u"\u028e\3\2\2\2\u0294\u0088\3\2\2\2\u0295\u0298\5\u009d")
        buf.write(u"L\2\u0296\u0299\5{;\2\u0297\u0299\n\n\2\2\u0298\u0296")
        buf.write(u"\3\2\2\2\u0298\u0297\3\2\2\2\u0299\u029a\3\2\2\2\u029a")
        buf.write(u"\u029b\5\u009dL\2\u029b\u008a\3\2\2\2\u029c\u02a1\5\u009d")
        buf.write(u"L\2\u029d\u02a0\5{;\2\u029e\u02a0\n\n\2\2\u029f\u029d")
        buf.write(u"\3\2\2\2\u029f\u029e\3\2\2\2\u02a0\u02a3\3\2\2\2\u02a1")
        buf.write(u"\u029f\3\2\2\2\u02a1\u02a2\3\2\2\2\u02a2\u02a4\3\2\2")
        buf.write(u"\2\u02a3\u02a1\3\2\2\2\u02a4\u02a5\5\u009dL\2\u02a5\u008c")
        buf.write(u"\3\2\2\2\u02a6\u02ab\5\u009fM\2\u02a7\u02aa\5{;\2\u02a8")
        buf.write(u"\u02aa\n\13\2\2\u02a9\u02a7\3\2\2\2\u02a9\u02a8\3\2\2")
        buf.write(u"\2\u02aa\u02ad\3\2\2\2\u02ab\u02a9\3\2\2\2\u02ab\u02ac")
        buf.write(u"\3\2\2\2\u02ac\u02ae\3\2\2\2\u02ad\u02ab\3\2\2\2\u02ae")
        buf.write(u"\u02af\5\u009fM\2\u02af\u008e\3\2\2\2\u02b0\u02b5\5\u009d")
        buf.write(u"L\2\u02b1\u02b4\5{;\2\u02b2\u02b4\n\n\2\2\u02b3\u02b1")
        buf.write(u"\3\2\2\2\u02b3\u02b2\3\2\2\2\u02b4\u02b7\3\2\2\2\u02b5")
        buf.write(u"\u02b3\3\2\2\2\u02b5\u02b6\3\2\2\2\u02b6\u0090\3\2\2")
        buf.write(u"\2\u02b7\u02b5\3\2\2\2\u02b8\u02bd\5\u0093G\2\u02b9\u02bd")
        buf.write(u"\4\62;\2\u02ba\u02bd\5\u00bd\\\2\u02bb\u02bd\t\f\2\2")
        buf.write(u"\u02bc\u02b8\3\2\2\2\u02bc\u02b9\3\2\2\2\u02bc\u02ba")
        buf.write(u"\3\2\2\2\u02bc\u02bb\3\2\2\2\u02bd\u0092\3\2\2\2\u02be")
        buf.write(u"\u02bf\t\r\2\2\u02bf\u0094\3\2\2\2\u02c0\u02c1\7k\2\2")
        buf.write(u"\u02c1\u02c2\7p\2\2\u02c2\u02c3\7v\2\2\u02c3\u0096\3")
        buf.write(u"\2\2\2\u02c4\u02c5\7^\2\2\u02c5\u0098\3\2\2\2\u02c6\u02c7")
        buf.write(u"\7<\2\2\u02c7\u009a\3\2\2\2\u02c8\u02c9\7<\2\2\u02c9")
        buf.write(u"\u02ca\7<\2\2\u02ca\u009c\3\2\2\2\u02cb\u02cc\7)\2\2")
        buf.write(u"\u02cc\u009e\3\2\2\2\u02cd\u02ce\7$\2\2\u02ce\u00a0\3")
        buf.write(u"\2\2\2\u02cf\u02d0\7*\2\2\u02d0\u00a2\3\2\2\2\u02d1\u02d2")
        buf.write(u"\7+\2\2\u02d2\u00a4\3\2\2\2\u02d3\u02d4\7}\2\2\u02d4")
        buf.write(u"\u00a6\3\2\2\2\u02d5\u02d6\7\177\2\2\u02d6\u00a8\3\2")
        buf.write(u"\2\2\u02d7\u02d8\7]\2\2\u02d8\u00aa\3\2\2\2\u02d9\u02da")
        buf.write(u"\7_\2\2\u02da\u00ac\3\2\2\2\u02db\u02dc\7/\2\2\u02dc")
        buf.write(u"\u02dd\7@\2\2\u02dd\u00ae\3\2\2\2\u02de\u02df\7>\2\2")
        buf.write(u"\u02df\u00b0\3\2\2\2\u02e0\u02e1\7@\2\2\u02e1\u00b2\3")
        buf.write(u"\2\2\2\u02e2\u02e3\7?\2\2\u02e3\u00b4\3\2\2\2\u02e4\u02e5")
        buf.write(u"\7A\2\2\u02e5\u00b6\3\2\2\2\u02e6\u02e7\7,\2\2\u02e7")
        buf.write(u"\u00b8\3\2\2\2\u02e8\u02e9\7-\2\2\u02e9\u00ba\3\2\2\2")
        buf.write(u"\u02ea\u02eb\7-\2\2\u02eb\u02ec\7?\2\2\u02ec\u00bc\3")
        buf.write(u"\2\2\2\u02ed\u02ee\7a\2\2\u02ee\u00be\3\2\2\2\u02ef\u02f0")
        buf.write(u"\7~\2\2\u02f0\u00c0\3\2\2\2\u02f1\u02f2\7&\2\2\u02f2")
        buf.write(u"\u00c2\3\2\2\2\u02f3\u02f4\7.\2\2\u02f4\u00c4\3\2\2\2")
        buf.write(u"\u02f5\u02f6\7=\2\2\u02f6\u00c6\3\2\2\2\u02f7\u02f8\7")
        buf.write(u"\60\2\2\u02f8\u00c8\3\2\2\2\u02f9\u02fa\7\60\2\2\u02fa")
        buf.write(u"\u02fb\7\60\2\2\u02fb\u00ca\3\2\2\2\u02fc\u02fd\7B\2")
        buf.write(u"\2\u02fd\u00cc\3\2\2\2\u02fe\u02ff\7%\2\2\u02ff\u00ce")
        buf.write(u"\3\2\2\2\u0300\u0301\7\u0080\2\2\u0301\u00d0\3\2\2\2")
        buf.write(u"\u0302\u0303\5\u00a9R\2\u0303\u0304\3\2\2\2\u0304\u0305")
        buf.write(u"\bf\t\2\u0305\u0306\bf\n\2\u0306\u00d2\3\2\2\2\u0307")
        buf.write(u"\u0308\5}<\2\u0308\u0309\3\2\2\2\u0309\u030a\bg\t\2\u030a")
        buf.write(u"\u00d4\3\2\2\2\u030b\u030c\5\u008dD\2\u030c\u030d\3\2")
        buf.write(u"\2\2\u030d\u030e\bh\t\2\u030e\u00d6\3\2\2\2\u030f\u0310")
        buf.write(u"\5\u008bC\2\u0310\u0311\3\2\2\2\u0311\u0312\bi\t\2\u0312")
        buf.write(u"\u00d8\3\2\2\2\u0313\u0314\5\u00abS\2\u0314\u0315\bj")
        buf.write(u"\13\2\u0315\u00da\3\2\2\2\u0316\u0317\7\2\2\3\u0317\u0318")
        buf.write(u"\3\2\2\2\u0318\u0319\bk\f\2\u0319\u00dc\3\2\2\2\u031a")
        buf.write(u"\u031b\13\2\2\2\u031b\u00de\3\2\2\2\u031c\u031d\5\u00a5")
        buf.write(u"P\2\u031d\u031e\3\2\2\2\u031e\u031f\bm\r\2\u031f\u0320")
        buf.write(u"\bm\4\2\u0320\u00e0\3\2\2\2\u0321\u0322\5}<\2\u0322\u0323")
        buf.write(u"\3\2\2\2\u0323\u0324\bn\r\2\u0324\u00e2\3\2\2\2\u0325")
        buf.write(u"\u0326\5\u008dD\2\u0326\u0327\3\2\2\2\u0327\u0328\bo")
        buf.write(u"\r\2\u0328\u00e4\3\2\2\2\u0329\u032a\5\u008bC\2\u032a")
        buf.write(u"\u032b\3\2\2\2\u032b\u032c\bp\r\2\u032c\u00e6\3\2\2\2")
        buf.write(u"\u032d\u032e\5w9\2\u032e\u032f\3\2\2\2\u032f\u0330\b")
        buf.write(u"q\r\2\u0330\u00e8\3\2\2\2\u0331\u0332\5u8\2\u0332\u0333")
        buf.write(u"\3\2\2\2\u0333\u0334\br\r\2\u0334\u00ea\3\2\2\2\u0335")
        buf.write(u"\u0336\5y:\2\u0336\u0337\3\2\2\2\u0337\u0338\bs\r\2\u0338")
        buf.write(u"\u00ec\3\2\2\2\u0339\u033a\5\u00a7Q\2\u033a\u033b\bt")
        buf.write(u"\16\2\u033b\u00ee\3\2\2\2\u033c\u033d\7\2\2\3\u033d\u033e")
        buf.write(u"\3\2\2\2\u033e\u033f\bu\f\2\u033f\u00f0\3\2\2\2\u0340")
        buf.write(u"\u0341\13\2\2\2\u0341\u00f2\3\2\2\2\u0342\u0343\5w9\2")
        buf.write(u"\u0343\u0344\3\2\2\2\u0344\u0345\bw\17\2\u0345\u0346")
        buf.write(u"\bw\2\2\u0346\u00f4\3\2\2\2\u0347\u0348\5u8\2\u0348\u0349")
        buf.write(u"\3\2\2\2\u0349\u034a\bx\20\2\u034a\u034b\bx\2\2\u034b")
        buf.write(u"\u00f6\3\2\2\2\u034c\u034d\5y:\2\u034d\u034e\3\2\2\2")
        buf.write(u"\u034e\u034f\by\21\2\u034f\u0350\by\2\2\u0350\u00f8\3")
        buf.write(u"\2\2\2\u0351\u0352\5\u00a5P\2\u0352\u0353\3\2\2\2\u0353")
        buf.write(u"\u0354\bz\22\2\u0354\u00fa\3\2\2\2\u0355\u0356\5\u00a7")
        buf.write(u"Q\2\u0356\u0357\3\2\2\2\u0357\u0358\b{\23\2\u0358\u0359")
        buf.write(u"\b{\f\2\u0359\u00fc\3\2\2\2\u035a\u035b\5\u0137\u0099")
        buf.write(u"\2\u035b\u035c\3\2\2\2\u035c\u035d\b|\24\2\u035d\u00fe")
        buf.write(u"\3\2\2\2\u035e\u035f\5\u00c7a\2\u035f\u0360\3\2\2\2\u0360")
        buf.write(u"\u0361\b}\25\2\u0361\u0100\3\2\2\2\u0362\u0363\5\u00b3")
        buf.write(u"W\2\u0363\u0364\3\2\2\2\u0364\u0365\b~\26\2\u0365\u0102")
        buf.write(u"\3\2\2\2\u0366\u0367\5\u008bC\2\u0367\u0368\3\2\2\2\u0368")
        buf.write(u"\u0369\b\177\27\2\u0369\u0104\3\2\2\2\u036a\u036b\5\u0081")
        buf.write(u">\2\u036b\u036c\3\2\2\2\u036c\u036d\b\u0080\30\2\u036d")
        buf.write(u"\u0106\3\2\2\2\u036e\u036f\5\u00b7Y\2\u036f\u0370\3\2")
        buf.write(u"\2\2\u0370\u0371\b\u0081\31\2\u0371\u0108\3\2\2\2\u0372")
        buf.write(u"\u0373\5\u00c5`\2\u0373\u0374\3\2\2\2\u0374\u0375\b\u0082")
        buf.write(u"\32\2\u0375\u010a\3\2\2\2\u0376\u0378\5o\65\2\u0377\u0376")
        buf.write(u"\3\2\2\2\u0378\u0379\3\2\2\2\u0379\u0377\3\2\2\2\u0379")
        buf.write(u"\u037a\3\2\2\2\u037a\u037b\3\2\2\2\u037b\u037c\b\u0083")
        buf.write(u"\33\2\u037c\u037d\b\u0083\2\2\u037d\u010c\3\2\2\2\u037e")
        buf.write(u"\u037f\5w9\2\u037f\u0380\3\2\2\2\u0380\u0381\b\u0084")
        buf.write(u"\17\2\u0381\u0382\b\u0084\2\2\u0382\u010e\3\2\2\2\u0383")
        buf.write(u"\u0384\5u8\2\u0384\u0385\3\2\2\2\u0385\u0386\b\u0085")
        buf.write(u"\20\2\u0386\u0387\b\u0085\2\2\u0387\u0110\3\2\2\2\u0388")
        buf.write(u"\u0389\5y:\2\u0389\u038a\3\2\2\2\u038a\u038b\b\u0086")
        buf.write(u"\21\2\u038b\u038c\b\u0086\2\2\u038c\u0112\3\2\2\2\u038d")
        buf.write(u"\u038e\5\u00a5P\2\u038e\u038f\3\2\2\2\u038f\u0390\b\u0087")
        buf.write(u"\22\2\u0390\u0114\3\2\2\2\u0391\u0392\5\u00a7Q\2\u0392")
        buf.write(u"\u0393\3\2\2\2\u0393\u0394\b\u0088\23\2\u0394\u0395\b")
        buf.write(u"\u0088\f\2\u0395\u0116\3\2\2\2\u0396\u0397\5\u0137\u0099")
        buf.write(u"\2\u0397\u0398\3\2\2\2\u0398\u0399\b\u0089\24\2\u0399")
        buf.write(u"\u0118\3\2\2\2\u039a\u039b\5\u00c7a\2\u039b\u039c\3\2")
        buf.write(u"\2\2\u039c\u039d\b\u008a\25\2\u039d\u011a\3\2\2\2\u039e")
        buf.write(u"\u039f\5\u00c3_\2\u039f\u03a0\3\2\2\2\u03a0\u03a1\b\u008b")
        buf.write(u"\34\2\u03a1\u011c\3\2\2\2\u03a2\u03a4\5o\65\2\u03a3\u03a2")
        buf.write(u"\3\2\2\2\u03a4\u03a5\3\2\2\2\u03a5\u03a3\3\2\2\2\u03a5")
        buf.write(u"\u03a6\3\2\2\2\u03a6\u03a7\3\2\2\2\u03a7\u03a8\b\u008c")
        buf.write(u"\33\2\u03a8\u03a9\b\u008c\2\2\u03a9\u011e\3\2\2\2\u03aa")
        buf.write(u"\u03ab\5w9\2\u03ab\u03ac\3\2\2\2\u03ac\u03ad\b\u008d")
        buf.write(u"\17\2\u03ad\u03ae\b\u008d\2\2\u03ae\u0120\3\2\2\2\u03af")
        buf.write(u"\u03b0\5u8\2\u03b0\u03b1\3\2\2\2\u03b1\u03b2\b\u008e")
        buf.write(u"\20\2\u03b2\u03b3\b\u008e\2\2\u03b3\u0122\3\2\2\2\u03b4")
        buf.write(u"\u03b5\5y:\2\u03b5\u03b6\3\2\2\2\u03b6\u03b7\b\u008f")
        buf.write(u"\21\2\u03b7\u03b8\b\u008f\2\2\u03b8\u0124\3\2\2\2\u03b9")
        buf.write(u"\u03ba\5\u00a5P\2\u03ba\u03bb\3\2\2\2\u03bb\u03bc\b\u0090")
        buf.write(u"\22\2\u03bc\u0126\3\2\2\2\u03bd\u03be\5\u00a7Q\2\u03be")
        buf.write(u"\u03bf\3\2\2\2\u03bf\u03c0\b\u0091\23\2\u03c0\u03c1\b")
        buf.write(u"\u0091\f\2\u03c1\u0128\3\2\2\2\u03c2\u03c3\5\u0137\u0099")
        buf.write(u"\2\u03c3\u03c4\3\2\2\2\u03c4\u03c5\b\u0092\24\2\u03c5")
        buf.write(u"\u012a\3\2\2\2\u03c6\u03c7\5\u00c7a\2\u03c7\u03c8\3\2")
        buf.write(u"\2\2\u03c8\u03c9\b\u0093\25\2\u03c9\u012c\3\2\2\2\u03ca")
        buf.write(u"\u03cb\5\u00c3_\2\u03cb\u03cc\3\2\2\2\u03cc\u03cd\b\u0094")
        buf.write(u"\34\2\u03cd\u012e\3\2\2\2\u03ce\u03d0\5o\65\2\u03cf\u03ce")
        buf.write(u"\3\2\2\2\u03d0\u03d1\3\2\2\2\u03d1\u03cf\3\2\2\2\u03d1")
        buf.write(u"\u03d2\3\2\2\2\u03d2\u03d3\3\2\2\2\u03d3\u03d4\b\u0095")
        buf.write(u"\33\2\u03d4\u03d5\b\u0095\2\2\u03d5\u0130\3\2\2\2\u03d6")
        buf.write(u"\u03d9\n\16\2\2\u03d7\u03d9\5}<\2\u03d8\u03d6\3\2\2\2")
        buf.write(u"\u03d8\u03d7\3\2\2\2\u03d9\u03da\3\2\2\2\u03da\u03d8")
        buf.write(u"\3\2\2\2\u03da\u03db\3\2\2\2\u03db\u03dc\3\2\2\2\u03dc")
        buf.write(u"\u03dd\b\u0096\35\2\u03dd\u0132\3\2\2\2\u03de\u03df\5")
        buf.write(u"\u00abS\2\u03df\u03e0\3\2\2\2\u03e0\u03e1\b\u0097\f\2")
        buf.write(u"\u03e1\u0134\3\2\2\2\u03e2\u03e3\7\2\2\3\u03e3\u03e4")
        buf.write(u"\3\2\2\2\u03e4\u03e5\b\u0098\f\2\u03e5\u0136\3\2\2\2")
        buf.write(u"\u03e6\u03ea\5\u0093G\2\u03e7\u03e9\5\u0091F\2\u03e8")
        buf.write(u"\u03e7\3\2\2\2\u03e9\u03ec\3\2\2\2\u03ea\u03e8\3\2\2")
        buf.write(u"\2\u03ea\u03eb\3\2\2\2\u03eb\u0138\3\2\2\2\u03ec\u03ea")
        buf.write(u"\3\2\2\2+\2\3\4\5\6\7\b\u015c\u016e\u0182\u0223\u022d")
        buf.write(u"\u0239\u023f\u0248\u024e\u0257\u025a\u0262\u026a\u0274")
        buf.write(u"\u0276\u0278\u027a\u0281\u0284\u0293\u0298\u029f\u02a1")
        buf.write(u"\u02a9\u02ab\u02b3\u02b5\u02bc\u0379\u03a5\u03d1\u03d8")
        buf.write(u"\u03da\u03ea\36\2\4\2\3\b\2\7\4\2\7\5\2\7\6\2\7\7\2\2")
        buf.write(u"\3\2\t;\2\7\3\2\3j\3\6\2\2\t>\2\3t\4\t\6\2\t\7\2\t\b")
        buf.write(u"\2\t%\2\t&\2\t\66\2\t\62\2\t*\2\t\n\2\t\t\2\t,\2\t\"")
        buf.write(u"\2\t\67\2\t!\2\5\2\2")
        return buf.getvalue()


class ANTLRv4Lexer(LexerAdaptor):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    OFF_CHANNEL = 2

    Argument = 1
    Action = 2
    Options = 3
    Tokens = 4
    Channels = 5
    LexerCharSet = 6

    TOKEN_REF = 1
    RULE_REF = 2
    LEXER_CHAR_SET = 3
    DOC_COMMENT = 4
    BLOCK_COMMENT = 5
    LINE_COMMENT = 6
    INT = 7
    STRING_LITERAL = 8
    UNTERMINATED_STRING_LITERAL = 9
    BEGIN_ARGUMENT = 10
    BEGIN_ACTION = 11
    OPTIONS = 12
    TOKENS = 13
    CHANNELS = 14
    IMPORT = 15
    FRAGMENT = 16
    LEXER = 17
    PARSER = 18
    GRAMMAR = 19
    PROTECTED = 20
    PUBLIC = 21
    PRIVATE = 22
    RETURNS = 23
    LOCALS = 24
    THROWS = 25
    CATCH = 26
    FINALLY = 27
    MODE = 28
    COLON = 29
    COLONCOLON = 30
    COMMA = 31
    SEMI = 32
    LPAREN = 33
    RPAREN = 34
    LBRACE = 35
    RBRACE = 36
    RARROW = 37
    LT = 38
    GT = 39
    ASSIGN = 40
    QUESTION = 41
    STAR = 42
    PLUS_ASSIGN = 43
    PLUS = 44
    OR = 45
    DOLLAR = 46
    RANGE = 47
    DOT = 48
    AT = 49
    POUND = 50
    NOT = 51
    ID = 52
    WS = 53
    ERRCHAR = 54
    END_ARGUMENT = 55
    UNTERMINATED_ARGUMENT = 56
    ARGUMENT_CONTENT = 57
    END_ACTION = 58
    UNTERMINATED_ACTION = 59
    ACTION_CONTENT = 60
    UNTERMINATED_CHAR_SET = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN", u"OFF_CHANNEL" ]

    modeNames = [ u"DEFAULT_MODE", u"Argument", u"Action", u"Options", u"Tokens", 
                  u"Channels", u"LexerCharSet" ]

    literalNames = [ u"<INVALID>",
            u"'import'", u"'fragment'", u"'lexer'", u"'parser'", u"'grammar'", 
            u"'protected'", u"'public'", u"'private'", u"'returns'", u"'locals'", 
            u"'throws'", u"'catch'", u"'finally'", u"'mode'" ]

    symbolicNames = [ u"<INVALID>",
            u"TOKEN_REF", u"RULE_REF", u"LEXER_CHAR_SET", u"DOC_COMMENT", 
            u"BLOCK_COMMENT", u"LINE_COMMENT", u"INT", u"STRING_LITERAL", 
            u"UNTERMINATED_STRING_LITERAL", u"BEGIN_ARGUMENT", u"BEGIN_ACTION", 
            u"OPTIONS", u"TOKENS", u"CHANNELS", u"IMPORT", u"FRAGMENT", 
            u"LEXER", u"PARSER", u"GRAMMAR", u"PROTECTED", u"PUBLIC", u"PRIVATE", 
            u"RETURNS", u"LOCALS", u"THROWS", u"CATCH", u"FINALLY", u"MODE", 
            u"COLON", u"COLONCOLON", u"COMMA", u"SEMI", u"LPAREN", u"RPAREN", 
            u"LBRACE", u"RBRACE", u"RARROW", u"LT", u"GT", u"ASSIGN", u"QUESTION", 
            u"STAR", u"PLUS_ASSIGN", u"PLUS", u"OR", u"DOLLAR", u"RANGE", 
            u"DOT", u"AT", u"POUND", u"NOT", u"ID", u"WS", u"ERRCHAR", u"END_ARGUMENT", 
            u"UNTERMINATED_ARGUMENT", u"ARGUMENT_CONTENT", u"END_ACTION", 
            u"UNTERMINATED_ACTION", u"ACTION_CONTENT", u"UNTERMINATED_CHAR_SET" ]

    ruleNames = [ u"DOC_COMMENT", u"BLOCK_COMMENT", u"LINE_COMMENT", u"INT", 
                  u"STRING_LITERAL", u"UNTERMINATED_STRING_LITERAL", u"BEGIN_ARGUMENT", 
                  u"BEGIN_ACTION", u"OPTIONS", u"TOKENS", u"CHANNELS", u"IMPORT", 
                  u"FRAGMENT", u"LEXER", u"PARSER", u"GRAMMAR", u"PROTECTED", 
                  u"PUBLIC", u"PRIVATE", u"RETURNS", u"LOCALS", u"THROWS", 
                  u"CATCH", u"FINALLY", u"MODE", u"COLON", u"COLONCOLON", 
                  u"COMMA", u"SEMI", u"LPAREN", u"RPAREN", u"LBRACE", u"RBRACE", 
                  u"RARROW", u"LT", u"GT", u"ASSIGN", u"QUESTION", u"STAR", 
                  u"PLUS_ASSIGN", u"PLUS", u"OR", u"DOLLAR", u"RANGE", u"DOT", 
                  u"AT", u"POUND", u"NOT", u"ID", u"WS", u"ERRCHAR", u"Ws", 
                  u"Hws", u"Vws", u"BlockComment", u"DocComment", u"LineComment", 
                  u"EscSeq", u"EscAny", u"UnicodeEsc", u"DecimalNumeral", 
                  u"HexDigit", u"DecDigit", u"BoolLiteral", u"CharLiteral", 
                  u"SQuoteLiteral", u"DQuoteLiteral", u"USQuoteLiteral", 
                  u"NameChar", u"NameStartChar", u"Int", u"Esc", u"Colon", 
                  u"DColon", u"SQuote", u"DQuote", u"LParen", u"RParen", 
                  u"LBrace", u"RBrace", u"LBrack", u"RBrack", u"RArrow", 
                  u"Lt", u"Gt", u"Equal", u"Question", u"Star", u"Plus", 
                  u"PlusAssign", u"Underscore", u"Pipe", u"Dollar", u"Comma", 
                  u"Semi", u"Dot", u"Range", u"At", u"Pound", u"Tilde", 
                  u"NESTED_ARGUMENT", u"ARGUMENT_ESCAPE", u"ARGUMENT_STRING_LITERAL", 
                  u"ARGUMENT_CHAR_LITERAL", u"END_ARGUMENT", u"UNTERMINATED_ARGUMENT", 
                  u"ARGUMENT_CONTENT", u"NESTED_ACTION", u"ACTION_ESCAPE", 
                  u"ACTION_STRING_LITERAL", u"ACTION_CHAR_LITERAL", u"ACTION_DOC_COMMENT", 
                  u"ACTION_BLOCK_COMMENT", u"ACTION_LINE_COMMENT", u"END_ACTION", 
                  u"UNTERMINATED_ACTION", u"ACTION_CONTENT", u"OPT_DOC_COMMENT", 
                  u"OPT_BLOCK_COMMENT", u"OPT_LINE_COMMENT", u"OPT_LBRACE", 
                  u"OPT_RBRACE", u"OPT_ID", u"OPT_DOT", u"OPT_ASSIGN", u"OPT_STRING_LITERAL", 
                  u"OPT_INT", u"OPT_STAR", u"OPT_SEMI", u"OPT_WS", u"TOK_DOC_COMMENT", 
                  u"TOK_BLOCK_COMMENT", u"TOK_LINE_COMMENT", u"TOK_LBRACE", 
                  u"TOK_RBRACE", u"TOK_ID", u"TOK_DOT", u"TOK_COMMA", u"TOK_WS", 
                  u"CHN_DOC_COMMENT", u"CHN_BLOCK_COMMENT", u"CHN_LINE_COMMENT", 
                  u"CHN_LBRACE", u"CHN_RBRACE", u"CHN_ID", u"CHN_DOT", u"CHN_COMMA", 
                  u"CHN_WS", u"LEXER_CHAR_SET_BODY", u"LEXER_CHAR_SET", 
                  u"UNTERMINATED_CHAR_SET", u"Id" ]

    grammarFileName = u"ANTLRv4Lexer.g4"

    def __init__(self, input=None, output=sys.stdout):
        super(ANTLRv4Lexer, self).__init__(input, output=output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx, ruleIndex, actionIndex):
    	if self._actions is None:
    		actions = dict()
    		actions[6] = self.BEGIN_ARGUMENT_action 
    		actions[104] = self.END_ARGUMENT_action 
    		actions[114] = self.END_ACTION_action 
    		self._actions = actions
    	action = self._actions.get(ruleIndex, None)
    	if action is not None:
    		action(localctx, actionIndex)
    	else:
    		raise Exception("No registered action for:" + str(ruleIndex))

    def BEGIN_ARGUMENT_action(self, localctx , actionIndex):
        if actionIndex == 0:
             self.handleBeginArgument() 
     

    def END_ARGUMENT_action(self, localctx , actionIndex):
        if actionIndex == 1:
             self.handleEndArgument() 
     

    def END_ACTION_action(self, localctx , actionIndex):
        if actionIndex == 2:
             self.handleEndAction() 
     

    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates is None:
            preds = dict()
            preds[8] = self.OPTIONS_sempred
            preds[9] = self.TOKENS_sempred
            preds[10] = self.CHANNELS_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def OPTIONS_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.getCurrentRuleType() == Token.INVALID_TYPE
         

    def TOKENS_sempred(self, localctx, predIndex):
            if predIndex == 1:
                return self.getCurrentRuleType() == Token.INVALID_TYPE
         

    def CHANNELS_sempred(self, localctx, predIndex):
            if predIndex == 2:
                return self.getCurrentRuleType() == Token.INVALID_TYPE
         


