# DEFAULT_STYLE = """
# QProgressBar{
#     border: 2px solid grey;
#     border-radius: 5px;
#     text-align: center;
# }
#
# QProgressBar::chunk {
#     background-color: lightblue;
#     width: 10px;
#     margin: 1px;
# }
# QProgressBar::chunk::hover {
#     background-color: blue;
#     width: 10px;
#     margin: 1px;
# }
# """
#
# COMPLETED_STYLE = """
# QProgressBar{
#     border: 2px solid grey;
#     border-radius: 5px;
#     text-align: center;
# }
#
# QProgressBar::chunk {
#     background-color: red;
#     width: 10px;
#     margin: 1px;
# }
# """
# STOP_STYLE = """
# QProgressBar{
#     border: 2px solid grey;
#     border-radius: 5px;
#     text-align: center;
# }
#
# QProgressBar::chunk {
#     background-color: rgb(0, 255, 0);
#     width: 10px;
#     margin: 1px;
# }
# """
# ANOTHER_STYLE = """
# QProgressBar{
#     border: 2px solid grey;
#     border-radius: 5px;
#     text-align: center;
# }
#
# QProgressBar::chunk {
# background: QLinearGradient( x1: 0, y1: 0,
#                              x2: 1, y2: 0,
#                             stop: 0 #000fff,
#                             stop: 1 #ff000f );
# }
# """
# QLCD_STYLES = """QLCDNumber
#                { background-color: #E3DEE2;
#                  color: #3B99FC;
#                }"""


SLIDERS_STYLE_NIGHT = """
            QSlider::groove:horizontal {  
                height: 10px;
                margin: 0px;
                border-radius: 5px;
                background: #B0AEB1;
            }
            QSlider::handle:horizontal {
                background: #fff;
                border: 1px solid #3B99FC;
                width: 17px;
                margin: -5px 0; 
                border-radius: 8px;
            }
            QSlider::sub-page:qlineargradient {
                background: #3B99FC;
                border-radius: 5px;
            }
        """

SLIDERS_STYLE_DAY = """
            QSlider::groove:horizontal {  
                height: 10px;
                margin: 0px;
                border-radius: 5px;
                background: #B0AEB1;
            }
            QSlider::handle:horizontal {
                background: #fff;
                border: 1px solid #3B99FC;
                width: 17px;
                margin: -5px 0; 
                border-radius: 8px;
            }
            QSlider::sub-page:qlineargradient {
                background: #3B99FC;
                border-radius: 5px;
            }
        """

DIAL_STYLES = ("background-color: #ff0000;"
               "font: 9pt \"MS Shell Dlg 2\";\n"
               "color: rgb(255, 255, 255);"
               )

EQUALIZER_NIGHT = ['#0C0786',
                   '#40039C',
                   '#6A00A7',
                   '#8F0DA3',
                   '#B02A8F',
                   '#CA4678',
                   '#E06461',
                   '#F1824C',
                   '#FCA635',
                   '#FCCC25',
                   '#EFF821']

EQUALIZER_DAY = ['#1f34f0',
                 '#1f5af0',
                 '#1f84f0',
                 '#1fa7f0',
                 '#1ff0ec',
                 '#1ff0c3',
                 '#1ff099',
                 '#1ff065',
                 '#1ff031',
                 '#68f01f',
                 '#a0f01f']
