from aqt.deckbrowser import DeckBrowser
from anki.lang import _
from anki.hooks import wrap
from aqt import mw

# Replace _renderStats method
def renderStats(self, _old):
    due = new = 0
    nodes = self.mw.col.sched.deck_due_tree().children
    for node in nodes:
        due += node.review_count + node.learn_count
        new += node.new_count

    # Setup data to print
    return _("Due") + ": <font color=#0a0> %(c)s </font>" % dict(c=due) \
        + _("New") + ": <font color=#00a> %(d)s </font> " % dict(d=new) \
        + "<br /> " \
        + _old(self)

DeckBrowser._renderStats = wrap(
    DeckBrowser._renderStats, renderStats, "around")
