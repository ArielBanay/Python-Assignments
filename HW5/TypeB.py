from Angry import Angry
from Explosive import Explosive
from Furious import Furious
from Personality import Personality
from Calm import Calm
from Chill import Chill

class TypeB(Personality):
    def adjust_mood(self,mood,waiting_time):
        if waiting_time>120 and isinstance(mood,Furious):
            return Explosive()
        elif waiting_time>90 and isinstance(mood,Angry):
            return Furious()
        elif waiting_time>60 and isinstance(mood,Calm):
            return Angry()
        elif waiting_time>40 and isinstance(mood,Chill):
            return Calm()
        return mood

    def __repr__(self):
        return "TypeB"