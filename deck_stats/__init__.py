from aqt.deckbrowser import DeckBrowser
from anki.lang import _
from anki.hooks import wrap
from aqt import mw

# Replace _renderStats method
def renderStats(self, _old):
    # Count number of cards that match each search term
    query = mw.col.build_search_string("is:due")
    due = len(mw.col.find_cards(query))
    query = mw.col.build_search_string("is:new")
    new = len(mw.col.find_cards(query))

    # Setup data to print
    return _("Due") + ": <font color=#0a0> %(c)s </font>" % dict(c=due) \
        + _("New") + ": <font color=#00a> %(d)s </font> " % dict(d=new) \
        + "<br /> " \
        + _old(self)

DeckBrowser._renderStats = wrap(
    DeckBrowser._renderStats, renderStats, "around")