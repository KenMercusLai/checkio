import random
import string
import unittest

from playfair_cipher import decode, encode


class Tests(unittest.TestCase):
    BASIC_TESTS = [
        [encode, ["Fizz Buzz is x89 XX.", "checkio101"], 'do2y7mt22kry94y2y2'],
        [decode, ["do2y7mt22kry94y2y2", "checkio101"], 'fizxzbuzzisx89xzxz'],
        [encode, ["How are you?", "hello"], 'ea2imb1ht0'],
        [decode, ["ea2imb1ht0", "hello"], 'howareyouz'],
        [encode, ["My name is Alex!!!", "alexander"], 'i1dlkxjqlexn'],
        [decode, ["i1dlkxjqlexn", "alexander"], 'mynameisalex'],
        [encode, ["Who are you?", "human"], 'rnvftc1jd5'],
        [decode, ["rnvftc1jd5", "human"], 'whoareyouz'],
        [encode, ["ATTACK AT DAWN", "general"], 'ewwektewhnua'],
        [decode, ["ewwektewhnua", "general"], 'attackatdawn'],
    ]

    ENCODE_TESTS = [
        [
            encode,
            [
                "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country",
                "42",
            ],
            'g2xl2s4yg64hijpbznk3luapu0tzcgmtg2xlulnsifiutousjftqpl2mgcbm4dpoummbtzgcznfqfkjuhqif2nhobvfwutqgmds2qhbvifxmjufjthl0plsgqlymulqjufhisbrzzni4mctulizngqgkbmuhau2m2shfm2mhschfuig4mbys2mrxjufqmbkg21cv4jlhmpyqazznfjvlm24ibmavvokmjfugqzhunzifkh4iryygsxqfhfof2mgchugudm2sb4gugkbsoiiutousz0',
        ],
        [
            encode,
            [
                "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa.",
                "checkio",
            ],
            'rcnoqhlvtnjerclxhwblhuhclukhuhuvonbfkqcwhoqdcnhwdcuddlhcrtrhjeqcdwslidhujercljducdpnlyyl',
        ],
        [
            encode,
            [
                "One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a horrible vermin. He lay on his armour-like back, and if he lifted his head a little he could see his brown belly, slightly domed and divided by arches into stiff sections. The bedding was hardly able to cover it and seemed ready to slide off any moment.",
                "goodmorming",
            ],
            'gacrdifghnspfaoinrditngvetdjfnidovid0kpciumifbgvpnaisbgkgrwnqcwobaxndircmghsgxcfmgasajjgiwigckcwperghscpnzgaqgtnirdtmpdqfcbejbbgfqpnqmaxbrqgysfbobqmusvjnpfedtkmwnnpgxedrtaccph1vhgojsh1mdrcobbgmgxmrbbkznmepnxgasgtxoq3nxfexogatupncfiumghnteyseomkznckawmamtpeoxbagufwcrbrepbozsgtqmrbianbh4rdrcas',
        ],
        [
            encode,
            ["The quick, brown fox jumps over a lazy dog.", "nobody"],
            'vfikwgejntasbcnzmrpqzeshwnqb2oybe1',
        ],
        [
            encode,
            [
                "A wonderful serenity has taken possession of my entire soul, like these sweet mornings of spring which I enjoy with my whole heart. I am alone, and feel the charm of existence in this spot, which was created for the bliss of souls like mine. I am so happy, my dear friend, so absorbed in the exquisite sense of mere tranquil existence, that I neglect my talents. I should be incapable of drawing a single stroke at the present moment; and yet I feel that I never was a greater artist than now. When, while the lovely valley teems with vapour around me, and the meridian sun strikes the upper surface of the impenetrable foliage of my trees, and but a few stray gleams steal into the inner sanctuary",
                "xyzqwerty",
            ],
            'czpokdfl4u3ddxohgtnhmddhzssple3dleokpolivtzsbgdxlp4uofsdagd3d3exydnpalhokmlilsbfmhzjjbijzsipzegbgnzeinsxkzbtbgtnrnpozdsakxxsagwdnhtllixykodypaqkmaijlelsmbzjjbjzdndtzddyrklbagqdoflelpkll1mlofsdogszhbnlnicnmwvtkdbtlfkqsalpbclptcdkhoagxyxyx1kogbd3zs3dlisydxath0x1foxykodypaydnhbgszfmwdgvtgrnzsdmkoin4urcqkpacnbcsxlirtczhohtokmhsxmdblsdbaagwsdx3dmanpsymah0teydjgxyxsagbahoy3xdzcndftzddytbtakoryagh0opeyzjzszjfoydkzmp3ymx0tursxtgxyyspegbg0cnl1tbbl0ltszdsaagysxdkbhbol0lmdbfsdmdkz2lswdl4fhrdwliagqknszsydtbroxkpmhbkylivtatxyd3h0rcvrrhxemdtbtmsxtnlemdzdofmambkzhoszdlh0da0rtx',
        ],
        [
            encode,
            [
                "But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure",
                "nobody",
            ],
            'dtwfu1tuczqmiqbrbadsey3ij0t0icukewwbskacognbgbcodscjcahmkfowvsiooyjviqwedcqyca3itonsonoyq3fqmfhwhodsnidkqmfsioj4enrdsbl0ifvotugknoog2jdsoyvfiofrwdt0ioeicaeubevffhscbwczqmnscsbevffssvvfvfgkowsftnwgmbcsbegvqdycyqqhocrzronzbocsckfeutagtkeqkznsywaeouqmiotvscfwzktlofinvtfcwfvkkfowvsfovuofinvtfseyzkvibybobsjoaseyruykvstvhkkfowvscsbweaonj0pbcoenrdsfxjbozkmwcoeftuiywbscczusgkfkhviqbctmobwnidcaewvfcsiooaboiseykbshzevjvstvkznsogwesctunzbdwbcaqycabefwzktlofinvtfcwfvkiqodvuofinvtkej4inwebobqpbecxj1utunoefzej4grwcariceisbfqnoymiqcjnojvnevsfigqzekgcuiovlkfowvsk5',
        ],
        [
            encode,
            [
                "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country",
                "data",
            ],
            'gdyldscsdzcdijlthncxlvalnvuhbgmugdylvlnaktbp0udukbuwqidmgbtmaepovmmtuhgbhndxdqo1dbktdohoabk3auxamcsdbdabkt4ro1bkotqvqisgxfzmvlxbvfhibteuhndembualihnaxaqtmbhawdmdskamdmhstkapbdtmtzsdmryo1dxmtqaertradlhmpxud1hnbkwlmdedtmarwnqmkbvgcuhbnhktqtedurzgy4xdkaofdmgbhbgvcmdstagvaqtbjbbp0uduz0',
        ],
        [
            encode,
            [
                "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa.",
                "goodmorming",
            ],
            'jmeprghwvdmdjmgwoxcoawamhyfewauvpeborqgxfmhncpoxbfafbaamivrdmdqmdsjcnrawmdjmoefafbcgnttn',
        ],
        [
            encode,
            [
                "One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a horrible vermin. He lay on his armour-like back, and if he lifted his head a little he could see his brown belly, slightly domed and divided by arches into stiff sections. The bedding was hardly able to cover it and seemed ready to slide off any moment.",
                "iddqd",
            ],
            'poflpllqunvjglknfhplviltbvrhfglptzlpwqslctcmhiltjfhm0uafdlylmexmqotepllfqdogeyijqdmuvhovx3lciphsklldoglsi1poeavilnnvlmcejibihcmqdejfsemzfieavehiqbseussmfjkinvmiylfjeycppvpqlss4ysqefvs4amlfqbmqqdsaifqc1ixkjfyemulvsdktetkisdpotujfijctqdunvbvecoim1iipfsrav1kldsqoitksflfilkbqzslvseifmhhdl0nplfmu',
        ],
        [
            encode,
            ["The quick, brown fox jumps over a lazy dog.", "iddqd"],
            'vfgisqkrcppvmgrvgwnrvlshocoi0zamf0',
        ],
        [
            encode,
            [
                "A wonderful serenity has taken possession of my entire soul, like these sweet mornings of spring which I enjoy with my whole heart. I am alone, and feel the charm of existence in this spot, which was created for the bliss of souls like mine. I am so happy, my dear friend, so absorbed in the exquisite sense of mere tranquil existence, that I neglect my talents. I should be incapable of drawing a single stroke at the present moment; and yet I feel that I never was a greater artist than now. When, while the lovely valley teems with vapour around me, and the meridian sun strikes the upper surface of the impenetrable foliage of my trees, and but a few stray gleams steal into the inner sanctuary",
                "9876543210",
            ],
            '1ytiefxlxiqgqfijszgbto1mhkqpryqgryomtircs5hkonqftpximjqkzngqgq7khqistljimyrctqolmhzeoicnhkipzxnognzxctkfcf0songs0mtig1jhgffkznfdgbslrcfwmoqhihcktzcnrytqpozeoiezgyfog1qhegpsznh1mjrytpgru9mrmjqknjkhm3sytc2ssvs5ef0slxkcjhtpb3tpt0fejiznfwfwowmonogqhkqgrckgqfosbmowjmfwmoqhihhqgbonkhfmfdsnzs0mhkotmoctxih2ckih2sb3kfrcfp1yjimgommhkftospqkbszndqqfqgtziskgtzbmgvhqlcfwfkznbsjidwfqy1ygfsg1qhs0somorzznbmitxyzehkzejmhqcfirwdmxy2r6kfzsfwgkqynodz2su9s0spzigjg1jhzngkfqjcm3mtzitoolqktocfvoqdstxog0dfrcznckjshkhqs00nfgrim3hfrcs5osfwgqbmh2zo0gk7tos05mkfgsrytog1mjtzpocfjikhstbmhoy3sx',
        ],
        [
            encode,
            [
                "But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure",
                "xyzqwerty",
            ],
            'r1bglvmdxysmbhmamql1inzcurmrijlnkoabsdohkdbnkrzsl1pahojmsxdn4fzdsalcbhokmhnchozcodlb0hsajqfomfg1xzl1bdpnsmydzdrwbp0lbmgrkzmemdysh0kdwll1saagzdda0rmrzdajhokmliagykdxbaxysmlbxdliagydf4agagysdndytc1fsrxdlif0nt0ncnojszlelolqpoxdwkwddmbklmjfd3lbt01ok3smzdl3dxgb3duldqdb3lqkbglssxdn4fqdvrdqdb3lydin3dzjsbpombhspqinycps4fl3wssxdn4fxdbao10hurmxzsbp0ldytdpo3dx1zsdwmdnhabdxxyatysxswmbhlh4uoptbhthokoagxdzdmzpoxeinmp3ylpcl4fl3d3lbkdokdxmdlq1iabhoncholigb3duldqdb3lqkbglsbhoavrdqdb3lqsrwdbokpornmxbjtdvlmdh0dwlprwr2bfpzijajbmfoh0csbhpah0lcpb4fzkgolpsyftzdcmsxdn4fxq',
        ],
    ]

    DECODE_TESTS = [
        [
            decode,
            [
                "gdyldscsdzcdijlthncxlvalnvuhbgmugdylvlnaktbp0udukbuwqidmgbtmaepovmmtuhgbhndxdqo1dbktdohoabk3auxamcsdbdabkt4ro1bkotqvqisgxfzmvlxbvfhibteuhndembualihnaxaqtmbhawdmdskamdmhstkapbdtmtzsdmryo1dxmtqaertradlhmpxud1hnbkwlmdedtmarwnqmkbvgcuhbnhktqtedurzgy4xdkaofdmgbhbgvcmdstagvaqtbjbbp0uduz0",
                "data",
            ],
            'farfarawaybehindthewordmountainsfarfromthecountriesvokaliaandconsonantiatherelivetheblindtextsseparatedtheyliveinboxokmarksgroverightatxthecoastofthesemanticsalargelanguageoceanasmallrivernamedxdudenflowsbytheirplaceandsuppliesitwiththenecesxsaryregelialiaitisaparadisematiccountryz',
        ],
        [
            decode,
            [
                "jmeprghwvdmdjmgwoxcoawamhyfewauvpeborqgxfmhncpoxbfafbaamivrdmdqmdsjcnrawmdjmoefafbcgnttn",
                "goodmorming",
            ],
            'loremipsumdolorsitametconsectetueradipiscingelitaeneancomxmodoligulaegetdoloraeneanmassa',
        ],
        [
            decode,
            [
                "poflpllqunvjglknfhplviltbvrhfglptzlpwqslctcmhiltjfhm0uafdlylmexmqotepllfqdogeyijqdmuvhovx3lciphsklldoglsi1poeavilnnvlmcejibihcmqdejfsemzfieavehiqbseussmfjkinvmiylfjeycppvpqlss4ysqefvs4amlfqbmqqdsaifqc1ixkjfyemulvsdktetkisdpotujfijctqdunvbvecoim1iipfsrav1kldsqoitksflfilkbqzslvseifmhhdl0nplfmu",
                "iddqd",
            ],
            'onemorningwhengregorsamsawokefromtroubledxdreamshefoundhimselftransformedinhisbedintoahorxribleverminhelayonhisarmourlikebackandifheliftedhisheadalitxtlehecouldseehisbrownbellyslightlydomedanddividedbyarchesintostifxfsectionsthebedxdingwashardlyabletocoveritandsexemedreadytoslideoffanymoment',
        ],
        [
            decode,
            ["vfikwgejntasbcnzmrpqzeshwnqb2oybe1", "nobody"],
            'thequickbrownfoxjumpsoveralazydogz',
        ],
        [
            decode,
            [
                "1ytiefxlxiqgqfijszgbto1mhkqpryqgryomtircs5hkonqftpximjqkzngqgq7khqistljimyrctqolmhzeoicnhkipzxnognzxctkfcf0songs0mtig1jhgffkznfdgbslrcfwmoqhihcktzcnrytqpozeoiezgyfog1qhegpsznh1mjrytpgru9mrmjqknjkhm3sytc2ssvs5ef0slxkcjhtpb3tpt0fejiznfwfwowmonogqhkqgrckgqfosbmowjmfwmoqhihhqgbonkhfmfdsnzs0mhkotmoctxih2ckih2sb3kfrcfp1yjimgommhkftospqkbszndqqfqgtziskgtzbmgvhqlcfwfkznbsjidwfqy1ygfsg1qhs0somorzznbmitxyzehkzejmhqcfirwdmxy2r6kfzsfwgkqynodz2su9s0spzigjg1jhzngkfqjcm3mtzitoolqktocfvoqdstxog0dfrcznckjshkhqs00nfgrim3hfrcs5osfwgqbmh2zo0gk7tos05mkfgsrytog1mjtzpocfjikhstbmhoy3sx",
                "9876543210",
            ],
            'awonderfulserenityhastakenposxsesxsionofmyentiresoullikethesesweetmorningsofspringwhichienjoywithmywholeheartiamaloneandfeelthecharmofexistenceinthisxspotwhichwascreatedfortheblisxsofsoulslikemineiamsohappymydearfriendsoabsorbedinthexexquisitesenseofmeretranquilexistencethatineglectmytalentsishouldbeincapableofdrawingasinglestrokeatthepresentmomentandyetifexelthatineverwasagreaterartistxthannowxwhenwhilethelovelyvalxleytexemswithvapouraroundmeandthemeridiansunstrikestheuppersurfaceoftheimpenetrablefoliageofmytrexesandbutafewstraygleamsxstealintotheinnersanctuary',
        ],
        [
            decode,
            [
                "r1bglvmdxysmbhmamql1inzcurmrijlnkoabsdohkdbnkrzsl1pahojmsxdn4fzdsalcbhokmhnchozcodlb0hsajqfomfg1xzl1bdpnsmydzdrwbp0lbmgrkzmemdysh0kdwll1saagzdda0rmrzdajhokmliagykdxbaxysmlbxdliagydf4agagysdndytc1fsrxdlif0nt0ncnojszlelolqpoxdwkwddmbklmjfd3lbt01ok3smzdl3dxgb3duldqdb3lqkbglssxdn4fqdvrdqdb3lydin3dzjsbpombhspqinycps4fl3wssxdn4fxdbao10hurmxzsbp0ldytdpo3dx1zsdwmdnhabdxxyatysxswmbhlh4uoptbhthokoagxdzdmzpoxeinmp3ylpcl4fl3d3lbkdokdxmdlq1iabhoncholigb3duldqdb3lqkbglsbhoavrdqdb3lqsrwdbokpornmxbjtdvlmdh0dwlprwr2bfpzijajbmfoh0csbhpah0lcpb4fzkgolpsyftzdcmsxdn4fxq",
                "xyzqwerty",
            ],
            'butimustexplaintoyouhowalxlthismistakenideaofdenouncingpleasureandpraisingpainwasbornandiwillgiveyouacompleteacxcountofthesystemandexpoundtheactualteachingsofthegreatexplorerofthetruththemasterbuilderofhumanhappinesxsnoxonerejectsdislikesoravoidspleasureitselfbecauseitispleasurebutbecausethosewhodonotknowhowtopursuepleasurerationalxlyencounterconsequencesthatareextremelypainfulnoragainisthereanyonewholovesorpursuesordesirestoxobtainpainofitselfbecauseitispainbutbecauseocxcasionallycircumstancesocxcurinwhichtoilandpaincanprocurehimsomegreatpleasurez',
        ],
        [
            decode,
            [
                "hrflbtcztzdqijsaagxelbtsl1mabholhrflblvgkzbp0latkqm3sirnhbh0rdpolp0hmahbagxdxsg1ydkzrohoraxydm3dnctbdyrakzxmg1qkoalqsintdfmkbl3ybfhiabryagwdnbmdliagd3ysh0bgdprnbtkynrmh0rkypbzd0hlnrnufg1xd0hsyrer3kdlhmpeptqagqkclnrdwh0k32lsmkqokcygbgakzszdwlendtxdxkyofrnhbgbkocnbtbrkoysbajbbp0latzq",
                "xyzqwerty",
            ],
            'farfarawaybehindthewordmountainsfarfromthecountriesvokaliaandconsonantiatherelivetheblindtextsseparatedtheyliveinboxokmarksgroverightatxthecoastofthesemanticsalargelanguageoceanasmallrivernamedxdudenflowsbytheirplaceandsuppliesitwiththenecesxsaryregelialiaitisaparadisematiccountryz',
        ],
        [
            decode,
            [
                "irqfnjqtyicpirstnogshqiumtfdqhozfq2gjomoiomhfkno1gkhbmiulyiscpmjcym0fhhqcpirs0hkg1ingyyg",
                "9876543210",
            ],
            'loremipsumdolorsitametconsectetueradipiscingelitaeneancomxmodoligulaegetdoloraeneanmassa',
        ],
        [
            decode,
            [
                "bogknsacdcvicocufhnswokui3esfgsnlusntdkfn1nuiokuifebrdyggqzktlusnotenskgagycewofagbrbneyx4wcfthscsqgycfknaboicwoujdstjeqfoniqooycgifqfl0goicveioynqfr00tfifedsmbzkfiewntasodfkpbtkchfvpbybkgynoyagwhogydanxjifwebrezwfc0etfewfbotuifofn1agdc3ivenwbmanftfsneyscsfwnoouczgkgoscnybvezqfogbeiboakdkgbr",
                "nobody",
            ],
            'onemorningwhengregorsamsawokefromtroubledxdreamshefoundhimselftransformedinhisbedintoahorxribleverminhelayonhisarmourlikebackandifheliftedhisheadalitxtlehecouldseehisbrownbellyslightlydomedanddividedbyarchesintostifxfsectionsthebedxdingwashardlyabletocoveritandsexemedreadytoslideoffanymoment',
        ],
        [
            decode,
            ["vfgisqkrcppvmgrvgwnrvlshocoi0zamf0", "iddqd"],
            'thequickbrownfoxjumpsoveralazydogz',
        ],
        [
            decode,
            [
                "etgarbievkwnepfgszjntubjfajrtswntsxggaiag1faxoeptgvkqmpbsjnwnw2pawrdgegfnyiawhighnspmfqgfata2soxlg2sjgpcpneoxococjgafbbgnfcpsjfejniriafwgxwaaefrasqgtswhazspmfpsntemfbwaibdisjfcqmtstgnxdthvqmpbrgafofgvgjejh2g1rbeoeirfbgtgbctgdebrgfsjfwfwkxgxoxnwfawniarcepwobakxmqfwgxwaaeawjnxoafmhfevozscjfautgxjgvkbkfraeejbcpciamietgfonxghnpctuidpbjzsjpwepwnasrdrcasbag0awfqfwcpsjjzgfcwpetetnoifbwaoeowgxussjbaagxsspfaspmqawpnjmwch1tcqvpczsfwcrtxoxlsejdtoeidsbmrfbbgsjcrpegmofhysbtuigpbtupnwkwpgwwdnbefiasjfrrlfaawoeckfnmjofrniag1wofwnwbabkvubnp2tuoe4npccotstufbqmasazpngfafgwbaavtbg2",
                "goodmorming",
            ],
            'awonderfulserenityhastakenposxsesxsionofmyentiresoullikethesesweetmorningsofspringwhichienjoywithmywholeheartiamaloneandfeelthecharmofexistenceinthisxspotwhichwascreatedfortheblisxsofsoulslikemineiamsohappymydearfriendsoabsorbedinthexexquisitesenseofmeretranquilexistencethatineglectmytalentsishouldbeincapableofdrawingasinglestrokeatthepresentmomentandyetifexelthatineverwasagreaterartistxthannowxwhenwhilethelovelyvalxleytexemswithvapouraroundmeandthemeridiansunstrikestheuppersurfaceoftheimpenetrablefoliageofmytrexesandbutafewstraygleamsxstealintotheinnersanctuary',
        ],
        [
            decode,
            [
                "tvbhnsuak3qmbguhl1nvinscqrndijzsgvbtqkohadbmlftqnvpthojmqdgzvsdtltlwbgvgmhmchoscvalvmtltjvfomfo1d3nvtepnqmdbdtewbp0ubnhdktrzuaaqtmadwqnvlthndtebstnddttjhomzlihnakxdtbk3qmlvdxlihndbsvhnhnaqgzbdvdvhrfdxlin0sguncmojqturumqvpodxckdeaubfrmjfaxlvbsvoarqmdtuvxdhbxarlcdetvubkbhwmqdgzvsdc0hcdetvudbinxaujlbponbhqpvinucpqvsuvcqqdgzvsdxtbovmtqrr4tqbp0ubdwdpoxanxtqeduagtbtxdk3duaqdq2lbglhrnopsdmghogvhndxdtl0pocxinmpxbvmwlvsuvaxlvadvgxduaqvvibthomcholihbxarlcdetvubkbhwmbgot0hcdetvubqewetvgpodmr4bjwdsnuatmedvmewtwvfpuijtjbnfotmclbgpttmlwpbvstkgovmqafsdtcnqdgzvsa3",
                "data",
            ],
            'butimustexplaintoyouhowalxlthismistakenideaofdenouncingpleasureandpraisingpainwasbornandiwillgiveyouacompleteacxcountofthesystemandexpoundtheactualteachingsofthegreatexplorerofthetruththemasterbuilderofhumanhappinesxsnoxonerejectsdislikesoravoidspleasureitselfbecauseitispleasurebutbecausethosewhodonotknowhowtopursuepleasurerationalxlyencounterconsequencesthatareextremelypainfulnoragainisthereanyonewholovesorpursuesordesirestoxobtainpainofitselfbecauseitispainbutbecauseocxcasionallycircumstancesocxcurinwhichtoilandpaincanprocurehimsomegreatpleasurez',
        ],
    ]

    def test_Basics(self):
        for i in self.BASIC_TESTS:
            assert i[0](*i[1]) == i[2]

    def test_Encode(self):
        for i in self.ENCODE_TESTS:
            assert i[0](*i[1]) == i[2]

    def test_Decode(self):
        for i in self.DECODE_TESTS:
            assert i[0](*i[1]) == i[2]

    def test_Random(self):
        for _ in range(5):
            length = random.randint(10, 18) * 2
            list_message = list(string.ascii_lowercase + string.digits)
            random.shuffle(list_message)
            message = "".join(list_message[:length])
            key = "".join(random.choice(string.ascii_lowercase) for __ in range(6))
            assert decode(encode(message, key), key) == message


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
