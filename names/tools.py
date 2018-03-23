# -*- coding: utf-8 -*-
"""
SMT ipc7351 naming convention
=============================

P = Pitch for components
X = separate two Body Dimensions (for example Body Height X Body Width X Height)
- = is used to separate the pin quantity.
C = Collapsing Balls (only for BGA)
N = Non-collapsing Balls (only for BGA)

PTH ipc7251 naming convention
=============================

P = Pitch for components with three or more leads
W = Maximum Lead Width or Diameter
L = Body Length for horizontal mounting
D = Body Diameter for round component body
T = Body Thickness for rectangular component body
H = Height for vertically mounted components
Q = Pin Quantity for components with three or more leads
R = Number of Rows for connectors


Here are 2 dictionaries :

key = string which describes the type of component with its prefix
value = 2 values tuple
   1st: string that represents the name format of component
   2nd: a string with all the variables which fill the first string of tuple.
        Those variables are used in the gui which creates the component name.

"""
from model import Model


SMT_COMPONENTS = {
    "BGA      - Ball Grid Array's": ("BGA{}{}{}P{}X{}_{}X{}X{}", "Pin Qty, C or N, Pitch, Ball Columns, Ball Rows, Body Length, Body Width, Height"),
    "BGA      - Ball Grid Array's Dual Pitch": ("BGA{}{}{}X{}P{}X{}_{}X{}X{}", "Pin Qty, C or N, Col Pitch, Row Pitch, Ball Columns, Ball Rows, Body Length, Body Width, Height"),
    "BGAS     - Ball Grid Array's Staggered Pins": ("BGAS{}{}{}P{}X{}_{}X{}X{}", "Pin Qty, C or N, Pitch, Ball Columns, Ball Rows, Body Length, Body Width, Height"),
    "CAPCAV   - Capacitors, Chip, Array, Concave": ("CAPCAV{}P{}X{}X{}-{}", "Pitch, Body Length, Body Width, Height, Pin Qty"),
    "CAPCAF   - Capacitors, Chip, Array, Flat": ("CAPCAF{}P{}X{}X{}-{}", "Pitch, Body Length, Body Width, Height, Pin Qty"),
    "CAPC     - Capacitors, Chip, Non-polarized": ("CAPC{}{}X{}", "Body Length, Body Width, Height"),
    "CAPCP    - Capacitors, Chip, Polarized": ("CAPCP{}{}X{}", "Body Length, Body Width, Height"),
    "CAPCWR   - Capacitors, Chip, Wire Rectangle": ("CAPCWR{}{}X{}", "Body Length, Body Width, Height"),
    "CAPM     - Capacitors, Molded, Non-polarized": ("CAPM{}{}X{}", "Body Length, Body Width, Height"),
    "CAPMP    - Capacitors, Molded, Polarized": ("CAPMP{}{}X{}", "Body Length, Body Width, Height"),
    "CAPAE    - Capacitors, Aluminum Electrolytic": ("CAPAE{}X{}", "Base Body Size, Height"),
    "CFP127P  - Ceramic Flat Packages, 1.27mm Pitch": ("CFP127P{}X{}-{}", "Lead Span Nominal, Height, Pin Qty"),
    "CGA      - Column Grid Array's": ("CGA{}P{}X{}X{}-{}", "Pitch, Number of Pin Columns, Number of Pin Rows, Height, Pin Qty"),
    "XTAL     - Crystals (2 leads)": ("XTAL{}X{}X{}", "Body Length, Body Width, Height"),
    "DIP      - Dual-in-Line Packages (Butt Mount)": ("DIP{}P{}X{}-{}", "Pitch, Lead Span Nominal, Height, Pin Qty"),
    "DFN      - Dual Flat No-lead": ("DFN{}X{}X{}-{}", "Body Length, Body Width, Height, Pin Qty"),
    "DIOC     - Diodes, Chip": ("DIOC{}{}X{}", "Body Length, Body Width, Height"),
    "DIOM     - Diodes, Molded": ("DIOM{}{}X{}", "Body Length, Body Width, Height"),
    "DIOMELF  - Diodes, metal electrode leadless face (MELF)": ("DIOMELF{}{}", "Body Length, Body Diameter"),
    "DIOSC    - Diodes, Side Concave": ("DIOSC{}X{}X{}-{}", "Body Length, Body Width, Height, Pin Qty"),
    "FUSM     - Fuses, Molded": ("FUSM{}{}X{}", "Body Length, Body Width, Height"),
    "INDC     - Inductors, Chip": ("INDC{}{}X{}", "Body Length, Body Width, Height"),
    "INDM     - Inductors, Molded": ("INDM{}{}X{}", "Body Length, Body Width, Height"),
    "INDP     - Inductors, Precision Wire Wound": ("INDP{}{}X{}", "Body Length, Body Width, Height"),
    "INDCAV   - Inductors, Chip, Array, Concave": ("INDCAV{}P{}X{}X{}-{}", "Pitch, Body Length, Body Width, Height, Pin Qty"),
    "INDCAF   - Inductors, Chip, Array, Flat": ("INDCAF{}P{}X{}X{}-{}", "Pitch, Body Length, Body Width, Height, Pin Qty"),
    "LGA      - Land Grid Array, Circular Lead": ("LGA{}C{}P{}X{}_{}X{}X{}", "Pin Qty, Pitch, Pin Columns, Pin Rows, Body Length, Body Width, Height"),
    "LGA      - Land Grid Array, Square Lead": ("LGA{}S{}P{}X{}_{}X{}X{}", "Pin Qty, Pitch, Pin Columns, Pin Rows, Body Length, Body Width, Height"),
    "LGA      - Land Grid Array, Rectangle Lead": ("LGA{}R{}P{}X{}_{}X{}X{}", "Pin Qty, Pitch, Pin Columns, Pin Rows, Body Length, Body Width, Height"),
    "LEDM     - LED, Molded": ("LEDM{}{}X{}", "Body Length, Body Width, Height"),
    "LEDSC    - LED's, Side Concave": ("LEDSC{}X{}X{}-{}", "Body Length, Body Width, Height, Pin Qty"),
    "OSCSC    - Oscillators, Side Concave": ("OSCSC{}P{}X{}X{}-{}", "Pitch, Body Length, Body Width, Height, Pin Qty"),
    "OSCJ     - Oscillators, J-Lead": ("OSCJ{}P{}X{}X{}-{}", "Pitch, Body Length, Body Width, Height, Pin Qty"),
    "OSCL     - Oscillators, L-Bend Lead": ("OSCL{}P{}X{}X{}-{}", "Pitch, Body Length, Body Width, Height, Pin Qty"),
    "OSCCC    - Oscillators, Corner Concave": ("OSCCC{}X{}X{}", "Body Length, Body Width, Height"),
    "PLCC     - Plastic Leaded Chip Carriers": ("PLCC{}P{}X{}X{}-{}", "Pitch, Lead Span L1, Lead Span L2 Nominal, Height, Pin Qty"),
    "PLCCS    - Plastic Leaded Chip Carrier Sockets Square": ("PLCCS{}P{}X{}X{}-{}", "Pitch, Lead Span L1, Lead Span L2 Nominal, Height, Pin Qty"),
    "QFP      - Quad Flat Packages (Pitch = 0.65mm, 0.80mm or 1.00mm; Height > 1.6mm)": ("QFP{}P{}X{}X{}-{}", "Pitch, Lead Span L1, Lead Span L2 Nominal, Height, Pin Qty"),
    "SQFP     - Shrink Quad Flat Packages (Pitch = 0.30mm, 0.40mm or 0.50mm; Height > 1.6mm)": ("SQFP{}P{}X{}X{}-{}", "Pitch, Lead Span L1, Lead Span L2 Nominal, Height, Pin Qty"),
    "TQFP     - Thin Quad Flat Packages (Pitch = 0.65mm or 0.80mm; Height <= 1.6mm)": ("TQFP{}P{}X{}X{}-{}", "Pitch, Lead Span L1, Lead Span L2 Nominal, Height, Pin Qty"),
    "TSQFP    - Thin Shrink Quad Flat Packages (Pitch = 0.30mm, 0.40mm or 0.50mm; Height <= 1.6mm)": ("TSQFP{}P{}X{}X{}-{}", "Pitch, Lead Span L1, Lead Span L2 Nominal, Height, Pin Qty"),
    "CQFP     - Ceramic Quad Flat Packages": ("CQFP{}P{}X{}X{}-{}", "Pitch, Lead Span L1, Lead Span L2 Nominal, Height, Pin Qty"),
    "QFN      - Quad Flat No-lead": ("QFN{}P{}X{}X{}-{}", "Pitch, Body Width, Body Length, Height, Pin Qty + Thermal Pad"),
    "PQFN     - Pull-back Quad Flat No-lead": ("PQFN{}P{}X{}X{}-{}", "Pitch, Body Width, Body Length, Height, Pin Qty + Thermal Pad"),
    "LCC      - Quad Leadless Ceramic Chip Carriers": ("LCC{}P{}X{}X{}-{}", "Pitch, Body Width, Body Length, Height, Pin Qty"),
    "LCCS     - Quad Leadless Ceramic Chip Carriers (Pin 1 on Side)": ("LCCS{}P{}X{}X{}-{}", "Pitch, Body Width, Body Length, Height, Pin Qty"),
    "RESC     - Resistors, Chip": ("RESC{}{}X{}", "Body Length, Body Width, Height"),
    "RESM     - Resistors, Molded": ("RESM{}{}X{}", "Body Length, Body Width, Height"),
    "RESMELF  - Resistors, MELF": ("RESMELF{}{}", "Body Length, Body Diameter"),
    "RESCAV   - Resistors, Chip, Array, Concave": ("RESCAV{}P{}X{}X{}-{}", "Pitch, Body Length, Body Width, Height, Pin Qty"),
    "RESCAXE  - Resistors, Chip, Array, Convex, E-Version (Even Pin Size)": ("RESCAXE{}P{}X{}X{}-{}", "Pitch, Body Length, Body Width, Height, Pin Qty"),
    "RESCAXS  - Resistors, Chip, Array, Convex, S-Version (Side Pins Diff)": ("RESCAXS{}P{}X{}X{}-{}", "Pitch, Body Length, Body Width, Height, Pin Qty"),
    "RESCAF   - Resistors, Chip, Array, Flat": ("RESCAF{}P{}X{}X{}-{}", "Pitch, Body Length, Body Width, Height, Pin Qty"),
    "SODFL    - Small Outline Diodes, Flat Lead": ("SODFL{}{}X{}", "Lead Span Nominal, Body Width, Height"),
    "SOJ      - Small Outline IC, J-Leaded": ("SOJ{}P{}X{}-{}", "Pitch, Lead Span Nominal, Height, Pin Qty"),
    "SOIC127P - Small Outline Integrated Circuit, (50 mil (1.27mm) Pitch SOIC)": ("SOIC127P{}X{}-{}", "Lead Span Nominal, Height, Pin Qty"),
    "SOP      - Small Outline Packages (Pitch = 0.635mm, 0.65mm, 0.80mm, 1.00mm or 1.27mm; Height > 1.6mm)": ("SOP{}P{}X{}-{}", "Pitch, Lead Span Nominal, Height, Pin Qty"),
    "SSOP     - Shrink Small Outline Packages (Pitch = 0.30mm, 0.40mm or 0.50mm; Height > 1.6mm)": ("SSOP{}P{}X{}-{}", "Pitch, Lead Span Nominal, Height, Pin Qty"),
    "TSOP     - Thin Small Outline Packages (Pitch = 0.65mm, 0.80mm, 1.00mm or 1.27mm; Height <= 1.6mm)": ("TSOP{}P{}X{}-{}", "Pitch, Lead Span Nominal, Height, Pin Qty"),
    "TSSOP    - Thin Shrink Small Outline Packages (Pitch = 0.30mm, 0.40mm, 0.50mm or 0.55mm; Height <= 1.6mm)": ("TSSOP{}P{}X{}-{}", "Pitch, Lead Span Nominal, Height, Pin Qty"),
    "SON      - Small Outline No-lead": ("SON{}P{}X{}X{}-{}", "Pitch, Body Width, Body Length, Height, Pin Qty + Thermal Pad"),
    "PSON     - Pull-back Small Outline No-lead": ("PSON{}P{}X{}X{}-{}", "Pitch, Body Width, Body Length, Height, Pin Qty + Thermal Pad"),
    "SOTFL    - Small Outline Transistors, Flat Lead": ("SOTFL{}P{}X{}-{}", "Pitch, Lead Span Nominal, Height, Pin Qty"),
    "SOD      - JEDEC": ("SOD{}{}X{}", "Lead Span Nominal, Body Width, Height"),
    "SOT143   - JEDEC Standard Package": ("SOT{}P{}X{}-{}", "Pitch, Lead Span Nominal, Height, Pin Qty"),
    "SOT343   - JEDEC Standard Package": ("SOT{}P{}X{}-{}", "Pitch, Lead Span Nominal, Height, Pin Qty"),
    "SOT143R  - Reverse JEDEC Standard Package": ("SOT{}P{}X{}-{}", "Pitch, Lead Span Nominal, Height, Pin Qty"),
    "SOT343R  - Reverse JEDEC Standard Package": ("SOT{}P{}X{}-{}", "Pitch, Lead Span Nominal, Height, Pin Qty"),
    "SOT23    - SOT23 Packages": ("SOT{}P{}X{}-{}", "Pitch, Lead Span Nominal, Height, Pin Qty"),
    "SOT223   - SOT223 Packages": ("SOT{}P{}X{}-{}", "Pitch, Lead Span Nominal, Height, Pin Qty"),
    "SOT89    - JEDEC Standard Package": ("SOT89", ""),
    "TO       - Generic DPAK, D2PAK": ("TO{}P{}X{}-{}", "Pitch, Lead Span, Height, Pin Qty"),
                }

