import unittest
from wrapt_timeout_decorator import timeout

from solution import Solution

TEST_TIMEOUT = 1


class TestSolution(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.solution = Solution()

    @timeout(TEST_TIMEOUT)
    def test_case_1(self):
        [beginWord, endWord] = ["hit", "cog"]
        wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
        expected = [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]
        actual = self.solution.findLadders(beginWord, endWord, wordList)
        self.assertCountEqual(actual, expected)

    @timeout(TEST_TIMEOUT)
    def test_case_2(self):
        [beginWord, endWord] = ["hit", "cog"]
        wordList = ["hot", "dot", "dog", "lot", "log"]
        expected = []
        actual = self.solution.findLadders(beginWord, endWord, wordList)
        self.assertCountEqual(actual, expected)

    @timeout(TEST_TIMEOUT)
    def test_case_19(self):
        [beginWord, endWord] = ["qa", "sq"]
        wordList = ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm",
                    "ar", "ci", "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe",
                    "ho", "ma", "re", "or", "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb",
                    "if", "pb", "ge", "th", "pm", "rb", "sh", "co", "ga", "li", "ha", "hz", "no", "bi", "di", "hi",
                    "qa", "pi", "os", "uh", "wm", "an", "me", "mo", "na", "la", "st", "er", "sc", "ne", "mn", "mi",
                    "am", "ex", "pt", "io", "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"]
        expected = [["qa", "na", "ni", "si", "sq"], ["qa", "pa", "pi", "si", "sq"], ["qa", "ha", "hi", "si", "sq"],
                    ["qa", "ma", "mi", "si", "sq"], ["qa", "ba", "bi", "si", "sq"], ["qa", "ta", "ti", "si", "sq"],
                    ["qa", "ca", "ci", "si", "sq"], ["qa", "la", "li", "si", "sq"], ["qa", "na", "no", "so", "sq"],
                    ["qa", "ga", "go", "so", "sq"], ["qa", "pa", "po", "so", "sq"], ["qa", "ha", "ho", "so", "sq"],
                    ["qa", "ma", "mo", "so", "sq"], ["qa", "ta", "to", "so", "sq"], ["qa", "ca", "co", "so", "sq"],
                    ["qa", "la", "lo", "so", "sq"], ["qa", "ya", "yo", "so", "sq"], ["qa", "na", "nb", "sb", "sq"],
                    ["qa", "ra", "rb", "sb", "sq"], ["qa", "pa", "pb", "sb", "sq"], ["qa", "ma", "mb", "sb", "sq"],
                    ["qa", "ta", "tb", "sb", "sq"], ["qa", "ya", "yb", "sb", "sq"], ["qa", "na", "ne", "se", "sq"],
                    ["qa", "ga", "ge", "se", "sq"], ["qa", "ra", "re", "se", "sq"], ["qa", "ha", "he", "se", "sq"],
                    ["qa", "ma", "me", "se", "sq"], ["qa", "ba", "be", "se", "sq"], ["qa", "la", "le", "se", "sq"],
                    ["qa", "fa", "fe", "se", "sq"], ["qa", "ya", "ye", "se", "sq"], ["qa", "ra", "rh", "sh", "sq"],
                    ["qa", "pa", "ph", "sh", "sq"], ["qa", "ta", "th", "sh", "sq"], ["qa", "ra", "rn", "sn", "sq"],
                    ["qa", "ma", "mn", "sn", "sq"], ["qa", "la", "ln", "sn", "sq"], ["qa", "pa", "pm", "sm", "sq"],
                    ["qa", "ta", "tm", "sm", "sq"], ["qa", "ca", "cm", "sm", "sq"], ["qa", "fa", "fm", "sm", "sq"],
                    ["qa", "pa", "pt", "st", "sq"], ["qa", "ma", "mt", "st", "sq"], ["qa", "la", "lt", "st", "sq"],
                    ["qa", "ma", "mr", "sr", "sq"], ["qa", "ba", "br", "sr", "sq"], ["qa", "ca", "cr", "sr", "sq"],
                    ["qa", "la", "lr", "sr", "sq"], ["qa", "fa", "fr", "sr", "sq"], ["qa", "ta", "tc", "sc", "sq"]]
        actual = self.solution.findLadders(beginWord, endWord, wordList)
        self.assertCountEqual(actual, expected)

    @timeout(TEST_TIMEOUT)
    def test_case_21(self):
        [beginWord, endWord] = ["cet", "ism"]
        wordList = ["kid", "tag", "pup", "ail", "tun", "woo", "erg", "luz", "brr", "gay", "sip", "kay", "per", "val",
                    "mes", "ohs", "now", "boa", "cet", "pal", "bar", "die", "war", "hay", "eco", "pub", "lob", "rue",
                    "fry", "lit", "rex", "jan", "cot", "bid", "ali", "pay", "col", "gum", "ger", "row", "won", "dan",
                    "rum", "fad", "tut", "sag", "yip", "sui", "ark", "has", "zip", "fez", "own", "ump", "dis", "ads",
                    "max", "jaw", "out", "btu", "ana", "gap", "cry", "led", "abe", "box", "ore", "pig", "fie", "toy",
                    "fat", "cal", "lie", "noh", "sew", "ono", "tam", "flu", "mgm", "ply", "awe", "pry", "tit", "tie",
                    "yet", "too", "tax", "jim", "san", "pan", "map", "ski", "ova", "wed", "non", "wac", "nut", "why",
                    "bye", "lye", "oct", "old", "fin", "feb", "chi", "sap", "owl", "log", "tod", "dot", "bow", "fob",
                    "for", "joe", "ivy", "fan", "age", "fax", "hip", "jib", "mel", "hus", "sob", "ifs", "tab", "ara",
                    "dab", "jag", "jar", "arm", "lot", "tom", "sax", "tex", "yum", "pei", "wen", "wry", "ire", "irk",
                    "far", "mew", "wit", "doe", "gas", "rte", "ian", "pot", "ask", "wag", "hag", "amy", "nag", "ron",
                    "soy", "gin", "don", "tug", "fay", "vic", "boo", "nam", "ave", "buy", "sop", "but", "orb", "fen",
                    "paw", "his", "sub", "bob", "yea", "oft", "inn", "rod", "yam", "pew", "web", "hod", "hun", "gyp",
                    "wei", "wis", "rob", "gad", "pie", "mon", "dog", "bib", "rub", "ere", "dig", "era", "cat", "fox",
                    "bee", "mod", "day", "apr", "vie", "nev", "jam", "pam", "new", "aye", "ani", "and", "ibm", "yap",
                    "can", "pyx", "tar", "kin", "fog", "hum", "pip", "cup", "dye", "lyx", "jog", "nun", "par", "wan",
                    "fey", "bus", "oak", "bad", "ats", "set", "qom", "vat", "eat", "pus", "rev", "axe", "ion", "six",
                    "ila", "lao", "mom", "mas", "pro", "few", "opt", "poe", "art", "ash", "oar", "cap", "lop", "may",
                    "shy", "rid", "bat", "sum", "rim", "fee", "bmw", "sky", "maj", "hue", "thy", "ava", "rap", "den",
                    "fla", "auk", "cox", "ibo", "hey", "saw", "vim", "sec", "ltd", "you", "its", "tat", "dew", "eva",
                    "tog", "ram", "let", "see", "zit", "maw", "nix", "ate", "gig", "rep", "owe", "ind", "hog", "eve",
                    "sam", "zoo", "any", "dow", "cod", "bed", "vet", "ham", "sis", "hex", "via", "fir", "nod", "mao",
                    "aug", "mum", "hoe", "bah", "hal", "keg", "hew", "zed", "tow", "gog", "ass", "dem", "who", "bet",
                    "gos", "son", "ear", "spy", "kit", "boy", "due", "sen", "oaf", "mix", "hep", "fur", "ada", "bin",
                    "nil", "mia", "ewe", "hit", "fix", "sad", "rib", "eye", "hop", "haw", "wax", "mid", "tad", "ken",
                    "wad", "rye", "pap", "bog", "gut", "ito", "woe", "our", "ado", "sin", "mad", "ray", "hon", "roy",
                    "dip", "hen", "iva", "lug", "asp", "hui", "yak", "bay", "poi", "yep", "bun", "try", "lad", "elm",
                    "nat", "wyo", "gym", "dug", "toe", "dee", "wig", "sly", "rip", "geo", "cog", "pas", "zen", "odd",
                    "nan", "lay", "pod", "fit", "hem", "joy", "bum", "rio", "yon", "dec", "leg", "put", "sue", "dim",
                    "pet", "yaw", "nub", "bit", "bur", "sid", "sun", "oil", "red", "doc", "moe", "caw", "eel", "dix",
                    "cub", "end", "gem", "off", "yew", "hug", "pop", "tub", "sgt", "lid", "pun", "ton", "sol", "din",
                    "yup", "jab", "pea", "bug", "gag", "mil", "jig", "hub", "low", "did", "tin", "get", "gte", "sox",
                    "lei", "mig", "fig", "lon", "use", "ban", "flo", "nov", "jut", "bag", "mir", "sty", "lap", "two",
                    "ins", "con", "ant", "net", "tux", "ode", "stu", "mug", "cad", "nap", "gun", "fop", "tot", "sow",
                    "sal", "sic", "ted", "wot", "del", "imp", "cob", "way", "ann", "tan", "mci", "job", "wet", "ism",
                    "err", "him", "all", "pad", "hah", "hie", "aim"]
        expected = [['cet', 'cat', 'can', 'ian', 'inn', 'ins', 'its', 'ito', 'ibo', 'ibm', 'ism'],
                    ['cet', 'cot', 'con', 'ion', 'inn', 'ins', 'its', 'ito', 'ibo', 'ibm', 'ism']]
        actual = self.solution.findLadders(beginWord, endWord, wordList)
        self.assertCountEqual(actual, expected)

    @timeout(TEST_TIMEOUT)
    def test_case_31(self):
        [beginWord, endWord] = ["a", "c"]
        wordList = ["a", "b", "c"]
        expected = [["a", "c"]]
        actual = self.solution.findLadders(beginWord, endWord, wordList)
        self.assertCountEqual(actual, expected)

    @timeout(TEST_TIMEOUT)
    def test_case_32(self):
        [beginWord, endWord] = ["aaaaa", "ggggg"]
        wordList = ["aaaaa", "caaaa", "cbaaa", "daaaa", "dbaaa", "eaaaa", "ebaaa", "faaaa", "fbaaa", "gaaaa", "gbaaa",
                    "haaaa", "hbaaa", "iaaaa", "ibaaa", "jaaaa", "jbaaa", "kaaaa", "kbaaa", "laaaa", "lbaaa", "maaaa",
                    "mbaaa", "naaaa", "nbaaa", "oaaaa", "obaaa", "paaaa", "pbaaa", "bbaaa", "bbcaa", "bbcba", "bbdaa",
                    "bbdba", "bbeaa", "bbeba", "bbfaa", "bbfba", "bbgaa", "bbgba", "bbhaa", "bbhba", "bbiaa", "bbiba",
                    "bbjaa", "bbjba", "bbkaa", "bbkba", "bblaa", "bblba", "bbmaa", "bbmba", "bbnaa", "bbnba", "bboaa",
                    "bboba", "bbpaa", "bbpba", "bbbba", "abbba", "acbba", "dbbba", "dcbba", "ebbba", "ecbba", "fbbba",
                    "fcbba", "gbbba", "gcbba", "hbbba", "hcbba", "ibbba", "icbba", "jbbba", "jcbba", "kbbba", "kcbba",
                    "lbbba", "lcbba", "mbbba", "mcbba", "nbbba", "ncbba", "obbba", "ocbba", "pbbba", "pcbba", "ccbba",
                    "ccaba", "ccaca", "ccdba", "ccdca", "cceba", "cceca", "ccfba", "ccfca", "ccgba", "ccgca", "cchba",
                    "cchca", "cciba", "ccica", "ccjba", "ccjca", "cckba", "cckca", "cclba", "cclca", "ccmba", "ccmca",
                    "ccnba", "ccnca", "ccoba", "ccoca", "ccpba", "ccpca", "cccca", "accca", "adcca", "bccca", "bdcca",
                    "eccca", "edcca", "fccca", "fdcca", "gccca", "gdcca", "hccca", "hdcca", "iccca", "idcca", "jccca",
                    "jdcca", "kccca", "kdcca", "lccca", "ldcca", "mccca", "mdcca", "nccca", "ndcca", "occca", "odcca",
                    "pccca", "pdcca", "ddcca", "ddaca", "ddada", "ddbca", "ddbda", "ddeca", "ddeda", "ddfca", "ddfda",
                    "ddgca", "ddgda", "ddhca", "ddhda", "ddica", "ddida", "ddjca", "ddjda", "ddkca", "ddkda", "ddlca",
                    "ddlda", "ddmca", "ddmda", "ddnca", "ddnda", "ddoca", "ddoda", "ddpca", "ddpda", "dddda", "addda",
                    "aedda", "bddda", "bedda", "cddda", "cedda", "fddda", "fedda", "gddda", "gedda", "hddda", "hedda",
                    "iddda", "iedda", "jddda", "jedda", "kddda", "kedda", "lddda", "ledda", "mddda", "medda", "nddda",
                    "nedda", "oddda", "oedda", "pddda", "pedda", "eedda", "eeada", "eeaea", "eebda", "eebea", "eecda",
                    "eecea", "eefda", "eefea", "eegda", "eegea", "eehda", "eehea", "eeida", "eeiea", "eejda", "eejea",
                    "eekda", "eekea", "eelda", "eelea", "eemda", "eemea", "eenda", "eenea", "eeoda", "eeoea", "eepda",
                    "eepea", "eeeea", "ggggg", "agggg", "ahggg", "bgggg", "bhggg", "cgggg", "chggg", "dgggg", "dhggg",
                    "egggg", "ehggg", "fgggg", "fhggg", "igggg", "ihggg", "jgggg", "jhggg", "kgggg", "khggg", "lgggg",
                    "lhggg", "mgggg", "mhggg", "ngggg", "nhggg", "ogggg", "ohggg", "pgggg", "phggg", "hhggg", "hhagg",
                    "hhahg", "hhbgg", "hhbhg", "hhcgg", "hhchg", "hhdgg", "hhdhg", "hhegg", "hhehg", "hhfgg", "hhfhg",
                    "hhigg", "hhihg", "hhjgg", "hhjhg", "hhkgg", "hhkhg", "hhlgg", "hhlhg", "hhmgg", "hhmhg", "hhngg",
                    "hhnhg", "hhogg", "hhohg", "hhpgg", "hhphg", "hhhhg", "ahhhg", "aihhg", "bhhhg", "bihhg", "chhhg",
                    "cihhg", "dhhhg", "dihhg", "ehhhg", "eihhg", "fhhhg", "fihhg", "ghhhg", "gihhg", "jhhhg", "jihhg",
                    "khhhg", "kihhg", "lhhhg", "lihhg", "mhhhg", "mihhg", "nhhhg", "nihhg", "ohhhg", "oihhg", "phhhg",
                    "pihhg", "iihhg", "iiahg", "iiaig", "iibhg", "iibig", "iichg", "iicig", "iidhg", "iidig", "iiehg",
                    "iieig", "iifhg", "iifig", "iighg", "iigig", "iijhg", "iijig", "iikhg", "iikig", "iilhg", "iilig",
                    "iimhg", "iimig", "iinhg", "iinig", "iiohg", "iioig", "iiphg", "iipig", "iiiig", "aiiig", "ajiig",
                    "biiig", "bjiig", "ciiig", "cjiig", "diiig", "djiig", "eiiig", "ejiig", "fiiig", "fjiig", "giiig",
                    "gjiig", "hiiig", "hjiig", "kiiig", "kjiig", "liiig", "ljiig", "miiig", "mjiig", "niiig", "njiig",
                    "oiiig", "ojiig", "piiig", "pjiig", "jjiig", "jjaig", "jjajg", "jjbig", "jjbjg", "jjcig", "jjcjg",
                    "jjdig", "jjdjg", "jjeig", "jjejg", "jjfig", "jjfjg", "jjgig", "jjgjg", "jjhig", "jjhjg", "jjkig",
                    "jjkjg", "jjlig", "jjljg", "jjmig", "jjmjg", "jjnig", "jjnjg", "jjoig", "jjojg", "jjpig", "jjpjg",
                    "jjjjg", "ajjjg", "akjjg", "bjjjg", "bkjjg", "cjjjg", "ckjjg", "djjjg", "dkjjg", "ejjjg", "ekjjg",
                    "fjjjg", "fkjjg", "gjjjg", "gkjjg", "hjjjg", "hkjjg", "ijjjg", "ikjjg", "ljjjg", "lkjjg", "mjjjg",
                    "mkjjg", "njjjg", "nkjjg", "ojjjg", "okjjg", "pjjjg", "pkjjg", "kkjjg", "kkajg", "kkakg", "kkbjg",
                    "kkbkg", "kkcjg", "kkckg", "kkdjg", "kkdkg", "kkejg", "kkekg", "kkfjg", "kkfkg", "kkgjg", "kkgkg",
                    "kkhjg", "kkhkg", "kkijg", "kkikg", "kkljg", "kklkg", "kkmjg", "kkmkg", "kknjg", "kknkg", "kkojg",
                    "kkokg", "kkpjg", "kkpkg", "kkkkg", "ggggx", "gggxx", "ggxxx", "gxxxx", "xxxxx", "xxxxy", "xxxyy",
                    "xxyyy", "xyyyy", "yyyyy", "yyyyw", "yyyww", "yywww", "ywwww", "wwwww", "wwvww", "wvvww", "vvvww",
                    "vvvwz", "avvwz", "aavwz", "aaawz", "aaaaz"]
        expected = [
            ['aaaaa', 'aaaaz', 'aaawz', 'aavwz', 'avvwz', 'vvvwz', 'vvvww', 'wvvww', 'wwvww', 'wwwww', 'ywwww', 'yywww',
             'yyyww', 'yyyyw', 'yyyyy', 'xyyyy', 'xxyyy', 'xxxyy', 'xxxxy', 'xxxxx', 'gxxxx', 'ggxxx', 'gggxx', 'ggggx',
             'ggggg']]
        actual = self.solution.findLadders(beginWord, endWord, wordList)
        self.assertCountEqual(actual, expected)

    @timeout(TEST_TIMEOUT)
    def test_case_34(self):
        [beginWord, endWord] = ["cater", "mangy"]
        wordList = ["kinds", "taney", "mangy", "pimps", "belly", "liter", "cooks", "finny", "buddy", "hewer", "roves",
                    "lusts", "toots", "fully", "acorn", "junes", "araby", "visas", "pyres", "siren", "limps", "paved",
                    "marla", "tulsa", "foxes", "purls", "stats", "bidet", "milky", "payee", "horny", "tanks", "mints",
                    "cindy", "forms", "files", "fucks", "dolts", "welts", "dykes", "riced", "rebel", "gulfs", "bully",
                    "meets", "tidal", "surer", "gecko", "noyes", "rents", "aaron", "rafts", "roils", "sower", "dicey",
                    "sties", "jamal", "bases", "locus", "gusts", "briar", "gills", "filly", "mixes", "fjord", "aggie",
                    "tails", "funks", "freon", "roods", "links", "natal", "melds", "abide", "hardy", "lands", "unpin",
                    "loges", "weest", "rices", "dicks", "gyros", "hands", "quoit", "hater", "rings", "loxed", "weeds",
                    "coeds", "handy", "boxer", "jamar", "cokes", "earls", "tings", "haley", "tangy", "hinds", "cater",
                    "mores", "lloyd", "bayes", "slice", "taker", "piped", "doses", "sides", "gorge", "sorta", "gavel",
                    "lanes", "wrote", "haney", "monet", "mikes", "bared", "pelts", "fails", "curry", "waken", "jaded",
                    "halos", "welds", "danes", "assad", "waded", "agree", "bents", "comet", "train", "crags", "fifes",
                    "rared", "noons", "scums", "steep", "haler", "waxen", "carey", "gamay", "larry", "diver", "honer",
                    "mandy", "poxed", "coded", "waned", "sades", "clair", "fared", "hangs", "sully", "tiled", "stoic",
                    "docks", "cloth"]
        expected = [["cater", "hater", "haler", "haley", "haney", "taney", "tangy", "mangy"],
                    ["cater", "hater", "haler", "haley", "haney", "handy", "mandy", "mangy"]]
        actual = self.solution.findLadders(beginWord, endWord, wordList)
        self.assertCountEqual(actual, expected)
