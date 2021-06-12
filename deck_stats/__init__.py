from aqt.deckbrowser import DeckBrowser
from anki.lang import _
from anki.hooks import wrap
from aqt import mw

# Replace _renderStats method
def renderStats(self, _old):
    due = new = 0
    for tree in self.mw.col.sched.deckDueTree():
        due += tree[2] + tree[3]
        new += tree[4]

    # Setup data to print
    return _("Due") + ": <font color=#0a0> %(c)s </font>" % dict(c=due) \
        + _("New") + ": <font color=#00a> %(d)s </font> " % dict(d=new) \
        + "<br /> " \
        + _old(self)

DeckBrowser._renderStats = wrap(
    DeckBrowser._renderStats, renderStats, "around")