# Dictionary
# k: v
# type_of_component_string: tuple(string_to_format_with_commented_values,
#                                 string_format_arguments)

PTH_COMPONENTS = {
    "CAPADH   - Capacitors, Non Polarized Axial Diameter Horizontal Mounting": ("CAPADH{}W{}L{}D{}", "Lead Spacing, Lead Width, Body Length, Body Diameter"),
    "CAPADV   - Capacitors, Non Polarized Axial Diameter Vertical Mounting": ("CAPADV{}W{}L{}D{}", "Lead Spacing, Lead Width, Body Length, Body Diameter"),
    "CAPARH   - Capacitors, Non Polarized Axial Rect. Horizontal Mounting": ("CAPARH{}W{}L{}T{}H{}", "Lead Spacing, Lead Width, Body Length, Body thickness, Body Height"),
    "CAPARV   - Capacitors, Non Polarized Axial Rect. Vertical Mounting": ("CAPARV{}W{}L{}T{}H{}", "Lead Spacing, Lead Width, Body Length, Body Thickness, Body Height"),
    "CAPRD    - Capacitors, Non Polarized Radial Diameter": ("CAPRD{}W{}D{}H{}", "Lead Spacing, Lead Width, Body Diameter, Body Height"),
    "CAPRRV   - Capacitors, Non Polarized Radial Rect. Vertical Mounting": ("CAPRRV{}W{}L{}T{}H{}", "Lead Spacing, Lead Width, Body Length, Body thickness, Body Height"),
    "CAPRB    - Capacitors, Non Polarized Radial Disk Button Vertical Mounting": ("CAPRB{}W{}L{}T{}H{}",  "Lead Spacing, Lead Width, Body Length, Body thickness, Body Height"),
    "CAPPAH   - Capacitors, Polarized Axial Diameter Horizontal Mounting": ("CAPPAH{}W{}L{}D{}", "Lead Spacing, Lead Width, Body Length, Body Diameter"),
    "CAPPRDV  - Capacitors, Polarized Radial Diameter Vertical Mounting": ("CAPPRDV{}W{}D{}H{}V{}-{}", "Lead Spacing, Lead Width, Body Diameter, Body Height, Height from PCB, Lead Length"),
    "CAPPRDHL - Capacitors, Polarized Radial Diameter Horizontal Bent Left Mounting": ("CAPPRDHL{}W{}D{}H{}HL{}-{}-{}", "Lead Spacing, Lead Width, Body Diameter, Body Height, Height from PCB, Lead Length, Lead Bent"),
    "CAPPRDHR - Capacitors, Polarized Radial Diameter Horizontal Bent Right Mounting": ("CAPPRDHR{}W{}D{}H{}HR{}-{}-{}", "Lead Spacing, Lead Width, Body Diameter, Body Height, Height from PCB, Lead Length, Lead Bent"),
    "CAPRR    - Capacitors, Non Polarized Radial Rectangular Vertical Mounting (lead length)": ("CAPRR{}W{}L{}T{}H{}-{}", "Lead Spacing, Lead Width, Body Length, Body thickness, Body Height, Lead Length"),
    "DIOAD    - Diode, Axial Diameter Horizontal Mounting": ("DIOAD{}W{}L{}D{}", "Lead Spacing, Lead Width, Body Length, Body Diameter"),
    "DIOADV   - Diode, Axial Diameter Vertical Mounting": ("DIOADV{}W{}L{}D{}", "Lead Spacing, Lead Width, Body Length, Body Diameter"),
    "DIP      - Dual-In-Line Package": ("DIP{}W{}P{}L{}H{}Q{}", "Lead Span, Lead Width, Pin Pitch, Body Length, Component Height, Pin Qty"), 
    "DIPS     - Dual-In-Line Socket": ("DIPS{}W{}P{}L{}H{}Q{}", "Lead Span, Lead Width, Pin Pitch, Body Length, Component Height, Pin Qty"),
    "FUSAD    - Fuses, Axial Diameter Horizontal Mounting": ("FUSAD{}W{}L{}D{}", "Lead Spacing, Lead Width, Body Length, Body Diameter"),
    "FUSRR    - Fuses, Radial Rectangular Vertical Mounting": ("FUSRR{}W{}L{}T{}H{}", "Lead Spacing, Lead Width, Body Length, Body thickness, Body Height"),
    "HDRV     - Header, Vertical": ("HDRV{}W{}P{}_{}X{}_{}X{}X{}", "total Pins, Lead Width, Row Pitch (+ X Column Pitch [if different]), Row s, Pins per Row, Body Length, Body Thickness, Component Height"),
    "HDRRA    - Header, Right Angle": ("HDRRA{}W{}P{}_{}X{}_{}X{}X{}", "total Pins, Lead Width, Row Pitch (+ X Column Pitch [if different]), Row s, Pins per Row, Body Length, Body Thickness, Component Height"),
    "INDAD    - Inductors, Axial Diameter Horizontal Mounting": ("INDAD{}W{}L{}D{}", "Lead Spacing, Lead Width, Body Length, Body Diameter"),
    "INDADV   - Inductors, Axial Diameter Vertical Mounting": ("INDADV{}W{}L{}D{}", "Lead Spacing, Lead Width, Body Length, Body Diameter"),
    "INDRD    - Inductors, Radial Diameter Vertical Mounting": ("INDRD{}W{}D{}H{}-{}", "Lead Spacing, Lead Width, Body Diameter, Body Height, Lead Length"),
    "LEDRD    - LEDs, Radial Diameter Vertical Mounting": ("LEDRD{}W{}D{}H{}", "Lead Spacing, Lead Width, Body Diameter, Body Height"),
    "PGA      - Pin Grid Array's": ("PGA{}P{}C{}R{}L{}X{}H{}", "Pin Qty, Pitch, Pin Columns, Pin Rows, Body Length, Body Width, Component Height"),
    "RESAD    - Resistors, Axial Diameter Horizontal Mounting": ("RESAD{}W{}L{}D{}", "Lead Spacing, Lead Width, Body Length, Body Diameter"),
    "RESADV   - Resistors, Axial Diameter Vertical Mounting": ("RESADV{}W{}L{}D{}", "Lead Spacing, Lead Width, Body Length, Body Diameter"),
    "RESAR    - Resistors, Axial Rectangular Horizontal Mounting": ("RESAR{}W{}L{}T{}H{}", "Lead Spacing, Lead Width, Body Length, Body thickness, Body Height"),
    "RESARV   - Resistors, Axial Rectangular Vertical Mounting": ("RESARV{}W{}L{}T{}H{}-{}-{}-{}", "Lead Spacing, Lead Width, Body Length, Body Thickness, Body Height, Height from PCB, Lead Length, Height"),
    "SIP      - Single-In-Line Packages (Resistors)": ("SIP{}W{}P{}L{}H{}Q{}", "Body Width, Lead Width, Pin Pitch, Body Length, Component Height, Pin Qty"),
    "JUMP     - Jumpers, Wire": ("JUMP{}W{}", "Lead Spacing, Lead Width"),
    "OSC      - Oscillators": ("OSC{}W{}P{}L{}H{}Q{}", "Lead Span, Lead Diameter, Pin Pitch, Body Length, Component Height, Pin Qty"),
                }


def import_to_django_db(dictionary, type_of='PTH'):
    model = Model()
    for key in dictionary.keys():
        pattern, arguments = dictionary.get(key)
        values = key.split(' - ')
        prefix = values[0].strip()
        description = values[1].strip()
        component = model.get_component(type_of, prefix, description)
        if component:
            print "WARNING: comp [%s] with prefix %s already exists!" % (
                type_of, prefix)
        else:
            model.new_component(type_of, prefix, description, pattern,
                                arguments)
            print "INFO: new comp [%s] with prefix %s stored!" % (
                type_of, prefix)
