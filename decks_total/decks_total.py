# Author: C9HDN

# Get DeckBrowser class
from aqt.deckbrowser import DeckBrowser

# Get language class
import anki.lang

import os

# Import for trnasnlating
import gettext

# Get fmtTimeSpan required for renderStats method
from anki.utils import fmtTimeSpan

# Replace _renderStats method
def renderStats(self):
    if os.path.isdir("../../addons/decks_total/locale/" + anki.lang.getLang()):
        lang = anki.lang.getLang()
    else:
        lang = "en"

    t = gettext.translation('defualt', '../../addons/decks_total/locale', [lang])
    translate_ = t.ugettext

    # Get due and new cards
    due = 0
    new = 0

    for tree in self.mw.col.sched.deckDueTree():
        due += tree[2] + tree[3]
        new += tree[4]

    # Get studdied cards
    cards, thetime = self.mw.col.db.first(
            """select count(), sum(time)/1000 from revlog where id > ?""",
            (self.mw.col.sched.dayCutoff - 86400) * 1000)

    cards = cards or 0
    thetime = thetime or 0
    
    msgp1 = ngettext("%d card", "%d cards", cards) % cards
    
    # Setup data to print
    buf = _("Due") + ": <font color=#0a0> %(c)s </font>" % dict(c=due) \
        + translate_("reviews") + ", <font color=#00a> %(d)s </font> " % dict(d=new) \
        + translate_("new cards") + " <br /> " + _("Studied %(a)s in %(b)s today.") \
        % dict(a=msgp1, b=fmtTimeSpan(thetime, unit=1))
    
    return buf

DeckBrowser._renderStats = renderStats
