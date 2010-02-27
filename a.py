print "***\n*** reading conf\n***"

global tonic
tonic = G


def myhighlight(x):
    print "hl", x
    if x in [tonic, tonic+4, tonic+7, tonic+10]:
        return QtCore.Qt.red
    return None

global highlight
highlight = myhighlight

Notemodule.use_numbers(tonic.value)



