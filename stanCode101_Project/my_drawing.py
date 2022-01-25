"""
File: my_drawing.py
Name: Anthony Ning
----------------------
The program draws pictures.
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GLabel, GLine
from campy.graphics.gwindow import GWindow


def main():
    """
    The anime, Naruto, is the inspiration.
    Further, inspired by the Uchiha clan and the Akatsuki org., I drew the picture.
    Between the Uchiha's symbol and the Akatsuki's, there is a peace sign,
    which I hope and believe they can bring peace to the world.
    """
    window = GWindow(width=800, title="Anthony's drawing")

    arc = GArc(175, 250, 330, 240)
    arc.filled = True
    arc.fill_color = 'firebrick'
    arc.color = 'firebrick'
    window.add(arc, x=150, y=150)

    rec = GRect(30, 120)
    rec.filled = True
    rec.fill_color = 'white'
    window.add(rec, x=225, y=300)

    arc_2 = GArc(200, 300, 220, 100)
    arc_2.filled = True
    arc_2.fill_color = 'white'
    window.add(arc_2, x=163, y=185)

    label = GLabel('The Uchiha Clan')
    label.font = '-20'
    window.add(label, x=170, y=100)

    oval_1 = GOval(60, 60)
    oval_1.filled = True
    oval_1.fill_color = 'firebrick'
    oval_1.color = 'firebrick'
    window.add(oval_1, x=520, y=250)

    oval_2 = GOval(70, 70)
    oval_2.filled = True
    oval_2.fill_color = 'firebrick'
    oval_2.color = 'firebrick'
    window.add(oval_2, x=550, y=200)

    oval_3 = GOval(60, 60)
    oval_3.filled = True
    oval_3.fill_color = 'firebrick'
    oval_3.color = 'firebrick'
    window.add(oval_3, x=515, y=220)

    oval_4 = GOval(80, 80)
    oval_4.filled = True
    oval_4.fill_color = 'firebrick'
    oval_4.color = 'firebrick'
    window.add(oval_4, x=560, y=235)

    oval_5 = GOval(80, 80)
    oval_5.filled = True
    oval_5.fill_color = 'firebrick'
    oval_5.color = 'firebrick'
    window.add(oval_5, x=580, y=210)

    oval_6 = GOval(50, 50)
    oval_6.filled = True
    oval_6.fill_color = 'firebrick'
    oval_6.color = 'firebrick'
    window.add(oval_6, x=495, y=235)

    arc_3 = GArc(40, 40, 50, 250)
    arc_3.color = 'white'
    window.add(arc_3, x=615, y=249)

    arc_4 = GArc(30, 40, 145, 220)
    arc_4.color = 'white'
    window.add(arc_4, x=550, y=213)

    arc_5 = GArc(45, 55, 10, 180)
    arc_5.color = 'white'
    window.add(arc_5, x=519, y=267)

    label_1 = GLabel('Akatsuki')
    label_1.font = '-20'
    window.add(label_1, x=535, y=100)

    oval_7 = GOval(50, 50)
    window.add(oval_7, x=400, y=235)

    line = GLine(425, 235, 425, 285)
    window.add(line)

    line_1 = GLine(425, 255, 413, 283)
    window.add(line_1)

    line_2 = GLine(425, 255, 437, 283)
    window.add(line_2)


if __name__ == '__main__':
    main()
