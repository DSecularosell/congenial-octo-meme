"""
Just messing around
"""
attribs = {
    'Valiance' : 'Your ability to withstand demoralization and deathblows. Increases will-to-live',
    'Condition' : 'The strength of you heart and lungs and their ability to work in extreme conditions. Increases will-to-act',
    'Ingenuity' : 'How quickly you can devise solutions to imminent problems. Increases chance of critical rolls',
    'Stability' : 'Balance, control, precision. Not only in body, but in mind. Increases will-to-fight',
    'Communion' : 'Your connection to "other" things. Affects many things, most unseen'

}


class player(object):
    def __init__(self, name, lvl,  val, cond, ing, stab, comm, wtl, wta, wtf):
        player.self = self
        player.name = name
        player.lvl = lvl
        player.val = val
        player.cond = cond
        player.ing = ing
        player.stab = stab
        player.comm = comm
        player.wtl = wtl
        player.wta = wta
        player.wtf = wtf

p_c = player('Dakota', 0, 3, 3, 3, 3, 3, 100, 20, 20)
print(p_c.wtl)