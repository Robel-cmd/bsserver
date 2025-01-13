# ba_meta require api 7
# By: zeenppay
import ba
from bastd.actor.spaz import Spaz
from bastd.actor.spazfactory import SpazFactory

turboSpamming = True 

def on_punch_press(self) -> None:
    """
    Called to 'press punch' on this spaz;
    used for player or AI connections.
    """
    if not self.node or self.frozen or self.node.knockout > 0.0:
        return
    t_ms = int(ba.time() * 800.0)
    assert isinstance(t_ms, int)
    self._punched_nodes = set()  # Reset this.
    if t_ms - self.last_punch_time_ms > self._punch_cooldown:
        if self.punch_callback is not None:
            self.punch_callback(self)
        self.last_punch_time_ms = t_ms
        self.node.punch_pressed = True
        if not self.node.hold_node:
            ba.timer(
                0.1,
                ba.WeakCall(
                    self._safe_play_sound,
                    SpazFactory.get().swish_sound,
                    0.8,
                ),
            )
    

def enable():
	Spaz.on_punch_press = on_punch_press

enable()