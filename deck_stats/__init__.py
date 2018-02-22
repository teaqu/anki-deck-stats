from aqt.deckbrowser import DeckBrowser
from anki.utils import fmtTimeSpan

# Replace _renderStats method
def renderStats(self):
    # Get data from deck tree
    due = new = 0
    for tree in self.mw.col.sched.deckDueTree():
        due += tree[2] + tree[3]
        new += tree[4]

    # Get studdied cards
    cards, thetime = self.mw.col.db.first(
        """select count(), sum(time)/1000 from revlog where id > ?""",
        (self.mw.col.sched.dayCutoff - 86400) * 1000)
    cards = cards or 0
    thetime = thetime or 0

    # Setup data to print
    msgp1 = ngettext("<!--studied-->%d card", "<!--studied-->%d cards", cards) % cards
    buf = _("Due") + ": <font color=#0a0> %(c)s </font>" % dict(c=due) \
        + _("New") + ": <font color=#00a> %(d)s </font> " % dict(d=new) \
        + "<br /> " \
        + _("Studied %(a)s in %(b)s today.") \
        % dict(a=msgp1, b=fmtTimeSpan(thetime, unit=1))

    return buf

DeckBrowser._renderStats = renderStats
